import random
import operator

"""
Функция сортировки пузырьком
param: array: массив, который должен быть отсортирован
type: array:  iterative with random access and comparable elements
"""

def bubble_sort(array):
    N = len(array)
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff
    return array

"""
Функция быстрой сортировки
param: array: массив, который должен быть отсортирован
type: array: iterative with random access and comparable elements
"""
            
def quick_sort(array):
   if len(array) < 2:
       return array
   else:
       q = random.choice(array)
       s_elem = []
       m_elem = []
       e_elem = []
       for n in array:
           if n < q:
               s_elem.append(n)
           elif n > q:
               m_elem.append(n)
           else:
               e_elem.append(n)
       return quick_sort(s_elem) + e_elem + quick_sort(m_elem)
   
"""
Функция сортировки слиянием
param: file_name: массив, который должен быть отсортирован
type: file_name:  iterative with random access and comparable elements
"""

def merge_sort(array, compare=operator.lt): #operator.lt - <
    if len(array) < 2:
        return array
    else:
        middle = int(len(array) / 2)
        #Дробление входного массива на половины
        left = merge_sort(array[:middle], compare)
        right = merge_sort(array[middle:], compare)
        return merge(left, right, compare)
    
"""
Функция, сравнивающая элементы из левой и правой части
param: left: левая граница
type: left: iterable
param: right: правая граница
type: right: iterable
"""

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

