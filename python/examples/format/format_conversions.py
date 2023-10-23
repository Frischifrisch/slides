class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b
    def __format__(self, spec):
        #print(spec) // empty string
        return("{{'x':{}, 'y':{}}}".format(self.x, self.y))
    def __str__(self):
        return f"({self.x},{self.y})"
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(2, 3)
print(p)                 # (2,3)
print(f"{p}")
print("{!s}".format(p))  # (2,3)
print("{!r}".format(p))  # Point(2, 3)
