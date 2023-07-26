def do_nothing():
    pass

do_nothing()
print(" ")

def make_a_sound():
    print('quack')
make_a_sound()
print(" ")

def agree():
    return True

if agree():
    print('Splendid!')
else:
    print('That was unexpected.')

def echo(anything):
    return anything + ' ' + anything
print(echo('Rumplestiltskin'))
print(" ")

def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == "green":
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."
comment = commentary('blue')
print(comment)
print(do_nothing())
print(" ")

thing = None
if thing:
    print("It's some thing")
else:
    print("It's no thing")

thing = None
if thing is None:
    print("It's nothing")
else:
    print("It's something")
print(" ")

def whatis(thing):
    if thing is None:
        print(thing, "is None")
    elif thing:
        print(thing, "is True")
    else:
        print(thing, "is False")

whatis(None)
whatis(True)
whatis(False)
print(" ")
whatis(0)
whatis(0.0)
whatis('')
whatis("")
whatis('''''')
whatis(())
whatis([])
whatis({})
whatis(set())
whatis(0.00001)
whatis([0])
whatis([''])
whatis(' ')
print(" ")

def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}
print(menu('chardonnay', 'chicken', 'cake'))
print(menu('beef', 'bagel', 'bordeaux'))
print(" ")

print(menu(entree='beef', dessert='bagel', wine='bordeaux'))
print(menu('frontenac', dessert='flan', entree='fish'))
print(" ")

def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}
print(menu('chardonnay', 'chicken'))
print(menu('dunkelfelder', 'duck', 'doughnut'))
print(" ")

def buggy(arg, result=[]):
    result.append(arg)
    print(result)
buggy('a')
buggy('b')
print(" ")

def works(arg):
    result = []
    result.append(arg)
    return result
print(works('a'))
print(works('b'))
print(" ")

def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)
nonbuggy('a')
nonbuggy('b')
print(" ")

def print_args(*args):
    print('Positional argument tuple:', args)

print_args()
print_args(3, 2, 1, 'wait!', 'uh...')
print(" ")

def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)
print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')
print(" ")

print_args(2, 5, 7, 'x')
args = (2, 5, 7, 'x')
print_args(args)
print_args(*args)
print(" ")

def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)
print_kwargs()
print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)
data = ['a', 'b', 'c', 'd', 'e', 'f']
print_data(data)
print(" ")
print_data(data, start=4)
print(" ")
print(print_data(data, end=2))
print(" ")

outside = ['one', 'fine', 'day']
def mangle(arg):
    arg[1] = 'terrible!'
print(outside)
mangle(outside)
print(outside)
print(" ")

def echo(anything):
    'echo returns its input argument'
    return anything

def print_if_true(thing, check):
    if check:
        print(thing)
#help(echo)
print(echo.__doc__)
print(" ")

def answer():
    print(42)
answer()
def run_something(func):
    func()
run_something(answer)
print(" ")

print(type(run_something))
def add_args(arg1, arg2):
    print(arg1 + arg2)
print(type(add_args))
print(" ")

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)
run_something_with_args(add_args, 5, 9)
print(" ")

add_args(5, 9)
print(" ")

def sum_args(*args):
    return sum(args)
def run_with_positional_args(func, *args):
    return func(*args)
print(run_with_positional_args(sum_args, 1, 2, 3, 4))
print(" ")

def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)
print(outer(4, 7))
print(" ")

def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)
print(knights('Ni!'))
print(" ")

def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2
a = knights2('Duck')
b = knights2('Hasenpfeffer')
print(type(a))
print(type(b))
print(a())
print(b())
print(" ")

def edit_story(words, func):
    for word in words:
        print(func(word))
stairs = ['thud', 'meow', 'thud', 'hiss']
def enliven(word):     # больше эмоций!
    return word.capitalize() + '!'
edit_story(stairs, enliven)
print(" ")
edit_story(stairs, lambda word: word.capitalize() + '!')
print(" ")

print(sum(range(1, 101)))
print(" ")

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step
print(my_range)
ranger = my_range(1, 5)
print(ranger)
print(" ")

for x in ranger:
    print(x)
print(" ")

for try_again in ranger:
    print(try_again)

genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))
print(genobj)
print(" ")

for thing in genobj:
    print(thing)

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function
print(" ")

def add_ints(a, b):
    return a + b
print(add_ints(3, 5))
print(" ")

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function
print(" ")

@document_it
@square_it
def add_ints(a, b):
    return a + b
add_ints(3, 5)
print(" ")
@square_it
@document_it
def add_ints(a, b):
    return a + b
add_ints(3, 5)
print(" ")
animal = 'fruitbat'
def print_global():
    print('inside print_global:', animal)
    print('at the top level:', animal)
print_global()
def change_and_print_global():
    print('inside change_and_print_global:', animal)
    animal = 'wombat'
    print('after the change:', animal)
def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))
change_local()
print(animal)
print(id(animal))
print(" ")

animal = 'fruitbat'
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)
print(animal)
change_and_print_global()
print(animal)
print(" ")

animal = 'fruitbat'
def change_local():
    animal = 'wombat'     # локальная переменная
    print('locals:', locals())
print(animal)
change_local()
print('globals:', globals())     # немного переформатировано для представления
print(" ")

def amazing():
    '''This is the amazing function.
    Want to see it again?'''
    print('This function is named:', amazing.__name__)
    print('And its docstring is:', amazing.__doc__)
amazing()

def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            for subitem in flatten(item):
                yield subitem
        else:
            yield item
lol = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]
print(flatten(lol))
print(list(flatten(lol)))
print(" ")

def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
lol = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]
print(list(flatten(lol)))
print(" ")

short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and', len(short_list)-1, ' but got',
          position)
print(" ")

short_list = [1, 2, 3]
while True:
    value = input('Position [q to quit]? ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        print('Something else broke:', other)
print(" ")
print('УПРАЖНЕНИЯ:')
print(" ")

# УПРАЖНЕНИЯ

# Определите функцию good() , которая возвращает следующий список:
# ['Harry', 'Ron', 'Hermione'].
def good():
    return['Harry', 'Ron', 'Hermione']
print(good())
print(" ")

# Определите функцию генератора get_odds(), которая возвращает нечетные
# числа из диапазона range(10). Используйте цикл for, чтобы найти и вывести
# третье возвращенное значение.
def get_odds():
    for number in range(1, 10, 2):
        yield number
count = 1
for number in get_odds():
    if count == 3:
        print("Третье возвращенное значения:", number)
        break
    count += 1
print(" ")

# Определите декоратор test, который выводит строку 'start' при вызове 
# функции и строку 'end', когда функция завершает свою работу.
def test(func):
    def new_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func
@test
def greeting():
    print("Greetings, Earthling")
greeting()
print(" ")

# Определите исключение OopsException. Сгенерируйте его и посмотрите, что
# произойдет. Затем напишите код, позволяющий поймать это исключение и 
# вывести строку 'Caught an oops'.
class OopsException(Exception):
    pass
try:
    raise OopsException
except OopsException:
    print('Caught an oops')
