import csv
from pprint import pprint


def insertion_sort(arr: list):
    '''
    Функция сортировки вставками по убыванию
    Args:
        arr (list): Список для сортировки

    Returns:
        :return
    '''
    arr = arr.copy()
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        flag = float(arr[j]['score'] if arr[j]['score'] != 'None' else 0) < float(
            temp['score'] if temp['score'] != 'None' else '0')
        while flag and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr


def merge_sort(arr: list):
    '''
    Функция сортировки слияниями по возрастанию
    Args:
        arr (list): Список для сортировки

    Returns:
        :return
    '''
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merge_sort(left)
    merge_sort(right)

    i, j, k = 0, 0, 0
    # i = j = k = 0
    while i < len(left) and j < len(right):
        if float(left[i]['score']) < float(right[j]['score']):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def quick_sort(arr: list, start, end):
    """
    Функция сортировки массива по возрастанию
    :param arr:
    :param start:
    :param end:
    :return:
    """
    if start >= end:
        return

    i_pivot = partition(arr, start, end - 1)

    quick_sort(arr, start, i_pivot)
    quick_sort(arr, i_pivot + 1, end)


def partition(arr, start, end):
    '''
    Функция разделения массива по средней оценке
    :param arr:
    :param start:
    :param end:
    :return:
    '''
    pivot = arr[end]
    i_pivot = start
    for j in range(start, end):
        if (float(arr[j]['score']) if arr[j]['score'] != 'None' else 0) > (float(pivot['score'])if pivot['score'] != 'None' else 0):
            arr[i_pivot], arr[j] = arr[j], arr[i_pivot]
            i_pivot += 1
    arr[i_pivot], arr[end] = arr[end], arr[i_pivot]

    return i_pivot


# Открываем файл CSV для чтения
with open('students.csv', encoding='utf8') as f:
    # Получаем список всех записей без заголовка
    reader = list(csv.DictReader(f, delimiter=',', quotechar='"'))[1:]
    quick_sort(reader, 0, len(reader))
    print(reader)

# print('10 class')
# count = 1
# for el in reader:
#     print(f'{el}')
