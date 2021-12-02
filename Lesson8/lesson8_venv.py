# sudo apt install virtualenv
# virtualenv venv  # Создание виртуального окружения
# source ./venv/bin/activate  # Активация виртуального окружения
# which python3  # проверка что используем python из виртуального окружения
# deactivate  # Деактивировать виртуальное окружение
# Создаем файл нужных библиотек:
# 1) Все установленные библиотеки
# pip freeze > req.txt
# less ./req.txt
# 2) Только нужные проекту
# pip install pipreqs
# python3 -m pipreqs.pipreqs ./
# less ./requirements.txt
# Удалить Виртуальное окружение
# rm -rf <env path>
