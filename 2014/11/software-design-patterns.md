labels: Blog
        SoftwareDevelopment
created: 2014-11-30T14:10
modified: 2016-12-21T15:01
place: Kyiv, Ukraine
comments: true

# Software design patterns

Do we need them all? Maybe there are a few principles we may use instead?

> As to methods there may be a million and then some, but principles are few. The man who grasps principles can successfully select his own methods. The man who tries methods, ignoring principles, is sure to have trouble.
>
> Ralph Waldo Emerson

[TOC]

## How to create it

### [Abstract factory](http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Factory.html#abstract-factories)

Abstract Factory has more then one factory methods.
Each of the methods creates a different kind of object.
We can select methods behavior by selecting particular factory.

Abstract Factory is used when you need to create a family of objects that do some work together.

```python
class Obstacle:

    def action(self):
        pass


class Character:

    def interactWith(self, obstacle):
        pass


class Kitty(Character):

    def interactWith(self, obstacle):
        print("Kitty has encountered a", obstacle.action())


class KungFuGuy(Character):

    def interactWith(self, obstacle):
        print("KungFuGuy now battles a", obstacle.action())


class Puzzle(Obstacle):

    def action(self):
        return "Puzzle"


class NastyWeapon(Obstacle):

    def action(self):
        return "NastyWeapon"


# The Abstract Factory
class GameElementFactory:

    def makeCharacter(self):
        pass

    def makeObstacle(self):
        pass


# Concrete factories
class KittiesAndPuzzles(GameElementFactory):

    def makeCharacter(self):
        return Kitty()

    def makeObstacle(self):
        return Puzzle()


class KillAndDismember(GameElementFactory):

    def makeCharacter(self):
        return KungFuGuy()

    def makeObstacle(self):
        return NastyWeapon()


class GameEnvironment:

    def __init__(self, factory):
        self.factory = factory
        self.character = factory.makeCharacter()
        self.obstacle = factory.makeObstacle()

    def play(self):
        self.character.interactWith(obstacle=self.obstacle)


if __name__ == '__main__':

    g1 = GameEnvironment(KittiesAndPuzzles())
    g2 = GameEnvironment(KillAndDismember())
    g1.play()
    # Kitty has encountered a Puzzle
    g2.play()
    # KungFuGuy now battles a NastyWeapon
```

### [Builder](http://en.wikipedia.org/wiki/Builder_pattern)

Instead of using numerous constructors use only one + methods to modify it.

```python
class Car(object):

    def __init__(self):
        self._wheels = []
        self._engine = None
        self._body = None

    def attachWheel(self, size):
        self._wheels.append(Wheel(size=size))

    def setEngine(self, horsepower):
        self._engine = Engine(horsepower=horsepower)

    def setBody(self, shape):
        self._body = Body(shape=shape)

    def getConfiguration(self):
        return str(self._body), str(self._engine), str(self._wheels)


class Wheel(object):

    def __init__(self, size=16):
        self._size = size

    def __str__(self):
        return 'Wheel size {size}.'.format(size=self._size)


class Engine(object):

    def __init__(self, horsepower=85):
        self._horsepower = horsepower

    def __str__(self):
        return 'Engine horsepower {horsepower}.'.format(horsepower=self._horsepower)


class Body(object):

    def __init__(self, shape='hatchback'):
        self._shape = shape

    def __str__(self):
        return 'Body shape {shape}.'.format(shape=self._shape)


class CarBuilder(object):

    def buid(self, wheel_size, engine_horsepower, body_shape):
        car = Car()
        car.setBody(shape=body_shape)
        car.setEngine(horsepower=engine_horsepower)
        for i in range(4):
            car.attachWheel(size=wheel_size)
        return car


if __name__ == '__main__':
    car = CarBuilder().buid(wheel_size=10, engine_horsepower=100, body_shape='hatchback')
    print(car.getConfiguration())
    # ('Body shape hatchback.', 'Engine horsepower 100.', '[<__main__.Wheel object at 0x10e0b01d0>, <__main__.Wheel object at 0x10e0b0210>, <__main__.Wheel object at 0x10e0b0250>, <__main__.Wheel object at 0x10e0b0290>]')
```

Links:

