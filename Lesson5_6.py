s={}
with open("les5_6.txt", "r", encoding='utf-8') as f:
    subj = f.read().split('\n')
    print(subj)
    for line in subj:
        sub = line.split()
        hour_list = [int(num) for num in filter(lambda num: num.isnumeric(), sub)]
        s[sub[0]] = sum(hour_list)
    print(s)
