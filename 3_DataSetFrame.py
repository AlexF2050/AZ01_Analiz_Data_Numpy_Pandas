# Считываем данные из файла csv or excel

import pandas as pd #импортируем библиотеку pandas и переименовываем ее в pd для удобства написание кода
from six import print_

df = pd.read_csv('World-happiness-report-2024.csv') # считываем данные из файла csv

print(df[df['Healthy life expectancy'] > 0.7]) # выводим значения и название столбца

#
# print(df[['Country name', 'Regional indicator']]) # выводим значения
# print("_____________________________________")
# print(df.loc[56]) # выводим значения
# print("_____________________________________")
# print(df.loc[56],'Healthy life expectancy') # выводим значения и название столбца


# print(df.columns) # выводим названия столбцов
# print(df.index) # выводим названия строк
# print(df.shape) # выводим количество строк и столбцов
# print(df.head()) # выводим первые 5 строк
# print(df.tail()) # выводим последние 5 строк
# print(df.describe()) # выводим статистику по всем столбцам
# print(df.describe(include=['object'])) # выводим статистику по всем строкам
# print(df.info()) # выводим информацию о данных
# print(df.dtypes) # выводим типы данных
# print(df.isnull().sum()) # выводим количество пустых значений




