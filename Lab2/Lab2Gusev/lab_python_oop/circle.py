from math import pi
from lab_python_oop.geometric_figure import GeometricFigure
from lab_python_oop.figure_color import FigureColor

#Класс фигур Круг
class Circle(GeometricFigure):
    def __init__(self, r, c):
        self.radius = r
        self.color = FigureColor(c)
        self.type = "Круг"

    def get_type(self):
        return self.type

    def area(self):
        return round(self.radius * self.radius * pi, 5)

    def __repr__(self):
        return '{} с радиусом {} и цветом {}, который имеет площадь {}'.format(self.get_type(), self.radius,
                                                                          self.color, self.area())
