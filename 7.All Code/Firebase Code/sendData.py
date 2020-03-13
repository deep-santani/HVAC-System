from firebase import firebase
url='https://testing-project111.firebaseio.com'
fb = firebase.FirebaseApplication('https://testing-project111.firebaseio.com/', None)
Temp=20
Humidity=48
Pressure=1
Gas=30000.25
Data2 = {
        'Temperature' : Temp,
        'Humidity' : Humidity,
        'Pressure' : Pressure,
        'Gas': Gas
        }

result = fb.patch('Data1/User',Data2)
#send = fb.patch('Data/i',Data2)
print(result) 
#print(send) 
   