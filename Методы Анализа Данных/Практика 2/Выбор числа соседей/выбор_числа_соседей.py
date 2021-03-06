# -*- coding: utf-8 -*-
"""Выбор числа соседей.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Dhb0MnqhrhlZo5WizqFyL68sVD3fTDZW
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import scale
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('wine.data')
data.head()

data.columns = ['Class','Alcohol','MalicAcid','Ash','AlcalinityOfAsh','Magnesium','TotalPhenols','Flavanoids','NonflavanoidPhenols','Proanthocyanins','ColorIntensity','Hue','OD280_OD315OfDilutedWines','Proline']
target = data['Class'] #вычленяем массив
model = data.drop(['Class'], axis=1) #Вычленяем модель из датасет

"""3.	Оценку качества необходимо провести методом кросс-валидации по 5 блокам (5-fold). Создайте генератор разбиений, который перемешивает выборку перед формированием блоков (shuffle=True). Для воспроизводимости результата, создавайте генератор KFold с фиксированным параметром random_state=42. В качестве меры качества используйте долю верных ответов (accuracy)."""

kf = KFold(n_splits=5, shuffle=True, random_state=42)

"""4.	Найдите точность классификации на кросс-валидации для метода k ближайших соседей (sklearn.neighbors.KNeighborsClassifier), при k от 1 до 50. При каком k получилось оптимальное качество? Чему оно равно (число в интервале от 0 до 1)? Данные результаты и будут ответами на вопросы 1 и 2."""

def CalculateScores(model,count):        
    validationTest={}
    for k in range(50):#счетчик идет от нуля
        model_knc = KNeighborsClassifier(n_neighbors = (k+1)) #в параметре передаем кол-во соседей
        scores = cross_val_score(model_knc, model, target, scoring='accuracy',cv=kf)
        validationTest[k+1]=scores.mean()#берем среднее значение оценки

    #формируем датасет для сортировки    
    validationTestDataFrame=pd.DataFrame.from_dict(validationTest, orient='index')#получаем из словаря датасет  
    validationTestDataFrame.index.name = 'k'
    validationTestDataFrame.columns =['Scores']
    validationTestDataFrame.sort_values(['Scores'], ascending=[False],inplace=True)
    print('При каком k получилось оптимальное качество? Чему оно равно (число в интервале от 0 до 1)? Данные результаты и будут ответами на вопросы 1 и 2.')
    print(validationTestDataFrame.head(count))

CalculateScores(model,1)
#Произведите масштабирование признаков с помощью функции sklearn.preprocessing.scale. 
model2=scale(model)#масштабирование выполняется перед обучением
CalculateScores(model2,11)#Снова найдите оптимальное k на кросс-валидации.