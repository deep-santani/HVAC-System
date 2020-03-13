from firebase import firebase

firebase = firebase.FirebaseApplication('https://pythondatabase-e8e3f.firebaseio.com/', None)

firebase.put('/pythondatabase-e8e3f/Deatil/-M0sT7t-O-RTw8IcMv3r','Name','Tiktok')
print('record updated')
