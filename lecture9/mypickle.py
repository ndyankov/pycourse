
import pickle

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

A = [
    2, 3, {3: 4}, 
    {5, 6}, "asjdfsdf",
    Point(2, 3)
]

name = 'data.pickle'

with open(name, 'wb') as f:
    pickle.dump(A, f)

with open(name, 'rb') as f:
    B = pickle.load(f)

print(B)
print(A==B)
