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

# region Модуль os
print("Модуль os:")
list_directory_files = os.listdir("Lesson4/lesson4_files/")
print("os.listdir: ", list_directory_files)
current_working_dir = os.getcwd()
# os.chdir("./vscode")
# os.mkdir("new_dir")

# Символ переноса строки в ОС
os_linesep = os.linesep
print("os.linesep: ", os_linesep)

# Символ разделения дириктории
os_sep = os.sep
print("os.sep: ", os_sep)
# endregion

# region Модуль os.path
print("Модуль os.path:")
lesson4_path = "Lesson4/lesson4_files"
print("Path to work: ", lesson4_path)

# Join two or more pathname components, inserting '/' as needed.
# If any component is an absolute path, all previous path components
# will be discarded.
# An empty last part will result in a path that ends with a separator.
file_name = "file1.txt"

# Join two or more pathname components, inserting '/' as needed.
# If any component is an absolute path,
# all previous path components will be discarded.
# An empty last part will result in a path that ends with a separator.
relative_path = os.path.join(lesson4_path, file_name)
print("os.path.join(relative_path+filename): ", relative_path)

# Return an absolute path.
abs_path = os.path.abspath(relative_path)
print("os.path.abspath: ", abs_path)

# Return true if the pathname refers to an existing directory.
is_path_a_dir = os.path.isdir(relative_path)
print("Path is dir?: ", is_path_a_dir)

# Test whether a path is a regular file
is_path_a_file = os.path.isfile(relative_path)
print("Path is file?: ", is_path_a_file)

# Split a pathname. Returns tuple "(head, tail)"
# where "tail" is everything after the final slash.
# Either part may be empty.
relative_path_split = os.path.split(relative_path)
print("os.path.split(relative_path): ", relative_path_split)
dir_from_relative_path_split = relative_path_split[0]
file_from_relative_path_split = relative_path_split[1]
abs_path_split = os.path.split(abs_path)
print("os.path.split(abs_path): ", abs_path_split)
dir_path_split = os.path.split(lesson4_path)
print("os.path.split(dir): ", dir_path_split)
file_path_split = os.path.split(file_name)
print("os.path.split(file): ", file_path_split)

# Test whether a path to dir or file exists.
# Returns False for broken symbolic links
is_path_exist = os.path.exists(relative_path)
print("Is path exist?: ", is_path_exist)

# Returns the directory component of a pathname
dir_name = os.path.dirname(relative_path)
print("os.path.dirname: ", dir_name)

# Returns the final component of a pathname
os_path_basename = os.path.basename(relative_path)
print("os.path.basename: ", os_path_basename)

# Split the extension from a pathname.
# Extension is everything from the last dot to the end,
# ignoring leading dots. Returns "(root, ext)"; ext may be empty.
splitext_relative_path = os.path.splitext(relative_path)
print("Splitext relative path: ", splitext_relative_path)
splitext_abs_path = os.path.splitext(abs_path)
print("Splitext abs path: ", splitext_relative_path)
splitext_filename_with_ext = os.path.splitext(relative_path_split[1])
print("Splitext abs path: ", splitext_filename_with_ext)

# Given a sequence of path names, returns the longest common sub-path.
os_path_commonpath = os.path.commonpath(['/usr/lib', '/usr/local/lib'])
print("os.path.commonpath: ", os_path_commonpath)

# Test whether a path is absolute
os_path_isabs_on_relpath = os.path.isabs(relative_path)
print("os.path.isabs: ", os_path_isabs_on_relpath)
os_path_isabs_on_abspath = os.path.isabs(abs_path)
print("os.path.isabs: ", os_path_isabs_on_abspath)

# Split a pathname into drive and path.
# On Posix, drive is always empty.
os_path_splitdrive = os.path.splitdrive(relative_path)
print("os.path.splitdrive(posix_os): ", os_path_splitdrive)
os_path_splitdrive_win_os = os.path.splitdrive(
    r'c:\Program files\Common\file.txt')
print("os.path.splitdrive(win_os): ", os_path_splitdrive_win_os)
os_path_splitdrive_win_os_2 = os.path.splitdrive(
    'c:/Program files/Common/file.txt')
print("os.path.splitdrive(win_os): ", os_path_splitdrive_win_os_2)
os_path_splitdrive_net = os.path.splitdrive(
    '//host/computer/dir/file.txt')
print("os.path.splitdrive(network_path): ", os_path_splitdrive_net)

# Переименование файла/дириктории
old_file_name = os.path.join(lesson4_path, "file_to_rename.txt")
new_file_name = os.path.join(lesson4_path, "file_renamed.txt")
os.rename(old_file_name, new_file_name)

# Getting the parent of specified path
my_path = "your/path/for/parent/directory"
parent = os.path.join(my_path, os.pardir)
# endregion


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
