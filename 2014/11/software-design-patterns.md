labels: Blog
        SoftwareDevelopment
created: 2014-11-30T14:10
modified: 2022-12-03T11:16
place: Kyiv, Ukraine
comments: true

# Software design patterns

Design patterns are solutions to recurring problems; guidelines on how to tackle certain problems.

> Conformity to patterns is not a measure of goodness.
>
> Ralph Johnson, Coauthor of the Design Patterns classic

> When I see patterns in my programs, I consider it a sign of trouble. The shape of a program should reflect only the problem it needs to solve. Any other regularity in the code is a sign, to me at least, that I'm using abstractions that aren't powerful enough - often that I'm generating by hand the expansions of some macro that I need to write.
>
> Paul Graham, Lisp hacker and venture capitalist

!!! caution "Caution"
    Design patterns are not a silver bullet to all your problems.

    Do not try to force them; bad things are supposed to happen, if done so. Keep in mind that design patterns are solutions to problems, not solutions finding problems; so don't overthink.

    If used in a correct place in a correct manner, they can prove to be a savior; or else they can result in a horrible mess of a code.

Do we need them all? Maybe there are a few principles we may use instead?

> As to methods there may be a million and then some, but principles are few. The man who grasps principles can successfully select his own methods. The man who tries methods, ignoring principles, is sure to have trouble.
>
> Ralph Waldo Emerson

Principles: SOLID, DRY, KISS, YAGNI.

[TOC]

There are 3 groups of design patterns:

- Creational (How to create it)
- Structural (Structure of it)
- Behavioral (How it behaves)

## How to create it

Creational patterns are focused towards how to instantiate an object or group of related objects.

### [Simple factory](https://github.com/kamranahmedse/design-patterns-for-humans#-simple-factory)

Simple factory simply generates an instance for client without exposing any instantiation logic to the client.

!!! tip "Real world example"
    Consider, you are building a house and you need doors. It would be a mess if every time you need a door, you put on your carpenter clothes and start making a door in your house. Instead you get it made from a factory.

Use when creating an object is not just a few assignments and involves some logic, it makes sense to put it in a dedicated factory instead of repeating the same code everywhere.

### [Factory method](http://en.wikipedia.org/wiki/Factory_method_pattern)

Provides a way to delegate the instantiation logic to child classes.

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

!!! tip "Real world example"
    Consider the case of a hiring manager. It is impossible for one person to interview for each of the positions. Based on the job opening, she has to decide and delegate the interview steps to different people.

Useful when there is some generic processing in a class but the required sub-class is dynamically decided at runtime. Or putting it in other words, when the client doesn't know what exact sub-class it might need.

Links:

