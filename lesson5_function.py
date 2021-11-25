# region Функции
def foo(x) -> str:
    print("func foo is started...")
    if x > 100:
        return x * x
    else:
        return x


def foo2():
    print("It was func foo2.")


def foo_append(y):
    y.append("new")


def get_sum_num(n):
    res = 0
    for i in str(n):
        res += int(i)
    return res


def foo_3(a, b, z=2):
    return a + b - z


def foo_4(a, b, *args):
    print(a)
    print(b)
    print(args)


# print("start")
# a = foo(10)
# print(a)
# print("end")
# print(type(foo(4)))

# y = 5
# res = foo(y)
# print(res)
# print(type(foo2()))

# list_1 = ["wes", 2]
# print(foo_append(list_1))

print("sum_num= ", get_sum_num(125))

print("foo_3= ", foo_3(3, b=5, z=6))
print("foo_3= ", foo_3(3, z=5, b=6))
print("foo_3= ", foo_3(3, 5))

print("foo_4= ", foo_4(2, 3, 5, 6, 7, 8, 9, 10))
# endregion


# region развертка списка
list_2 = [2, 4, 5]
print("foo_3 (с разверткой)= ", foo_3(*list_2))
# endregion


# region развертка словаря
def dict_razvernut(masha=0, petya=1, kolya=3):
    print(
        f'func dict_razvernut: masha= {masha}, petya= {petya}, kolya= {kolya}')


dict_2 = {"masha": 2, "petya": 4, "kolya": 5}
print("foo_3 (с разверткой)= ", dict_razvernut(**dict_2))
# endregion


# region Функции с именованными аргументами
def print_pet_names(owner, **pets):
    """Здесь размещается Документация по функции print_pet_names"""
    print(f"Owner Name: {owner}")
    for pet, name in pets.items():
        print(f"{pet}: {name}")


print_pet_names("Jonathan", dog="Brock", fish=[
    "Larry", "Curly", "Moe"], turtle="Shelldon")
print(print_pet_names.__doc__)
print(print_pet_names.__name__)
"""
Owner Name: Jonathan
dog: Brock
fish: ['Larry', 'Curly', 'Moe']
turtle: Shelldon
"""
# endregion


# region Глобальные переменные в функции
def foo_6(x):
    global c
    c = 9
    return x - c


c = 100
print("foo_6= ", foo_6(7))
print("c= ", c)
# endregion


# region Аннотации
def foo_7(x: int) -> str:
    return str(x)
# endregion


# region Lambda functions
def foo_7(x: str) -> int:
    return len(x)


def foo_8(x: str) -> str:
    return x.upper()


def foo_9(x: str) -> str:
    return x[-2:].upper()


sp = ["Masha", "Kolya", "U", "Dina", "andy", "andx"]

print(sorted(sp))
print(sorted(sp, key=foo_7))
print(sorted(sp, key=foo_8))
print(sorted(sp, key=foo_9))

users = [
    ["Vasya", 176, 344332],
    ["Vasya2", 16, 342656],
    ["Vasya14", 551, 342787],
    ["Vasya4", 51, 34342],
    ["Vasya23", 14, 1111342],
    ["Vasya9", 13, 334352],
    ["Vasya11", 21, 343562],
]


def two(x):
    return x[1]


# two_lambda = lambda x: x[1]


def three(x):
    return x[2]


# three_lambda = lambda x: x[2]


choice = input("Enter your choice (1, 2, 3): ")
if choice == '2':
    print(sorted(users, key=two))
elif choice == '3':
    print(sorted(users, key=lambda x: x[2]))
else:
    print(sorted(users))

res = 2 + 10 * (lambda x, y, z: x + y + z)(1, 2, 3)
# endregion

# region Функции высшего порядка: map, filter
sp = "32423565646546343546566787895"
sp = list(sp)
list(map(lambda x: int(x), sp))
list(map(int, sp))
n = "234241"
print(sum(map(int, list(n))))
s = "34 434 67 87 554"
s2 = map(int, s.split())
print(
    sum(map(int, s.split()))
)

res = sum(map(int, input().split))
print(type(res))
print("first print res:", res)
print("second print res:", res)
print(type(list(res)))
print("first print list(res):", list(res))
print("second print list(res):", list(res))

res2 = list(filter(lambda x: x < 80, map(int, s.split())))
res3 = list(filter(lambda x: x < 80, s2))
# endregion
