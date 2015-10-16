labels: Blog
        Python
created: 2014-12-27T14:41
place: Kyiv, Ukraine

# Python static method and class inheritance

Just to be sure that it works the way I thought:
```python
class Base(object):

    _MY_VALUE = None

    @classmethod
    def my_value(cls, value=None):
        if value:
            cls._MY_VALUE = value
        return cls._MY_VALUE


class Child1(Base):

    pass


class Child2(Base):

    pass


if __name__ == '__main__':
    print Child1.my_value()
    print Child1.my_value(value=1)
    print Child1.my_value()
    print Child1().my_value()
    print Child2.my_value()
    print Child2().my_value()
    print Base.my_value()
```

Output:
```text
None
1
1
1
None
None
None
```
