print(" ")
print("Сравниваем с помощью операторов if,elif и else")
print(" ")
furry = True
large = True
if furry:
    large = True
if furry:
    if large:
        print("It's a yeti.")
    else:
        print("It's a cat!")
else:
    if large:
        print("It's a whale!")
    else:
        print("It's a human. Or a hairless cat.")
print(" ")
color = "mauve"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color", color)
print(" ")
x = 7
print(bool(5 > x and x > 10))
print(" ")
print("Выполняем несколько сравнений с помощью оператора in")
print(" ")
letter = 'o'
if letter == 'a' or letter == 'e' or letter == 'i' \
                 or letter == 'o' or letter == 'u':
    print(letter, 'is a vowel')
else:
    print(letter, 'is not a vowel')

print(" ")
vowels = 'aeiou'
letter = 'o'
print(bool(letter in vowels))
print(" ")
if letter in vowels:
    print(letter, 'is a vowel')
print(" ")
letter = 'o'
vowel_set = {'a', 'e', 'i', 'o', 'u'}
print(bool(letter in vowel_set))
vowel_list = ['a', 'e', 'i', 'o', 'u']
print(bool(letter in vowel_list))
vowel_tuple = ('a', 'e', 'i', 'd', 'u')
print(bool(letter in vowel_tuple))
vowel_dict = {'a': 'apple', 'e': 'elephant', 'i': 'impala', 'w': 'ocelot',
              'u': 'unicorn'}
print(bool(letter in vowel_dict))
print(" ")
print("Новое: I Am the Walrus (оператор морж)")
print(" ")

tweet_limit = 280
tweet_string = "Blah" * 50
diff = tweet_limit - len(tweet_string)
if diff >= 0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))
print(" ")
tweet_limit = 280
tweet_string = "Blah" * 50
if diff := tweet_limit - len(tweet_string) >= 0:   # := оператор присваивания
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))

print(" ")
print("Создаем строки с помощью кавычек")
print(" ")
print("'Nay,' said the naysayer. 'Neigh?' said the horse.")
print('The rare double quote in captivity: ".')
print('A "two by four" is actually 1 1/2" × 3 1/2".')
print("'There's the man that shot my paw!' cried the limping hound.")
print('''Boom!''')
print("""Eek!""")
print(" ")

print("Создаем escape-последовательности с помощью символа '\' ")
print(" ")
palindrome = 'A man,\nA plan,\nA canal:\nPanama.'
print(palindrome)
print(" ")
print('\tabc')
print('a\tbc')
print('ab\tc')
print('abc\t')
print(" ")
testimony = "\"I did nothing!\" he said. \"Or that other thing.\""
testimony
print(testimony)
fact = "The world's largest rubber duck was 54'2\" by 65'7\" by 105'"
print(fact)
speech = 'The backslash (\\) bends over backwards to please you.'
print(speech)
print(" ")

print("Объединяем строки с использованием символа + ")
print(" ")
print('Release the kraken! ' + 'No, wait!')
vowels = ('a' "e" '''i''' 'o' """u""")
print(vowels)
a = 'Duck.'
b = a
c = 'Grey Duck!'
a + b + c
print(a, b, c)
print(" ")
print("Размножаем строки с помощью символа *")
print(" ")
start = 'Na ' * 4 + '\n'
middle = 'Hey ' * 3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end)
print(" ")
print("Извлекаем символ с помощью символов [ ]")
print(" ")
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])
print(letters[1])
print(letters[-1])
print(letters[-2])
print(letters[25])
print(letters[5])
name = 'Henny'
name.replace('H', 'P')
print('P' + name[1:])
print(" ")
print("Извлекаем подстроки, используя разделение")
print(" ")
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[:])
print(letters[20:])
print(letters[10:])
print(letters[12:15])
print(letters[-3:])
print(letters[18:-3])
print(letters[-6:-2])
print(letters[::7])
print(letters[4:20:3])
print(letters[19::4])
print(letters[:21:5])
print(letters[-1::-1])
print(letters[::-1])
print(letters[-50:])
print(letters[-51:-50])
print(letters[:70])
print(letters[70:71])

