import os
import os.path
import lesson4_mymodele

# Импорт части модуля
# from lesson4_mymodele import func_1, func_2

# Импорт из модуля с заменой имени обращения
# import lesson4_mymodele as my_mod

# Менеджеры контекста (объекты имеющие функцию close)
# Почитать про другие менеджеры контекста
# один из них это:
# file_name = "lesson4.txt"
# with open(file_name, mode="rb") as read_file:
#     s = read_file.read()
#     # ...

# Модули
# Использование импортированого самописного модуля
# print(lesson4_mymodele.A)
# В случае from "lesson4_mymodele import func_1, func_2"
# print(func_1)

# Желательно обрамлять код в форму чтобы не выполнялись
#  исполняемые строки из других модулей
if __name__ == '__main':
    # Begin of program code
    # This is sample of code
    for i in range(10):
        print(i)
    # End of program code

# Модуль os
list_directory_files = os.listdir("lesson4_files/")
print(list_directory_files)
# current_working_dir = os.getcwd()
# os.chdir("./vscode")
# os.mkdir("new_dir")
# and other

# Модуль os.path
full_name = os.path.join("lesson4_files", "file1.txt")
print(full_name)
print(os.path.isdir(full_name))
print(os.path.isfile(full_name))
print(os.path.splitext(full_name))
print(os.path.exists(full_name))
print(os.path.dirname(full_name))

# Задание: переименовать файлы заданного расширения на новое расширение
# пока тупо и без реальных переименований,
# нужно ввести проверки и корректировки ввода
# === пример простого с занятия ===
# files = os.listdir(target_dir)
# for file in files:
#     name, ext = os.path.splitext(file)
#     if ext == "." + ext_old:
#         os.rename(
#           os.path.join(target_dir, file),
#           f"{target_dir}/{name}.{ext_new}")
# === end ===

ext_new = input("new extension: ")
ext_old = input("old extension: ")
target_dir = ("lesson4_files")
b1 = os.path.exists(target_dir)
if os.path.exists(target_dir):
    os.chdir(target_dir)
    cwd = os.getcwd()
    list_directory_files = os.listdir()
    for file in list_directory_files:
        file_ext = os.path.splitext(file)[1]
        b2 = os.path.splitext(file)[1] == f'.{ext_old}'
        if b2:
            s1 = file
            s2 = f'{os.path.splitext(file)[0]}.{ext_new}'
            # os.rename(file, file.split()[0] + ext_new)
            print(s1 + "\n" + s2)
    os.chdir("..")
