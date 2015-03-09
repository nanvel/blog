Software design patterns
========================

How to create it
----------------

- Abstract factory
- Builder
- Factory method
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
