# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 13:40:32 2019

@author: Xandr
"""
"""
datetime

Клас datetime дозволяє описувати дані у певний момент часу, 
який враховує не тільки години та хвилини, але і відомості про дату.

"""
import datetime
a = datetime.datetime(2020, 7, 18, 4, 52, 33, 51204)
print(a)

a = datetime.datetime(2019, 2, 13)
b = datetime.datetime(2016, 8, 25, 12, 8, 12)
print(a)
print(b)

a = datetime.datetime.today()
b = datetime.datetime.now()
print(a)
print(b)

#Перетворення дати і часу у рядок
a = datetime.datetime.today().strftime("%d.%m.%Y")
b = datetime.datetime.today().strftime("%H:%M:%S")
print(a)
print(b)

a = datetime.datetime.today().strftime("%d.%A.%m.%Y")
b = datetime.datetime.today().strftime("%Y:%B:%S")
print(a)
print(b)

"""
% a -- назва дня тижня в скороченому вигляді
% A -- назву дня тижня в повному вигляді
% w -- номер дня тижня у вигляді цілого числа
% D -- номер дня місяця у вигляді цілого числа
% b -- назва місяця в скороченому вигляді
% B -- назва місяця в повному вигляді
% M -- номер місяця в числовому поданні
% y -- номер року без сторіччя
% Y -- номер року в повному поданні
% H -- кількість годин в 24-годинному форматі
% I -- кількість годин в 12-годинному форматі
% P -- до полудня або після полудня в 12-годинному форматі
% M -- кількість хвилин у вигляді цілого числа
% S -- кількість секунд у вигляді цілого числа
% F -- кількість мікросекунд у вигляді цілого числа
% z -- часовий пояс в форматі UTC
% Z -- назва часового поясу
% J -- номер дня в році
% U -- номер тижня в році, якщо рахувати з неділі
% w -- номер тижні в році, якщо рахувати з понеділка
% C -- місцеве уявлення дати і часу
% x -- місцеве уявлення дати
% X -- місцеве уявлення часу
%% -- символ відсотка

"""