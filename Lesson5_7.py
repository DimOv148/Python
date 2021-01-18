import json
profit = {}
a_pr = {}
res = []
prof = 0
average_profit = 0
i = 0


with open("les 5_7.txt", "r", encoding='utf-8') as f:
    for line in f:
        firm, owner, rev, cost = line.split()
        profit[firm] = int(rev) - int(cost)
        if profit.setdefault(firm) >= 0:
            prof = prof + profit.setdefault(firm)
            i += 1
        if i != 0:
            average_profit = prof / i
        else:
            print(f'Прибыль отсутствует')
        a_pr = {'average_profit ': average_profit}

res.append(profit)
res.append(a_pr)
print(res)

with open("les 5_7.json", "w", encoding='utf-8') as f:
    json.dump(res, f)




