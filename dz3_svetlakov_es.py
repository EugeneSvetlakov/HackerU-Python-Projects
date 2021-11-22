import json
import timeit
# ДЗ №3 Светлаков Евгений Сергеевич
# Даны три списка: список имен пользователей, список их ip, список логинов.
#
# Создайте список, содержащий информацию о каждом пользователе
# в виде словарая с ключами name, ip, login.
# Пример итогового списка:
# [{"name":"vasya","ip":"192.168.10.1","login":"vasya123"},{....},{....}].
#
# Сдампите его в виде json-файла, используя модуль json.
# Код для дампа:
# import json
# sp = ... # ваш объект для дампа (список пользователей)
# json.dump(sp,open("users.json","w"))
#
# * Сделайте ввод пользователей и их данных (с клавиатуры или из файла(ов))


# Создайте список
name_list = ["Vasya", "Nike", "Maksim", "Olga", "Katerina", "Dmitri"]
ip_list = ["192.168.1.2", "192.168.1.11", "192.168.1.9",
           "192.168.1.250", "192.168.1.5", "192.168.1.15"]
login_list = ["p15ink2", "p15bu2", "p15ink5",
              "p15bu76", "p15clo32", "p15log23"]
key_list = ["name", "ip", "login"]

my_list = []
start = timeit.timeit()
for n, i, l in zip(name_list, ip_list, login_list):
    # print(n, i, l)
    dict_1 = {k: v for k, v in zip(key_list, [n, i, l])}
    my_list.append(dict_1)
    print(dict_1)
print("My_set:")
print(my_list)
stop = timeit.timeit()
elapsed_time = stop - start
print(f"Elapsed time: {elapsed_time}")

start = timeit.timeit()
my_list_2 = []
for i in range(len(name_list)):
    my_list_2.append(
        {key_list[0]: name_list[i],
         key_list[1]: ip_list[i],
         key_list[2]: login_list[i]})
print(my_list_2)
stop = timeit.timeit()
elapsed_time = stop - start
print(f"Elapsed time: {elapsed_time}")

# Сдампите его в виде json-файла
with open("dump_my_list_2.json", "w") as write_file:
    json.dump(my_list_2, write_file)
