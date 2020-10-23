# Б 12, Гусев Сергей Романович, ИУ5Ц-72Б
# 1:М соответствует: определенное средство разработки включает много языков программирования
from operator import itemgetter


class Group:
    """Студенческие группы"""
    def __init__(self, id, name, rating, group_id):
        self.id = id  # id студ группы
        self.name = name  # название группы
        self.rating = rating  # рейтинг группы
        self.group_id = group_id  # id студенческой группы


class Caf:
    """Кафедры"""
    def __init__(self, id, name):
        self.id = id  # id Кафедры 
        self.name = name  # название кафедры


class GroupCaf:
    """'Студ группы на кафедрах'
    необходимо для реализации связи многие-ко-многим"""
    def __init__(self, caf_id, group_id):
        self.caf_id = caf_id
        self.group_id = group_id


# Кафедры
cafs = [
    Caf(1, 'Informatica'),
    Caf(2, 'Fundomental'),
    Caf(3, 'Raketstroi'),

    Caf(11, 'IU5'),
    Caf(22, 'FN1'),
    Caf(33, 'RK9'),
]

# Студенческие группы
groups = [
    Group(1, 'IU8-72B', 1, 1),
    Group(2, 'FN4-32B', 20, 2),
    Group(3, 'RK2-73B', 3, 3),
    Group(4, 'IU5-52B', 17, 3),
    Group(5, 'FN1-12M', 5, 3),
    Group(6, 'RK9-14B', 12, 3)
]

groups_cafs= [
    GroupCaf(1, 1),
    GroupCaf(2, 2),
    GroupCaf(3, 3),
    GroupCaf(3, 4),
    GroupCaf(3, 5),
    GroupCaf(3, 6),

    GroupCaf(11, 1),
    GroupCaf(22, 2),
    GroupCaf(33, 3),
    GroupCaf(33, 4),
    GroupCaf(33, 5),
    GroupCaf(33, 6)
]


def main():

    """Основная функция"""
    # Соединение данных один-ко-многим
    one_to_many = [(g.name, g.rating, c.name)
                   for c in cafs
                   for g in groups
                   if g.group_id == c.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.name, gc.group_id, gc.caf_id)
                         for c in groups
                         for gc in groups_cafs
                         if c.id == gc.caf_id]

    many_to_many = [(g.name, g.rating, cafs_name)
                    for cafs_name, cafs_id, group_id in many_to_many_temp
                    for g in groups if g.id == group_id]

    print('Задание Б1')
    res_11 = sorted(one_to_many, key=itemgetter(0))
    print(res_11)  # сортировка по имени студенческих групп

    print('\nЗадание Б2')
    res_12_unsorted = []
    for c in cafs:
        c_groups = list(filter(lambda x: x[2] == c.name, one_to_many))
        if len(c_groups) > 0:
            g_count = len(c_groups)
            res_12_unsorted.append((c.name, g_count))
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)  # сортировка по убыванию количества групп

    print('\nЗадание Б3')
    res_13 = {}
    for g in groups:
        if 'B' == g.name[-1:]:
            c_groups = list(filter(lambda x: x[0] == g.name, many_to_many))
            c_groups_names = [x[2] for x in c_groups]
            res_13[g.name] = c_groups_names
    
    print(res_13) 


if __name__ == '__main__':
    main()
