import random

team1_num = random.randint(4, 6)
team2_num = random.randint(4, 6)
score_1 = random.randint(30, 60)
score_2 = random.randint(30, 60)
team1_time = round(random.uniform(1500, 2200), 5)
team2_time = round(random.uniform(1500, 2200), 5)
tasks_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / 2, 5)

if score_1 >= score_2 and team1_time <= team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 and team1_time >= team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

# %
print('В команде Мастера кода участников: %s!' % team1_num)
print('В команде Волшебники Данных: %s!' % team2_num)
print('Итого сегодня в командах участников: %s и  %s!' % (team1_num, team2_num))

# format()
print('Команда Мастера кода решила задач: {}'.format(score_1))
print('Команда Мастера кода решили задачи за {}'.format(team1_time))
print('Команда Волшебники данных решила задач: {}'.format(score_2))
print('Команда Волшебники данных решили задачи за {}'.format(team2_time))

# f
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg/tasks_total, 5)} секунды на задачу!')