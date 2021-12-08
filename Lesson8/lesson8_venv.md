# VENVs:

## using virtualenv
sudo apt install virtualenv
### Создание виртуального окружения
virtualenv venv
### Активация виртуального окружения
source ./venv/bin/activate
### Деактивировать виртуальное окружение
deactivate

## using python3
sudo apt-get install python3-venv
python3 -m venv .venv
> When you create a new virtual environment,
> a prompt will be displayed to allow you to select it for the workspace.
> Теперь можно выбрать нужное виртупльное окружение слева внизу
> Когда откроем новый терминал - будет видно что используется виртуальное окружение
## Проверка что используем python из виртуального окружения
which python3

## Создаем файл нужных библиотек:
### Все установленные библиотеки
pip freeze > req.txt
less ./req.txt

### Только нужные проекту
pip install pipreqs
python3 -m pipreqs.pipreqs ./
less ./requirements.txt

### Устанавливаем зависимости по полученному списку:
pip install -r ./requirements.txt

## Удалить Виртуальное окружение
rm -rf <env path>
