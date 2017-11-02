
from tree import Node


class File(Node):
	
	def add_child(self, node):
		raise Exception('not allowed')


class Dir(Node):
	
	def add_child(self, node):
		if not isinstance(node, (File, Dir)):
			raise Exception('not file or dir')

		super(Dir, self).add_child(node)


def main():

	directory = Dir("dir1", [
		File('file1.py'),
		File('file2.py'),
		Dir('package/', [
			File('foo.py'),
			File('bar.py'),
		])
	])

	print(directory)


if __name__ == "__main__":
	main()
