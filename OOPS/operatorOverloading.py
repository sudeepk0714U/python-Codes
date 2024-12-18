class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    def __sub__(self, v):
        return Vector(self.x - v.x, self.y - v.y, self.z - v.z)
    def dot_product(self,d):
        return self.x * d.x + self.y * d.y + self.z * d.z
v1 = Vector(2,3,4)
v2 = Vector(5,6,7)
v3 = Vector(8,9,10)
print(v1)
print(v2)
print(v3)
print(v1 + v2)  # Output: (7, 9, 11)
print(v1 - v2)  # Output: (-3, -3, -3)
print(v1.dot_product(v2))  # Output: 63
print(v1.dot_product(v3))  # Output: 139
print(v1+v2+v3)
