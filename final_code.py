from geopy.geocoders import Nominatim
from twilio.rest import Client
import time, serial, threading

def proceso(lat, longt, l, tel):
    i=0
    while(True):
        geolocalization=Nominatim(user_agent="equipo3")#identificarse para usar
        place=lat[i]+","+longt[i]
        print(place)
        ubication=geolocalization.reverse(place)#coordenadas
        text = ubication.address
        print(text)

        for k in range(l):
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=text,
                to='whatsapp:'+tel[k]
            )
            print(tel[k])
        i+=1
        time.sleep(60)



latitud = ["17.171516", "17.14162", "17.04216", "17.11365", "17.032159", "17.0673505"]
longitud = ["-96.824960", "-96.824960", "-96.824960", "-96.824960", "-96.824960", "-96.824960", "-96.824960"]
telefono = ['+5219511518818', '+5219513992610', '+5219511819919', '+5219511819919']
n=len(telefono)
client = Client('AC4f81f5f2252685f876d26b8f89de64c3','4e4aff23c6a6bf9964b39b3891992a71')
puerto = serial.Serial('COM6', 9600)
entrada = int(puerto.readline().decode('ascii'))
valor = int(entrada)
print(entrada)
print(valor)

hilo1=threading.Thread(target=proceso, args=(latitud, longitud, n, telefono), daemon=True)

while(valor<1):
    entrada = int(puerto.readline().decode('ascii'))
    valor = int(entrada)
    print(valor)

if (valor == 1):
    hilo1.start()

while(valor ==1):
    entrada = int(puerto.readline().decode('ascii'))
    valor = int(entrada)
    print(valor)
    if(valor == 2):
        exit()