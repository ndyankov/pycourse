
class PropExample(object):

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        print('setting name:', name)
        self.__name = name

class C(object):

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value


def main():
    p = PropExample(name="myname")
    print(p.name)
    p.name = "foobar"
    print (p.name)

    c = C()
    c.x = 5
    print(c.x)


if __name__ == "__main__":
    main()
