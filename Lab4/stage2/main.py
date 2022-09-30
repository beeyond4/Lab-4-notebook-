#python3.10 main.py

def tableprint(dicts): # Вывод ТАБЛИЦЫ в консоль
    print("{:<3} {:<30} {:<6} {:<12} {:<15} {:<10}".format('Num','Task','Time','Date','Status','Result'))
    for dict in dicts:
        num, task, time, date, status, result = dict.values()
        print("{:<3} {:<30} {:<6} {:<12} {:<15} {:<10}".format(num, task, time, date, status, result))


def schedule_data(): # Запись данных с ФАЙЛА 'notebook1.csv'

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
    return schedule


def schedule_add(schedule): # Добавление заметки
    Counter = len(schedule)
    notice = input('Введите новую заметку (Введите Close для завершения):\n')
    if notice == 'Close':
        return True
    note = list(notice.split(', '))
    note[3]=str('(' + note[3] + ')')
    note.insert(0, str(Counter))

    with open('notebook1.csv', 'a', encoding='utf-8') as String:
        String.write(','.join(note)  + '\n')

# Блок работы приложения
while True:
    schedule = schedule_data()
    tableprint(schedule)
    trigger = schedule_add(schedule)
    if trigger:
        break
