
try:
    a = input("a=")
    b = 100
    c = b / a
    print(c)
    if a == 5:
        raise AttributeError  # Выбросить исключение по определенному событию
except ZeroDivisionError as e:
    print("'a' не может быть = 0")
except ValueError as e:
    print("Вводите только цифры!\n", e)
except AttributeError as e:
    print("Прыгаем в эту ветку по нашему выброшенному исключению")
except Exception as e:  # If exception. Общее исключение ставим всегда в конце
    print("error:", e)
finally:  # Блок выполняется всегда, но он не обязателен
    print("finally")
print("After try-except block.")
