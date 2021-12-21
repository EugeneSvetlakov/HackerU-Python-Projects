import re
# from re import RegexFlag, split


def check_port_int(port: int):
    return bool(1 < port < 65353)


def check_port_tuple(port):
    return bool(
        port[0] <= port[1]
        and check_port_int(port[0])
        and check_port_int(port[1])
    )


def check_port(port):
    if type(port) is int:
        return check_port_int(port)
    if type(port) is tuple:
        return check_port_tuple(port)
    return False


def filter_ports(ports: str):
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
            lambda p: check_port(p),
            pre_list
        )
    )


def check_ip(ip: str):
    # TODO: проверку не только IP, но и диаппазона и сети
    # Примеры:
    # - Правилньо 192.168.1.1 or 192.168.1.5-15 or 192.168.1.0/24
    # - Не правильно: 352.2.2.2 or 192.168.1.55-40 or 192.168.1.0/35
    # regexp_ip = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match_str = r"^((\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3}))(([/-])(\d{1,3})){,1}$"
    # if groups number = 8 - range or netw
    # if groups number = 5 - ip address
    # group(0) - ip
    # group(1) - 1's part of ip
    # group(2) - 2's part of ip
    # group(3) - 3's part of ip
    # group(4) - 4's part of ip
    # group(6) - spliter simbol
    # group(7) - number after spliter

    spliter_simbol = None
    num_after = ""

    ip_match = re.match(match_str, ip)
    group_s = ip_match.groups() if ip_match else tuple()
    groups_len = len(group_s)
    if groups_len == 0:
        return False
    num_before = group_s[4]
    ip = group_s[0]
    spliter_simbol = group_s[6]
    num_after = group_s[7]
    check_ip_digits = all(
        map(lambda n: 0 <= int(n) <= 255, ip_match.groups()[1:4])
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


regexp_ip = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
match_str = r"^((\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3}))(([/-])(\d{1,3})){,1}$"
# if groups number = 8 - range or netw
# if groups number = 5 - ip address
# group(0) - ip
# group(1) - 1's part of ip
# group(2) - 2's part of ip
# group(3) - 3's part of ip
# group(4) - 4's part of ip
# group(6) - spliter simbol
# group(7) - number after spliter

ip = "192.168.1.21"
print(check_ip(ip))



ports = [
    "22,24,80-88,54,96-102-55,04-55,25-20",
    "22",
    "22-25",
    "80,8080",
    "f55",
    "55;5",
    "55-57-59",
    "25,55-78-96"
    ]

for p in ports:
    f_list = filter_ports(p)
    print(f_list)
