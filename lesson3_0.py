from collections import Counter

# Словари, Множества
# - Ключем может быть любой не изменяемый тип данных (строка, число, ...),
# в том числе и кортеж и др.
# До версии version 3.6 порядок элементов в словаре не гарантирован
# (он мог меняться)
sp = ["1", 2, 4, 5, "we"]
my_dict = {
    "key1": "propertie1",
    "key2": "propertie2",
    "key3": ["propertie3_1", "propertie3_2"],
    "key4": {"sub_key1": "sub_prop1", "sub_key2": "sub_prop2"}}
print(my_dict.keys(), end="\n\n")
print(list(my_dict.keys())[1], end="\n\n")
print(f"{my_dict.get('key3')} == {my_dict['key3']}", end="\n\n")
print(my_dict.items(), end="\n\n")

for s in sp:
    print(s)

for d in my_dict:  # = for d in my_dict.keys():
    print(d)

for k, v in my_dict.items():
    print(f"key={k} value={v}")

# словарь из 2х списков
sp = ["a", "b", "c"]
value_list = [1, 2, 3]
dict_2 = {k: v for k, v in zip(sp, value_list)}
print(dict_2)

# сшить 3 словаря
value_list_2 = [11, 22, 23]
print(list(zip(sp, value_list, value_list_2)))

# словарь символов из строки
my_text = "mama mila ramu"
text_dict = {}
for letter in my_text:
    # if i in text_dict:
    #     text_dict[i] += 1
    # else:
    #     text_dict[i] =1
    text_dict[letter] = text_dict.get(letter, 0) + 1
print(text_dict)

text_dict_2 = {}.fromkeys(my_text, 0)
print(text_dict_2)
use_counter = Counter(my_text)
print(f"Counter= {use_counter}")

new_dict = {}
for letter in my_text:
    new_dict.setdefault(letter, []).append("add_result_of_func_to_values_list")

print(new_dict)
