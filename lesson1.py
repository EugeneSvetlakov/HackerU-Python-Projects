a = 123
n1 = a // 100
n2 = a // 10 % 10
n3 = a % 10
print(f"n1={n1}, n2={n2}, n3={n3}")

""" Приведение типов"""
a = int(input("Введите число:"))
print("if is started")
if a > 0:
    print("a > 0")
    print("it 'if'")
    if a > 10:
        print("a > 10")
        print("it 'if' second level")
    else:
        print("0 < a < 10")
        print("it 'else' second level")
elif a < 0:
    print("a < 0")
    print("it 'elif'")
else:
    print("a = 0")
    print("it 'else'")
print("if is finished")

x1 = int(input("x1="))
x2 = int(input("x2="))
if x1 > x2:
    print(f"{x2}, {x1}")
elif x1 == x2:
    print(f"{x1} = {x2}")
else:
    print(f"{x1}, {x2}")

s = "ssad asdsad asdsa sa"
print(s[2])
print(s[2:9])  # [стартовый_элемент:конечный_элемент_не_включительно]
print(s[2:9:3])  # [стартовый_элемент:конечный_элемент_не_включительно:шаг]

# файл зд формат: dz1_FIO
# внутри: dz1 ФИО + текст задания

# почитать про классы
