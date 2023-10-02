import math


class Circle:

    def __init__(self, radius):
        self.rad = radius

    def area(self):
        if self.rad > 0:
            return round(math.pi * pow(self.rad, 2), 2)
        else:
            return 'Радиус не может быть меньше или равен 0'


class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            self.P = (self.a + self.b + self.c) // 2
            self.S = round(pow(self.P * (self.P - self.a) * (self.P - self.b) * (self.P - self.c), 0.5), 2)
            return self.S
        else:
            return 'Треугольник не существует'

    def type_of_triangle(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            if pow(self.a, 2) == pow(self.b, 2) + pow(self.c, 2):
                self.type_tr = 'прямоугольный'
            elif pow(self.b, 2) == pow(self.a, 2) + pow(self.c, 2):
                self.type_tr = 'прямоугольный'
            elif pow(self.c, 2) == pow(self.a, 2) + pow(self.b, 2):
                self.type_tr = 'прямоугольный'
            else:
                self.type_tr = 'не прямоугольный'
            return f'Заданный треугольник {self.type_tr}'
        else:
            return 'Треугольник не существует'
