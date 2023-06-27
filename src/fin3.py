# Создайте список years_list, содержащий год, в который вы родились, и каждый
# последующий год вплоть до вашего пятого дня рождения.
years_list = [1990 + n for n in range(6)]
#years_list = ["1990", "1991","1992", "1993", "1994", "1995"]

# В какой год из списка years_list был ваш третий день рождения?
print(" ")
print("Мой третий день рождения: ",years_list[2])
print(" ")
print(type(years_list))
# В какой год из списка years_list вам было больше всего лет?
print("Мне было больше всего лет в")
print(max(years_list))
print(" ")

# Создайте список things, содержащий три элемента: "mozzarella", "cinderella", "salmonella".
things = ["mozzarella", "cinderella", "salmonella"]

# Напишите с большой буквы тот элемент списка things, который означает чело-
# века, а затем выведите список. Изменился ли элемент списка?
str.title(things[1])
print(things) #Без изменений...
print(" ")
# Переведите сырный элемент списка things в верхний регистр целиком и выведите список.
things.remove("salmonella")
print(things)
print(" ")

# Удалите из списка things заболевание, получите Нобелевскую премию и затем выведите список на экран.
print(things[0:2])
print(" ")
#things.remove("salmonella")

# Создайте список с элементами "Groucho" , "Chico" и "Harpo" ; назовите его surprise.
surprise = ["Groucho" , "Chico" , "Harpo"]
print(type(surprise))
print(" ")

# Напишите последний элемент списка surprise со строчной буквы, затем вы-
# ведите эту строку в обратном порядке и с прописной буквы.
## str.lower(surprise) выдает ошибку descriptor 'lower' for 'str' objects doesn't apply to a 'list' object 
print(surprise[::-1])
print(" ")

# Используйте списковое включение, чтобы создать список с именем even, в ко-
# тором будут содержаться четные числа в промежутке range(10).
even = [number for number in range(10) if number % 2 == 0]
print(even)
print(" ")

# Попробуйте создать генератор рифм для прыжков через скакалку. Напе­чатайте
# последовательность двухстрочных рифм. Начните программу с этого фрагмента:
# Затем следуйте инструкциям.
# Для каждого кортежа (first, second) в списке rhymes.
### Для первой строки:
# - выведите на экран каждую строку списка start1: начните ее с большой
# буквы, а закончите восклицательным знаком с пробелом;
# - выведите на экран значение переменной first, также записав его с боль-
# шой буквы и с восклицательным знаком на конце.
# Для второй строки:
# - выведите на экран значение переменной start2 и пробел;
# - выведите на экран значение переменной second и точку.
start1 = ["fee", "fie", "foe"]
rhymes = [
("flop", "get a mop"),
("fope", "turn the rope"),
("fa", "get your ma"),
("fudge", "call the judge"),
("fat", "pet the cat"),
("fog", "walk the dog"),
("fun", "say we're done"),
]
start2 = "Someone better"