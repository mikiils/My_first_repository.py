class Vector():
    def __init__(self, x=0, y=0, z=0, m=0):
        self.x = x
        self.y = y
        self.z = z
        self.m = m

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __nummul__(self):
        return Vector(self.m * self.x, self.m * self.y, self.m * self.z)



N = int(input())
l = 0.0
M = (0, 0, 0)
for i in range(N):
    x, y, z = map(int, input().split())
    A = Vector(x, y, z)
    if abs(A) > l:
        l = abs(A)
        M = A
print(M.x, M.y, M.z)