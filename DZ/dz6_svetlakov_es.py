from __future__ import annotations
from typing import Optional
import argparse
import os
import os.path
import subprocess

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


def args():
    parser = argparse.ArgumentParser(
        description="Программа создания резервного архива файла/дириктории.")
    parser.add_argument(
        "file", help="file or directory to archieving", type=str)
    parser.add_argument(
        "-o", "--outfile", help="output file name without extention", type=str)
    return parser.parse_args()


def get_out_path(prog_options) -> Optional[str]:
    if os.path.exists(prog_option.file):
        is_slash = prog_option.file[-1] != "/"
        prog_option.file = (prog_option.file[:-1], prog_option.file)[is_slash]
        inpath_split = os.path.split(prog_option.file)
        file_ext = ".zip"
        out_file_name = (
            str(inpath_split[1]).split(".")[0],
            prog_option.outfile
            )[bool(prog_option.outfile)]
        return os.path.join(inpath_split[0], out_file_name + file_ext)
    else:
        return None


if __name__ == '__main__':
    prog_option = args()
    print("is path exist: ", os.path.exists(prog_option.file))
    input_path: str = prog_option.file
    out_path: str = get_out_path(prog_option)
    print("input_path: ", input_path)
    print("out_path: ", out_path)
    is_out_path_exist: bool = os.path.exists(out_path)
    print("is_out_path_exist: ", is_out_path_exist)
    bkp_exit_code = subprocess.call(["zip", "-rq", out_path, input_path])
    if bkp_exit_code == 0:
        print("Резервное копирование выполнено успешно.")
    else:
        print("При выполнении резервного копирования произошел сбой.")

# zip -rq out_path input_path

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
