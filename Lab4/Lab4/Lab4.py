from lab_python_pt.facade.Facade import Facade

# Фасад — это структурный паттерн проектирования, который предоставляет простой интерфейс к сложной системе классов, библиотеке или фреймворку.
"""
    Класс Фасада предоставляет простой интерфейс для сложной логики одной или
    нескольких подсистем. Фасад делегирует запросы клиентов соответствующим
    объектам внутри подсистемы. Фасад также отвечает за управление их жизненным
    циклом. Все это защищает клиента от нежелательной сложности подсистемы.
    """

def main():
    facade = Facade()
    facade.create_shops(1, 2)
    facade.create_clients(1, 2, 1)
    facade.attach_clients()

    facade.sport_shop_business_logic()
    facade.electronic_shop_business_logic()

    facade.detach_clients()

    facade.sport_shop_business_logic()
    facade.electronic_shop_business_logic()


if __name__ == '__main__':
    main()