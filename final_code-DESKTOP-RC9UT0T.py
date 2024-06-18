from geopy.geocoders import Nominatim
from twilio.rest import Client
from baseDatos import Mostrar
import time, serial, threading

def proceso(ubi, tel):#Función para el subproceso
    i=0
    while(True):
        geolocalization=Nominatim(user_agent="equipo3")#identificarse para usar
        place=ubi
        print(place)
        ubication=geolocalization.reverse(place)#coordenadas
        text = ubication.address
        print(text)

        for k in range(5):
            numero = str(tel[k])
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=text,
                to='whatsapp:'+ numero.strip(",()'")
            )
            print(tel[k])
        i+=1
        time.sleep(30)


telefono = list(Mostrar())
client = Client('AC4f81f5f2252685f876d26b8f89de64c3','4e4aff23c6a6bf9964b39b3891992a71')
puerto = serial.Serial('COM8', 115200)
entrada = puerto.readline().decode('ascii').strip()
valores = entrada.split("_")
print(len(valores))
time.sleep(5)
entrada = puerto.readline().decode('ascii').strip()
valores = entrada.split("_")
print(valores)
selector = int(valores[1])
#print(selector)
ubicación = valores[0]
#print(ubicación)

hilo1=threading.Thread(target=proceso, args=(ubicación, telefono), daemon=True)#Hilo

#Condiciones y acciones de los procesos
while(selector<1):
    entrada = puerto.readline().decode('ascii').strip()
    valores = entrada.split("_")
    selector = int(valores[1])
    ubicación = valores[0]
    print(valores)

if (selector == 1):
    hilo1.start()

while(selector ==1):
    entrada = puerto.readline().decode('ascii').strip()
    valores = entrada.split("_")
    selector = int(valores[1])
    ubicación = valores[0]
    print(valores)
    if(valores == 2):
        exit()