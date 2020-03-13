import pandas as pd
from sklearn import linear_model
from firebase import firebase

fb = firebase.FirebaseApplication('Here Put Your Firebase Url/', None)

df = pd.read_csv("Put your Data1 Path/data1.csv")

Temperature = fb.get('Data1/User/Temperature','')
Humidityi = fb.get('Data1/User/Humidity','')
#Gasi = fb.get('Data1/User/Gas','')

X = df[['Temp','Humidity']]
y = df['Probability']

regr = linear_model.LinearRegression()
regr.fit(X,y)

Probability = regr.predict([[Temperature,Humidityi]])

print(Probability,"%") 
