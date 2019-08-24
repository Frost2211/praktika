#!/usr/bin/env python
# coding: utf-8

# In[2]:


###Переменные в Python
x = float(input("Введите переменную x: ")) #float - преобразует введеную строку в вещественное число
#Также есть int - данная функция преобразует строку в целое число
#Переменные в Python регистро-зависимые. "x" и "X" - разные переменные
#Введите ещё несколько переменных:
y = float(input("Введите переменную y: "))
z = x ** y #Возведение числа в степень

# Нажав Shift + Enter запустится данное приложение.
# Если в поле ввести имя имеющейся переменной, то выведется её значение
aa = 0.0000012421
aA = 1/2421e-6
c0 = 299000000
c1 = 2.99e8

###Вывод на экран
print("Hello world!") #Выводит запись "Hello world!"
print("Число x в степени y равно z: ",z) #Выводит значение переменной z


# In[3]:


#Вывод форматированного текста
text_y = "Число x = {0}, число y = {1}".format(x,y) #Число "x" заменяет {0}, а число "y" - {1}
print(text_y)


# In[ ]:


###Арифметические действия
f = x + y #сумма
f = x - y #разность
f = x / y #деление
f = x * y #умножение

import math
yy = math.sqrt(z) #Квадратный корень
uu = math.fabs(y) #Модуль числа

n = math.pi #Число Пи

cos = math.cos(x) #Косинус
sin = math.sin(x) #Синус


# In[4]:


###Массивы и последовательности
arr=[1,3,4,6,9,43] #Стандартный одномерный массив, состоящий из 6 элементов

#Можно создать пустой массив и заполнить его с клавиатуры:
A = [] #Создаем пустой массив
print("Заполните массив: ")
for i in range(int(input("Введите последний индекс массива: "))):
    A.append(int(input())) #Заполнение массива целыми числами
print("Одномерный массив A: ",A) #Вывод массива

dlina = len(A) #Получаем длину массива (кол-во элементов)


# In[5]:


#Двумерные массивы
Arr = [[1,2,3],[8,5,9]]  #Первая строка данного массива - "1,2,3", а вторая - "8,5,9"

arr_x = [1,2,3] #Матрица-строка
arr_Y = [[1],[2],[3]] #Матрица-столбец 

#Обращение к элементам массива:
Arr[0][0] #Элемент первой строки первого столбца
Arr[0][1] #Элемент первой строки второго стобца

o = [100,200,300]
p = o + [400,500,600] #К массиву o дабавили массив p


# In[6]:


###Использование циклов

#ПРИМЕР №1
array_1 = []

print("Массив чисел, которые равны удвоенному значению индексов: ")
for ii in range(10):    
    array_1.append(ii*2)
    print(array_1[ii])


# In[7]:


#Пример №2
N = 10
print("\n") # Пропускает строку в выводе
for m in range(1,N,2):
    if m==4:
        print("m равно 4")
    elif m==5:
        print("m равно 5")
    else:
        print("m = ",m)


# In[8]:


#Цикл while
NN = 1
ii = 1
while NN < 100 and ii<1e5:
    print(NN)
    NN = NN + 1
    ii = ii + 1
    if ii==1e5:
        print("Экстренное прерывание")
        break   #Останавливает цикл


N = 100
n = 1
ii = 1
nnn = 1e4
print("\n")


# In[9]:


#Сколько максимально раз будет выполняться цикл
while n <= N and ii<nnn:
    print("n = ",n)
    n = n + 5
    ii = ii + 1
    if ii >= nnn:
        print("Экстренное прерывание")
        break
print("Цикл выполнился ", ii," раз")


# In[11]:


#Ввод переменной с клавиатуры:
# m  = int(input())
import math
print("\n")

x = 1.23 * math.e
print("1.23*e равно x = ",x)
print("Две цифры после запятой: ","{:.2f}".format(x)) #Две цифры после запятой(точки)
print("Целая часть числа: ","{:.0f}".format(x)) #Целая часть числа


# In[ ]:


#Объявление переменных

#x = 10
#X = 11
#xX = x + X

#print("Переменная икс: ") #Вывод текста на экран 
#print(x) #Вывод переменной на экран
#
#print(x*y)
#print(x/y)
#print(x**y) #Два знака '*' обозначает возведение числа в степень


# In[12]:


###Строки
s1 = "Стр"
s2 = "оки"
print(" Строка s1: ",s1,"\n","Строка s2: ",s2,"\n",s1+s2) #Сложение строк
print(s1*3) #Дублирование строки (Важно: это НЕ умножение!)
n = len(s1)
print("Длина строки s1: ",n)


# In[13]:


#У строк возможен доступ по индексу:
s = "Привет"
print(s)
print(s[0])
print(s[2])


# In[14]:


#Также можно вырезать часть строки:
print(s[1:3])
print(s[1:])


# In[15]:


#Можно задать шаг, с которым нужно извлекать срез:
print(s[::-1])
print(s[2::2])


# In[16]:


#Можно заменить символ в строке:
print(s[0:3] + 'л' + s[4:])
ss = "Hello World!"
print(ss.split(' ')) #Разбиение строки по разделителю


# In[ ]:




