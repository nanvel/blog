Software design patterns
========================

How to create it
----------------

- Abstract factory
- Builder
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
- Observer
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
