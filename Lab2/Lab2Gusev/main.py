# Лабороторная 2 

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from lab_python_oop.figure_color import FigureColor

#Пишем фигуры и даём им раазмер
def main(): 
    rectangle1 = Rectangle(16, 9, "blue") 
    circle1 = Circle(5, "green")
    square1 = Square(4, "red")
    print(rectangle1)
    print(circle1)
    print(square1)

if __name__ == "__main__":
    main()
