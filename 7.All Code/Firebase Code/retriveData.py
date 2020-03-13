
from firebase import firebase

firebase = firebase.FirebaseApplication('https://testing-project111.firebaseio.com/', None)

#Humidity = firebase.get('Data/-M10lHL13p03gIvr0BXF/Humidity','')
#Pressure = firebase.get('Data/-M10lHL13p03gIvr0BXF/Pressure','')
Temperature = firebase.get('testing-project111 /','')
print("Temperature :",Temperature)
#print("Pressure    :", Pressure)
#print("Humidity    :",Humidity)