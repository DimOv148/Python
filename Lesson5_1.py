with open("test.txt", "w", encoding='utf-8') as f:
    while True:
        a = input('enter data: ')
        if not a:
            break
        f.write(a + '\n')


