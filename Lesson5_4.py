my_dict_rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
ml = []
with open("les5_4.txt", "r", encoding='utf-8') as f:
   my_list = f.read().split('\n')
   for i in my_list:
       i = i.split(" ", 1)
       ml.append(my_dict_rus[i[0]] + " " + i[1])
print(ml)

with open("les5_4_1.txt", "w", encoding='utf-8') as f:
    ml = map(lambda x: x + '\n', ml)
    f.writelines(ml)
