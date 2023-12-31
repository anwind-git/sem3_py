"""
Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
- Какие вещи взяли все три друга
- Какие вещи уникальны, есть только у одного друга
- Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
- Для решения используйте операции с множествами. Код должен расширяться
на любое большее количество друзей.
"""
import re

print("--------------------------")
print("семинар 8-я задача")
print("--------------------------")

friends = {
    'Друг 1': ('телефон', 'нож', 'рюкзак', 'вода', 'еда'),
    'Друг 2': ('телефон', 'нож', 'рюкзак', 'еда', 'спички'),
    'Друг 3': ('вода', 'рюкзак', 'карта', 'еда', 'спальник')
}

common_items = set.intersection(*map(set, friends.values()))
print("Вещи, которые взяли все три друга:", common_items)

all_items = set().union(*friends.values())
unique_items = {item for item in all_items if sum([1 for items in friends.values() if item in items]) == 1}

print(f"Уникальные вещи которые есть только у одного друга: {unique_items}")

for friend in friends.keys():
    to_remove = set(friends[friend])
    my_set = set.intersection(*[set(friends[other_friends]) for other_friends in friends.keys() if other_friends != friend])
    my_set -= to_remove

    if my_set:
        print(f'У {friend} отсутствуют вещи которые есть у его друзей: {my_set}')

"""
Дан список повторяющихся элементов. Вернуть список
с дублирующимися элементами. В результирующем списке
не должно быть дубликатов.
"""
print("--------------------------")
print("dz1")
print("--------------------------")
orig_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
dup_list = list(set(orig_list))
print(dup_list)

print("--------------------------")
print("dz2")
print("--------------------------")
"""
В большой текстовой строке подсчитать количество встречаемых
слов и вернуть 10 самых частых. Не учитывать знаки препинания
и регистр символов. За основу возьмите любую статью
из википедии или из документации к языку.
"""

text = "Python — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью," \
       " ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение " \
       "переносимости написанных на нём программ[27]. Язык является полностью объектно-ориентированным в том плане, что " \
       "всё является объектами[25]. Необычной особенностью языка является выделение блоков кода пробельными отступами." \
       "Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации[27]. " \
       "Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов[25]. Недостатками языка являются " \
       "зачастую более низкая скорость работы и более высокое потребление памяти написанных на нём программ по сравнению " \
       "с аналогичным кодом, написанным на компилируемых языках, таких как C или C++."

# удаляем знаки препинания и переводим все символы в нижний регистр
text = re.sub(r'[^\w\s]', '', text).lower()

# разбиваем текст на список слов
words = text.split()

# создаем словарь для подсчета количества каждого слова
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# сортируем словарь по убыванию количества встречаемости слов
sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# выводим 10 наиболее часто встречающихся слов
for word, count in sorted_word_count[:10]:
    print(word, count)

print("--------------------------")
print("dz3")
print("--------------------------")

"""
Создайте словарь со списком вещей для похода в качестве
ключа и их массой в качестве значения. Определите какие
вещи влезут в рюкзак передав его максимальную
грузоподъёмность. Достаточно вернуть один допустимый вариант.
"""
items = {
  'нож': 0.1,
  'фляга': 0.5,
  'компас': 0.2,
  'первая помощь': 0.5,
  'еда': 1.5,
  'спальник': 1.2,
  'палатка': 2.0,
  'карта': 0.3
}

max_weight = 5.0

backpack = {}
current_weight = 0

for item, weight in sorted(items.items(), key=lambda x: x[1], reverse=True):
    if current_weight + weight <= max_weight:
        backpack[item] = weight
        current_weight += weight

print(f'Предметы в рюкзаке: {backpack}')
print(f'Общий вес рюкзака: {sum(backpack.values())} кг')