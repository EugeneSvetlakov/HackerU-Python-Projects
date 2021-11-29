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
        description="Программа создания резервного архива файла/дириктории."
    )
    parser.add_argument("file", help="file or directory to archieving",
                        type=str)
    parser.add_argument("-o", "--outfile", help="output file name",
                        type=str)
    return parser.parse_args()


if __name__ == '__main__':
    prog_option = args()
    if os.path.exists(prog_option.file):
        is_path_a_file = os.path.isfile(prog_option.file)
        is_path_a_dir = os.path.isdir(prog_option.file)
