import random

# форматирование строк старое
name = "Masha"
age = 33

hello = "Hello, %s, your age is  %d!"
formatted_str = hello % (name, age)
print(hello)
print(formatted_str)
sp = ["Masha", "Kolya", "U", "Yan", "Navoohodonoser"]
for name in sp:
    c = random.randint(100, 1000) / 33
    s = "%8.8s : % 3.4f" % (name, c)
    string_2 = "%8.8s : %+.2f" % (name, c)
    print(s)
    print(string_2)

# форматирование строк новое
hello = "Hello, {}, your age is  {}!"
formatted_str = hello.format(name, age)
print(formatted_str)
hello = "Hello, {1}, your age is  {0}!"
formatted_str = hello.format(name, age)
print(formatted_str)
hello = "Hello, {name_2}, your age is  {age_2}!"
formatted_str = hello.format(name_2=name, age_2=age)
print(formatted_str)
print(hello)
print(formatted_str)
sp = ["Masha", "Kolya", "U", "Yan", "Navoohodonoser"]
for name in sp:
    c = random.randint(100, 1000) / 33
    s = "{:>8.6} : {:+8.5}".format(name, c)
    print(s)
    string_2 = "{name_3:*^8.6} : {number_3:> 8.5}".format(
        name_3=name, number_3=c)
    print(string_2)

hello_2 = f"Hello, {name}, your age is  {age}!"
