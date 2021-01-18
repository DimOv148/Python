with open("les5_2.txt", "r", encoding='utf-8') as f:
    lines = f.readlines()
    for i, v in enumerate(lines):
        words = len(v.split())
        print(f'Строка {i+1} содержит {words} слов')
    print(f'Всего строк в файле {i+1}')

