# -*- coding: utf-8 -*-
"""Нормализация признаков.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xi3q7IS37Ko9aCSDFFvIhYdf1rm2CueF
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

"""1.	Загрузите обучающую и тестовую выборки из файлов perceptron-train.csv и perceptron-test.csv. Целевая переменная записана в первом столбце, признаки — во втором и третьем."""

data1 = pd.read_csv('perceptron-train.csv',header=None)
y_train = data1[0] #Класс
x_train = data1.loc[:, 1:] #Характеристики

data2= pd.read_csv('perceptron-test.csv',header=None)
y_test = data2[0] #Класс
x_test = data2.loc[:, 1:]#Характеристики

"""2.	Обучите персептрон со стандартными параметрами и random_state=241.
3.	Подсчитайте качество (долю правильно классифицированных объектов, accuracy) полученного классификатора на тестовой выборке.
"""

def PerceptronTrain(typeStr,X_train, y_train,X_test,y_test):     
    #Обучаем персептрон со стандартными параметрами и random_state=241.
    clf = Perceptron(random_state=241)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)#предсказание по тестовым данным
    accuracyScore=accuracy_score(y_test, predictions)#проверка точности по тестовым данным

    print('Подсчитайте качество '+typeStr)
    accuracyScoreRounded=round(accuracyScore,3)
    print(accuracyScoreRounded)
    return accuracyScoreRounded

#обучаем перцептрон
accuracyScoreGeneral=PerceptronTrain('без нормализации',x_train, y_train,x_test,y_test)

#Нормализуем обучающую и тестовую выборку с помощью класса StandardScaler
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

#Обучите персептрон на новых выборках. Найдите долю правильных ответов на тестовой выборке.
accuracyScoreScaled=PerceptronTrain('c нормализацией',x_train_scaled, y_train,x_test_scaled,y_test)

#Найдите разность между качеством на тестовой выборке после нормализации и качеством до нее. Это число и будет ответом на задание.
Comparation=accuracyScoreScaled-accuracyScoreGeneral
print('Разница')
print(Comparation)