import random
import time
from main import *

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

# --- FUNCIÓN DISPARO JUGADOR  ---
def disparoJugador(tableroRival):
    letras_validas = ["A","B","C","D","E","F","G","H","I","J"]
    mapa_letras = {letra: i+1 for i, letra in enumerate(letras_validas)} # TRADUCIMOS LAS LETRAS A NUMEROS PARA EL ORDENADOR

    while True:
        coordenada = input("\nTu turno. Introduce coordenada (ej. A3): ").upper().strip()
        
        # Validación básica de longitud
        if len(coordenada) < 2:
            print("Coordenada no válida. Debe ser Letra + Número.")
            continue

        letra = coordenada[0]
        numero_str = coordenada[1:]

        # Validar que la letra y el número sean correctos
        if letra not in mapa_letras or not numero_str.isdigit():
            print("Formato incorrecto. Usa letras A-J y números 0-9.")
            continue
        
        fila = mapa_letras[letra]
        columna = int(numero_str) + 1 # +1 porque tu array empieza en " " y luego "0"

        # Validar rango de columna (1 a 10)
        if columna < 1 or columna > 10:
            print("Número fuera de rango (0-9).")
            continue

        # Verificar si ya se disparó ahí
        celda_actual = tableroRival[fila][columna]
        if celda_actual in ["X", "O", "A"]:
            print("¡Ya has disparado ahí! Elige otra casilla.")
            continue
        
        # Lógica de impacto
        if celda_actual in ["L", "B", "Z", "P"]:
            print(f"¡TOCADO! Has dado a un barco en {coordenada}.")
            tableroRival[fila][columna] = "X" # Marcamos tocado
            return tableroRival # Retornamos tablero actualizado
        elif celda_actual == "-":
            print(f"Agua en {coordenada}.")
            tableroRival[fila][columna] = "A" # A de Agua (o usa O)
            return tableroRival
    

# --- DISPARO DE LA CPU ---
def disparoAleatorio(tablero):
    while True:
        # Random entre 1 y 10 porque 0 son las etiquetas
        filaC = random.randint(1, 10)
        columnaC = random.randint(1, 10)

        celda = tablero[filaC][columnaC]

        # Si la celda no ha sido disparada
        if celda not in ["X", "O", "A"]:
            letras = [" ", "A","B","C","D","E","F","G","H","I","J"]
            coord_nombre = f"{letras[filaC]}{columnaC-1}"

            print(f"La CPU dispara a: {coord_nombre}")
            time.sleep(1)

            if celda in ["L","B","Z","P"]:
                print("¡La CPU ha acertado! ¡TOCADO!")
                tablero[filaC][columnaC] = "X"
            else:
                print("La CPU ha fallado. AGUA.")
                tablero[filaC][columnaC] = "A"
            break # Salir del bucle cuando dispara correctamente



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

#Funcion de quedanBarcos, con esta funcion indicamos si aun quedan barcos en el tablero del para saber si ganamos o perdimos

def quedanBarcos(tablero):
    for fila in range(1, 11):
        for columna in range(1, 11):
            if tablero[fila][columna] in ["L", "B", "Z", "P"]:
                return True
    return False

#Funcion de tableroJugador, con esta creamos el tablero del jugador.

def tableroJugador():
    print("Tablero del jugador:")
    for fila in tableroJugador:
        print(" ".join(fila))
    print()

#Funcion de tableroRival, con esta creamos el tablero del rival.

def tableroRival():
    print("Tablero del rival:")
    for fila in tableroRival:
        print(" ".join(fila))
    print()
