
from funciones import *

#menu()
tableroA = crearMatriz(11,11,"-")
Pasarletra(tableroA)
PasarNumeros(tableroA)
print("    ##TU TABLERO##  ")
imprimirFilasMatriz(tableroA)
##TABLERO DISPAROS
tableroB = crearMatriz(11,11,"-")
Pasarletra(tableroB)
PasarNumeros(tableroB)
print()
print("##TABLERO DE DISPAROS##")
imprimirFilasMatriz(tableroB)



