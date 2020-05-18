import time
import pylab
import matplotlib.pyplot as plt
from SortsL1 import bubble_sort, quick_sort ,merge_sort
from DBgenL1 import generate, teacher, structure_scheme, structure_data

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
"""

def make(db_file_name, count_range, structure_scheme, structure_data):
   results = {'quick': [], 'bubble': [], 'merge':[]}
   for count in count_range:
       print('{} elements '.format(count))
       #Генерируем базу данных
       generate(db_file_name, count, structure_scheme, structure_data) 
       
       #Извлекаем данные из файла в массив
       file = open(db_file_name, 'r')
       tch_list = []
       for line in file:
          tch_list.append(teacher(*line.replace('\n', '').split(';')))
       
       print('bubble sort start')
       tch_list_sorted = tch_list.copy()
       tb = time.time() # запускаем счетчик времени
       bubble_sort(tch_list_sorted) # выполняем сортировку пузырьком
       ta = time.time()
       results['bubble'].append((count, ta - tb))
       
       del tch_list_sorted
       
       print('quick sort start')
       tch_list_sorted = tch_list.copy()
       tb = time.time() # запускаем счетчик времени
       quick_sort(tch_list_sorted) # выполняем быструю сортировку
       ta = time.time()
       results['quick'].append((count, ta - tb))
       
       del tch_list_sorted
       
       print('merge sort start')
       tch_list_sorted = tch_list.copy()
       tb = time.time() # запускаем счетчик времени
       merge_sort(tch_list_sorted) # выполняем сортировку слиянием
       ta = time.time()
       results['merge'].append((count, ta - tb))
       print('\n')
       
       del tch_list_sorted
       
       del tch_list 

   #Построение графиков
   xlist = count_range
   ylist1 = [el[1] for el in results['bubble']]
   ylist2 = [el[1] for el in results['quick']]
   ylist3 = [el[1] for el in results['merge']]
   plt.loglog(xlist, ylist1, label = 'Сортировка пузырьком')
   plt.loglog(xlist, ylist2, label = 'Быстрая')
   plt.loglog(xlist, ylist3, label = 'Сортировка слиянием')
   pylab.title('Сравнение быстрой, пузырьковой и сортировки слиянием')
   pylab.xlabel('Количество объектов')
   pylab.ylabel('Время на сортировку')
   pylab.legend(title='Легенда')
   
   #Вывод количества элементов, и времени сортировки
   print("Bubble")
   for element in results['bubble']:
       print(str(element[0]) + ';' + str(element[1]))
       
   print("Quick")
   for element in results['quick']:
       print(str(element[0]) + ';' + str(element[1]))
       
   print("Merge")
   for element in results['merge']:
       print(str(element[0]) + ';' + str(element[1]))
       
   pylab.show()
   
"""
Функция сортировки пузырьком
param file_name: имя базы данных
type: file_name: str
"""

def print_bubble_sort(file_name):
    file = open(file_name, 'r')
    tch_list = []
    for line in file:
        tch_list.append(teacher(*line.replace('\n', '').split(';')))
    print(bubble_sort(tch_list))

"""
Функция быстрой сортировки
param: file_name: имя базы данных
type: file_name: str
"""
 
def print_quick_sort(file_name):
    file = open(file_name, 'r')
    tch_list = []
    for line in file:
        tch_list.append(teacher(*line.replace('\n', '').split(';')))
    print(quick_sort(tch_list))

"""
Функция сортировки слиянием
param: file_name: имя базы данных
type: file_name: str
"""
  
def print_merge_sort(file_name):
    file = open(file_name, 'r')
    tch_list = []
    for line in file:
        tch_list.append(teacher(*line.replace('\n', '').split(';')))
    print(merge_sort(tch_list))
    
elements_quantity = [1000, 1500, 2000, 3000]
filename = 'teachers.txt'
make(filename, elements_quantity, structure_scheme, structure_data)