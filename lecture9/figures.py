
import math


class Ellipse(object):

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def area(self):
		return math.pi * self.a * self.b


class Circle(Ellipse):

	def __init__(self, r):
		super(Circle, self).__init__(r, r)

	@property
	def radius(self):
		return self.a


def main():

	ellipse = Ellipse(2, 3)
	print(ellipse.a, ellipse.b, ellipse.area())

	circle = Circle(5)
	print(circle.radius, circle.area())


if __name__ == "__main__":
	main()
