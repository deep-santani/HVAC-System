# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 12:59:14 2020

@author: deep
"""
import matplotlib.pyplot as plt
import csv
filename="data.csv"

Temp = []
Humidity = []
Gas = []
Pressure = []

with open('e:/data.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        Temp.append(int(row[0]))
        Humidity.append(int(row[1]))
        
plt.plot(Temp,Humidity, marker='o')

plt.title('Data from the CSV File: Temp and Humdity')

plt.xlabel('Temp')
plt.ylabel('Humidity')

plt.show()
     