import random
import time

# Crear una matriz del tamaño indicado con un valor por defecto
def crearMatriz(filas, columnas, valor):
    return [[valor for _ in range(columnas)] for _ in range(filas)]

# Imprimir la matriz de forma legible
def imprimirFilasMatriz(matriz):
    print()
    for fila in matriz:
        print(" ".join(str(x) for x in fila))

# Modificar un valor específico en la matriz
def modificarMatriz(matriz, fila, columna, valor):
    matriz[fila][columna] = valor
    return matriz

# Agregar letras al eje vertical (columna 0)
def Pasarletra(matriz):
    letras = [" ", "A","B","C","D","E","F","G","H","I","J"]
    for i, letra in enumerate(letras):
        matriz[i][0] = letra
    return matriz

# Agregar números al eje horizontal (fila 0)
def PasarNumeros(matriz):
    numeros = [" ", "0","1","2","3","4","5","6","7","8","9"]
    for j, num in enumerate(numeros):
        matriz[0][j] = num
    return matriz

# Función para generar los barcos según la dificultad
def generarBarcos(tablero, dificultad):
    if dificultad == 1:
        barcos = [
            ("Lancha", 1, "L"),
            ("Lancha", 1, "L"),
            ("Lancha", 1, "L"),
            ("Lancha", 1, "L"),
            ("Lancha", 1, "L"),
            ("Buque", 3, "B"),
            ("Buque", 3, "B"),
            ("Buque", 3, "B"),
            ("Acorazado", 4, "Z"),
            ("Portaaviones", 5, "P")
        ]
    elif dificultad == 2:
        barcos = [
            ("Lancha", 1, "L"),
            ("Lancha", 1, "L"),
            ("Buque", 3, "B"),
            ("Acorazado", 4, "Z"),
            ("Portaaviones", 5, "P")
        ]
    elif dificultad == 3:
        barcos = [
            ("Lancha", 1, "L"),
            ("Buque", 3, "B")
        ]
    else:
        barcos = []

    for nombre, longitud, simbolo in barcos:
        colocado = False
        intentos = 0
        while not colocado and intentos < 100:
            intentos += 1

            # Orientación según el tipo de barco
            if nombre == "Portaaviones":
                orientacion = "vertical"
            elif nombre in ["Buque", "Acorazado"]:
                orientacion = "horizontal"
            else:
                orientacion = random.choice(["horizontal", "vertical"])

            if orientacion == "horizontal":
                fila = random.randint(1, 10)
                columna = random.randint(1, 10 - longitud + 1)
                if all(tablero[fila][columna + i] == "-" for i in range(longitud)):
                    for i in range(longitud):
                        tablero[fila][columna + i] = simbolo
                    colocado = True

            elif orientacion == "vertical":
                fila = random.randint(1, 10 - longitud + 1)
                columna = random.randint(1, 10)
                if all(tablero[fila + i][columna] == "-" for i in range(longitud)):
                    for i in range(longitud):
                        tablero[fila + i][columna] = simbolo
                    colocado = True

    return tablero

# Oculta los barcos del rival y no borra ninguna letra de las Coordenadas
def ocultarBarcos(tablero):
    oculto = []
    for i, fila in enumerate(tablero):
        nueva_fila = []
        for j, celda in enumerate(fila):
            if i == 0 or j == 0:
                nueva_fila.append(celda)
            elif celda in ["L", "B", "Z", "P"]:
                nueva_fila.append("-")
            else:
                nueva_fila.append(celda)
        oculto.append(nueva_fila)
    return oculto

def disparoAleatorio():
    fila = random.randint(0,9)
    columna = random.randint(0,9)

    
    return  fila, columna 


#Funcion de fin del juego, con opcion de volver a jugar y opcion de no jugar mas
def FinDeJuego(ganador):
    print("Fin de la partida")
    time.sleep(1)
    if ganador == "Jugador": 
        print("¡¡¡Has ganado!!!")
    else:
        print("Has perdido")
    time.sleep(1)
    print("¿Quieres volver a jugar?")
    print("1. Si")
    print("2. No")
    eleccion = input("Elige una opción: ")
    if eleccion == "1":
        print("Volverás a la elección de dificultad...")
        return main()
    elif eleccion == "2":
        print("Fin del juego")
        exit()
    else:
        print("Opción no válida. Fin del juego.")
        exit()
    
def menu():
    print("""
  ___ ___                   .___.__         .__             _____.__          __          
 /   |   \ __ __  ____    __| _/|__|______  |  | _____    _/ ____\  |   _____/  |______   
/    ~    \  |  \/    \  / __ | |  \_  __ \ |  | \__  \   \   __\|  |  /  _ \   __\__  \  
\    Y    /  |  /   |  \/ /_/ | |  ||  | \/ |  |__/ __ \_  |  |  |  |_(  <_> )  |  / __ \_
 \___|_  /|____/|___|  /\____ | |__||__|    |____(____  /  |__|  |____/\____/|__| (____  /
       \/            \/      \/                       \/                               \/ 
""")


def quedanBarcos(tablero):
    for fila in range(1, 11):
        for columna in range(1, 11):
            if tablero[fila][columna] in ["L", "B", "Z", "P"]:
                return True
    return False