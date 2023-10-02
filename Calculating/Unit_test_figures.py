import unittest
from Figures import Circle, Triangle


class TestFigures(unittest.TestCase):
    def setUp(self) -> None:
        self.circle = Circle(27)
        self.triangle = Triangle(13, 25, 17)

    def test_circle_area(self):
        self.assertEqual(self.circle.area(), 2290.22)

    def test2_circle_area(self):
        self.circle = Circle(0)
        self.assertEqual(self.circle.area(), 'Радиус не может быть меньше или равен 0')

    def test_triangle_area(self):
        self.assertEqual(self.triangle.area(), 86.95)

    def test2_triangle_area(self):
        self.triangle = Triangle(0, 0, 0)
        self.assertEqual(self.triangle.area(), 'Треугольник не существует')

    def test_triangle_type(self):
        self.assertEqual(self.triangle.type_of_triangle(), 'Заданный треугольник не прямоугольный')


if __name__ == '__main__':
    unittest.main()
