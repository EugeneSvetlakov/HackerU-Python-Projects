import os


# Работа с файлами
# Чтение файла в текстовом режиме
file_name = "lesson4.txt"
if os.path.isfile(file_name):
    with open(file_name, encoding="utf-8", mode="rt") as read_file:
        # Прочитать файл полностью
        # read_file = file.read()
        # прочитать очередные 10 символов
        # read_file = file.read(10)
        # Перемотать позицию чтения файла в начало
        # file.seek(0, 0)
        # Текущая позиция чтения в файле
        file_position = read_file.tell()
        # Прочитать очередную строку файла
        # read_file_line_per_iteration = file.readline()
        # Прочитать весь файл по строкам в массив строк
        # (символы переноса строки остаются)
        # read_file_lines = file.readlines()
        # Прочитать символы из файла с дочиткой до конца строки по строкам
        # в массив строк (символы переноса строки остаются)
        # read_file_lines = file.readlines(10)
        for line in read_file:
            print(line)

# Запись в файл
with open("lesson4_write.txt", encoding="utf-8", mode="w") as write_file:
    write_file.write("one\ntwo\nthree")
    # file.writelines()

# Чтение файла в бинарном режиме
if os.path.isfile(file_name):
    with open(file_name, mode="rb") as read_file:
        read_bites = read_file.read()
        bites_to_text = read_bites.decode('cp1256')
        print(bites_to_text)

# Запись в финарном режиме
# Реализовано не совсем верно вроде, стоит почитать про
# конвертауию текста в бинарный код и запись кода в файл
# за одно потренироваться чтению и декодированию бинарника
file_name = "lesson4_wr_bite.bit"
with open(file_name, mode="wb") as write_file:
    bytes_example = bytes("one two", 'utf-8')
    write_file.write(bytes_example)

# Комбинированные режимы
# Open_to_read_and_can_write = open("file.txt", "r+")
# Open_to_read_and_can_write.close()
# Open_to_read_and_can_write = open("file.txt", "r+")
# Open_to_read_and_can_write.close()
# Open_to_read_and_can_write_to_end = open("file.txt", "w+")
# Open_to_read_and_can_write_to_end.close()
