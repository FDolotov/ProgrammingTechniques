import random

class teacher:
    def __init__(self, faculty = '', fio = '', degree = '', rank = ''):
        self._fio = str(fio)
        self._faculty = str(faculty)
        self._degree = str(degree)
        self._rank = str(rank)
    
    # перегрузка оператора >=
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
        
    # перегрузка оператора <=
    
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
        
      # перегрузка оператора >
    def __gt__(self, other):
        return not self.__le__(other)
    
    #перегрузка оператора <
    def __lt__(self, other):
        return not self.__ge__(other)
        
    def __repr__(self):
        return '(' + str(self.faculty) + ',' + str(self.fio) + ',' + str(self.degree) + ',' + str(self.rank) + ')\n'
    
    #строковое представление классового типа
    def __str__(self):
        return str(self.faculty) + ',' + str(self.fio) + ',' + str(self.degree) + ',' + str(self.rank)
        
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
                    'Искусство', 'Мировая политика'],

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

        'degree' : ['Аспирант', 'Ассистент', 'Доцент', 'Преподаватель', 'Профессор', 'Старший преподаватель'],
        
        'rank' : ['Доцент', 'Профессор', 'Член - корреспондент', 'Академик']
            }

#Функция, генерирующая базу данных
def generate(file_name, count, structure_scheme, structure_data):
    file = open(file_name, 'w')
    for i in range(count):
        str_data = []
        for element in structure_scheme[0]:
            str_data.append(random.choice(structure_data[element[1]]))
        file.write(structure_scheme[1].format(*tuple(str_data)))
    file.close()
    
    
    