import time
import pylab
import matplotlib.pyplot as plt
from SortsL1 import merge_sort
from DBgenL1Backup import generate, teacher, structure_scheme, structure_data, multimap_creation
from SearchL2 import linear_search, bin_search

"""
Основная функция лабораторной
param db_filename: имя базы данных
type: db_filename: str
param: count_range: массив кол - ва обьектов в базе данных
type: count_range: iterable 
param: structure_shceme: структура данных для генерации
type: structure_scheme: tuple(tuple(str, iterable) .. str)
param: structure_data: данные для генерации структуры
type: structure_data: dict('key' : [val])
param key: элемент поиска
type: key: str
"""

def make(db_file_name, elements_quantity, structure_scheme, structure_data, key):
    
    results = {'linear': [], 'binary+sort': [], 'binaryinsorted':[], 'multimap':[]}
    
    for count in elements_quantity:
        generate(db_file_name, count, structure_scheme, structure_data) 
        print('{} elements '.format(count))
    
        file = open(db_file_name, 'r')
        tch_list = []
        for line in file:
            tch_list.append(teacher(*line.replace('\n', '').split(';')))
        
        print("Linear search start")
        tb = time.time()
        linear_search(tch_list, key)
        ta = time.time()
        results['linear'].append((count, ta - tb))
        
        print("Binary search with merge sort start")
        ta = time.time()
        bin_search(merge_sort(tch_list), 0, len(tch_list), key)
        ta = time.time()
        results['binary+sort'].append((count, ta - tb))
        
        print("Binary search in sorted array start")
        tch_list_copy = tch_list.copy()
        tch_list_copy = merge_sort(tch_list_copy)
        tb = time.time()
        bin_search(tch_list_copy, 0, len(tch_list_copy), key)
        ta = time.time()
        results['binaryinsorted'].append((count, ta - tb))
        
        del tch_list_copy
        
        print("Search in multimap<key, obj> started")
        multimap = multimap_creation(tch_list)
        tb = time.time()
        multimap['КБ']
        ta = time.time()
        results['multimap'].append((count, ta - tb))
        
        del tch_list
        print('\n')
        
    xlist = elements_quantity
    ylist1 = [el[1] for el in results['linear']]
    ylist2 = [el[1] for el in results['binary+sort']]
    ylist3 = [el[1] for el in results['binaryinsorted']]
    ylist4 = [el[1] for el in results['multimap']]
    plt.plot(xlist, ylist1, label = 'Линейный поиск')
    plt.plot(xlist, ylist2, label = 'Бинарный + сортировка')
    plt.plot(xlist, ylist3, label = 'Бинарный')
    plt.plot(xlist, ylist4, label = 'multimap')
    pylab.title('Сравнение линейного, бинарных поисков, и поиска в асс. массиве')
    pylab.xlabel('Количество объектов')
    pylab.ylabel('Время на поиск')
    pylab.legend(title='Легенда')
    
    print("Linear")
    for element in results['linear']:
        print(str(element[0]) + ';' + str(element[1]))
    print('\n')
       
    print("Bin + merge sort")
    for element in results['binary+sort']:
        print(str(element[0]) + ';' + str(element[1]))
    print('\n')
       
    print("Bin")
    for element in results['binaryinsorted']:
        print(str(element[0]) + ';' + str(element[1]))
    print('\n')
    
    print("Mult")
    for element in results['multimap']:
        print(str(element[0]) + ';' + str(element[1]))
    print('\n')
    
    pylab.show()    

"""
Функция выполняет линейный поиск по элементу key и выводит строки с ним в файл
param: filename: имя файла в котором осуществляется поиск
type: filename: str
param: key: элемент, который нужно найти
type: key: str
return: файл с элементами = key
"""

def linsearch_and_print(filename, key):
    file = open(filename, 'r')
    tch_list = []
    for line in file:
        tch_list.append(teacher(*line.replace('\n', '').split(';')))
    file2 = open('Linsearch_result.txt', 'w')
    keys = linear_search(tch_list, key)
    for i in keys:
        file2.write(str(tch_list[i]) + '\n')
    file2.close()
    
"""
Функция выполняет бинарный поиск по элементу key и выводит строки с ним в файл
param: filename: имя файла в котором осуществляется поиск
type: filename: str
param: key: элемент, который нужно найти
type: key: str
return: файл с элементами = key
"""    
    
def Binsearch_and_print(filename, key):
    file = open(filename, 'r')
    tch_list = []
    for line in file:
        tch_list.append(teacher(*line.replace('\n', '').split(';')))
    merge_sort(tch_list)
    file2 = open('Binsearch_result.txt', 'w')
    keys = bin_search(tch_list, 0, len(tch_list), key)
    for i in keys:
        file2.write(str(tch_list[i]) + '\n')
    file2.close()    
    

elements_quantity = [25, 50, 75, 100, 250, 500, 1000]
db_file_name = 'teachers.txt'
make(db_file_name, elements_quantity, structure_scheme, structure_data, 'КБ')