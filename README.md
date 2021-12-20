# Учеба на HackerU модуль Python Programming For Penetration Testing

## vscode addons:
- Better Comments
- GitLens
- Material Icon Theme
- Python
- Pylance
- Visual Studio IntelliCode

## Linter
[inting Python in Visual Studio Code](https://code.visualstudio.com/docs/python/linting)
```
python3.8 -m pip install -U flake8
python3.9 -m pip install -U flake8
python3.8 -m pip install -U flake8-return flake8-simplify pep8-naming flake8-functions flake8-use-fstring flake8-length flake8-type-checking flake8-future-annotations flake8-broken-line autopep8

Ctrl+Shift+P
Python: Select Linter
Python: Select Linter -> flake8
```

## Git and GitHub
### clone repo
git clone https://github.com/EugeneSvetlakov/HackerU-Python-Projects.git
### config to push
```
git config user.name "EugeneSvetlakov"
git config user.email eugene.svetlakov@gmail.com
```
> now try to push, and on ask to login - go auth process

> Авторизация по токену (token)
> [Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
```
git remote set-url origin https://[APPLICATION]:[NEW TOKEN]@github.com/[ORGANISATION]/[REPO].git
```