# ДЗ №2 Светлаков Евгений Сергеевич
# Дан список чисел (задайте его сами). напечатайте все числа большие 0,
# но меньшие 100.
# Со звездочкой*: дан список - удалите все одинаковые элементы,
# если они больше 0.
# **: пользователь вводит список чисел (заранее неизвестно сколько их).
# Конец ввода по вводу слова "end".
# Найдите второй максимальный элемент в этом списке.
# (т.е. для списка [1,6,3,0] ответ 3)
# ЗЫ: задачу решаем с помощью циклов, т.е. filter и прочее не используем
# ЗЗЫ: и да, функцию max, тоже не используем:)
# ЗЗЗЫ: и функцию sort/sorted тоже:))

# dz part 1:
# Дан список чисел (задайте его сами). напечатайте все числа большие 0,
# но меньшие 100.
list_of_nums = [1, 3, 42, -4, 33, 908, 11, 2, -4, -5, 0, 2]
list_of_nums_between_0_100 = [i for i in list_of_nums if 0 < i < 100]
print("Исходный список чисел:")
print(list_of_nums)
print("Список чисел > 0 и < 100:")
print(list_of_nums_between_0_100)
print()

# dz part 2 (*):
# Со звездочкой*: дан список - удалите все одинаковые элементы,
# если они больше 0.
list_of_nums = [1, 1, 1, 3, 3, 3, 33, 42, -4,
                33, 908, 11, 2, -4, -5, 0, 2, 1, 3, 42]
list_unic_nums = []
for i in list_of_nums:
    if (i not in list_unic_nums and i > 0) or (i <= 0):
        list_unic_nums.append(i)
print("Исходный список чисел:")
print(list_of_nums)
print("Список чисел после удаления положительных дублей:")
print(list_unic_nums)
print()

# dz part 3 (**)
# **: пользователь вводит список чисел (заранее неизвестно сколько их).
# Конец ввода по вводу слова "end".
# Найдите второй максимальный элемент в этом списке.

while_bool = True
user_input = None
list_of_nums = []
recieved_num = None
print("!!! Внимание: делителем дробной части числа является точка ('.')")
while while_bool:
    user_input = input(
        "Введите число или 'end' для завершения ввода чисел):")
    user_input = user_input.strip()
    is_digit = user_input.replace(
        "-", "", 1).replace("+", "", 1).replace('.', '', 1).isdigit()
    if not is_digit and user_input != 'end':
        print(
            f"'{user_input}' - это не число и не команда завершения ввода.\n"
            f" Пожалуйста не вводите лишние и некорректные символы.")
    elif user_input == 'end':
        while_bool = False
    else:
        recieved_num = float(user_input)
        recieved_num = int(
            recieved_num) if recieved_num.is_integer() else recieved_num
        list_of_nums.append(recieved_num)

success_find = "Второй максимальный элемент в списке:"
false_find = "Второго максимального элемента нет. Первый максимум равен:"
false_find2 = "В списке только один элемент:"
if len(list_of_nums) > 0:
    print("Вы ввели следующий набор цифр:")
    print(list_of_nums)
    max_num = list_of_nums[0]
    second_max_num = None
    if len(list_of_nums) >= 2:
        for i in list_of_nums[1:]:
            if i > max_num:
                second_max_num = max_num
                max_num = i
            elif i < max_num and second_max_num is None:
                second_max_num = i
            elif second_max_num is not None:
                if second_max_num < i < max_num:
                    second_max_num = i
        if second_max_num is not None:
            print(f"{success_find} {second_max_num}")
        else:
            print(f"{false_find} {list_of_nums[0]}")
    else:
        print(f"{false_find2} {list_of_nums[0]}")
else:
    print("Ваш список цифр пуст.")
