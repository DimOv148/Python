def user_data(**kwargs):
    """Функция принимает неограниченное количество аргументов и выводи их на экран"""
    return kwargs
a = user_data(name = 'Александр', l_name = 'Петров', year_bth = '1988', sity_res = 'Москва', email = 'a_petr@mail.ru',
              phone='79176543321', street = 'Tverskaya', house = '18', flat = '17')
print(' '.join(a.values()))


def user_data_1(name, l_name, year_bth, sity_res, email, phone):
    """Функция принимает именованные аргументы и выводит их на экран одной строкой"""
    return f'{name}, {l_name}, {year_bth}, {sity_res}, {email}, {phone}'


print(user_data_1('Василий', 'Сидоров', 1888, 'Брянск', 'vsa@mail.ru', 79634586789))

