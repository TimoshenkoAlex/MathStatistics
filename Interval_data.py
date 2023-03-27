import Data
import matplotlib.pyplot as plt


class IntervalData:
    def __init__(self, data: Data.Data):
        self.interval = list(range(min(data.ages_sorted), max(data.ages_sorted), data.len_interval))
        self.interval.append(max(data.ages_sorted))
        self.names = [str(self.interval[i]) + '-' + str(self.interval[i+1]) for i in range(len(self.interval) - 1)]
        self.values = [sum([data.ages_sorted.count(i)
                            for i in range(j, j + data.len_interval)]) for j in self.interval[:-1]]
        self.ages_lib = {self.names[i]: self.values[i] for i in range(data.groups_number)}
        # Средняя интервальная
        self.middle = sum([(self.interval[i] + self.interval[i + 1]) / 2 * self.values[i]
                           for i in range(len(self.interval) - 1)]) / data.people_number
        # Дисперсия
        self.dispersion = sum([((self.interval[i] + self.interval[i + 1]) / 2 - self.middle) ** 2
                               * self.values[i] for i in range(len(self.interval) - 1)]) / data.people_number
        # Мода
        frequencies_mode = self.values.copy()
        frequencies_mode.append(0)
        frequencies_mode.insert(0, 0)
        index_mode_interval = self.values.index(max(self.values))
        self.mode = self.interval[index_mode_interval] + data.len_interval * \
                    (frequencies_mode[index_mode_interval + 1] - frequencies_mode[index_mode_interval]) / \
                    ((frequencies_mode[index_mode_interval + 1] - frequencies_mode[index_mode_interval]) +
                     frequencies_mode[index_mode_interval + 1] - frequencies_mode[index_mode_interval + 2])
        # Медиана
        median_sum = 0
        for i in range(len(self.values)):
            median_sum += self.values[i]
            if median_sum > data.people_number / 2:
                median_index = i
                break
        self.median = (self.interval[median_index] + data.len_interval *
                       (data.people_number / 2 - median_sum + self.values[median_index]) / self.values[median_index])
        self.scope = data.scope
        self.coef_variation = self.dispersion ** (1/2) / self.middle * 100

    def histogram(self):
        plt.bar(self.names, self.values)
        plt.show()

    def print_results(self):
        print()
        print('ИНТЕРВАЛЬНЫЙ РЯД')
        print(f'Интервальный ряд: {self.ages_lib}')
        print(f'Средняя: {self.middle}')
        print(f'Дисперсия: {self.dispersion}')
        print(f'Мода: {self.mode}')
        print(f'Медиана: {self.median}')
        print(f'Размах: {self.scope}')
        print(f'Коэффициент вариации: {self.coef_variation}')


