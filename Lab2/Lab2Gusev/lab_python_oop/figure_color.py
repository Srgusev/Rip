#Класс цвета фигур

class FigureColor:
    def __init__(self, c):
        self._color = c

    def get_color(self):
        return self._color

    def set_color(self, c):
        self._color = c

    def del_color(self):
        del self._color

    def __repr__(self):
        return self._color

    color = property(get_color, set_color, del_color, "Цвет фигуры 'color'")
