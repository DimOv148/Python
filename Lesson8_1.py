class Date:

    @classmethod
    def num_date(cls, my_date):
        my_list = my_date.split('-')
        my_list = [int(my_list[i]) for i in range(len(my_list))]
        return my_list

    @staticmethod
    def val_date(day, month, year):
        if day > 0 and day < 31:
            if month > 0 and month <= 12:
                if year == 2020:
                    return f'Текущая дата {day}.{month}.{year}'
                else:
                    return 'Неверный год'
            else:
                return 'Неверный месяц'
        else:
            return 'Неверный день месяца'


print(Date.num_date('12-01-2020'))
print(Date.val_date(2, 12, 2020))
print(Date.val_date(32, 12, 2020))
print(Date.val_date(2, 15, 2020))
print(Date.val_date(2, 12, 2022))
