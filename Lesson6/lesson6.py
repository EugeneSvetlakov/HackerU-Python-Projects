import os
import subprocess
import sys
import argparse

# Запуск системных комманд
# Запуск команды из скрипта
code = os.system("ls -h")
print(f'Returned code= {code}')

# Чтобы получать результат выполнения команды, добавить интерактивность
# применяют "import subprocess"
# Запуск команды с параметрами
r1 = subprocess.call("ls -lA", shell=True)
# или
r1 = subprocess.call(["ls", "-lA"])

# Перенаправит вывод в файл
file = open("sds.txt", "w")
r1 = subprocess.call("ls -lA", shell=True, stdout=file)

# Получить вывод работы команды внутрь Python
# не выгоден для команд с длительным процессом выполнения
# (антивирус, посик по всем дириктрриям)
r1 = subprocess.check_output("ls -lA", shell=True)
print("r1:", r1)
print("decoded r1:", r1.decode("utf-8"))
print("decoded r1:", r1.decode("866"))  # if using windows

# Вернуть процесс команды (добавляется взаимодействие)
r1 = subprocess.run(
    ["ls", "-lA"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(r1)
print(r1.stdout.decode())
print("errors: ", r1.stderr.decode())

r1 = subprocess.run(
    ["ls", "-z"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(r1)
print(r1.stdout.decode())
print("errors: ", r1.stderr.decode())

r1 = subprocess.Popen(
    'find ~ -name "*.txt"', shell=True, stdout=subprocess.PIPE)
r1.wait()
print(r1.stdout.read().decode())
print("end")

p = subprocess.Popen(["ping", "8.8.8.8", "-c", "4"])
p.wait()

r1 = subprocess.Popen(
    ["ls", "-lA"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(r1)
print(r1.stdout.read().decode())
print("errors: ", r1.stderr.read().decode())


print("\nwhile...")
r1 = subprocess.Popen(
    'find ./ -name "*.txt"', shell=True,
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
r1.wait()
while True:
    output = r1.stdout.readline()
    if output == b'' or p.poll() is not None:
        break
    print(output.decode())
print("out: ", r1.stdout.read().decode())
print("errors: ", r1.stderr.read().decode())
print("end")

# p = subprocess.Popen(["python", "lesson2.py"])

p = subprocess.run("ip link", shell=True)
