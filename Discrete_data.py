import Data
import matplotlib.pyplot as plt


class DiscreteData:
    def __init__(self, data: Data):
        self.ages_set = list(set(data.ages_sorted))                                       # Возраста
        self.ages_lib = {i: data.ages_sorted.count(i) for i in self.ages_set}       # Возраста с частотой
        self.ages_frequencies = list(self.ages_lib.values())                          # Частоты
        # Среднее для дискретных значений
        self.middle = sum([self.ages_frequencies[i] * self.ages_set[i]
                           for i in range(len(self.ages_set))]) / data.people_number
        self.deviations = [age - self.middle for age in self.ages_set]              #Отклонения
        # Дисперсия
        self.dispersion = sum([self.deviations[i] ** 2 * self.ages_frequencies[i]
                               for i in range(len(self.ages_frequencies))]) / data.people_number
        self.middle_quad_deviation = self.dispersion ** (1/2)
        # Мода
        self.mode = self.ages_set[self.ages_frequencies.index(max(self.ages_frequencies))]
        # Медиана
        if len(self.ages_set) % 2 == 1:
            self.median = self.ages_set[len(self.ages_set) // 2 + 1]
        else:
            self.median = (self.ages_set[len(self.ages_set) // 2] + self.ages_set[len(self.ages_set) // 2 + 1]) / 2
        self.scope = data.scope
        self.variation_coef = self.middle_quad_deviation / self.middle * 100

    def histogram(self):
        plt.bar(self.ages_set, self.ages_frequencies)
        plt.show()

    def print_results(self):
        print()
        print('ДИСКРЕТНЫЙ РЯД')
        print(f'Дискретный ряд: {self.ages_lib}')
        print(f'Средняя: {self.middle}')
        print(f'Отклонения: {self.deviations}')
        print(f'Дисперсия: {self.dispersion}')
        print(f'Среднее квадратичное отклонение: {self.middle_quad_deviation}')
        print(f'Мода: {self.mode}')
        print(f'Медиана: {self.median}')
        print(f'Размах: {self.scope}')
        print(f'Коэффициент вариации: {self.variation_coef}')
