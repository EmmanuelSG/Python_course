#////////////////////////// ADIVINA EL NUMERO ///////////////////////////////////

from random import *

numero_random = randint(1,100)

print("\n")
nombre = input("¿Cuál es tu nombre?  ")

print("\n")
print (f"{nombre} he pensado un numero entre el 1 y el 100 y tienes 8 intentos para adivinarlo")

print("\n")

for n in range(1,9):
    numero = int(input("¿Cuál crees que es el número? "))
    print("\n")

    if ((numero < 1) or (numero > 100)):
        print (f"Este número no esta permitido, intenta otra vez... te quedan {8 - n} intentos")
        print("\n")

    elif (numero < numero_random):
        print (f"Este número es menor, intenta otra vez... te quedan {8 - n} intentos")
        print("\n")

    elif (numero > numero_random):
        print (f"Este número es mayor, intenta otra vez... te quedan {8 - n} intentos")
        print("\n")
    
    elif (numero == numero_random):
        print (f"Adivinaste!!!!... te tomó {n} intentos")
        print("\n")
        break

 