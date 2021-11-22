# ДЗ №1, Светлаков Евгений Сергеевич
"""Задание:
пользователь вводит имя файла (например notes.txt) и новое расширение
(например: log) напечатайте на экране имя файла с новым расширением,
т.е. в данном случае notes.log расширением файла считайте строку после
самой правой точки, т.е. в имени "файл.тхт.пп".
- расширение это "пп"
учтите, что в имени файла точка может встречаться несколько раз, а сам
файл может не иметь расширения вовсе
* добавьте к итоговому имени файла длину его имени без расширения через
подчеркивание, т.е. для файла notes.txt и расширения log итог будет notes_5.log
предусмотрите, что пользователь может вводить расширение как с точкой,
так и без точки и корректно это обработайте (т.е. возможен ввод как '.log',
так и 'log')"""
print_result = '\x1b[6;30;42m'
+ "Внимание: во введенном имени файла расширением будет считатья набор"
+ " символов введенный после последней точки!"
+ '\x1b[0m'
print(print_result)
input_question = "Введите имя файла с расширением (пример: 'file_name.txt'):"
file_name_full = input(input_question)
print_value = '\x1b[6;30;42m'
+ 'Внимание: в введенном расширении файла будут удалены все точки!'
+ '\x1b[0m'
print(print_value)
new_file_ext = input("Введите новое расширени (пример: 'log'):").replace(".")

index_of_dot = file_name_full.rfind(".")
file_name_without_ext = file_name_full if index_of_dot < 0 else file_name_full[
    :index_of_dot]
new_file_name = file_name_without_ext + "." + new_file_ext
new_file_with_len_name = (file_name_without_ext + "_" +
                          str(len(file_name_without_ext)) +
                          "." + new_file_ext)
print(f"Новое имя файла: {new_file_name}")
print_value = "Имя файла с добавлением длины имени (без учета расширения):"
print(
    f"{print_value} {new_file_with_len_name}")
