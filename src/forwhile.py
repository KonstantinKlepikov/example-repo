# цикл for, чтобы вывести на экран значения списка [3, 2, 1, 0].
print(" ")
# list(range(0, 3))
for x in range(3, -1, -1):
    print(x)
print(" ")

# Присвойте значение 7 переменной guess_me и значение 1 переменной number.
# Напишите цикл while, который сравнивает переменные number и guess_me.
# Выведите строку 'too low', если значение переменной number меньше значе-
# ния переменной guess_me. Если значение переменной start равно значению
# переменной guess_me, выведите строку 'found it!' и выйдите из цикла. Если
# значение переменной number больше значения переменной guess_me, выведите
# строку 'oops' и выйдите из цикла. Увеличьте значение переменной number на
# выходе из цикла.
number = 0
guess_me = 8
start_text = input('Введите число для поиска: ')
start = int(start_text)
while number < start < guess_me:
    start += 1
    print('too short!', start - 1)
    continue
if start == guess_me:
    print('found it:', guess_me - 1)
else:
    print('oops!')
print(" ")
# print('No even number found')
# Присвойте значение 5 переменной guess_me. Используйте цикл for для того,
# чтобы проитерировать с помощью переменной number по диапазону range(10).
# Если значение переменной number меньше, чем значение guess_me, выведите
# на экран сообщение 'too low'. Если оно равно значению guess_me — выведите
# сообщение 'found it!', а затем выйдите из цикла. Если значение переменной
# number больше, чем guess_me, выведите на экран сообщение 'oops' и выйдите
# из цикла.
number = range(10)
for guess_me in number:
    print('too short!', guess_me)
    guess_me += 1
    if guess_me == 5:
        print('found it')
        break
else:
    print('oops')
