# получить список из строки с отфильтрованными символами "a" и "i"
s = "mama mila ramu"

sp = []
for i in s:
    if i != "a" and i != "i":
        sp.append(i)
print(sp)

sp2 = []
for i in s:
    if i not in ["a", "i"]:
        sp2.append(i)
print(sp2)

sp3 = []
for i in s:
    if i not in "ai":
        sp3.append(i)
print(sp3)

print(list(s.replace("a", "").replace("i", "")))

print([a for a in s if a not in "ai"])
