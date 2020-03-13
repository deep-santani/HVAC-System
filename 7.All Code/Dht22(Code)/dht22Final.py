import Adafruit_DHT
from firebase import firebase
url='https://testing-project111.firebaseio.com'
fb = firebase.FirebaseApplication('https://testing-project111.firebaseio.com/', None)
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        Data2 = {
        'Temperature' : temperature,
        'Humidity' : humidity
        }
        result = fb.patch('Data1/User',Data2)
    else:
        print("Failed to retrieve data from humidity sensor")

        