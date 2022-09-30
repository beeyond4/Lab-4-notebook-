#python3.10 main.py
def tableprint(dicts):
    print("{:<3} {:<30} {:<6} {:<12} {:<15} {:<10}".format('Num','Task','Time','Date','Status','Result'))
    for dict in dicts:
        num, task, time, date, status, result = dict.values()
        print("{:<3} {:<30} {:<6} {:<12} {:<15} {:<10}".format(num, task, time, date, status, result))


# Считываем файл и сохраняем в СПИСОК
with open('notebook1.csv', encoding='utf-8') as data:
    schedule_lst = list(map(lambda x: list(x.strip('\n').split(',')),data.readlines()))

#Наполняем НОВЫЙ список 'schedule' СЛОВАРЯМИ, со значениями из каждой строки
schedule = []
keys = ["number","task","time","date","status","result"]
for String in schedule_lst:
    Dictionary = {}
    for index in range(len(keys)):
        Dictionary[keys[index]] = String[index]
    schedule.append(Dictionary)

tableprint(schedule)
