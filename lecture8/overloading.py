
###
# overloading
###


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def main():
    p1 = Point(1, 2)
    p2 = Point(3, 4)

    p = p1+p2
    print(p)


if __name__ == "__main__":
    main()
