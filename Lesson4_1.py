from sys import argv
script, job_hour, cost_hour, prize = argv

def wages(job_hour, cost_hour, prize):
    wag = (int(job_hour) * int(cost_hour)) + int(prize)
    return wag
print(f'Заработная плата сотрудника составляет: {wages(job_hour, cost_hour, prize)} руб.')


