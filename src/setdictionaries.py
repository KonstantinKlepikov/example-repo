# Создайте англо-французский словарь с названием e2f и выведите его на экран.
# Вот ваши первые слова: dog/chien, cat/chat и walrus/morse.
print(" ")
e2f = {'dog':'chien', 'cat':'chat' , 'walrus':'morse'}
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
life_list = {"cats":["Henri", "Grumpy", "Lucky"],"octopi":{},"emus":{}}
life = {"animals":life_list, "plants":{}, "others":{}}
print("Ключ 1 = ",life.keys())
print("Ключ 2 = ",life["animals"].keys())
print("Ключ 3 = ",life["animals"]["cats"])
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
for i in range(10):
    squares[i] = i**2
    print(squares[i])
print(" ")
# Используйте генератор множества, чтобы создать множество odd из нечетных
print("Введите число:")
number = int(input())
even = 0
odd = 0
digits = "02468"
for i in number:
    if i in digits:
        even += 1
    else:
        odd += 1

print("Even: %d, odd: %d" % (even, odd))  #Не понимаю почему выдает ошибку. Цикл вроде правильно составил.

# Используйте включение генератора, чтобы вернуть строку 'Got ' и числа из
# диапазона range(10). Итерируйте по этой конструкции с помощью цикла for.


# Используйте функцию zip() , чтобы создать словарь из кортежа ключей
# ('optimist', 'pessimist', 'troll') и кортежа значений ('The glass is half full',
# 'The glass is half empty', 'How did you get a glass?').


# Используйте функцию zip(), чтобы создать словарь с именем movies, в котором
# объединены списки titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On
# a Plane'] и plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check
# your exits'].