print("Измеряем длину строки с помощью функции len()")
print(" ")
print(len(letters))
empty = ""
print(len(empty))
print(" ")
print("Разделяем строку с помощью функции split()")
print(" ")
tasks = 'get gloves,get mask,give cat vitamins,call ambulance'
print(tasks.split(','))
print(" ")
print("Объединяем строки с помощью функции join()")
print(" ")
crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_string)
print(" ")
print("Заменяем символы с использованием функции replace()")
print(" ")
setup = "a duck goes into a bar..."
print(setup.replace('duck', 'marmoset'))
print(setup)
print(setup.replace('a ', 'a famous ', 100))
print(setup.replace('a', 'a famous', 100))
print(" ")
print("Устраняем символы с помощью функции strip()")
print(" ")
world = "   earth   "
print(world.strip())
print(world.strip(' '))
print(world.lstrip())
print(world.rstrip())
print(world.strip('!'))
blurt = "What the...!!?"
print(blurt.strip('.?!'))
import string
print(string.whitespace)
print(string.punctuation)
blurt = "What the...!!?"
print(blurt.strip(string.punctuation))
prospector = "What in tarnation ...??!!"
print(prospector.strip(string.whitespace + string.punctuation))
print(" ")
print("Поиск и выбор")
print(" ")
poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''
print(poem[:13])
print(len(poem))
print(bool(poem.startswith('All')))
print(bool(poem.endswith('That\'s all, folks!')))
word = 'the'
print(poem.find(word))
print(poem.index(word))
word = 'the'
print(poem.rfind(word))
print(poem.rindex(word))
word = "duck"
print(poem.find(word))
word = 'the'
print(poem.count(word))
print(bool(poem.isalnum()))
print(" ")
print("Регистр")
print(" ")
setup = 'a duck goes into a bar...'
print(setup.strip('.'))
print(setup.capitalize())
print(setup.title())
print(setup.upper())
print(setup.lower())
print(setup.swapcase())
print(" ")
print("Выравнивание")
print(" ")
print(setup.center(30))
print(setup.ljust(30))
print(setup.rjust(30))
print(" ")
print("Форматирование")
print(" ")
print('%s' % 42)
print('%d' % 42)
print('%x' % 42)
print('%o' % 42)
print('%s' % 7.03)
print('%f' % 7.03)
print('%e' % 7.03)
print('%g' % 7.03)
print('%d%%' % 100)
actor = 'Richard Gere'
cat = 'Chester'
weight = 28
print("My wife's favorite actor is %s" % actor)
print("Our cat %s weighs %s pounds" % (cat, weight))
thing = 'woodchuck'
print('%s' % thing)
print('%12s' % thing)
print('%+12s' % thing)
print('%-12s' % thing)
print('%.3s' % thing)
print('%12.3s' % thing)
print('%-12.3s' % thing)
thing = 98.6
print('%f' % thing)
print('%12f' % thing)
print('%+12f' % thing)
print('%-12f' % thing)
print('%.3f' % thing)
print('%12.3f' % thing)
print('%-12.3f' % thing)
thing = 9876
print('%d' % thing)
print('%12d' % thing)
print('%+12d' % thing)
print('%-12d' % thing)
print('%.3d' % thing)
print('%12.3d' % thing)
print('%-12.3d' % thing)
print(" ")
print("Новый стиль: используем символы {} и функцию format()")
print(" ")
thing = 'woodchuck'
print('{}'.format(thing))
thing = 'woodchuck'
place = 'lake'
print('The {} is in the {}.'.format(thing, place))
print('The {1} is in the {0}.'.format(place, thing))
print('The {thing} is in the {place}'.format(thing='duck', place='bathtub'))
d = {'thing': 'duck', 'place': 'bathtub'}
print('The {0[thing]} is in the {0[place]}.'.format(d))
thing = 'wraith'
place = 'window'
print('The {} is at the {}'.format(thing, place))
print('The {:10s} is at the {:10s}'.format(thing, place))
print('The {:<10s} is at the {:<10s}'.format(thing, place))
print('The {:^10s} is at the {:^10s}'.format(thing, place))
print('The {:>10s} is at the {:>10s}'.format(thing, place))
print('The {:!^10s} is at the {:!^10s}'.format(thing, place))
print(" ")
print("Самый новый стиль: f-строки")
print(" ")
thing = 'wereduck'
place = 'werepond'
print(f'The {thing} is in the {place}')
print(f'The {thing.capitalize()} is in the {place.rjust(20)}')
print(f'The {thing:>20} is in the {place:.^20}')
print(f'{thing =}, {place =}')
print(f'{thing[-4:] =}, {place.title() =}')
print(f'{thing = :>4.4}')
