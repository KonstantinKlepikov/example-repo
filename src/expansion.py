# ОБРАБАТЫВАЕМ ДАННЫЕ

# Создайте строку Unicode с именем mystery
# и присвойте ей значение '\U0001f4a9'.
# Выведите на экран значение mystery и ее имя Unicode.
import unicodedata
mystery = '\U0001f984'
print(mystery)
print(unicodedata.name(mystery))
print(" ")

# Закодируйте строку mystery, на этот раз с использованием
# кодировки UTF-8, в переменную типа bytes
# с именем pop_bytes. Выведите на экран
# значение переменной pop_bytes.
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)
print(" ")

# Используя кодировку UTF-8, декодируйте переменную popbytes
# в строку pop_string. Выведите на экран значение
# переменной pop_string. Равно ли оно
# значению переменной mystery?
pop_string = pop_bytes.decode('utf-8')
print(pop_string)
print(pop_string == mystery)
print(" ")

# При работе с текстом вам могут пригодиться регулярные выражения.
# Мы воспользуемся ими несколькими способами
# в следующем примере текста. Перед вами стихотворение
# Ode on the Mammoth Cheese, написанное Джеймсом Макинтайром
# в 1866 году во славу головки сыра весом 7000 фунтов, которая
# была изготовлена в Онтарио и отправлена в международное путешествие.
# Если не хотите самостоятельно перепечатывать это стихотворение,
# используйте свой любимый поисковик и скопируйте текст в программу.
# Или скопируйте стихотворение из проекта «Гутенберг»
# (http://bit.ly/mcintyre-poetry).
# Назовите следующую строку mammoth.
mammoth = '''
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.
May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.
Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.
We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.
'''

# Импортируйте модуль re, чтобы использовать функции регулярных
# выражений в Python. Примените функцию re.findall() для
# вывода на экран всех слов, которые начинаются с буквы с.
import re
pat = r'\bc\w*'
print(re.findall(pat, mammoth))
print(" ")

# Найдите все четырехбуквенные слова, которые начинаются с буквы c.
pat = r'\bc\w{3}'
print(re.findall(pat, mammoth))
print(" ")

# Найдите все слова, которые заканчиваются на букву r.
pat = r'\b[\w\']*l\b'
print(re.findall(pat, mammoth))
print(" ")

# Найдите все слова, которые содержат три гласные подряд.
pat = r'\b\w*[aeiou]{3}[^aeiou\s]\w*\b'
print(re.findall(pat, mammoth))
print(" ")

# Используйте метод unhexlify для того, чтобы преобразовать эту
# шестнадцатеричную строку, созданную путем объединения двух строк
# для размещения на странице, в переменную типа bytes с именем gif.
# '47494638396101000100800000000000ffffff21f9' +
# '0401000000002c000000000100010000020144003b'
import binascii
hex_str = '47494638396101000100800000000000ffffff21f9' + \
            '0401000000002c000000000100010000020144003b'
gif = binascii.unhexlify(hex_str)
print(len(gif))
print(" ")

# Байты, содержащиеся в переменной gif, определяют однопиксельный
# прозрачный GIF-файл. Этот формат является одним из самых
# распространенных. Корректный файл формата GIF
# начинается со строки GIF89a. Корректен ли этот файл?
print(gif[:6] == b'GIF89a')
print(gif[:6] == 'GIF89a')
print(type(gif))
print(type('GIF89a'))
print(type(b'GIF89a'))

# Ширина GIF-файла в пикселах является шестнадцатибитным целым числом
# с обратным порядком байтов, которое начинается со смещения 6 байт.
# Высота имеет такой же размер и начинается со смещения 8 байт. Извлеките
# и выведите на экран эти значения для переменной gif. Равны ли они 1?
import struct
width, height = struct.unpack('<HH', gif[6:10])
print(width, height)
print(" ")

# КАЛЕНДАРИ И ЧАСЫ

# Запишите текущие дату и время как строку в текстовый файл today.txt.
from datetime import date
now = date.today()
now_str = now.isoformat()
with open('today.txt', 'wt') as output:
    print(now_str, file=output)

# Прочтите текстовый файл today.txt и разместите данные
# в строке today_string.
with open('today.txt', 'rt') as input:
    today_string = input.read()

print(today_string)
print(" ")

# Проанализируйте дату из строки today_string.
from datetime import datetime
fmt = '%Y-%m-%d\n'
print(datetime.strptime(today_string, fmt))
print(" ")

# Создайте объект date с датой вашего рождения.
my_day = date(1982, 8, 14)
print(my_day)
# datetime.date(1982, 8, 14)
print(" ")

# В какой день недели вы родились?
print(my_day.weekday())
print(" ")
print(my_day.isoweekday())
print(" ")

# Когда вам будет (или уже было) 10 000 дней от роду?
from datetime import timedelta
party_day = my_day + timedelta(days=10000)
print(party_day)
print(" ")

# ФАЙЛЫ И КАТАЛОГИ

# Выведите на экран список файлов текущего каталога.
import os
print(os.listdir('.'))
print(" ")

# Выведите на экран список всех файлов родительского каталога.
import os
print(os.listdir('..'))
print(" ")

# Присвойте строку This is a test of the emergency text system
# переменной test1 и запишите эту переменную в файл с именем test.txt.
test1 = 'This is a test of the emergency text system'
print(len(test1))
print(" ")

# Откройте файл test.txt и считайте его содержимое в строку test2.
# Будут ли одинаковыми строки test1 и test2?
with open('test.txt', 'rt') as infile:
    test2 = infile.read()

print(len(test2))
print(" ")
print(test1 == test2)
print(" ")

# ДАННЫЕ ВО ВРЕМЕНИ: ПРОЦЕССЫ И КОНКУРЕНТНОСТЬ

# Используйте модуль multiprocessing, чтобы создать три отдельных
# процесса. Заставьте каждый из них подождать случайное количество
# секунд между нулем и единицей, вывести текущее время,
# а затем завершить работу.
import multiprocessing
def now(seconds):
    from datetime import datetime
    from time import sleep
    sleep(seconds)
    print('wait', seconds, 'seconds, time is', datetime.utcnow())

if __name__ == '__main__':
    import random
    for n in range(3):
        seconds = random.random()
        proc = multiprocessing.Process(target=now, args=(seconds,))
        proc.start()

# ДАННЫЕ В КОРОБКЕ: УСТОЙЧИВЫЕ ХРАНИЛИЩА

# Сохраните следующие несколько строк в файл books.csv. Обратите внимание
# на то, что, если поля разделены запятыми, вам нужно заключить в кавычки
# поле, содержащее запятую:
text = '''author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"
'''
with open('test.csv', 'wt') as outfile:
    print(outfile.write(text))

print(" ")

# Используйте модуль csv и его метод DictReader, чтобы считать содержимое
# файла books.csv в переменную books. Выведите на экран
# значения переменной books. Обработал ли метод DictReader
# кавычки и запятые в заголовке второй книги?
