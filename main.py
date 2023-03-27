import Data, Discrete_data, Interval_data, Additional_group_task


def main():
    data = Data.Data('Статистика_Возраст_Москва_2021.txt')
    discrete = Discrete_data.DiscreteData(data)
    discrete.print_results()
    discrete.histogram()
    interval = Interval_data.IntervalData(data)
    interval.print_results()
    interval.histogram()

    print()
    print('ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:')
    groups = list()
    groups.append(Additional_group_task.Group(discrete, 14, 32))
    groups.append(Additional_group_task.Group(discrete, 33, 50))
    groups.append(Additional_group_task.Group(discrete, 51, 73))
    Additional_group_task.all_groups(groups, discrete)


if __name__ == '__main__':
    main()


