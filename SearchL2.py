from DBgenL1Backup import teacher, structure_data, check

"""
Функция быстрой сортировки
param: cringe: массив, в котором производится поик элемента key
type: cringe: iterative with random access and comparable elements
param key: элемент поиска
type: key: str
return: list, список индексов элементов = key
"""

def linear_search(cringe, key):
    array = cringe.copy()
    result = []
    for i in range(len(array)):
        array[i] = teacher.str_to_list(str(array[i]))
        if key in array[i]:
            result.append(i)
    if len(result) == 0:
        return "No elements found"
    else:
        return result

"""
Функция бинарного поиска
param: cringe: массив, в котором производится поик элемента key
type: cringe: iterative with random access and comparable elements
param: first: нижняя граница поиска
type: first: int
param: last: верхняя граница поиска
type: last: int
param key: элемент поиска
type: key: str
return: list, список индексов элементов = key
"""

def bin_search(cringe, first, last, key):
    array = cringe.copy()
    result = []
    i = check(key, structure_data) - 1
    
    if first >= last:
        return "Wrong borders"
    
    mid = first + (last - first) // 2
    array[mid] = teacher.str_to_list(str(array[mid]))
    
    while key not in array[mid] and first <= last:
        if key > array[mid][i]:
            first = mid + 1
        else:
            last = mid - 1
        mid = first + (last - first) // 2
        array[mid] = teacher.str_to_list(str(array[mid]))
    if first <= last:
        result.append(mid)
        bound = mid + 1
        while bound < len(array) and key in teacher.str_to_list(str(array[bound])):
            result.append(bound)
            bound += 1
        bound = mid - 1
        while bound >= 0 and key in teacher.str_to_list(str(array[bound])):
            result.append(bound)
            bound -= 1
    return result