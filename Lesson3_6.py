def int_func(word):
    """Функция заменяет первую букву слова на заглавную"""
    result = word[0].upper() + word[1:]
    return result


my_list_word = []
my_str = input('введите слова через пробел: ').lower().split()
for word in my_str:
    my_list_word.append(int_func(word))
print(my_list_word)
