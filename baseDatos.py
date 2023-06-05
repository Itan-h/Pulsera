import sqlite3

def Agregar():
    for i in range (5):
        num = input(f"Numero de telefono {i}: ")
        numLada = '+521'+num
        cursorBD.execute("INSERT INTO Telefonos VALUES (?)", [numLada])
    conexion.commit()

def Mostrar():
    cursorBD.execute("SELECT * FROM Telefonos")
    Telefonos = cursorBD.fetchall()
    return Telefonos


conexion = sqlite3.connect('BaseDeDatos.db')
cursorBD = conexion.cursor()

cursorBD.execute(""" CREATE TABLE IF NOT EXISTS Telefonos 
                (numeros TEXT PRIMARY KEY)""")

#Agregar()

print(Mostrar())