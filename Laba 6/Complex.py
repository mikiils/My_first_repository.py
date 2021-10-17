class Complex():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Complex(self.x * other.x - self.y * other.y, self.x * other.y + other.x * self.y)

    def __sub__(self, other):
        return Complex(self.x - other.x, self.y - other.y)

    def __truediv__(self, other):
        return Complex((self.x * other.x + self.y * other.y) / (other.x ** 2 + other.y ** 2),
                       (self.y * other.x - self.x * other.y) / (other.x ** 2 + other.y ** 2))

    def __abs__(self):
        return ((self.x ** 2 + self.y ** 2) ** 0.5)


A = Complex( -1, 3 )
B = Complex( -2, 1 )
C = A + B
D = A * B
E = A / B
a = abs(A)