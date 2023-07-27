# Создайте англо-французский словарь с названием e2f и выведите его на экран.
# Вот ваши первые слова: dog/chien, cat/chat и walrus/morse.
print(" ")
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print(type(e2f))
print(e2f)
print(" ")

# Используя словарь e2f, выведите французский вариант слова walrus.
print(e2f['walrus'])
print(" ")

# Создайте французско-английский словарь f2e на основе словаря e2f .
# Используйте метод items.
f2e = {}
for english, french in e2f.items():
    f2e[french] = english
print(f2e)
print(" ")

# Используя словарь f2e, выведите английский вариант слова chien.
print(f2e['chien'])
print(" ")

# Выведите на экран множество английских слов из ключей словаря e2f.
print(set(e2f.keys()))

# Создайте многоуровневый словарь life. Используйте следующие строки для
# ключей верхнего уровня: 'animals', 'plants' и 'other'. Сделайте так, чтобы
# ключ 'animals' ссылался на другой словарь, имеющий ключи 'cats', 'octopi'
# и 'emus'. Сделайте так, чтобы ключ 'cats' ссылался на список строк со значени-
# ями 'Henri', 'Grumpy' и 'Lucy'. Остальные ключи должны ссылаться на пустые
# словари.
life_list = {"cats": ["Henri", "Grumpy", "Lucky"], "octopi": {}, "emus": {}}
life = {"animals": life_list, "plants": {}, "others": {}}
print("Ключ 1 = ", life.keys())
print("Ключ 2 = ", life["animals"].keys())
print("Ключ 3 = ", life["animals"]["cats"])
print(" ")

# Выведите на экран высокоуровневые ключи словаря life.
print(life.keys())
print(" ")
# Выведите на экран ключи life['animals'].
print(life['animals'])
print(type(life['animals']))
print(" ")

# Выведите значения life['animals']['cats'].
print(life['animals']['cats'])
print(type(life['animals']['cats']))
print(" ")

# Используйте генератор словаря, чтобы создать словарь squares. Используйте
# range(10), чтобы получить ключи. В качестве значений используйте возведен-
# ное в квадрат значение каждого ключа.
squares = {}
squares = {k: k**2 for k in range(10)}
print(squares)
print(" ")

# Используйте включение генератора, чтобы вернуть строку 'Got ' и числа из
# диапазона range(10). Итерируйте по этой конструкции с помощью цикла for.
for thing in ('Got %s' % number for number in range(10)):
    print(thing)
print(" ")

# Используйте   функцию zip() , чтобы создать словарь из кортежа ключей
# ('optimist', 'pessimist', 'troll') и кортежа значений
# ('The glass is half full',
# 'The glass is half empty', 'How did you get a glass?').
keys = ('optimist', 'pessimist', 'troll')
values = ('The glass is half full',
          'The glass is half empty',
          'How did you get a glass?')
print(dict(zip(keys, values)))
print(" ")

# Используйте функцию zip(), чтобы создать словарь с именем movies, в котором
# объединены списки titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On
# a Plane'] и plots = ['A nun turns into a monster', 'A haunted yarn shop',
# 'Check your exits'].
titles = ['Creature of Habbit',
          'Crewel Fate',
          'Sharks On a Plane']
plots = ['A nun turns into a monster',
         'A haunted yarn shop',
         'Check your exits']
movies = dict(zip(titles, plots))
print(movies)
