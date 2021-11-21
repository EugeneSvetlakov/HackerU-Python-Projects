import re
import os.path

# ДЗ №3 Светлаков Евгений Сергеевич
# * Сделайте ввод пользователей и их данных из файла
file_name = "data.txt"
data_format = "user_name, user_ip_address, user_login"
data_format_example = "Nikita, 192.168.12.11, wsd3Ws323"
data_rexp = r'^[a-zA-Zа-яА-Я]\w*, \d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}, [a-zA-Z]\w*'
key_list = ["name", "ip", "login"]
my_list = []
if os.path.isfile(file_name):
    with open(file_name, "r") as read_file:
        for line in read_file:
            search_data = re.search(data_rexp, line)
            if search_data is not None:
                dict_1 = {k: v for k, v in zip(
                    key_list, search_data.string.split(", "))}
                my_list.append(dict_1)
print(my_list)
