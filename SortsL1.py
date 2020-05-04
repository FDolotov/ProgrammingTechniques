import random
import operator

#Алгоритм сортировки пузырьком
def bubble_sort(array):
    N = len(array)
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff
    return array

#Алгоритм быстрой сортировки                
def quick_sort(array):
   if len(array) <= 1:
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
   
#Алгоритм сортировки слиянием
def merge_sort(array, compare=operator.lt): #operator.lt - <
    if len(array) < 2:
        return array[:]
    else:
        middle = int(len(array) / 2)
        #Дробление входного массива на половины
        left = merge_sort(array[:middle], compare)
        right = merge_sort(array[middle:], compare)
        return merge(left, right, compare)
    
#Функция, сравнивающая элементы из левой и правой части
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

