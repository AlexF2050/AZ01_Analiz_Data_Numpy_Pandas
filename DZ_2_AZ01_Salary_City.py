# Определите среднюю зарплату (Salary) по каждому городу (City)
# убрать из таблицы строку Salary = NaN
# Группировать по городу и вывести среднюю зарплату по городу
# если City = NaN, то вывести среднюю зарплату и написать, что город не известен

import pandas as pd
import numpy as np

# Загрузите набор данных из CSV-файла в DataFrame
df = pd.read_csv('dz.csv')
print('  ')
print('______________набор всех данных:')
print(df)
# Уберите строки с 'NaN' в столбце 'Salary'
df = df.dropna(subset=['Salary'])
# Уберите строки с 'NaN' в столбце 'City'
df = df.dropna(subset=['City'])
print('  ')
print('_________набор актуальных данных:')
print(df)
# Группируйте данные по городу и выведите среднюю зарплату по городу
grouped = df.groupby('City')['Salary'].mean()
print('  ')
for city, salary in grouped.items():
    print(f"Город: {city} - Средняя зарплата: {salary}")
print('  ')
print('Расчёт данных окончен!')








