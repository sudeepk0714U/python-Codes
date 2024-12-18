class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
a = Vector(2,3)
b = Vector(-1,7)
c = a+b
print(c)
