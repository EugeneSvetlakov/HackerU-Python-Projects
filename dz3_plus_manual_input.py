import re

# ДЗ №3 Светлаков Евгений Сергеевич
# * Сделайте ввод пользователей и их данных с клавиатуры
regexp_str = r'^[a-zA-Zа-яА-Я]\w*'
question_str = 'Введите имя пользователя: '
error_message = 'Ошибка! В имени первый символ обязательно буква.' \
    ' Допустимо исрользоавать цифры.'
bool_question = True
while bool_question:
    recieved_str = input(question_str)
    search_regexp = re.search(regexp_str, recieved_str)
    check_value = search_regexp is not None
    if check_value:
        bool_question = False
    else:
        print(error_message)
user_name = recieved_str
print(f"name: {user_name}")

regexp_str = r'^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$'
question_str = f'Введите IP пользователя с именем "{user_name}": '
error_message = 'Ошибка! Пример корректного ip адреса: 192.168.15.3'
bool_question = True
while bool_question:
    recieved_str = input(question_str)
    search_regexp = re.search(regexp_str, recieved_str)
    check_value = search_regexp is not None
    if check_value:
        bool_question = False
    else:
        print(error_message)
user_ip = recieved_str
print(f"user_ip: {user_ip}")

regexp_str = r'[a-zA-Z]\w*'
question_str = f'Введите login для пользователя с именем "{user_name}": '
error_message = 'Ошибка! login должен состоять минимум из одной ' \
    'английской буквы. Допустимо вводить цифры и "_".'
bool_question = True
while bool_question:
    recieved_str = input(question_str)
    search_regexp = re.search(regexp_str, recieved_str)
    check_value = search_regexp is not None
    if check_value:
        bool_question = False
    else:
        print(error_message)
user_login = recieved_str
print(f"user_login: {user_login}", end="\n\n")

users_data = [{"name": user_name, "ip": user_ip, "login": user_login}]
