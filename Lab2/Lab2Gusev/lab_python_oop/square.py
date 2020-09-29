from lab_python_oop.rectangle import Rectangle


#Класс фигур Квадрат
class Square(Rectangle):
    def __init__(self, s, c):
        super().__init__(s, s, c)
        self.type = "Квадрат"

    def get_type(self):
        return self.type

    def __repr__(self):
        return '{} с радиусом {} и цветом {}, который имеет площадь {}'.format(self.get_type(), self.height,
                                                                        self.color, self.area())