- [https://gist.github.com/pazdera/1121157](https://gist.github.com/pazdera/1121157)


### [Factory method](http://en.wikipedia.org/wiki/Factory_method_pattern)

The essence of this pattern is to "Define an interface for creating an object, but let the classes that implement the interface decide which class to instantiate. The Factory method lets a class defer instantiation to subclasses [[Design Patterns: Elements of Reusable Object-Oriented Software from the Gang Of Four](http://en.wikipedia.org/wiki/Design_Patterns)].
Example:
```python
class Pizza(object):
    """ Implements interface. """

    def __init__(self):
        self._price = None

    def get_price(self):
        return self._price


class HamAndMushroomPizza(Pizza):

    def __init__(self):
        self._price = 8.5


class DeluxePizza(Pizza):

    def __init__(self):
        self._price = 10.5


class HawaiianPizza(Pizza):

    def __init__(self):
        self._price = 11.5


class PizzaFactory(object):

    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == 'HamMushroom':
            return HamAndMushroomPizza()
        elif pizza_type == 'Deluxe':
            return DeluxePizza()
        elif pizza_type == 'Hawaiian':
            return HawaiianPizza()

if __name__ == '__main__':
    for pizza_type in ('HamMushroom', 'Deluxe', 'Hawaiian'):
        pizza = PizzaFactory.create_pizza(pizza_type=pizza_type)
        print('Price of {pizza_type} is {price}'.format(
            pizza_type=pizza_type, price=pizza.get_price()))
    # Price of HamMushroom is 8.5
    # Price of Deluxe is 10.5
    # Price of Hawaiian is 11.5
```

Links:

- [Factory method](http://en.wikibooks.org/wiki/Computer_Science_Design_Patterns/Factory_method) on Wikipedia

### Prototype (TODO)

TODO

### [Singleton](http://en.wikipedia.org/wiki/Singleton_pattern)

```python
class Singleton(object):

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(
                cls, *args, **kwargs)
        return cls.__instance


if __name__ == '__main__':
    instance1 = Singleton()
    instance2 = Singleton()
    # points to the same object
    print(instance1, instance2)
    # <__main__.Singleton object at 0x1032f1950> <__main__.Singleton object at 0x1032f1950>
```

    or

```python
class MyClass(object):

    __instance = None

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = cls(*args, **kwargs)
        return cls.__instance


if __name__ == '__main__':
    instance1 = MyClass.get_instance()
    instance2 = MyClass.get_instance()
    instance3 = MyClass()
    print(instance1, instance2, instance3)
    # <__main__.MyClass object at 0x10b3a4990> <__main__.MyClass object at 0x10b3a4990> <__main__.MyClass object at 0x10b3a49d0>
```

Using metaclasses:
```python
class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=Singleton):
    pass

class RegularClass:
    pass


if __name__ == '__main__':

	x = SingletonClass()
	y = SingletonClass()
	print(x == y)

	x = RegularClass()
	y = RegularClass()
	print(x == y)

# True
# False
```

Links:
- [Python Course - Metaclasses](http://www.python-course.eu/python3_metaclasses.php)

### [Monostate (Borg pattern)](http://placidrage.bitbucket.org/0-computer/0-software-engineer/0-design-patterns/0-monostate/index.html)

```python
class BorgClass(object):

    __shared_state = {}

    def __init__(self, *args, **kwargs):
        self.__dict__ = self.__shared_state


if __name__ == '__main__':
    instance1 = BorgClass()
    instance2 = BorgClass()
    print(instance1, instance2)
    instance1.a = 1
    print(instance1.a, instance2.a)
    instance2.a = 10
    print(instance1.a, instance2.a)
    # <__main__.BorgClass object at 0x105a45910> <__main__.BorgClass object at 0x105a45950>
    # 1 1
    # 10 10
```

## Structure of it

### Adapter (TODO)

TODO

### Bridge (TODO)

TODO

### Composite (TODO)

TODO

### Decorator (TODO)

TODO

### Facade (façade)

> If something is ugly, hide it inside an object.

Goal: make a software library easier to use, understand and test.

This design pattern aggregates classes that implement the functionality of the subsystem but does not hide them completely. Should not add any new functionality, just simplify the access to a system.

```python
class WheelBuilder():

    def build_a_wheel(self):
        return "Wheel"


class BodyBuilder():

    def build_a_body(self):
        return "Body"


class EngineBuilder():

    def build_an_engine(self):
        return "Engine"


def give_a_name():
    return "Some name"


class BuildACarFacade:

    wheel_builder = WheelBuilder()
    body_builder = BodyBuilder()
    engine_builder = EngineBuilder()

    @classmethod
    def build_a_car(cls):
        return [
            cls.wheel_builder.build_a_wheel() * 4,
            cls.body_builder.build_a_body(),
            cls.engine_builder.build_an_engine(),
            "Name: " + give_a_name()
        ]


if __name__ == '__main__':
    print(BuildACarFacade.build_a_car())
    # ['WheelWheelWheelWheel', 'Body', 'Engine', 'Name: Some name']
```

### Flyweight (TODO)

TODO

### Proxy

Relates to: State (or State provider), Surrogate. Proxy is used to control access to its implementation, while State allows you to change the implementation dynamically. Surrogate - uses for both (controlling access to implementation).

A Proxy is a design pattern that helps to decouple the client code from the object that the client code uses. Proxy acts like a real object but delegates all calls to the real object.

Use cases:

- lazy initialization
- logging
- facilitate network connections
- control access to shared objects
- caching
- ...

```python
class SomeImplementation:

	def do_something(self):
		print("Something.")

	def do_something_else(self):
		print("Something else.")


class ImplementationProxy:

	def __init__(self):
		self._implementation = SomeImplementation()

	def __getattr__(self, name):
		print("Call method {name}.".format(name=name))
		return getattr(self._implementation, name)


if __name__ == '__main__':
	implementation_proxy = ImplementationProxy()
	implementation_proxy.do_something()
	implementation_proxy.do_something_else()
	# Call method do_something.
	# Something.
	# Call method do_something_else.
	# Something else.
```

## How it behaves

### Chain of Responsibility (TODO)

TODO

### Command

Choosing the operation at runtime.

Use for:

- keep a history of calls
- decouple an invoker from an executor
- macro command - a sequence of simpler commands

```python
import abc


class BaseCommand(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self):
        pass


class Command1(BaseCommand):

    def execute(self):
        print('Comamnd 1')


class Command2(BaseCommand):

    def execute(self):
        print('Comamnd 2')


class Macro:

    def __init__(self, *commands):
        self._commands = commands

    def execute(self):
        for command in self._commands:
            command.execute()


if __name__ == '__main__':

    macro = Macro(Command1(), Command2())
    macro.execute()

# Comamnd 1
# Comamnd 2
```

### Interpreter (TODO)

TODO

### Iterator (TODO)

TODO

### Mediator (TODO)

TODO

### Memento (TODO)

TODO

### State

Or State provide.

See Proxy.

### Strategy (TODO)

TODO

### Template method

Defines the basis of an algorithm and enables successors to redefine some steps of the algorithm without changing its structure.

There is a method that calls some other methods. Some of these methods remain the same for different algorithms and some may be changed.

Benefits:

- extensibility
- minimize code duplication
- easier algorithm modification

```python
class Car:

    CAR_NAME = "Base car"

    def start_engine(self):
        print("Start engine.")

    def check_fasten(self):
        print("Check is fasten.")
        return True

    def switch_gear(self):
        print("Switch gear.")

    def accelerate(self):
        print("Accelerate.")

    def run(self):
        print("Running a {name} ...".format(name=self.CAR_NAME))
        self.start_engine()
        is_fasten = self.check_fasten()
        if is_fasten:
            self.switch_gear()
            self.accelerate()


class NoBeltsCar(Car):

    CAR_NAME = "No belts car"

    def check_fasten(self):
        print("No belts.")
        return False


if __name__ == '__main__':
    Car().run()
    NoBeltsCar().run()


# Running a Base car ...
# Start engine.
# Check is fasten.
# Switch gear.
# Accelerate.
# Running a No belts car ...
# Start engine.
# No belts.
```

### Visitor (TODO)

TODO

### [Observer](http://en.wikipedia.org/wiki/Observer_pattern)

Pattern in which an object, called the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods.

Tries to facilitate one-to-many relationship in software engineering. Reduces coupling between objects.

There are a Subject (aka Observable) and Observers:

- a subject knows only a list observers and an interface
- a subject can broadcast a message to all observers subscribed to it
- number of subscriptions is not limited and can be changed at runtime

```python
import abc


class BaseObserver(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def on_message(self, message):
        print(message)


class Subject:

    def __init__(self):
        self._observers = {}

    def connect_observer(self, observer):
        self._observers[observer.__class__.__name__] = observer

    def disconnect_observer(self, observer):
        name = observer.__class__.__name__
        if name in self._observers:
            del self._observers[name]

    def emit_message(self, message):
        for observer in self._observers.values():
            observer.on_message(message)


class Observer1(BaseObserver):

    def on_message(self, message):
        print("Observer 1:", message)


class Observer2(BaseObserver):

    def on_message(self, message):
        print("Observer 2:", message)


if __name__ == '__main__':
    observer1 = Observer1()
    observer2 = Observer2()

    subject = Subject()
    subject.connect_observer(observer1)
    subject.connect_observer(observer2)

    subject.emit_message("Hi!")

    subject.disconnect_observer(observer1)

    subject.emit_message("Again!")

# Observer 2: Hi!
# Observer 1: Hi!
# Observer 2: Again!
```

Also known as:

- Signals and slots (Qt)
- Target-Action pattern (iOS, IBOutlets/IBActions)
- Publishing-subscriber pattern

Links:

- [http://www.giantflyingsaucer.com/blog/?p=5117](http://www.giantflyingsaucer.com/blog/?p=5117)
- [Observer - Python 3 Patterns, Recipes and Idioms](http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Observer.html)

## Architectural

### [Model View Controller](http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)

We need smart models, thin controllers and dumb views.

Links:

- [Дизайн-патерни — просто, як двері](http://designpatterns.andriybuday.com/)
- [Python 3 Patterns, Recipes and Idioms](http://python-3-patterns-idioms-test.readthedocs.org/en/latest/index.html)
- [A collection of design patterns/idioms in Python](https://github.com/faif/python-patterns)
