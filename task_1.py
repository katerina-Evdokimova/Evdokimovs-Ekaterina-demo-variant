import csv

# Открываем файл CSV для чтения
with open('students.csv', encoding='utf8') as f:
    # Получаем список всех записей без заголовка
    reader = list(csv.reader(f, delimiter=',', quotechar='"'))[1:]

    # Поиск оценки по проекту для ученика с определенным именем
    for id, name, titleProject, level, score in reader:
        if 'Хадаров Владимир' in name:
            print(f'')
            break

    # Подсчет количества учеников в каждом классе и расчет средней оценки
    count_class = {}
    sum_class = {}
    for el in reader:
        count_class[el[-2]] = count_class.get(el[-2], 0) + 1
        sum_class[el[-2]] = sum_class.get(el[-2], 0) + (int(el[-1]) if el[-1] != 'None' else 0)

    # Обновлении записей с отсутствующей оценкой
    for el in reader:
        if el[-1] == 'None':
            el[-1] = round(sum_class[el[-2]] / count_class[el[-2]], 3)

# Запись в файл CSV
with open('students_new.csv', 'w', newline='', encoding='utf8') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"')
    writer.writerows(reader)
