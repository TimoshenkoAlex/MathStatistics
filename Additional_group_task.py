import Discrete_data


class Group:
    def __init__(self, data: Discrete_data.DiscreteData, start, end):
        self.ages_set = data.ages_set[data.ages_set.index(start): data.ages_set.index(end) + 1]
        self.ages_frequencies = data.ages_frequencies[data.ages_set.index(start): data.ages_set.index(end) + 1]
        self.amount = sum(self.ages_frequencies)
        self.middle = sum([self.ages_set[i] * self.ages_frequencies[i]
                           for i in range(len(self.ages_set))]) / self.amount
        self.dispersion = sum([(self.ages_set[i] - self.middle) ** 2 * self.ages_frequencies[i]
                               for i in range(len(self.ages_set))]) / self.amount

    def print_results(self):
        print(f'Для группы {min(self.ages_set)}-{max(self.ages_set)}')
        print(f'Общая сумма группы: {self.amount}')
        print(f'Групповая средняя: {self.middle}')
        print(f'Групповая дисперсия: {self.dispersion}')


def all_groups(array, data: Discrete_data.DiscreteData):
    for group in array:
        print()
        group.print_results()
    overall_average = sum([group.middle * group.amount for group in array]) / sum(data.ages_frequencies)
    print(f'Общая средняя: {overall_average}')
    ingroup_dispersion = sum([group.dispersion * group.amount for group in array]) / sum(data.ages_frequencies)
    print(f'Внутригрупповая дисперсия: {ingroup_dispersion}')
    intergroup_dispersion = sum([(group.middle - data.middle) ** 2 * group.amount
                                 for group in array]) / sum(data.ages_frequencies)
    print(f'Межгрупповая дисперсия: {intergroup_dispersion}')
    general_dispersion = ingroup_dispersion + intergroup_dispersion
    print(f'Общая дисперсия: {general_dispersion}')








