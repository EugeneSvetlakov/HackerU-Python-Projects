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
python3.8 -m pip install -U flake8-return flake8-simplify pep8-naming flake8-functions flake8-use-fstring flake8-length flake8-type-checking flake8-future-annotations flake8-broken-line flake8-mypy autopep8

Ctrl+Shift+P
Python: Select Linter
Python: Select Linter -> flake8
```

---- ./.vscode/settings.json ----
```
{
    "python.languageServer": "Pylance",
    "python.envFile": "${workspaceRoot}/.env",
    "python.pythonPath": ".env/bin/python",
    "python.linting.enabled": true,
    "python.linting.lintOnSave": true,
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Path": "flake8",
    "python.linting.mypyEnabled": true,
    "python.formatting.autopep8Args": ["--max-line-length", "79", "--experimental"],
    "python.linting.ignorePatterns": [
        "**/site-packages/**/*.py",
        ".vscode/*.py",
        ".venv/*/*.py"
    ]
}
```
---- end ----

---- ./.vscode/launch.json ----
```
{
    // Используйте IntelliSense, чтобы узнать о возможных атрибутах.
    // Наведите указатель мыши, чтобы просмотреть описания существующих атрибутов.
    // Для получения дополнительной информации посетите: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python",
            "type": "python",
            "request": "launch",
            "stopOnEntry": false,
            "pythonPath": "${config:python.pythonPath}",
            "program": "${file}",
            "cwd": "${workspaceRoot}",
            "env": {},
            "envFile": "${workspaceRoot}/.env",
            "console": "integratedTerminal",
            "debugOptions": [
                "WaitOnAbnormalExit",
                "WaitOnNormalExit",
                "RedirectOutput"
            ]
        }
    ]
}
```
---- end ----

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