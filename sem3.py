"""
Вручную создайте список с целыми числами, которые
повторяются. Получите новый список, который содержит
уникальные (без повтора) элементы исходного списка.

Подготовьте два решения, короткое и длинное, которое
не использует другие коллекции помимо списков.
"""
"""
numbers = [32, 17, 2, 2, 1, 24, 7, 15, 14, 99, 7, 32, 15]

# Короткое решение (используя множества):
unique_numbers = set(numbers)
print(unique_numbers)

# Длинное решение (без использования других коллекций):
unique_numbers = []

for i in numbers:
    if i not in unique_numbers:
        unique_numbers.append(i)

print(unique_numbers)
"""
"""
Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
- Целое положительное число
- Вещественное положительное или отрицательное число
- Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
- Строку в нижнем регистре в остальных случаях
"""
"""
while True:
    input_str = input('Введите данные (выход-1): ')
    if input_str == 'exit':
        break
    if input_str.isdigit():
        print('Целое положительное число', int(input_str))
    else:
        try:
            print('Вещественное: ', float(input_str))
        except:
            if any(i.isupper() for i in input_str):
                print('В строке есть заглавные', input_str.upper())
            else:
                print('В нижний регистр: ', input_str.lower())
"""
"""
Создайте вручную кортеж содержащий элементы разных типов.
- Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
"""
"""
# Создание кортежа с элементами разных типов
my_tuple = (1, 2.0, 'three', [4, 5], {'six': 6})

# Инициализация пустого словаря
my_dict = {}

# Перебор элементов кортежа
for item in my_tuple:
    # Получение типа элемента
    item_type = type(item).__name__
    # Добавление элемента в список значений для данного типа
    if item_type not in my_dict:
        my_dict[item_type] = [item]
    else:
        my_dict[item_type].append(item)

# Вывод полученного словаря списков
print(my_dict)
"""
"""
Создайте вручную список с повторяющимися элементами.
- Удалите из него все элементы, которые встречаются дважды.
"""
"""
my_list = [2, 5, 2, 3, 4, 4, 1, 5, 6, 6, 1, 8, 8, 9]
unique_list = []
for i in my_list:
    if my_list.count(i) == 1:
        unique_list.append(i)
print(unique_list)
"""
"""
- Создайте вручную список с повторяющимися целыми числами.
- Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
- Нумерация начинается с единицы.
"""
"""
numbers = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 7]
odd_indices = [i+1 for i in range(len(numbers)) if numbers[i] % 2 != 0]
print(odd_indices)
"""
"""
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
- Строки нумеруются начиная с единицы.
- Слова выводятся отсортированными согласно кодировки Unicode.
- Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.
"""
"""
text = input("Введите текст: ")
words = sorted(text.split(), key=str.lower)

max_len = len(max(words, key=len))

for i, word in enumerate(words, start=1):
    print('{i:>{width}} {word}'.format(i=i, width=len(str(len(words))), word=word.rjust(max_len)))
"""
""""
Пользователь вводит строку текста.Подсчитайте сколько раз встречается
каждая буква в строке без использования метода count и с ним.
Результат сохраните в словаре, где ключ — символ, а значение — частота встречи
символа в строке. Обратите внимание на порядок ключей.
Объясните почему они совпадают или не совпадают в ваших решениях.
"""
"""
text = input("Введите строку текста: ")
freq = {} # создаем пустой словарь для частот

for char in text:
    if char in freq:
        freq[char] += 1 # добавляем к существующему ключу в словаре
    else:
        freq[char] = 1 # добавляем новый ключ со значением 1

print(freq)

text = input("Введите строку текста: ")
freq = {char: text.count(char) for char in set(text)}

print(freq)
"""
