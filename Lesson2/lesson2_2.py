sum_result = 0
get_number = int(input("Введите число (для завершения программы введите 0):"))
while get_number != 0:
    sum_result += get_number
    get_number = int(
        input("Введите число (для завершения программы введите 0):"))

print(f"Результат сложения введеных чисел: {sum_result}")
