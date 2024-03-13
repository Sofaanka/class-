import mysql.connector
import math as mh
import numpy as np
import matplotlib.pyplot as mp

# создаём подключение к БД
db = mysql.connector.connect(
host="localhost", # адрес сервера
user="root", # ваше имя пользователя
password="", # ваш пароль
database="history" # имя базы данных
)


cursor = db.cursor()

a=[]
print("Напиши свой ID")
key = input()
a.append(float(key))

def add(a):
    AddQuery = ("INSERT INTO operation" + "(number,name)" + "VALUES(%s,%s)")
    AddVal = [a]

    cursor.executemany(AddQuery, AddVal)
    db.commit()
print("Что вы хотите узнать у нашего приложения по теме Диффузия?"
      " 1. Посчитать время, концентрацию, глубину"
      " 2. Построить график зависимости D от T")
num=int(input())
if num==1:
    def erf1(C, Cs):
       v = np.linspace(0, 10, 1000)
       delta = 0
       deltamin = 1
       zmin = 0
       k = 0
       for i in v:
           k = mh.erf(i)
           delta = abs(k - C / Cs)
           if delta < deltamin:
               deltamin = delta
               zmin = i
       return zmin
    def erf2(C, Cs):
       v = np.linspace(0, 10, 1000)
       delta = 0
       deltamin = 1
       zmin = 0
       k = 0
       for i in v:
           k = mh.erfc(i)
           delta = abs(k - C / Cs)
           if delta < deltamin:
               deltamin = delta
               zmin = i
       return zmin
    input("Какие краевые условия? "
       "1:Диффузия "
       "2:Обратная диффузия")
    condition = int(input())
    input('Что нужно найти: 1.Время(c) 2.Концентрацию 3.Глубина(м)')
    search = int(input())
    input('Введите данные для расчета в каждой строчке')
    if condition == 1:
        if search == 1:
            input('1.Cs 2.x 3.D 4.C(x, t)')
            Cs = float(input())
            x = float(input())
            D = float(input())
            C = float(input())
            z = erf2(C, Cs)
            if (4 * D * mh.pow(z, 2)) == 0:
                print("Вы неправильно ввели данные, попробуйте еще раз!")
                exit()
            t = (mh.pow(x, 2) / (4 * D * mh.pow(z, 2)))
            print(t)
            name=t
            a.append(name)
            add(a)

        elif search == 2:
            input('1.Cs 2.x 3.D 4.t')
            Cs = float(input())
            x = float(input())
            D = float(input())
            t = float(input())
            if (2 * mh.sqrt(D * t))==0:
                print("Вы неправильно ввели данные, попробуйте еще раз!")
                exit()
            C = Cs * (mh.erf(x / (2 * mh.sqrt(D * t))))
            print(C)
            name = C
            a.append(name)
            add(a)
        elif search == 3:
           input('1.Cs 2.C(x, t) 3.D 4.t')
           Cs = float(input())
           C = float(input())
           D = float(input())
           t = float(input())
           z = erf2(C, Cs)
           x = 2 * mh.sqrt(D * t) * z
           print(x)
           name = x
           a.append(name)
           add(a)
        else:
           print('Вы не правильно ввели данные, попробуйте снова!')
    elif condition == 2:
        if search == 1:
            input('1.Cs 2.x 3.D 4.C(x, t)')
            Cs = float(input())
            x = float(input())
            D = float(input())
            C = float(input())
            z = erf1(C, Cs)
            if (4 * D * mh.pow(z, 2)) == 0:
                print("Вы неправильно ввели данные, попробуйте еще раз!")
                exit()
            t = (mh.pow(x, 2) / (4 * D * mh.pow(z, 2)))
            print(t)
            name = t
            a.append(name)
            add(a)
        elif search == 2:
            input('1.Cs 2.x 3.D 4.t')
            Cs = float(input())
            x = float(input())
            D = float(input())
            t = float(input())
            if x / (2 * mh.sqrt(D * t))==0:
                print("Вы неправильно ввели данные, попробуйте еще раз!")
                exit()
            C = Cs * mh.erf(x / (2 * mh.sqrt(D * t)))
            print(C)
            name = C
            a.append(name)
            add(a)
        elif search == 3:
            input('1.Cs 2.C(x, t) 3.D 4.t')
            Cs = float(input())
            C = float(input())
            D = float(input())
            t = float(input())
            z = erf1(C, Cs)
            x = 2 * mh.sqrt(D * t) * z
            name = x
            a.append(name)
            add(a)
    else:
        print('Вы не правильно ввели данные, попробуйте снова!')
elif num == 2:
    input('Введите данные для построения графика:')
    k = 8.31
    input('Введите D(м^2/c)')
    D = float(input())
    input('Введите E (Дж)')
    E = float(input())
    input('T1 (K) - начальная температура')
    T1 = int(input())
    input('T2 (K) -  конечная температура')
    T2 = int(input())
    input('Кол-во точек на графике')
    n = int(input())
    x = np.linspace(T1, T2, n)
    y = []
    for i in x:
        y.append(D*(mh.exp(-E/(k*i))))
    mp.plot(x, y, color='blue', marker='*', markersize=3)
    mp.grid(True)
    mp.xlabel('Ось T')
    mp.ylabel('Ось D')
    mp.title('Зависимость D от T')
    mp.show()

