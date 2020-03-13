from firebase import firebase

firebase = firebase.FirebaseApplication('https://pythondatabase-e8e3f.firebaseio.com/', None)

firebase.delete('/pythondatabase-e8e3f/Deatil/' , '-M0sZyM5VIh7rfARAG8f')
print('record deleted')
