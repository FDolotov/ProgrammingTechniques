import math
import time
import numpy as np
from scipy.stats import chi2
import pylab
import matplotlib.pyplot as plt
import random

X = int(time.time())
Y = 362436069
Z = 521288629
W = 88675123
seed = time.time()

def XORShift(max_number):
    """
    Функция генерации случайного числа методом XORShift
    param: max_number: максимальное значение
    """
    global X, Y, Z, W
    t = X ^ (X << 11)
    X = Y & 0xFFFFFFFF
    Y = Z & 0xFFFFFFFF
    Z = W & 0xFFFFFFFF
    W = W ^ (W >> 19) ^ t ^ (t >> 8) & 0xFFFFFFFF
    return W % max_number

def XORShift_generate(max_number, quantity):
    nums = []
    for i in range(quantity):
        nums.append(XORShift(max_number))
    return nums

def linear_congruential(max_number):
    """
    Функция генерации случайного числа линейным конгруэнтным методом
    param: max_number: максимальное значение
    """
    global seed
    seed = (69069*int(seed)+5)%(2**32)
    return seed % max_number

def Lincong_generate(max_number, quantity):
    nums = []
    for i in range(quantity):
        nums.append(linear_congruential(max_number))
    return nums
    

def mean(seq):
    """
    Вычисление мат. ожидания
    param: seq: Последовательность чисел
    type: seq: iterable
    return: Выборочное среднее
    """
    return sum(seq)/len(seq)

def deviation(seq):
    """
    Вычисление дисперсии
    param: seq: Последовательность чисел
    type: seq: iterable
    return: Выборочное стандартное отклонение
    """
    return (sum((el - mean(seq)) ** 2 for el in seq) / len(seq)) ** (1/2)

def cv(seq):
    """
    Вычисление выборочного коэффициента вариации
    param: seq: Последовательность чисел
    type: seq: iterable
    return: Выборочный коэффициент вариации
    """
    return deviation(seq) / mean(seq)

def xi2_check(seq, max_number):
    """
    Функция проверки последовательности критерием Пирсона
    param: seq: послеовательость
    param: max_number: максимальный элемент последовательности
    """
    l = len(seq)
    k = 1 + int(3.322*math.log(len(seq)))
    p = 1/k
    
    kek = np.zeros(k) 
    for el in seq:
        for j in range(k):
            if j*max_number/k <= el <= (j+1)*max_number/k:
                kek[j] += 1
                break
            
    dev = sum(kek[i]**2 / p for i in range(k)) / l - l
    if dev < chi2.ppf(.1, k-1):
        print('выборка недостаточно случайна')
    elif dev > chi2.ppf(.9, k-1):
        print('выборка недостаточно равномерна')
    else:
        for quantile in np.arange(.1, .91, .01):
            if chi2.ppf(quantile, k-1) >= dev:
                break
        print('выборка равномерна и случайна с вероятностью', '%.2f' % quantile)
        

def make_plot(max_number, size):
    """
    Функция, выводящая график зависимости объемов выборки от времени
    param: max_number: максимальное число выборки
    param: size: кол- во элементов выборки
    """
    
    results = {'XORSift': [], 'linear_congruential': [], 'random': []}
    for el in size:
        print("{} elements".format(el))
        
        print("XORSift: ")
        ti = time.time()
        XORShift_generate(max_number, el)
        results['XORSift'].append((el, time.time() - ti))
        
        print("Linear_congruential: ")
        ti = time.time()
        Lincong_generate(max_number, el)
        results['linear_congruential'].append((el, time.time() - ti))
        
        print("Random: ")
        ti = time.time()
        for i in range(el):
            random.randint(0, max_number)
        results['random'].append((el, time.time() - ti))
        
    xlist = size
    ylist1 = [el[1] for el in results['XORSift']]
    ylist2 = [el[1] for el in results['linear_congruential']]
    ylist3 = [el[1] for el in results['random']]
    plt.plot(xlist, ylist1, label = 'XORShift')
    plt.plot(xlist, ylist2, label = 'Linear_congruential')
    plt.plot(xlist, ylist3, label = 'Random')
    pylab.title('Сравнение скоростей работ алгоритмов ГПСЧ')
    pylab.xlabel('Объем выборки')
    pylab.ylabel('Время на поиск')
    pylab.legend(title='Легенда')
    
    pylab.show()
        
def make(max_number, quantity, stages):
    """
    Функция, выводящая параметры выборки
    param: max_number: максимальное число выборки
    param: quantity: кол- во элементов выборки
    param: stages: количество итераций
    """
    for i in range(stages):
        print("XORShift")
        seq = XORShift_generate(max_number, quantity)
        print("Мат. ожидание: ", mean(seq))
        print("Дисперсия: ", deviation(seq))
        print("Коэфф. вариации: ", cv(seq))
        xi2_check(seq, max_number)
        
        print('\n')
        
        print("Линейный конгруэнтный: ")
        seq = Lincong_generate(max_number, quantity)
        print("Мат. ожидание: ", mean(seq))
        print("Дисперсия: ", deviation(seq))
        print("Коэфф. вариации: ", cv(seq))
        xi2_check(seq, max_number)
        print('\n')
        
make(10000, 30, 10)

#size = [1000, 5000, 10000, 50000, 100000, 200000, 500000, 1000000]
#make_plot(10000, size)