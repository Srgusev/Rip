from lab_python_oop.geometric_figure import GeometricFigure
from lab_python_oop.figure_color import FigureColor


#Класс фигур Прямоугольник 
class Rectangle(GeometricFigure):
    def __init__(self, w, h, c):
        self.width = w
        self.height = h
        self.color = FigureColor(c)
        self.type = "Прямоугольник"

    def get_type(self):
        return self.type

    def area(self):
        return self.height * self.width

    def __repr__(self):
        return '{} с радиусом {}, который имеет площадь {} и цветом {}'.format(self.get_type(), self.width,
                                                                                    self.height,
                                                                                    self.color, self.area())
