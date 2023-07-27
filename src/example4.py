print("Повторяем действия с помощью цикла while")
print(" ")
count = 1
while count <= 5:
    print(count)
    count += 1
print(" ")

print("Прерываем цикл с помощью оператора break")
print(" ")
while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())
print(" ")

print("Пропускаем итерации, используя оператор continue")
print(" ")
while True:
    value = input("Integer, please [q to quit]: ")
    if value == 'q':   # выход
        break
    number = int(value)
    if number % 2 == 0:   # нечетное число
        continue
    print(number, "squared is", number*number)
    print(" ")
print(" ")
print("Проверяем, завершился ли цикл раньше,с помощью блока else")
print(" ")

numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else:   # break не вызываем
    print('No even number found')

print(" ")
print("Выполняем итерации с использованием ключевых слов for и in ")
print(" ")

word = 'thud'
offset = 0
while offset < len(word):
    print(word[offset])
    offset += 1
print(" ")

for letter in word:
    print(letter)
print(" ")
print("Прерываем цикл с помощью оператора break")
word = 'thud'
for letter in word:
    if letter == 'u':
        break
    print(letter)
print(" ")
print("Проверяем, завершился ли цикл раньше,с помощью блока else")
print(" ")
word = 'thud'
for letter in word:
    if letter == 'x':
        print("Eek! An 'x'!")
    break
    print(letter)
else:
    print("No 'x' in there.")
print(" ")
print("Генерируем числовые последовательности с помощью функции range()")
print(" ")
for x in range(0, 3):
    print(x)
print(" ")
list(range(0, 3))
for x in range(2, -1, -1):
    print(x)
print(" ")
list(range(0, 11, 2))
for x in range(0, 11, 2):
    print(x)
