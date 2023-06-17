# Создаем кортежи с помощью запятых и оператора ()
empty_tuple = ()
empty_tuple
one_marx = 'Groucho',
print(one_marx)
one_marx = 'Groucho',
print(one_marx)
one_marx = ('Groucho',)
print(one_marx)
one_marx = ('Groucho')
print(one_marx)
print(type(one_marx))
print(" ")
marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)
marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple)
one_marx = 'Groucho',
print(type(one_marx))
print(type('Groucho',))
print(type(('Groucho',)))
print(" ")
marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
print(a)
print(b)
print(c)
print(" ")
password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
print(password)
print(icecream)
print(" ")

# Создаем кортежи с помощью функции tuple()
marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_list))
print(" ")

# Объединяем кортежи с помощью оператора +
print(('Groucho',) + ('Chico', 'Harpo'))
print(" ")

# Размножаем элементы с помощью оператора *
print(('yada',) * 3)
print(" ")

# Сравниваем кортежи
a = (7, 2)
b = (7, 2, 9)
print(a == b)
print(a <= b)
print(a < b)

# Итерируем по кортежам с помощью for и in
words = ('fresh','out', 'of', 'ideas')
for word in words:
    print(word)
print(" ")

# Изменяем кортеж
t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
print(t1 + t2)
t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
t1 += t2
print(t1)
t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
print(id(t1))
t1 += t2
print(id(t1))

# Создаем списки с помощью скобок []
empty_list = [ ]
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
leap_years = [2000, 2004, 2008]
randomness = ["Punxsatawney", {"groundhog": "Phil"}, "Feb. 2"]
print(" ")

# Создаем список или преобразуем в список с помощью функции list()
another_empty_list = list()
print(another_empty_list)
print(list('cat'))
a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

# Создаем список из строки с использованием функции split()
talk_like_a_pirate_day = '9/19/2019'
print(talk_like_a_pirate_day.split('/'))
splitme = 'a/b//c/d///e'
print(splitme.split('/'))
splitme = 'a/b//c/d///e'
print(splitme.split('//'))
print(" ")

# Получаем элемент с помощью конструкции [смещение]
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])
print(marxes[1])
print(marxes[2])
print(marxes[-1])
print(marxes[-2])
print(marxes[-3])
print(" ")

# Извлекаем элементы с помощью разделения
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0:2])
print(marxes[::2])
print(marxes[::-2])
print(marxes[::-1])
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.reverse()
print(marxes)
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[4:])
print(marxes[-6:])
print(marxes[-6:-2])
print(marxes[-6:-4])
print(" ")

#Добавляем элемент в конец списка с помощью функции append()
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo')
print(marxes)
print(" ")

# Добавляем элемент на определенное место с помощью функции insert()
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.insert(2, 'Gummo')
print(marxes)
marxes.insert(10, 'Zeppo')
print(marxes)
print(" ")

# Размножаем элементы с помощью оператора *
print(["blah"] * 3)
print(" ")

# Объединяем списки с помощью метода extend() или оператора +
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes)
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
print(marxes)

# Изменяем элемент с помощью конструкции [смещение]
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
print(marxes)
print(" ")

# Изменяем элементы с помощью разделения
numbers = [1, 2, 3, 4]
numbers[1:3] = [8, 9]
print(numbers)
numbers = [1, 2, 3, 4]
numbers[1:3] = [7, 8, 9]
print(numbers)
numbers = [1, 2, 3, 4]
numbers[1:3] = []
print(numbers)
numbers = [1, 2, 3, 4]
numbers[1:3] = (98, 99, 100)
print(numbers)
numbers = [1, 2, 3, 4]
numbers[1:3] = 'wat?'
print(numbers)
print(" ")

# Удаляем заданный элемент с помощью оператора del
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
print(marxes[-1])
del marxes[-1]
print(marxes)
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo']
del marxes[1]
print(marxes)
print(" ")

# Удаляем элемент по значению с помощью функции remove()
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.remove('Groucho')
print(marxes)
print(" ")

# Получаем и удаляем заданный элемент с помощью функции pop()
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.pop())
print(marxes)
print(marxes.pop(1))
print(marxes)
print(" ")

