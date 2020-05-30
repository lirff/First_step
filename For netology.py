residence_limit = 90
schengen_constraint = 180

visits = [[1, 10], [21, 30], [45, 46], [251, 260], 2]
# 10, 10 + 10, 10 + 10 + 2, 10 + 10 + 2 + 10

for visit in visits:
    if not isinstance(visit, list):
        raise Exception("Ошибка в типе поездки: ", visit)

days_in_es = []

total_time_in_es = 0

for visit in visits:
    past_days = 0
    for past_visit in visits:
        #if past_visit[0] <= visit[0] and past_visit[0] > visit[0] - schengen_constraint: #аналдогичен условию ниже
        if visit[0] - schengen_constraint < past_visit[0] <= visit[0]:
            past_days += past_visit[1] - past_visit[0] + 1
    days_in_es.append(past_days)
    total_time_in_es += visit[1] - visit[0] + 1

#assert total_time_in_es == 10 + 10 + 2 + 10

print(days_in_es)
#print(visits)
assert days_in_es == [10, 10 + 10, 10 + 10 + 2, 10]

for visit, days in zip(visits, days_in_es):
    if days > residence_limit:
        print('В течении поездки', visit, 'вы пребывали в ЕС слишком дого:', days)

if total_time_in_es > residence_limit:
    print('Вы не можете прибывать в ЕС так долго')

print('Вы пробудете в ЕС:', total_time_in_es)