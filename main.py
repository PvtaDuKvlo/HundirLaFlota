from funciones import *

def main():
    menu()
    print("#################################")
    print("Bienvenido a Hundir la Flota")
    print("#################################")
    print()

    # Elegir dificultad
    print("Elige la dificultad del juego:")
    print("1. Fácil")
    print("2. Intermedio")
    print("3. Difícil")

    while True:
        try:
            dificultad = int(input("Selecciona una opción: "))
            if dificultad in [1, 2, 3]:
                break
            else:
                print("Opción no válida, intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce un número válido (1, 2 o 3).")

    print()

    # Mostrar información sobre los barcos
    if dificultad == 1:
        print("Dificultad Fácil: 10 barcos → 5 Lanchas, 3 Buques, 1 Acorazado, 1 Portaaviones")
    elif dificultad == 2:
        print("Dificultad Intermedia: 5 barcos → 2 Lanchas, 1 Buque, 1 Acorazado, 1 Portaaviones")
    elif dificultad == 3:
        print("Dificultad Difícil: 2 barcos → 1 Lancha, 1 Buque")

    print()
    print("Leyenda de barcos:")
    print("L = Lancha (1 casilla)")
    print("B = Buque (3 casillas horizontales)")
    print("Z = Acorazado (4 casillas horizontales)")
    print("P = Portaaviones (5 casillas verticales)")
    print()

    # --- TABLERO DEL JUGADOR ---
    tableroJugador = crearMatriz(11, 11, "-")
    tableroJugador = Pasarletra(tableroJugador)
    tableroJugador = PasarNumeros(tableroJugador)
    tableroJugador = generarBarcos(tableroJugador, dificultad)

    # --- TABLERO DEL RIVAL ---
    tableroRival = crearMatriz(11, 11, "-")
    tableroRival = Pasarletra(tableroRival)
    tableroRival = PasarNumeros(tableroRival)
    tableroRival = generarBarcos(tableroRival, dificultad)

    # Mostrar tableros
    print("=== TABLERO DEL JUGADOR ===")
    imprimirFilasMatriz(tableroJugador)

    print("\n=== TABLERO DEL RIVAL  ===")
    imprimirFilasMatriz(ocultarBarcos(tableroRival))

    print()
    print("¡Los tableros están listos para jugar!")


    ##TU TURNO

    ##TURNO  DEL ORDENADOR
    disparoAleatorio()



    # Comprueba si quedan barcos en los dos tableros y declara el ganador
    if not quedanBarcos(tableroRival):
        FinDeJuego("Jugador")
        print("Has ganado!")
    elif not quedanBarcos(tableroJugador):
        FinDeJuego("Ordenador")
        print("Has perdido")

if __name__ == "__main__":
    main()