# Напишите с заглавной буквы слово, которое начинается с буквы m:
print(" ")
song = """When an eel grabs your arm, And it causes great harm, That's - a moray!"""
song.replace('m','M',100)
print(song.replace('m','M',100))
print(" ")
# Выведите на экран все вопросы из списка, а также правильные ответы в таком виде:
# Q: вопрос
# A: ответ
questions = ["We don't serve strings around here. Are you a string?",
 "What is said on Father's Day in the forest?", "What makes the sound 'Sis! Boom! Bah!'?" ]
answers = ["An exploding sheep.","No, I'm a frayed knot.","'Pop!' goes the weasel."]
print("Q: ",questions[0])
print("A: ",answers[0])
print(" ")
print("Q: ",questions[1])
print("A: ",answers[1])
print(" ")
print("Q: ",questions[2])
print("A: ",answers[2])
print(" ")
# Выведите на экран следующее стихотворение, используя старый стиль форматирования
# Подставьте в него такие строки: 'roast beef', 'ham', 'head' и 'clam':
kitty1 = 'My kitty cat likes'
kitty2 = 'My kitty cat fell on his'
kitty3 = 'And now thinks he is a'
thing1 = 'roast beef'
thing2 = 'ham'
thing3 = 'head'
thing4 = 'clam'
print(kitty1, '%s' %thing1)
print(kitty1, '%s' %thing2)
print(kitty2, '%s' %thing3)
print(kitty3, '%s.112' %thing4)
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

#Thank you for your letter. We are sorry that our {product}
#{verbed} in your {room}. Please note that it should never
#be used in a {room}, especially near any {animals}.
#Send us your receipt and {amount} for shipping and handling.
#We will send you another {product} that, in our tests,
#is {percent}% less likely to have {verbed}.
#Thank you for your support.
#Sincerely,
#{spokesman}
#{job_title}
this = 'sometext'
print("""some text {1} {1} """.format('this', 'that'))
print(f'some text {this = } ') 

# bigtext = f"""Thank you for your letter. We are sorry that our {product}
# {verbed} in your {room}. Please note that it should never
# be used in a {room}, especially near any {animals}.
# Send us your receipt and {amount} for shipping and handling.
# We will send you another {product} that, in our tests,
# is {percent}% less likely to have {verbed}.
# Thank you for your support.
# Sincerely,
# {spokesman}
# {job_title}
# """ 