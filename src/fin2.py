# Напишите с заглавной буквы слово, которое начинается с буквы m:
print(" ")
song = """When an eel grabs your arm, And it causes great harm,
That's - a moray!"""
song.replace('m', 'M', 100)
print(song.replace('m', 'M', 100))
print(" ")
# Выведите на экран все вопросы из списка,
# а также правильные ответы в таком виде:
# Q: вопрос
# A: ответ
questions = ["We don't serve strings around here. Are you a string?",
             "What is said on Father's Day in the forest?",
             "What makes the sound 'Sis! Boom! Bah!'?"]
answers = ["An exploding sheep.",
           "No, I'm a frayed knot.", "'Pop!' goes the weasel."]
print("Q: ", questions[0])
print("A: ", answers[0])
print(" ")
print("Q: ", questions[1])
print("A: ", answers[1])
print(" ")
print("Q: ", questions[2])
print("A: ", answers[2])
print(" ")
# Выведите на экран следующее стихотворение,
# используя старый стиль форматирования
# Подставьте в него такие строки: 'roast beef', 'ham', 'head' и 'clam':
kitty1 = 'My kitty cat likes'
kitty2 = 'My kitty cat fell on his'
kitty3 = 'And now thinks he is a'
thing1 = 'roast beef'
thing2 = 'ham'
thing3 = 'head'
thing4 = 'clam'
print(kitty1, '%s' % thing1)
print(kitty1, '%s' % thing2)
print(kitty2, '%s' % thing3)
print(kitty3, '%s.112' % thing4)
print(" ")
# Напишите письмо с использованием нового стиля форматирования.
sometext = """Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.
Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}."""
# Сохраните предложенную строку в переменной letter
# (она понадобится вам в упражнении ниже):
# Thank you for your letter. We are sorry that our {product}
# {verbed} in your {room}. Please note that it should never
# be used in a {room}, especially near any {animals}.
# Send us your receipt and {amount} for shipping and handling.
# We will send you another {product} that, in our tests,
# is {percent}% less likely to have {verbed}.
# Thank you for your support.
# Sincerely,
# {spokesman}
# {job_title}
this = 'sometext'
print("""some text {1} {0} {2} """.format('this', 'that', 'those'))
print(f'{this = } ')
print(" ")

# Присвойте значения переменным 'salutation', 'name', 'product', 'verbed'
# (глагол в прошедшем времени), 'room' , 'animals' , 'percent' , 'spokesman'
# и 'job_title'. С помощью функции letter.format() выведите на экран значение
# переменной letter, в которую подставлены эти значения.
product = "product"
verbed = "verbed"
room = "room"
animals = "animals"
amount = "amount"
percent = "percent"
print("Изначальный текст:")
print(f"""Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.
Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.""")
print(" ")

product = "chicken"
verbed = "verbed"
room = "box"
animals = "wolfes"
amount = "amount"
percent = "percent"
letter = """Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.
Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}."""
letter2 = """Thank you for your letter. We are sorry that our {}
{} in your {}. Please note that it should never
be used in a {}, especially near any {}.
Send us your receipt and {} for shipping and handling.
We will send you another {} that, in our tests,
is {}% less likely to have {}."""
print("Измененный текст:")
print(letter2.format(product, verbed, room, room, animals, amount, product,
                     percent, verbed))
print(" ")

# Форматирование строк %
duck = 'Boaty McBoatface'
pumpkin = 'Horsey McHorseface'
spitz = 'Trainy McTrainface'
print("And the winner in the tournament is %s" % pumpkin)
print(" ")

# Форматирование с функцией format()
print("And the winner in the tournament is {} or {} ".format(duck, spitz))
print(" ")
# Самый новый стиль: f-строки
print(f'among the three candidates {duck}, {pumpkin}, {spitz} in the \
      competition for the best name wins: {spitz}')
