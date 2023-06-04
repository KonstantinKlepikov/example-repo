print(" ")
print("Булевые значения")
a1 = bool(True)
print("a1 =",a1)
a2 = bool(1)
print("a2 =",a2)
a3 = bool(45)
print("a3 =",a3)
a4 = bool(-45)
print("a4 =",a4)
a5 = bool(False)
print("a5 =",a5)
a6 = bool(0)
print("a6 =",a6)
a7 = bool(0.0)
print("a7 =",a7)
print(" ")
print("Операции с целыми числами и переменными")
b1 = 5 + 9
print("b1 =",b1)
b2 = 100 - 7
print("b2 =",b2)
b3 = 4 - 10
print("b3 =",b3)
b4 = 5 + 9 + 3
print("b4 =",b4)
b5 = 4 + 3 - 2 - 1 + 6
print("b5 =",b5)
b6 = 5 + 9                +            3
print("b6 =",b6)
b7 = 6*7
print("b7 =",b7)
b7 = 7*6
print("b7 =",b7)
b8 = 6*7*2*3
print("b8 =",b8)
b9 = 9/5
print("b9 =",b9)
b9 = 9//5
print("b9 =",b9)
a = 95
print("a =",a)
a = a - 3
print("a - 3 =",a)
a = 95
a -= 3
print("a =",a)
a = 92
a += 8
print("a =",a)
a = 100
a *= 2
print("a =",a)
a = 200
a /= 3
print("a =",a)
a = 13  
a //= 4
print("a =",a)
a = 9 % 5
print("a =",a)
a = divmod(9,5)
print("a =",a)
b = 2 ** 3
print("b =",b)
b = 2.0 ** 3
print("b =",b)
b = 3 ** 2.0
print("b =",b)
b = 0 ** 3
print("b =",b)
print(" ")
print("Приоритет операций")
b = 2 + 3 * 4
print("b =",b)
b = (2 + 3) * 4
print("b =",b)
b = -5 ** 2
print("b =",b)
b = (-5) ** 2
print("b =",b)
print(" ")
print("Системы счисления")
с = 10
print("с =",с)
с = 0b10
print("с =",с)
с = 0o10
print("с =",с)
с = 0x10
print("с =",с)
value = 65
bin(value)
print(bin(value))
oct(value)
print(oct(value))
hex(value)
print(hex(value))
d = chr(65)
print(d)
ord('A')
print(ord('A'))
print(" ")
print("Преобразования типов")
print(int(True))
print(int(False))
print(bool(1))
print(bool(0))
print(int(98.6))
print(int(1.0e4))
print(bool(1.0))
print(bool(0.0))
print(int('99'))
print(int('-23'))
print(int('+12'))
print(int('1_000_000'))
print(int('10', 2)) #двоичная
print(int('10', 8)) #восьмеричная
print(int('10', 16)) # шестнадцатеричная
print(int('10', 22)) #двадцатидвухричная
print(int(12345))
print(4 + 7.0)
print(True + 2)
print(False + 5.0)
print(" ")
print("Насколько объемен тип int")
googol = 10**100
print(googol)
print(" ")
print(googol * googol)
print(" ")
print("Числа с плавающей точкой")
print(5.)
print(5.0)
print(05.0)
print(5e0)
print(5e1)
print(5.0e1)
print(5.0 * (10 ** 1))
million = 1_000_000.0
print(million)
print(1.0_0_1)
print(float(True))
print(float(False))
print(float(98))
print(float('99'))
print(float('98.6'))
print(float('-1.5'))
print(float('1.0e4'))
print(43 + 2.)
print(False + 0)
print(False + 0.)
print(True + 0)
print(True + 0.)
print(" ")
print("Упражнения")
seconds_per_min = 60 # 1 минута = 60 секунд 1 час = 60 минут сутки = 24 часа
seconds_per_hour = seconds_per_min ** 2
print("секунды в часе:",seconds_per_hour)
seconds_per_day = seconds_per_hour * 24
print("секунды в дне:",seconds_per_day)
print(seconds_per_day / seconds_per_hour)
print(seconds_per_day // seconds_per_hour)
#Я сделаль