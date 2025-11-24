from funciones import *
import sys

def main():
    while True: # Bucle para poder volver a jugar
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

        dificultad = 0
        while True:
            try:
                dificultad = int(input("Selecciona una opción: "))
                if dificultad in [1, 2, 3]:
                    break
                else:
                    print("Opción no válida, intenta de nuevo.")
            except ValueError:
                print("Por favor, introduce un número válido.")

        print()
        print("Iniciando partida...")
        time.sleep(1)

        # --- CREAMOS TABLEROS ---
        tableroJugador = crearMatriz(11, 11, "-")
        tableroJugador = Pasarletra(tableroJugador)
        tableroJugador = PasarNumeros(tableroJugador)
        tableroJugador = generarBarcos(tableroJugador, dificultad)

        tableroRival = crearMatriz(11, 11, "-")
        tableroRival = Pasarletra(tableroRival)
        tableroRival = PasarNumeros(tableroRival)
        tableroRival = generarBarcos(tableroRival, dificultad)

        juego_activo = True

        # --- BUCLE DEL JUEGO ---
        while juego_activo:
            # 1. Mostrar Tableros
            print("\n" + "="*30)
            print("=== TABLERO DEL RIVAL ===")
            imprimirFilasMatriz(ocultarBarcos(tableroRival))
            
            print("\n=== TU TABLERO ===")
            imprimirFilasMatriz(tableroJugador)
            print("="*30)

            # 2. Turno Jugador
            disparoJugador(tableroRival)
            
            # Comprobar victoria Jugador
            if not quedanBarcos(tableroRival):
                imprimirFilasMatriz(tableroRival) # Ver el resultado final
                FinDeJuego("Jugador")
                juego_activo = False
                break

            time.sleep(1)
            print("\n--------------------------------")
            print("Turno del Ordenador...")
            time.sleep(1)

            # 3. Turno Ordenador
            disparoAleatorio(tableroJugador)

            # Comprobar victoria Ordenador
            if not quedanBarcos(tableroJugador):
                imprimirFilasMatriz(tableroJugador)
                FinDeJuego("Ordenador")
                juego_activo = False
                break
        
        # Preguntar si jugar de nuevo
        print("\n¿Quieres volver a jugar?")
        print("1. Si")
        print("2. No")
        while True:
            try:
                opcion = int(input("Elige: "))
                if opcion != "1":
                    print("Gracias por jugar. ¡Adiós!")
                    sys.exit()
            except ValueError:
                print("Opción no válida")
        

if __name__ == "__main__":
    main()