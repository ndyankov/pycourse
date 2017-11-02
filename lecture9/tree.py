
class Node(object):

    def __init__(self, data=None, children=None):
        self.data = data
        self.children = []
        if children:
            for child in children:
                self.add_child(child)

    def add_child(self, node):
        if not isinstance(node, Node):
            raise ValueError('not a tree node: {}'.format(node))

        self.children.append(node)

    def __str__(self):
        lines = []
        print_tree(self, printer=lines.append)
        return '\n'.join(lines)


def print_tree(node, level=0, printer=print):
    printer("{}{}".format('-' * level, node.data))
    for child in node.children:
        print_tree(child, level+1, printer=printer)


def main():
    root = Node(5)
    root.add_child(Node(6))
    n2 = Node(2)
    root.add_child(n2)
    n2.add_child(Node(3))

    print(root)

    tree = Node(
        5, [
            Node(6),
            Node(2, [Node(3)])
        ]
    )
    print(tree)


if __name__ == "__main__":
    main()
