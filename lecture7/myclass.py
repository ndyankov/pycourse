
class MyClass:

    my_classvar = 5

    def __init__(self):
        self.my_instancevar = 5

    def my_instancemethod(self):
        print(self)

    @classmethod
    def my_classmethod(cls):
        print(cls)

    @staticmethod
    def my_staticmethod():
        pass


def main():

    my_instance = MyClass()
    my_instance.my_instancemethod()
    my_instance.my_classmethod()
    my_instance.my_staticmethod()


if __name__ == "__main__":
    main()
