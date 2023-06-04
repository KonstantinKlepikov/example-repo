# Выберите число от 1 до 10 и присвойте его переменной secret. Выберите еще
# одно число от 1 до 10 и присвойте его переменной guess. 
# Далее напишите условные проверки (if, else и elif), чтобы вывести строку 
# 'too low', если значение переменной guess меньше 7, 
# 'too high', если оно больше 7, 
# 'just right', если равно secret.
print(" ")
secret = 8
guess = 8
if guess < 7:
    print('too low') #Здесь есть подвох
elif guess == secret:
    print('just right')
else:
    print('too high') 
print(" ")
# Присвойте значения True или False переменным small и green. Напишите не-
# сколько утверждений if/else, которые выведут на экран информацию о том,
# соответствуют ли заданным условиям следующие растения: вишня, горошек,
# арбуз, тыква.
small = False
green = True
if small == True and green == True:
    print(bool(small),bool(green),'это вишня',',это горошек')
elif small == green == False:
    print('это тыква')
else:
    print('это арбуз')