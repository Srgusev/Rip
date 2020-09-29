from abc import abstractmethod, ABC


#Абстрактный  метод  классов для дальнейшего использования и написания классов геом. фигур
class GeometricFigure(ABC):
    @abstractmethod
    def area(self): #self – это ссылка на текущий экземпляр класса
        pass
