# Множества (набор не повторяющихся элементов)
sp = [1, 2, 3, 1, 3, 4, 3, 5, 6, 3, 2, 44, 6, 2]
set_0 = set(sp)  # создать из списка множество
set_1 = {1, 2, 4}  # ручной ввод множества
set_2 = set()  # создать пустое множество

set_diff = set_0 - set_2
set_1.difference_update(set_2)
set_sum = set_0 & set_2
print(set_sum)
set_union = set_0 | set_2
print(set_union)
set_crossing = set_0 ^ set_2
print(set_crossing)

set_0[10]  # add element to set
set_0.remove(10)
