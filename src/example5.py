empty_dict = {}
print(empty_dict)
bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses",
}
print(bierce)
print(" ")

acme_customer = {'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}
print(acme_customer)
print(" ")
acme_customer = dict(first="Wile", middle="E", last="Coyote")
print(acme_customer)
print(" ")

lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(lol))
print(" ")

lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
print(dict(lot))
print(" ")

tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
print(dict(tol))
print(" ")

los = ['ab', 'cd', 'ef']
print(dict(los))
print(" ")

tos = ('ab', 'cd', 'ef')
print(dict(tos))
print(" ")

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}
print(pythons)
print(" ")

pythons['Gilliam'] = 'Gerry'
print(pythons)
print(" ")

pythons['Gilliam'] = 'Terry'
print(pythons)
print(" ")

some_pythons = {
    'Graham': 'Chapman',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Michael': 'Palin',
    'Terry': 'Jones',
}
print(some_pythons)
print(" ")
print(some_pythons['John'])
print('Groucho' in pythons)
print(pythons.get('John'))
print(pythons.get('Groucho', 'Not a Python'))
print(pythons.get('Groucho'))
print(" ")

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
print(signals.keys())
print(" ")

print(list(signals.keys()))
print(list(signals.values()))
print(list(signals.items()))
print(len(signals))
print(" ")

first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}
print({**first, **second})
third = {'d': 'donuts'}
print({**first, **third, **second})
print(" ")

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Gilliam': 'Terry',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}
print(pythons)
print(" ")

others = {'Marx': 'Groucho', 'Howard': 'Moe'}
pythons.update(others)
print(pythons)
print(" ")

first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}
first.update(second)
print(first)
print(" ")

del pythons['Marx']
print(pythons)
del pythons['Howard']
print(pythons)
print(" ")

print(len(pythons))
print(pythons.pop('Palin'))
print(len(pythons))
print(pythons.pop('First', 'Hugo'))
print(len(pythons))
print(" ")

pythons.clear()
print(pythons)
pythons = {}
print(pythons)
print(" ")

pythons = {'Chapman': 'Graham', 'Cleese': 'John',
                      'Jones': 'Terry', 'Palin': 'Michael', 'Idle': 'Eric'}
print('Chapman' in pythons)
print('Palin' in pythons)
print('Gilliam' in pythons)

signals = {'green': 'go',
           'yellow': 'go faster',
           'red': 'smile for the camera'}
save_signals = signals
signals['blue'] = 'confuse everyone'
print(save_signals)
print(" ")

original_signals = {'green': 'go',
                    'yellow': 'go faster',
                    'red': 'smile for the camera',
                    'blue': 'confuse everyone'}
print(original_signals)
print(" ")

signals = {'green': 'go',
                    'yellow': 'go faster',
                    'red': ['stop', 'smile']}
signals_copy = signals.copy()
print(signals)
print(signals_copy)
print(" ")

signals['red'][1] = 'sweat'
print(signals)
print(signals_copy)
print(" ")

import copy
signals = {'green': 'go',
           'yellow': 'go faster',
           'red': ['stop', 'smile']}
signals_copy = copy.deepcopy(signals)
print(signals)
print(signals_copy)
signals['red'][1] = 'sweat'
print(signals)
print(signals_copy)
print(" ")

a = {1: 1, 2: 2, 3: 3}
b = {3: 3, 1: 1, 2: 2}
print(a == b)
a = {1: [1, 2], 2: [1], 3: [1]}
b = {1: [1, 1], 2: [1], 3: [1]}
print(a == b)
print(" ")

accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
              'person': 'Col. Mustard'}
for card in accusation:   # или for card in accusation.keys():
    print(card)
print(" ")

for value in accusation.values():
    print(value)
print(" ")

for item in accusation.items():
    print(item)
print(" ")

for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)
print(" ")

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)
print(" ")

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)
print(" ")

vowels = 'aeiou'
word = 'onomatopoeia'
vowel_counts = {letter: word.count(letter) for letter in set(word) if letter
                in vowels}
print(vowel_counts)
print(" ")

empty_set = set()
print(empty_set)
even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)
odd_numbers = {1, 3, 5, 7, 9}
print(odd_numbers)
print(" ")

print(set('letters'))
print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']))
print(set(('Ummagumma', 'Echoes', 'Atom Heart Mother')))
print(set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'}))
print(" ")

reindeer = set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])
print(len(reindeer))
s = set((1, 2, 3))
print(s)
s.add(4)
print(s)
s = set((1, 2, 3))
s.remove(3)
print(s)
print(" ")

furniture = set(('sofa', 'ottoman', 'table'))
for piece in furniture:
    print(piece)
print(" ")

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}
for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)
print(" ")

for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or
                                    'cream' in contents):
        print(name)
print(" ")

for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)
print(" ")

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)
print(" ")

bruss = drinks['black russian']
wruss = drinks['white russian']
a = {1, 2}
b = {2, 3}
print(a & b)
print(a.intersection(b))
print(bruss & wruss)
print(a | b)
print(a.union(b))
print(bruss | wruss)
print(a - b)
print(a.difference(b))
print(bruss - wruss)
print(wruss - bruss)
print(a ^ b)
print(a.symmetric_difference(b))
print(bruss ^ wruss)
print(" ")

print(a <= b)
print(a.issubset(b))
print(bruss <= wruss)
print(a <= a)
print(a.issubset(a))
print(a < b)
print(a < a)
print(bruss < wruss)
print(a >= b)
print(a.issuperset(b))
print(wruss >= bruss)
print(a >= a)
print(a.issuperset(a))
print(a > b)
print(wruss > bruss)
print(a > a)
print(" ")

a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)
print(frozenset([3, 2, 1]))
print(frozenset(set([2, 1, 3])))
print(frozenset({3, 1, 2}))
print(frozenset((2, 3, 1)))
fs = frozenset([3, 2, 1])
print(fs)
print(" ")

marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = 'Groucho', 'Chico', 'Harpo'
marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}
marx_set = {'Groucho', 'Chico', 'Harpo'}
print(marx_list[2])
print(marx_tuple[2])
print(marx_dict['Harpo'])
print('Harpo' in marx_list)
print('Harpo' in marx_tuple)
print('Harpo' in marx_dict)
print('Harpo' in marx_set)
print(" ")

marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']
tuple_of_lists = marxes, pythons, stooges
print(tuple_of_lists)
print(" ")

list_of_lists = [marxes, pythons, stooges]
print(list_of_lists)
print(" ")

dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
print(dict_of_lists)
