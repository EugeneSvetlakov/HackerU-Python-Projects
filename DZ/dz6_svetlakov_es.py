from __future__ import annotations
from typing import Optional
import argparse
import subprocess
import os
import os.path
import typing
import re

# ДЗ № 6 Светлаков Евгений Сергеевич
# Напишите программу backuper.py,
# делающую бэкап указанной директории или файла в архив.
# Предусмотрите проверку существования целевой директори и файла,
# и информирование пользователя о результатах
# Примерный синтаксис запуска:
#  ./backuper.py -d <dir>
# (создаст архив dir.tar или dir.zip (или другой формат на ваш выбор)
# в родительской директории директории dir)
#  ./backuper.py -d <dir> -o newname
# (создаст архив newname в родительской директории директории dir)
# т.е. если запустить "./backuper.py -d images/photos",
# то в результате в папке images/ появится архив photos.tar
# ./backuper.py -f <file>
# (создаст архив с файлом в той же директории, где лежит исходный файл)
# ./backuper.py -f <file> -o newname
# (создаст архив с именем newname в той же директории, где лежит исходный файл)
# *предусмотрите возможность предупреждения пльзователя
# о уже существующем архиве с таким же именем и предложите ему
# варианты "перезаписать", "переименовать" и т.п. на ваше усмотрение


def args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Программа создания резервного архива файла/дириктории.")
    parser.add_argument(
        "file", help="file or directory to archieving", type=str)
    parser.add_argument(
        "-o", "--outfile", help="output file name without extention", type=str)
    return parser.parse_args()


def get_out_path(
        prog_options: argparse.Namespace
        ) -> typing.Tuple[Optional[str], Optional[str]]:
    """Функция возвращает кротеж: (bkp_path, file_name.bkp_ext)"""
    is_slash = prog_option.file[-1] != "/"
    prog_option.file = (prog_option.file[:-1], prog_option.file)[is_slash]
    inpath_split = os.path.split(prog_option.file)
    file_ext = ".zip"
    out_file_name = (
        str(inpath_split[1]).split(".")[0],
        prog_option.outfile
    )[bool(prog_option.outfile)]
    return (inpath_split[0], out_file_name + file_ext)


def get_new_out_path(
    file_path: str, new_name: str
) -> typing.Tuple[str, str]:
    """Функция возвращает кортеж (message: str, new_path: str)"""
    result_msg = 'Новое имя файла принято.'
    new_path = file_path
    regx_name = re.search(r'^[\w-]+$', new_name)
    if regx_name is None:
        result_msg = f'Не корректное имя файла "{new_name}"'
        return (result_msg, new_path)
    file_exist = os.path.exists(file_path)
    path_is_file = os.path.isfile(file_path)
    len_new_name = len(new_name) > 0
    if file_exist and path_is_file and len_new_name:
        new_name = regx_name[0]
        path_split: str = os.path.split(file_path)
        file_and_ext = path_split[1].split(".")
        new_path = os.path.join(path_split[0], f'{new_name}.{file_and_ext[1]}')
        if os.path.exists(new_path):
            result_msg = f'Такой файл "{new_path}" уже существует'
    return (result_msg, new_path)


if __name__ == '__main__':
    # Получаем аргументы
    prog_option = args()
    if not os.path.exists(prog_option.file):
        msg = (f'{prog_option.file} - такого файла/дириктории не существует.\n'
               f'Выполнение программы прервано.')
        print(msg)
        exit(1)
    # Что архивировать
    input_path: str = prog_option.file
    # Куда архивитровать
    get_path = get_out_path(prog_option)
    out_path = os.path.join(get_path[0], get_path[1])
    if os.path.exists(out_path):
        print(f"Архив '{out_path}' уже существует.")
        answer = input(
            'Введите: \n'
            '0 - перезаписать архив,\n'
            'или новое имя архива без расширения.\n'
            'Ваш выбор: ')
        if answer == "0":
            os.remove(out_path)
            print("Файл будет перезаписан.")
        else:
            new_path = get_new_out_path(out_path, answer)
            msg = new_path[0]
            out_path = new_path[1]
            while os.path.exists(out_path):
                print(msg)
                new_name: str = input(
                    "Введите новое имя для архива без расширения: ")
                new_path = get_new_out_path(out_path, new_name)
                msg = new_path[0]
                out_path = new_path[1]
    print("Выполняется резервное копирование: ", input_path)
    bkp_exit_code = subprocess.call(["zip", "-rq", out_path, input_path])
    if bkp_exit_code == 0:
        print("Резервное копирование выполнено успешно.")
        print("Результат: ", out_path)
    else:
        print("При выполнении резервного копирования произошел сбой.")

# Не все идеально реализовано, но работает

# Tests:
# python3 ./DZ/dz6_svetlakov_es.py -o newfile ./Lesson1/lesson1.py
# python3 ./DZ/dz6_svetlakov_es.py -o newfile.tar ./Lesson1/lesson1.py
# python3 ./DZ/dz6_svetlakov_es.py ./Lesson1/lesson1.py
# python3 ./DZ/dz6_svetlakov_es.py -o newfile.tar ./Lesson1
# python3 ./DZ/dz6_svetlakov_es.py -o newfile.tar ./Lesson1/
# python3 ./DZ/dz6_svetlakov_es.py -o newfile ./Lesson1
# python3 ./DZ/dz6_svetlakov_es.py -o newfile ./Lesson1/
# python3 ./DZ/dz6_svetlakov_es.py ./Lesson1/
# python3 ./DZ/dz6_svetlakov_es.py ./Lesson1
