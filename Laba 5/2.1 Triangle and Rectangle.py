class Shape():
    width = 0
    height = 0
    def set_width(self, a):
        if a >= 0:
            self.width = a
        else:
            print('Wrong parameter')
    def set_height(self, a):
        if a >= 0:
            self.height = a
        else:
            print('Wrong parameter')
    pass

class Triangle(Shape):
    def area(self):
        return s.width * s.height / 2

class Rectangle(Shape):
    def area(self):
        return s.width * s.height

if __name__ == "__main__":
    s = Shape()
    t = Triangle()
    r = Rectangle()
    s.set_width(10)
    s.set_height(20)
    print('width = {} , height = {}'.format (s.width, s.height))
    print('Triangle area:', t.area())
    print('Rectangle area:',r.area())

