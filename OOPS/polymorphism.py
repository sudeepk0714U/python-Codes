class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def show(self):
        print(f"{self.real} + {self.imaginary}i")
    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)
    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real, imaginary)
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

num1 = Complex(1,2)
num2 = Complex(3,9)
num3 = num1+num2
num4 = num1-num2
num5 = num1*num2
print(num3)
print(num4)
print(num5)