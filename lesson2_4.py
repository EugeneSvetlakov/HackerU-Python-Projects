# for each
import copy
my_list = [1, 2, 3]
my_list = "sfdsfddsfds"
my_list = range(1, 10, 2)

for element in my_list:
    print(element)

# получаем список элементов
list_of_num = list(range(10))
list_from_string = list("my string to get list of cher")
sp = []  # пустой список
sp = [1]*100  # получим список из 100 элементов
g = (x for x in range(30))  # генератор
g = [x for x in range(30)]  # список


# особенности списков по размещению в памяти
list_with_list_inside = [1, 2, [2, 3, "sd"]]
print(list_from_string[1])  # = 'y'
# по факту создали ссылку на объект в памяти
# list2 и list_of_num ссылаются на один объект в памяти
list2 = list_of_num

# copy_of_list2 - Новый объект, вложенный список для них это
# ссылка на один и тот же объект в памяти
copy_of_list2 = list_with_list_inside.copy()

# copy_of_list2 - Новый объект, вложенный список для них
# это ссылка на один и тот же объект в памяти
copy_of_list2 = list_with_list_inside[:]

fyll_list_copy = copy.deepcopy(list2)  # если нужно сделать полноценную копию

# склейка списка в строку
string_from_list = "; ".join(fyll_list_copy)
print(f"print joined string: {string_from_list}")

# ДЗ: поизучать генераторы/(структуры-генераторы)/iterable в питоне

# Кортежи - не изменяемые списки.
t = (1, 2, 4, "ssad")
name, ip, *phone = t
# t[2] = 6 # будет ошибка
print(name, ip, phone)
print(t)
