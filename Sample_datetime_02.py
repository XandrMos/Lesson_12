# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 13:28:00 2019

@author: Xandr
"""

"""
time

Клас time служить для демонстрації даних про час, 
повністю ігноруючи дату. Як і у випадку з попереднім класом date, 
слід імпортувати модуль datetime за допомогою ключового слова import.

"""
import datetime
a = datetime.time(12, 18, 35)
print(a)

print("hour :", a.hour)
print("minute :", a.minute)
print("second :", a.second)
print("microsecond :", a.microsecond)