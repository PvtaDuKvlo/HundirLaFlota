

import time #Libreria para las pausas - time.sleep(0)

#Procedemos a crear la matriz para el tablero
def crearMatriz(filas,columnas,valor):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(valor)
    return matriz 

#Aqui creamos la funcion para imprimir las filas de la matriz
def imprimirFilasMatriz(matriz):
    print(" ")
    for fila in matriz:
        print(" ".join(str(elemento) for elemento in fila))

#Procedemos el eje de las letras a la matriz
def modificarMatriz(matriz,fila,columna,valor):
    matriz[fila][columna] = valor
    return matriz

#Creamos el borde de la tabla con las coordenadas en letras
def Pasarletra(matriz):
    matriz = modificarMatriz(matriz,0,0," ")
    matriz = modificarMatriz(matriz,1,0,"A")
    matriz = modificarMatriz(matriz,2,0,"B")
    matriz = modificarMatriz(matriz,3,0,"C")
    matriz = modificarMatriz(matriz,4,0,"D")
    matriz = modificarMatriz(matriz,5,0,"E")
    matriz = modificarMatriz(matriz,6,0,"F")
    matriz = modificarMatriz(matriz,7,0,"G")
    matriz = modificarMatriz(matriz,8,0,"H")
    matriz = modificarMatriz(matriz,9,0,"I")
    matriz = modificarMatriz(matriz,10,0,"J")
    return matriz   


#Creamos el otro borde de la tabla con las coordenadas en numeros
def PasarNumeros(matriz):
    matriz = modificarMatriz(matriz,0,0," ")
    matriz = modificarMatriz(matriz,0,1,"0")
    matriz = modificarMatriz(matriz,0,2,"1")
    matriz = modificarMatriz(matriz,0,3,"2")
    matriz = modificarMatriz(matriz,0,4,"3")
    matriz = modificarMatriz(matriz,0,5,"4")
    matriz = modificarMatriz(matriz,0,6,"5")
    matriz = modificarMatriz(matriz,0,7,"6")
    matriz = modificarMatriz(matriz,0,8,"7")
    matriz = modificarMatriz(matriz,0,9,"8")
    matriz = modificarMatriz(matriz,0,10,"9")
    return matriz

#Creamos la funcion para el final de la partida
def FinDeJuego(ganador):
    print("Fin de la partida")
    time.sleep(1)
    if ganador == "Jugador": 
        print("¡¡¡Has ganado!!!")
        time.sleep(1)
    else:
        print("Has perdido")
        time.sleep(1)
    print("¿Quieres volver a jugar?")
    time.sleep(1)
    print("1. Si")
    print("2. No")
    eleccion = input("Elige una opción: ")
    if eleccion == "1":
        print("Volverás a la elección de dificultad")
        time.sleep(1)
        print("Elige la dificultad del juego:")
        print("1. Fácil")
        print("2. Intermedio")
        print("3. Difícil")
        time.sleep(1)
    elif eleccion == "2":
        print("Fin del juego")
        time.sleep(1)
    else:
        print("Opción no válida, por favor elige una opción válida")
    time.sleep(1)
print()


#Introducimos un ASCI para darle un toque personal
def menu():
    print("""
  ___ ___                   .___.__         .__             _____.__          __          
 /   |   \ __ __  ____    __| _/|__|______  |  | _____    _/ ____\  |   _____/  |______   
/    ~    \  |  \/    \  / __ | |  \_  __ \ |  | \__  \   \   __\|  |  /  _ \   __\__  \  
\    Y    /  |  /   |  \/ /_/ | |  ||  | \/ |  |__/ __ \_  |  |  |  |_(  <_> )  |  / __ \_
 \___|_  /|____/|___|  /\____ | |__||__|    |____(____  /  |__|  |____/\____/|__| (____  /
       \/            \/      \/                       \/                               \/ 

""")


#Creamos la bienvenida al juego
print("#################################")
print("Bienvenido a Hundir la flota")
print("#################################")

#Selección de dificultad del juego
print("Elige la dificultad del juego:")
print("1. Fácil")
print("2. Intermedio")
print("3. Difícil")


#Creamos un bucle para que el usuario elija la dificultad
while True:
    try:
        dificultad = int(input("Elige una opción: "))
        #time.sleep(1)
        if dificultad == 1:
            print("Has elegido la dificultad Fácil")
            break
        elif dificultad == 2:
            print("Has elegido la dificultad Intermedio")
            break
        elif dificultad == 3:
            print("Has elegido la dificultad Difícil")
            break
        else:
            print("Opción no válida, por favor elige una opción válida")
    except ValueError:
        print("Opción no válida, por favor elige una opción válida")
#time.sleep(1)
print()


#Mostramos la cantidad de barcos según la dificultad
if dificultad == 1:
    print("En la dificultad Fácil hay 10 barcos: 5 lanchas, 3 buques, 1 acorazado y 1 portaaviones")
    print()
elif dificultad == 2:
    print("En la dificultad Intermedio hay 5 barcos: 2 lanchas, 1 buques, 1 acorazado y 1 portaaviones")
    print()
elif dificultad == 3:
    print("En la dificultad Difícil hay 2 barcos: 1 lancha y 1 buque")
    print()
#time.sleep(1)
print()


#Mostramos la longitud de los barcos
print("La longitud de la lancha es de 1 casilla")
print("La longitud del buque es de 3 casillas")
print("La longitud del portaaviones es de 5 casillas")
print("La longitud del acorazado es de 4 casillas")
print()
#time.sleep(1)

#Mostramos las posibles posiciones
print("La A es de Agua")
print("El - es de posición no disparada")
print("La X es de posición tocada")
#time.sleep(1)
print()


