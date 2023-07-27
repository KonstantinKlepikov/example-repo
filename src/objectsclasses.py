class Cat:
    pass


a_cat = Cat()
another_cat = Cat()


class Cat:
    pass


a_cat = Cat()
print(a_cat)
another_cat = Cat()
print(another_cat)
print(" ")

a_cat.age = 3
a_cat.name = "Mr. Fuzzybuttons"
a_cat.nemesis = another_cat
print('Возраст:', a_cat.age, 'years')
print('Имя:', a_cat.name)
print(a_cat.nemesis)
a_cat.nemesis.name = "Mr. Bigglesworth"
print(a_cat.nemesis.name)
print(" ")


class Cat:
    def __init__(self):
        pass


class Cat():
    def __init__(self, name):
        self.name = name


furball = Cat('Grumpy')
print('Our latest addition: ', furball.name)
print(" ")


class Car():
    pass


class Yugo(Car):
    pass


print(issubclass(Yugo, Car))
give_me_a_car = Car()
give_me_a_yugo = Yugo()


class Car():
    def exclaim(self):
        print("I'm a Car!")


class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")


give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()
print(" ")


class Person():
    def __init__(self, name):
        self.name = name


class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name


class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"


person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
print(person.name)
print(doctor.name)
print(lawyer.name)
print(" ")


class Car():
    def exclaim(self):
        print("I'm a Car!")


class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

    def need_a_push(self):
        print("A little help here?")


give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_yugo.need_a_push()
print(" ")


class Person():
    def __init__(self, name):
        self.name = name


class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name)
print(bob.email)


class EmailPerson(Person):
    def __init__(self, name, email):
        self.name = name
        self.email = email


print(" ")


class Animal:
    def says(self):
        return 'I speak!'


class Horse(Animal):
    def says(self):
        return 'Neigh!'


class Donkey(Animal):
    def says(self):
        return 'Hee-haw!'


class Mule(Donkey, Horse):
    pass


class Hinny(Horse, Donkey):
    pass


print(Mule.mro())
print(Hinny.mro())
print(" ")

mule = Mule()
hinny = Hinny()
print(mule.says())
print(hinny.says())
print(" ")


class PrettyMixin():
    def dump(self):
        import pprint
        pprint.pprint(vars(self))


class Thing(PrettyMixin):
    pass


t = Thing()
t.name = "Nyarlathotep"
t.feature = "ichor"
t.age = "eldritch"
t.dump()
print(" ")

a_car = Car()
a_car.exclaim()

Car.exclaim(a_car)
print(" ")


class Duck:
    def __init__(self, input_name):
        self.name = input_name


fowl = Duck('Daffy')
print(fowl.name)
fowl.name = 'Daphne'
print(fowl.name)
print(" ")


class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name


don = Duck('Donald')
print(don.get_name())
print(" ")
print(don.set_name('Donna'))
print(" ")
print(don.get_name())
print(" ")


class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)


don = Duck('Donald')
print(don.get_name())
print(" ")
print(don.set_name('Donna'))
print(" ")
print(don.get_name())
print(" ")

don = Duck('Donald')
print(don.name)
print(" ")
don.name = 'Donna'
print(don.name)
print(" ")


class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name


fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Donald'
print(" ")
print(fowl.name)
print(" ")


class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius


c = Circle(5)
print(c.radius)
print(c.diameter)
c.radius = 7
print(c.diameter)
print(" ")


class Duck():
    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.__name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name


fowl = Duck('Howard')
print(fowl.name)
print(" ")
fowl.name = 'Donald'
print(fowl.name)
print(" ")


class Fruit:
    color = 'red'


blueberry = Fruit()
print(Fruit.color)
print(blueberry.color)
blueberry.color = 'blue'
print(blueberry.color)
print(Fruit.color)
Fruit.color = 'orange'
print(Fruit.color)
print(blueberry.color)
new_fruit = Fruit()
print(new_fruit.color)
print(" ")


class A():
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A!")

    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")


easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()
print(" ")


class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')


CoyoteWeapon.commercial()
print(" ")


class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words + '.'


class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'


class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'


hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())
hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())
hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())
print(" ")


class BabblingBrook():
    def who(self):
        return 'Brook'

    def says(self):
        return 'Babble'


brook = BabblingBrook()


def who_says(obj):
    print(obj.who(), 'says', obj.says())


who_says(hunter)
who_says(hunted1)
who_says(hunted2)
who_says(brook)
print(" ")


class Word():
    def __init__(self, text):
        self.text = text

    def equals(self, word2):
        return self.text.lower() == word2.text.lower()


first = Word('ha')
second = Word('HA')
third = Word('eh')
print(first.equals(second))
print(first.equals(third))
print(" ")


class Word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()


first = Word('ha')
second = Word('HA')
third = Word('eh')
print(first == second)
print(first == third)
print(" ")

first = Word('ha')
print(first)
print(" ")


class Word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

    def __str__(self):
        return self.text

    def __repr__(self):
        return Word("' self.text '")


first = Word('ha')
print(first)
print(" ")


class Bill():
    def __init__(self, description):
        self.description = description


class Tail():
    def __init__(self, length):
        self.length = length


class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print('This duck has a', self.bill.description, 'bill and a',
              self.tail.length, 'tail')


а_tail = Tail('long')
а_bill = Bill('wide orange')
duck = Duck(а_bill, а_tail)
duck.about()
print(" ")


