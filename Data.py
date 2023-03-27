import math


class Data:
    def __init__(self, filename):
        file = open(filename, 'r')
        self.all_ages =[int(line.strip()) for line in file]
        self.people_number = len(self.all_ages)                         # Количество всех людей
        self.scope = max(self.all_ages) - min(self.all_ages)            # Размах
        self.groups_number = round(1 + 3.222 * math.log10(self.scope))  # Количество групп
        self.len_interval = math.ceil(self.scope / self.groups_number)  # Длина интервала
        self.ages_sorted = sorted(self.all_ages)


