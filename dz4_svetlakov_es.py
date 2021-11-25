import os
# ДЗ №4 Светлаков Евгений Сергеевич
# Написать программу,читающую информацию из всех файлов с указанным расширением
# в указанной директории.
# Прочитанную информацию сохранить в log-файл в следующем формате:
# ====
# Название файла 1
# Данные из файла 1
# Количество символов в данных
# *
# Название файла 2
# Данные из файла 2
# Количество символов в данных
# *
# И т.д
# ====
# Лог-файл сохранить в той же директории.
# Пример: если пользователь задал директорию Дир и расширение тхт,
# и в этой директории есть два файла ф1.тхт и ф2.тхт
# со строками "аа" и "ббб" соответственно,то в лог файле будет:

# ====
# ф1.тхт
# аа
# 2
# ***
# ф2.тхт
# ббб
# 3
# ====
given_ext = ".txt"
given_dir = "lesson4_files"
log_filename = "scan_result.log"
is_dir_exist = os.path.isdir(given_dir)
if is_dir_exist:
    with open(os.path.join(given_dir, log_filename), "w") as logfile:
        files = filter(
            lambda file_with_given_ext:
                os.path.splitext(file_with_given_ext)[1] == given_ext,
            os.listdir(given_dir))
        for file in files:
            some_filename = os.path.join(given_dir, file)
            with open(some_filename) as some_file:
                file_text = some_file.read() + '\n'
                count_symbols_in_file = str(len(file_text)) + '\n'
            logfile.writelines([
                file + '\n',
                file_text,
                count_symbols_in_file,
                "***\n"
            ])

# Проверить работу с относительными путями, пустым путем и в разных ОС
# Сделать ввод данных и проверку их правильности + отработку в случае ошибок
# Добавить чуть разговорчивости прорамме о процессе и результатам
