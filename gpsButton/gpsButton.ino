#include "BluetoothSerial.h"
#include <TinyGPS++.h>

#define RXD2 16
#define TXD2 17
HardwareSerial neogps(1);

BluetoothSerial SerialBT;
TinyGPSPlus gps;

const int button=26;
int state=0, valor=0;

void setup() 
{
    SerialBT.begin("ESP32 Bluetooh");
    SerialBT.begin(115200);
    neogps.begin(9600, SERIAL_8N1, RXD2, TXD2);  
    pinMode(button, INPUT);
    delay(2000);
}

void loop() 
{  
    if(neogps.available())
    {
        gps.encode(neogps.read());
        sendDataGps();
    }
    else
    {
        sendDataGps();
    }  

    sendDataButton();
}

void sendDataButton()
{
    state = digitalRead(button);
    delay(100);
    if(state != 0){
        valor++;
    }
    SerialBT.println(String(valor));
    if (valor==2){
        valor = 0;}
}

void sendDataGps(void)
{ 
    if (gps.location.isValid() ==  1)
    {  
        SerialBT.print(String(gps.location.lat(),6)+","+String(gps.location.lng(),6) + "_");
    }
    else
    {
        SerialBT.print("Sinsenalgps_");  
    }  
}