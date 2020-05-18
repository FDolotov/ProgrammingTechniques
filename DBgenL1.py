import random

class teacher:
    def __init__(self, faculty = '', fio = '', degree = '', rank = ''):
        
        """
        Инициализация объекта teacher
        param: faculty: Факультет
        type: faculty: comparable object
        param: fio: ФИО
        type: fio: comparable object
        param: degree: ученая степень
        type: fio: comparable object
        param: rank: ученое звание
        type: fio: comparable object
        """

        
        self._fio = str(fio)
        self._faculty = str(faculty)
        self._degree = str(degree)
        self._rank = str(rank)
    
    """
    Перегрузка оператора >=.
    Сравнение ведется вначале по факультету, потом по фио, степень и звание
    param: other: Объект справа от оператора
    return: True, если self >= other; False в другом случае
    """
    
    def __ge__(self, other):          
        if self.faculty == other.faculty:
            if self.fio == other.fio:
                if self.degree == other.degree:
                    return self.rank >= other.rank
                else:
                    return self.degree > other.degree
            else:
                return self.fio > other.fio
        else:
            return self.faculty > other.faculty
    
    """
    Перегрузка оператора <=.
    Сравнение ведется вначале по факультету, потом по фио, степень и звание
    param: other: Объект справа от оператора
    return: True, если self <= other; False в другом случае
    """
    
    def __le__(self, other):
        if self.faculty == other.faculty:
            if self.fio == other.fio:
                if self.degree == other.degree:
                    return self.rank <= other.rank
                else:
                    return self.degree < other.degree
            else:
                return self.fio < other.fio
        else:
            return self.faculty < other.faculty
        
    """
    Перегрузка оператора >.
    Сравнение ведется вначале по факультету, потом по фио, степень и звание
    param: other: Объект справа от оператора
    return: True, если self > other; False в другом случае
    """
      
    def __gt__(self, other):
        return not self.__le__(other)
    
    """
    Перегрузка оператора <.
    Сравнение ведется вначале по факультету, потом по фио, степень и звание
    param: other: Объект справа от оператора
    return: True, если self < other; False в другом случае
    """
    
    def __lt__(self, other):
        return not self.__ge__(other)
    
    """
    Перегрузка оператора =.
    Сравнение ведется вначале по факультету, потом по фио, степень и звание
    param: other: Объект справа от оператора
    return: True, если self = other; False в другом случае
    """
    
    def __eq__(self, other):
        if self <= other and self >= other:
            return True
        else:
            return False
        
    """
    Описывает строковое представление для print(obj). Позволяет красиво
    выводить в консоли.
    return: str 'teacher(*properties)'
    """
        
    def __repr__(self):
        return '(' + str(self.faculty) + ',' + str(self.fio) + ',' + str(self.degree) + ',' + str(self.rank) + ')\n'
    
    """
    Описывает строковое представление для str(obj). Позволяет легко
    вывести объекты в файл.
    return: str данные в формате .csv
    """
    
    def __str__(self):
        return str(self.faculty) + ',' + str(self.fio) + ',' + str(self.degree) + ',' + str(self.rank)
    
    """
    Функция, переводящая классовый обьект, str, в список
    return: list
    """
    
    def str_to_list(self):
        return str(self).replace(',', '').split()
        
    #Геттеры
    
    @property
    def fio(self):
        return self._fio
    
    @property
    def degree(self):
        return self._degree
    
    @property
    def rank(self):
        return self._rank
    
    @property
    def faculty(self):
        return self._faculty

#Структура базы данных в формате .csv
structure_scheme = ((
        ('scheme_data', 'faculty'),
        ('scheme_data', 'second_name'),
        ('scheme_data', 'first_name'), 
        ('scheme_data', 'fathername'), 
        ('scheme_data', 'degree'), 
        ('scheme_data', 'rank')), '{}; {} {} {}; {}; {}\n')


#Набор данных для генерации случайных элементов 

structure_data = {
        'faculty' : ['КБ', 'ИТСС', 'ПМ', 'Японистика', 'Китаистика', 'Дизайн', 'Маркетинг', 'МехМат', 'Реставрация', 'ВМК',
                    'Искусство', 'Мировая_политика'],

        'second_name' : ['Синицын', 'Петров', 'Смирнов', 'Кокорин', 'Сидоров', 'Панков', 'Смирнов', 'Минин', 'Пожарский', 'Дудь',
                        'Хованский', 'Ларин', 'Путин', 'Иванов', 'Лось', 'Сорокин', 'Бусяцкий', 'Кержаков', 'Лебедев',
                        'Истратов', 'Рожков', 'Петросян', 'Галкин', 'Пугачев', 'Какашин', 'Трусов', 'Михалицын', 'Дворцов', 'Мищенко',
                        'Павлов', 'Леонтьев', 'Мирзаев', 'Пусько', 'Илонов', 'Гамов', 'Иванченков', 'Соколов', 'Коврижных', 'Саидов',
                        'Лапенко', 'Локтев', 'Рыбаков', 'Чикатило', 'Ростов'],
                         
        'first_name' :  ['Фёдор', 'Александр', 'Петр', 'Дмитрий', 'Иван', 'Анатолий', 'Афонасий', 'Игорь', 'Илья', 'Ипполит',
                        'Егор', 'Влад', 'Владимир', 'Николай', 'Максим', 'Алексей', 'Федор', 'Андрей', 'Павел', 'Патрик', 'Даниил', 'Юрий',
                        'Виктор', 'Антон', 'Евграф', 'Филипп', 'Роман', 'Вадим', 'Марк', 'Кузьма', 'Григорий', 'Кирилл', 'Денис', 'Георгий'],

        'fathername' : ['Андреевич', 'Александрович', 'Петрович', 'Дмитриевич', 'Иванович', 'Анатолиевич', 'Афонасиевич',
                       'Игоревич', 'Ильич', 'Ипполитович', 'Егорович', 'Владиславович', 'Владимирович', 'Николаевич', 'Максимович',
                       'Алексеевич', 'Федорович', 'Андреевич', 'Павлович', 'Патрикович', 'Даниилович', 'Юрьевич', 'Викторович',
                       'Антонович', 'Евграфович', 'Филиппович', 'Романович', 'Вадимович', 'Маркович', 'Кузьмич', 'Григориевич', 'Кириллович',
                       'Денисович', 'Георгиевич'],

        'degree' : ['Аспирант', 'Ассистент', 'Преподаватель', 'Старший_преподаватель'],
        
        'rank' : ['Доцент', 'Профессор', 'Член-корреспондент', 'Академик']
            }

"""
Функция генерации базы данных
param file_name: имя базы данных
type: file_name: str
param: count: массив кол - ва обьектов в базе данных
type: count: iterable 
param: structure_shceme: структура данных для генерации
type: structure_scheme: tuple(tuple(str, iterable) .. str)
param: structure_data: данные для генерации структуры
type: structure_data: dict('key' : [val])
"""

def generate(file_name, count, structure_scheme, structure_data):
    file = open(file_name, 'w')
    for i in range(count):
        str_data = []
        for element in structure_scheme[0]:
            str_data.append(random.choice(structure_data[element[1]]))
        file.write(structure_scheme[1].format(*tuple(str_data)))
    file.close()

"""
Функция проверки содержания и индекса строки элемента
param element: элемент
type: element: str
param: structure_data: данные для генерации структуры
type: structure_data: dict('key' : [val])
"""

def check(element, structure_data):
    structure = list(structure_data.values())
    for i in range(len(structure)):
        if element in structure[i-1]:
            return i
    return "No element in structure data"
            
    
    
    