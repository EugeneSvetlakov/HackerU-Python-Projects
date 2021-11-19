text = " mama mila ramu"
text_len = len(text)
i = 0
while i < text_len:
    if text[i] != " ":
        print(text[i])
    if i == 777:
        continue
    if i == 299:
        break
    i += 1
else:
    print("Если цикл завершился без выхода по brake")

print("my first print", end="")  # чать без переноса на новую строку
print("My second print on same string as first")
