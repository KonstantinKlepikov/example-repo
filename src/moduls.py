#УПРАЖНЕНИЯ

# Создайте файл с именем zoo.py. В нем объявите функцию hours(), которая
# выводит на экран строку 'Open 9-5 daily'. Далее используйте интерактивный
# интерпретатор, чтобы импортировать модуль zoo и вызвать его функцию
# hours().                                                                      # (см zoo.py)

# В интерактивном интерпретаторе импортируйте модуль zoo под именем
# menagerie и вызовите его функцию hours().
import zoo as menagerie
menagerie.hours()
print(" ")

# Оставаясь в интерпретаторе, импортируйте непосредственно функцию hours()
# из модуля zoo и вызовите ее.
from zoo import hours
hours()
print(" ")

# Импортируйте функцию hours() под именем info и вызовите ее.
from zoo import hours as info
info()
print(" ")

# Создайте словарь с именем plain, содержащий пары «ключ — значение» 'a': 1,
# 'b': 2 и 'c':3, а затем выведите его на экран.
plain =  {'a':1, 'b':2, 'c':3}
print(plain)

# Создайте OrderedDict с именем fancy из пар «ключ — значение», приведенных
# в упражнении 11.5, и выведите его на экран. Изменился ли порядок ключей?
from collections import OrderedDict
fancy = OrderedDict([('a',1),('b',2),('c',3)])
print(fancy)
print(" ")

# Создайте defaultdict с именем dict_of_lists и передайте ему аргумент
# list. Создайте список dict_of_lists['a'] и присоедините к нему значение
# 'something for a' за одну операцию. Выведите на экран dict_of_lists['a'].
from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])