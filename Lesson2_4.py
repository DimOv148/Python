wds = input('Введите несколько слов через пробел или напишите предложение: ')
wds = wds.split()
for i, n in enumerate(wds, 1):
    print(f'{i}: {n[:10]}')
