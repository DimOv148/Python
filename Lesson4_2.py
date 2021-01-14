from random import randint
my_list = [randint(0, 300) for i in range(15)]
fin_list = [el for i, el in enumerate(my_list) if my_list[i - 1] < my_list[i] and i <= (len(my_list)-1)]
print(my_list)
print(fin_list)




