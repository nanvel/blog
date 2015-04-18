Software design patterns
========================

How to create it
----------------

- Abstract factory
- `Builder <http://en.wikipedia.org/wiki/Builder_pattern>`__

    Instead of using numerous constructors use only one + methods to modify it.

    .. code-block:: python

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


    Links:
        - https://gist.github.com/pazdera/1121157


- `Factory method <http://en.wikipedia.org/wiki/Factory_method_pattern>`__

    The essence of this pattern is to "Define an interface for creating an object, but let the classes that implement the interface decide which class to instantiate. The Factory method lets a class defer instantiation to subclasses [`Design Patterns: Elements of Reusable Object-Oriented Software from the Gang Of Four <http://en.wikipedia.org/wiki/Design_Patterns>`__].

    Example:

    .. code-block:: python

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

    Links:
        - http://en.wikibooks.org/wiki/Computer_Science_Design_Patterns/Factory_method

- Prototype
- `Singleton <http://en.wikipedia.org/wiki/Singleton_pattern>`__

    .. code-block:: python

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

    or

    .. code-block:: python

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

- `Monostate (Borg pattern) <http://placidrage.bitbucket.org/0-computer/0-software-engineer/0-design-patterns/0-monostate/index.html>`__

    .. code-block:: python

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

Structure of it
---------------

- Adapter
- Bridge
- Composite
- Decorator
- Facade
- Flyweight
- Proxy

How it behaves
--------------

- Chain of Responsibility
- Command
- Interpreter
- Iterator
- Mediator
- Memento
- `Observer <http://en.wikipedia.org/wiki/Observer_pattern>`__

    Pattern in which an object, called the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods. 

    Links:
        - http://www.giantflyingsaucer.com/blog/?p=5117

- State
- Strategy
- TemplateMethod
- Visitor

Architectural
-------------

- `Model View Controller <http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller>`__

    We need smart models, thin controllers and dumb views.

Links:
    - `Дизайн-патерни — просто, як двері <http://designpatterns.andriybuday.com/>`__

.. info::
    :tags: Software development
    :place: Kyiv, Ukraine