from collections import namedtuple


Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)
print(duck.bill)
print(duck.tail)
print(" ")

parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
print(duck2)
duck2 = Duck(bill='wide orange', tail='long')
duck3 = duck2._replace(tail='magnificent', bill='crushing')
print(duck3)
duck_dict = {'bill': 'wide orange', 'tail': 'long'}
print(duck_dict)
duck_dict['color'] = 'green'
print(duck_dict)
print(" ")


class TeenyClass():
    def __init__(self, name):
        self.name = name


teeny = TeenyClass('itsy')
print(teeny.name)


from dataclasses import dataclass


@dataclass
class TeenyDataClass:
    name: str


teeny = TeenyDataClass('bitsy')
print(teeny.name)
print(" ")


from dataclasses import dataclass


@dataclass
class AnimalClass:
    name: str
    habitat: str
    teeth: int = 0


snowman = AnimalClass('yeti', 'Himalayas', 46)
duck = AnimalClass(habitat='lake', name='duck')
print(snowman)
print(duck)
print(duck.habitat)
print(snowman.teeth)
print(" ")

# УПРАЖНЕНИЯ

# Создайте класс Thing, не имеющий содержимого, и выведите его на экран.
# Затем создайте объект example этого класса и также выведите его. Совпада-
# ют ли выведенные значения?


class Thing:
    pass


print(Thing)
example = Thing()
print(example)
print(Thing is Thing())
print(Thing == Thing())
print("Выведенные значения не совпадают")
print(" ")

# Создайте новый класс с именем Thing2 и присвойте атрибуту класса letters зна-
# чение 'abc'. Выведите на экран значение letters.


class Thing2:
    letters = 'abc'


print(Thing2.letters)
print(" ")

# Создайте еще один класс, который, конечно же, называется Thing3. В этот раз
# присвойте значение 'xyz' атрибуту объекта letters. Выведите на экран зна-
# чение атрибута letters. Понадобилось ли вам создавать объект класса, чтобы
# сделать это?


class Thing3():
    def __init__(self):
        self.letters = 'xyz'


this = Thing3()
print(this.letters)
print(" ")

# Создайте класс Element, имеющий атрибуты объекта name, symbol и number.
# Создайте объект этого класса со значениями 'Hydrogen', 'H' и 1.


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen)
print(" ")

# Создайте словарь со следующими ключами и значениями: 'name': 'Hydrogen',
# 'symbol': 'H', 'number': 1. Далее создайте объект с именем hydrogen класса
# Element с помощью этого словаря.
e1_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(e1_dict['name'], e1_dict['symbol'], e1_dict['number'])
print(hydrogen.name)
print(" ")

# Для класса Element определите метод с именем dump(), который выводит на
# экран значения атрибутов объекта (name, symbol и number). Создайте объект
# hydrogen из этого нового определения и используйте метод dump(), чтобы вы-
# вести на экран его атрибуты.


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print('name=%s, symbol=%s, number=%s' %
              (self.name, self.symbol, self.number))


hydrogen = Element(**e1_dict)
hydrogen.dump()
print(" ")

# Вызовите функцию print(hydrogen). В определении класса Element измените
# имя метода dump на __str__, создайте новый объект hydrogen и затем снова вы-
# зовите метод print(hydrogen).
print(hydrogen)


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return ('name=%s, symbol=%s, number=%s' %
                (self.name, self.symbol, self.number))


hydrogen = Element(**e1_dict)
print(hydrogen)
print(" ")

# Модифицируйте класс Element, сделав атрибуты name, symbol и number приват-
# ными. Определите свойство получателя для каждого атрибута, возвращающее
# его значение.


class Element2:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number


hydrogen2 = Element2('Hydrogen', 'H', 1)
print(hydrogen2.name)
print(hydrogen2.symbol)
print(hydrogen2.number)
print(" ")

# Определите три класса: Bear, Rabbit и Octothorpe. Для каждого из них опре-
# делите всего один метод — eats(). Он должен возвращать значения 'berries'
# (для Bear), 'clover' (для Rabbit) или 'campers' (для Octothorpe). Создайте
# по одному объекту каждого класса и выведите на экран то, что ест указанное
# животное.


class Bear:
    def eats(self):
        return 'berries'


class Rabbit:
    def eats(self):
        return 'clover'


class Octothorpe:
    def eats(self):
        return 'campers'


b = Bear()
r = Rabbit()
o = Octothorpe()
print(b.eats())
print(r.eats())
print(o.eats())
print(" ")

# Определите три класса: Laser, Claw и SmartPhone. Каждый из них имеет только
# один метод — does(). Он возвращает значения 'disintegrate' (для Laser),
# 'crush' (для Claw) или 'ring' (для SmartPhone). Далее определите класс Robot,
# который содержит по одному объекту каждого из этих классов. Определите
# метод does() для класса Robot, который выводит на экран все, что делают его
# компоненты.


class Laser:
    def does(self):
        return 'disintegrate'


class Claw:
    def does(self):
        return 'crush'


class SmartPhone:
    def does(self):
        return 'ring'


class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        return '''Laser, %s.
            Claw, %s.
            Smartphone, %s.''' % (
                self.laser.does(),
                self.claw.does(),
                self.smartphone.does()
                    )


r = Robot()
print(r.does())
