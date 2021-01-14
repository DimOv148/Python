from random import randint
my_list = [randint(0, 15) for i in range(20)]
print(my_list)
lst = [i for i in my_list if my_list.count(i) == 1]
print(lst)