# Удаляем все элементы с помощью функции clear()
work_quotes = ['Working hard?', 'Quick question!', 'Number one priorities!']
print(work_quotes)
work_quotes.clear()
print(work_quotes)
print(" ")

# Определяем смещение по значению с помощью функции index()
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.index('Chico'))
simpsons = ['Lisa', 'Bart', 'Marge', 'Homer', 'Bart']
print(simpsons.index('Bart'))
print(" ")

# Проверяем на наличие элемента в списке с помощью оператора in
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print('Groucho' in marxes)
print('Bob' in marxes)
words = ['a', 'deer', 'a' 'female', 'deer']
print('deer' in words)
print(" ")

# Подсчитываем количество включений значения с помощью функции count()
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes.count('Harpo'))
print(marxes.count('Bob'))
snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
print(snl_skit.count('cheeseburger'))
print(" ")

# Преобразуем список в строку с помощью функции join()
marxes = ['Groucho', 'Chico', 'Harpo']
print(', '.join(marxes))
friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
print(joined)
separated = joined.split(separator)
print(separated)
print(separated == friends)
print(" ")

# Меняем порядок элементов с помощью функций sort() или sorted()
marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
print(sorted_marxes)
print(marxes)
marxes.sort()
print(marxes)
numbers = [2, 1, 4.0, 3]
numbers.sort()
print(numbers)
numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)
print(numbers)
print(" ")

# Получаем длину списка с помощью функции len()
marxes = ['Groucho', 'Chico', 'Harpo']
print(len(marxes))
print(" ")

# Присваиваем с помощью оператора =
a = [1, 2, 3]
print(a)
b = a
print(b)
a[0] = 'surprise'
print(a)
print(b)
b[0] = 'I hate surprises'
print(b)
print(a)
print(" ")

# Копируем списки с помощью функций copy() и list() или путем разделения
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]
a[0] = 'integer lists are boring'
print(a)
print(b)
print(c)
print(d)
print(" ")

# Копируем все с помощью функции deepcopy()
a = [1, 2, [8, 9]]
b = a.copy()
c = list(a)
d = a[:]
print(a)
print(b)
print(c)
print(d)
a[2][1] = 10
print(a)
print(b)
print(c)
print(d)
import copy
a = [1, 2, [8, 9]]
b = copy.deepcopy(a)
print(a)
print(b)
a[2][1] = 10
print(a)
print(b)
print(" ")

# Сравниваем списки
a = [7, 2]
b = [7, 2, 9]
print(a == b)
print(a <= b)
print(a < b)
print(" ")

# Итерируем по спискам с помощью операторов for и in
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    print(cheese)
print(" ")
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith('g'):
        print("I won't eat anything that starts with 'g'")
        break
    else:
        print(cheese)
print(" ")
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith('x'):
        print("I won't eat anything that starts with 'x'")
        break
    else:
        print(cheese)
else:
    print("Didn't find anything that started with 'x'")
print(" ")
cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else: # отсутствие break означает отсутствие сыра
    print('This is not much of a cheese shop, is it?')

# Итерируем по нескольким последовательностям с помощью функции zip()
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "eat", fruit, "enjoy", dessert)
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
print(list(zip(english, french)))
print(dict(zip(english, french)))
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)
number_list = []
for number in range(1, 6):
    number_list.append(number)
print(number_list)
number_list = list(range(1, 6))
print(number_list)
number_list = [number for number in range(1,6)]
print(number_list)
number_list = [number-1 for number in range(1,6)]
print(number_list)
a_list = [number for number in range(1,6) if number % 2 == 1]
print(a_list)
print(" ")
rows = range(1,4)
cols = range(1,3)
for row in rows:
    for col in cols:
        print(row, col)
print(" ")
rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)
print(" ")
for row, col in cells:
    print(row, col)
print(" ")

# Списки списков
small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
print(all_birds)
print(" ")
print(all_birds[0])
print(" ")
print(all_birds[1])
print(" ")
print(all_birds[1][0])

# Включений кортежей не существует
number_thing = (number for number in range(1, 6))
print(type(number_thing))