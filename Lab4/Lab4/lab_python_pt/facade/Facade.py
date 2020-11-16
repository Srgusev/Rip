from __future__ import annotations
from lab_python_pt.factory.ShopFactory import SportShopFactory, ElectronicsShopFactory, get_shop
from lab_python_pt.factory.ClientFactory import SportShopClientFactory, ElectronicsShopClientFactory, \
    SportElectronicsShopClientFactory, get_client


class Facade:
    """ В зависимости от потребностей вашего приложения вы можете предоставить
        Фасаду существующие объекты подсистемы или заставить Фасад создать их
        самостоятельно.
        """

    def __init__(self, sport_shops=None,
                 electronics_shops=None,
                 sport_shop_clients=None,
                 electronics_shop_clients=None,
                 sport_electronics_shop_clients=None):
        if sport_electronics_shop_clients is None:
            sport_electronics_shop_clients = []
        if electronics_shop_clients is None:
            electronics_shop_clients = []
        if sport_shop_clients is None:
            sport_shop_clients = []
        if electronics_shops is None:
            electronics_shops = []
        if sport_shops is None:
            sport_shops = []
        self.__sport_shops = sport_shops
        self.__electronics_shops = electronics_shops
        self.__sport_shop_clients = sport_shop_clients
        self.__electronics_shop_clients = electronics_shop_clients
        self.__sport_electronics_shop_clients = sport_electronics_shop_clients

    @property
    def sport_shops(self):
        return self.__sport_shops

    @property
    def electronics_shops(self):
        return self.__electronics_shops

    @property
    def sport_shop_clients(self):
        return self.__sport_shop_clients

    @property
    def electronics_shop_clients(self):
        return self.__electronics_shop_clients

    @property
    def sport_electronics_shop_clients(self):
        return self.__sport_electronics_shop_clients

    def sport_shop_business_logic(self):
        print('Бизнес-логика спортивного магазина:')
        for i in range(0, len(self.__sport_shops)):
            self.__sport_shops[i].business_logic()
        print('\n')

    def electronic_shop_business_logic(self):
        print('Бизнес-логика магазина электроники:')
        for i in range(0, len(self.__electronics_shops)):
            self.__electronics_shops[i].business_logic()
        print('\n')

    def create_shops(self, sport_shop_count, electronics_shops_count):
        print('Заводские магазины:')
        self.__create_shops('спорт',
                            self.__sport_shops,
                            sport_shop_count,
                            SportShopFactory())

        self.__create_shops('электроника',
                            self.__electronics_shops,
                            electronics_shops_count,
                            ElectronicsShopFactory())

        print('\n')

    def create_clients(self,
                       sport_shop_clients_count,
                       electronics_shop_clients_count,
                       sport_electronics_shop_clients_count):

        print('\nЗаводской клиент:')
        self.__create_clients('спорт',
                              self.__sport_shop_clients,
                              sport_shop_clients_count,
                              SportShopClientFactory())

        self.__create_clients('элетроника',
                              self.__electronics_shop_clients,
                              electronics_shop_clients_count,
                              ElectronicsShopClientFactory())

        self.__create_clients('спорт электроника',
                              self.__sport_electronics_shop_clients,
                              sport_electronics_shop_clients_count,
                              SportElectronicsShopClientFactory())

        print('\n')

    def attach_clients(self):
        print('Прикрепление наблюдателя:')
        self.__attach_clients('спорт',
                              self.__sport_shops,
                              self.__sport_shop_clients)

        self.__attach_clients('электроника',
                              self.__electronics_shops,
                              self.__electronics_shop_clients)

        self.__attach_clients('спорт электроника',
                              self.__sport_shops,
                              self.__sport_electronics_shop_clients)

        self.__attach_clients('спорт электроника',
                              self.__electronics_shops,
                              self.__sport_electronics_shop_clients)

        print('\n')
        
        """
        Методы Фасада удобны для быстрого доступа к сложной функциональности
        подсистем. Однако клиенты получают только часть возможностей подсистемы.
        """

    def detach_clients(self):
        print('Прикрепление наблюдателя:')
        self.__detach_clients('спорт',
                              self.__sport_shops,
                              self.__sport_shop_clients)

        self.__detach_clients('электроника',
                              self.__electronics_shops,
                              self.__electronics_shop_clients)

        self.__detach_clients('электроника спорт',
                              self.__sport_shops,
                              self.__sport_electronics_shop_clients)

        self.__detach_clients('спорт электроника',
                              self.__electronics_shops,
                              self.__sport_electronics_shop_clients)
        print('\n')

    def __create_shops(self, str, shops_list, count, factory):
        print('\nСоздать {} {} магазины:'.format(count, str))
        for i in range(0, count):
            shops_list.append(get_shop(factory, i))

    def __create_clients(self, str, clients_list, count, factory):
        print('\nСоздать {} {} магазин клиенты:'.format(count, str))
        for i in range(0, count):
            clients_list.append(get_client(factory, i))

    def __attach_clients(self, str, shop_list, clients_list):
        print('\nПрикрепить {} {} магазин клиенты:'.format(len(clients_list), str))
        for i in range(0, len(shop_list)):
            for j in range(0, len(clients_list)):
                shop_list[i].attach(clients_list[j])

    def __detach_clients(self, str, shop_list, clients_list):
        print('\nОткрепить {} {} магазин клиенты:'.format(len(clients_list), str))
        for i in range(0, len(shop_list)):
            for j in range(0, len(clients_list)):
                shop_list[i].detach(clients_list[j])