- [Factory method](http://en.wikibooks.org/wiki/Computer_Science_Design_Patterns/Factory_method) on Wikipedia

### [Abstract factory](http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Factory.html#abstract-factories)

A factory of factories; a factory that groups the individual but related/dependent factories together without specifying their concrete classes.

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

!!! tip "Real world example"
    Based on your needs you might get a wooden door from a wooden door shop, iron door from an iron shop or a PVC door from the relevant shop. Plus you might need a guy with different kind of specialities to fit the door, for example a carpenter for wooden door, welder for iron door etc. As you can see there is a dependency between the doors now, wooden door needs carpenter, iron door needs a welder etc.

Use when there are interrelated dependencies with not-that-simple creation logic involved.

### [Builder](http://en.wikipedia.org/wiki/Builder_pattern)

Allows you to create different flavors of an object while avoiding constructor pollution. Useful when there could be several flavors of an object. Or when there are a lot of steps involved in creation of an object.

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

!!! tip "Real world example"
    Imagine you are at Hardee's and you order a specific deal, lets say, "Big Hardee" and they hand it over to you without any questions; this is the example of simple factory. But there are cases when the creation logic might involve more steps. For example you want a customized Subway deal, you have several options in how your burger is made e.g what bread do you want? what types of sauces would you like? What cheese would you want? etc. In such cases builder pattern comes to the rescue.

Use when there could be several flavors of an object and to avoid the constructor telescoping. The key difference from the factory pattern is that; factory pattern is to be used when the creation is a one step process while builder pattern is to be used when the creation is a multi step process.

Links:

- [https://gist.github.com/pazdera/1121157](https://gist.github.com/pazdera/1121157)

### Prototype

Create object based on an existing object through cloning.

!!! tip "Real world example"
    Remember dolly? The sheep that was cloned! Lets not get into the details but the key point here is that it is all about cloning.

Use when an object is required that is similar to existing object or when the creation would be expensive as compared to cloning.

### [Singleton](http://en.wikipedia.org/wiki/Singleton_pattern)

Ensures that only one object of a particular class is ever created.

!!! tip "Real world example"
    There can only be one president of a country at a time. The same president has to be brought to action, whenever duty calls. President here is singleton.

!!! warning "Use with caution"
    Singleton pattern is actually considered an anti-pattern and overuse of it should be avoided. It is not necessarily bad and could have some valid use-cases but should be used with caution because it introduces a global state in your application and change to it in one place could affect in the other areas and it could become pretty difficult to debug. The other bad thing about them is it makes your code tightly coupled plus it mocking the singleton could be difficult.

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

Structural patterns are mostly concerned with object composition or in other words how the entities can use each other. Or yet another explanation would be, they help in answering "How to build a software component?"

### Adapter

Adapter pattern lets you wrap an otherwise incompatible object in an adapter to make it compatible with another class.

!!! tip "Real world example"
    Consider that you have some pictures in your memory card and you need to transfer them to your computer. In order to transfer them you need some kind of adapter that is compatible with your computer ports so that you can attach memory card to your computer. In this case card reader is an adapter. Another example would be the famous power adapter; a three legged plug can't be connected to a two pronged outlet, it needs to use a power adapter that makes it compatible with the two pronged outlet. Yet another example would be a translator translating words spoken by one person to another.

### Bridge

Bridge pattern is about preferring composition over inheritance. Implementation details are pushed from a hierarchy to another object with a separate hierarchy.

!!! tip "Real world example"
    Consider you have a website with different pages and you are supposed to allow the user to change the theme. What would you do? Create multiple copies of each of the pages for each of the themes or would you just create separate theme and load them based on the user's preferences? Bridge pattern allows you to do the second i.e.

### Composite

Composite pattern lets clients treat the individual objects in a uniform manner.

!!! tip "Real world example"
    Every organization is composed of employees. Each of the employees has the same features i.e. has a salary, has some responsibilities, may or may not report to someone, may or may not have some subordinates etc.

### Decorator

Decorator pattern lets you dynamically change the behavior of an object at run time by wrapping them in an object of a decorator class.

!!! tip "Real world example"
    Imagine you run a car service shop offering multiple services. Now how do you calculate the bill to be charged? You pick one service and dynamically keep adding to it the prices for the provided services till you get the final cost. Here each type of service is a decorator.

### Facade (façade)

> If something is ugly, hide it inside an object.

Facade pattern provides a simplified interface to a complex subsystem.

This design pattern aggregates classes that implement the functionality of the subsystem but does not hide them completely. Should not add any new functionality, just simplify the access to a system.

Goal: make a software library easier to use, understand and test.

!!! tip "Real world example"
    How do you turn on the computer? "Hit the power button" you say! That is what you believe because you are using a simple interface that computer provides on the outside, internally it has to do a lot of stuff to make it happen. This simple interface to the complex subsystem is a facade.

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

### Flyweight

It is used to minimize memory usage or computational expenses by sharing as much as possible with similar objects.

!!! tip "Real world example"
    Did you ever have fresh tea from some stall? They often make more than one cup that you demanded and save the rest for any other customer so to save the resources e.g. gas etc. Flyweight pattern is all about that i.e. sharing.

### Proxy

Using the proxy pattern, a class represents the functionality of another class.

Relates to: State (or State provider), Surrogate. Proxy is used to control access to its implementation, while State allows you to change the implementation dynamically. Surrogate - uses for both (controlling access to implementation).

A Proxy is a design pattern that helps to decouple the client code from the object that the client code uses. Proxy acts like a real object but delegates all calls to the real object.

!!! tip "Real world example"
    Have you ever used an access card to go through a door? There are multiple options to open that door i.e. it can be opened either using access card or by pressing a button that bypasses the security. The door's main functionality is to open but there is a proxy added on top of it to add some functionality. Let me better explain it using the code example below.

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

Use cases:

- lazy initialization
- logging
- facilitate network connections
- control access to shared objects
- caching
- ...

## How it behaves

It is concerned with assignment of responsibilities between the objects. What makes them different from structural patterns is they don't just specify the structure but also outline the patterns for message passing/communication between them. Or in other words, they assist in answering "How to run a behavior in software component?"

### Chain of Responsibility

It helps building a chain of objects. Request enters from one end and keeps going from object to object till it finds the suitable handler.

!!! tip "Real world example"
    For example, you have three payment methods (`A`, `B` and `C`) setup in your account; each having a different amount in it. `A` has 100 USD, `B` has 300 USD and `C` having 1000 USD and the preference for payments is chosen as `A` then `B` then `C`. You try to purchase something that is worth 210 USD. Using Chain of Responsibility, first of all account `A` will be checked if it can make the purchase, if yes purchase will be made and the chain will be broken. If not, request will move forward to account `B` checking for amount if yes chain will be broken otherwise the request will keep forwarding till it finds the suitable handler. Here `A`, `B` and `C` are links of the chain and the whole phenomenon is Chain of Responsibility.

### Command

Choosing the operation at runtime.

Allows you to encapsulate actions in objects. The key idea behind this pattern is to provide the means to decouple client from receiver.

!!! tip "Real world example"
    A generic example would be you ordering a food at restaurant. You (i.e. Client) ask the waiter (i.e. Invoker) to bring some food (i.e. Command) and waiter simply forwards the request to Chef (i.e. Receiver) who has the knowledge of what and how to cook. Another example would be you (i.e. Client) switching on (i.e. Command) the television (i.e. Receiver) using a remote control (Invoker).

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

Use for:

- keep a history of calls
- decouple an invoker from an executor
- macro command - a sequence of simpler commands

### Interpreter (TODO)

TODO

### Iterator

It presents a way to access the elements of an object without exposing the underlying presentation.

!!! tip "Real world example"
    An old radio set will be a good example of iterator, where user could start at some channel and then use next or previous buttons to go through the respective channels. Or take an example of MP3 player or a TV set where you could press the next and previous buttons to go through the consecutive channels or in other words they all provide an interface to iterate through the respective channels, songs or radio stations.

### Mediator

Mediator pattern adds a third party object (called mediator) to control the interaction between two objects (called colleagues). It helps reduce the coupling between the classes communicating with each other. Because now they don't need to have the knowledge of each other's implementation.

!!! tip "Real world example"
    A general example would be when you talk to someone on your mobile phone, there is a network provider sitting between you and them and your conversation goes through it instead of being directly sent. In this case network provider is mediator.

### Memento

Memento pattern is about capturing and storing the current state of an object in a manner that it can be restored later on in a smooth manner.

!!! tip "Real world example"
    Take the example of calculator (i.e. originator), where whenever you perform some calculation the last calculation is saved in memory (i.e. memento) so that you can get back to it and maybe get it restored using some action buttons (i.e. caretaker).

Usually useful when you need to provide some sort of undo functionality.

### State

Or State provide. See Proxy.

It lets you change the behavior of a class when the state changes.

!!! tip "Real world example"
    Imagine you are using some drawing application, you choose the paint brush to draw. Now the brush changes its behavior based on the selected color i.e. if you have chosen red color it will draw in red, if blue then it will be in blue etc.

### Strategy

Aka policy.

Strategy pattern allows you to switch the algorithm or strategy based upon the situation.

!!! tip "Real world example"
    Consider the example of sorting, we implemented bubble sort but the data started to grow and bubble sort started getting very slow. In order to tackle this we implemented Quick sort. But now although the quick sort algorithm was doing better for large datasets, it was very slow for smaller datasets. In order to handle this we implemented a strategy where for small datasets, bubble sort will be used and for larger, quick sort.

### Template method

Template method defines the skeleton of how a certain algorithm could be performed, but defers the implementation of those steps to the children classes.

Defines the basis of an algorithm and enables successors to redefine some steps of the algorithm without changing its structure.

There is a method that calls some other methods. Some of these methods remain the same for different algorithms and some may be changed.

!!! tip "Real world example"
    Suppose we are getting some house built. The steps for building might look like

    - Prepare the base of house
    - Build the walls
    - Add roof
    - Add other floors

    The order of these steps could never be changed i.e. you can't build the roof before building the walls etc but each of the steps could be modified for example walls can be made of wood or polyester or stone

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

### Visitor

Visitor pattern lets you add further operations to objects without having to modify them.

!!! tip "Real world example"
    Consider someone visiting Dubai. They just need a way (i.e. visa) to enter Dubai. After arrival, they can come and visit any place in Dubai on their own without having to ask for permission or to do some leg work in order to visit any place here; just let them know of a place and they can visit it. Visitor pattern lets you do just that, it helps you add places to visit so that they can visit as much as they can without having to do any legwork.

### [Observer](http://en.wikipedia.org/wiki/Observer_pattern)

Defines a dependency between objects so that whenever an object changes its state, all its dependents are notified.

Pattern in which an object, called the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods.

!!! tip "Real world example"
    A good example would be the job seekers where they subscribe to some job posting site and they are notified whenever there is a matching job opportunity.

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

## Other

[Circuit breaker design pattern](https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern)

## Links

- [Дизайн-патерни — просто, як двері](http://designpatterns.andriybuday.com/)
- [Python 3 Patterns, Recipes and Idioms](http://python-3-patterns-idioms-test.readthedocs.org/en/latest/index.html)
- [A collection of design patterns/idioms in Python](https://github.com/faif/python-patterns)
- [Design Patterns](https://sourcemaking.com/design_patterns) on sourcemaking.com
- [Design Patterns for Humans](https://github.com/kamranahmedse/design-patterns-for-humans)
- [Cloud Design Patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/)
