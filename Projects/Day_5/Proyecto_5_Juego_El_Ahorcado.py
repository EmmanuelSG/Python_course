import random

def Bienvenida():
    print("\n")
    print("""Este es el juego del Ahorcado""")

def elegir_palabra():
    palabras = ["camino", "ventana", "luz", "piedra", "mar", "nube", "sol", "libro", "cielo", "hoja"]

    return random.choice(palabras)

def imprimir_guiones(palabra):
    palabra_guiones = []
    for n in palabra:
        palabra_guiones.append(" _ ")
    print("\n")
    print(palabra_guiones)
    return palabra_guiones

def pedir_letra():
    print("\n")
    return input("Por favor, ingresa una letra: ")

def validar_letra(letra):
    abecedario = 'abcdefghijklmnopqrstuvwxyz'

    if letra.lower() not in abecedario:
        return False
    else:
        return True

def validar_letra_en_palabra(letra, palabra, lista_letras_invalidas, palabra_guiones):
    lista = list(palabra)

    if letra.lower() not in palabra:
        print("\n")
        print("La letra no es valida.")
        lista_letras_invalidas.append(letra)
        return False
    else:
        print("\n")
        print("La letra sí es valida.")
        for index, n in enumerate(lista):
            if n == letra.lower(): 
                palabra_guiones[index] = n

            else:
                pass
        return True
            


palabra_estatus = []
letras_invalidas = []
vidas = 6
letras_faltantes = 0

Bienvenida()

palabra_elegida = elegir_palabra()

palabra_estatus = imprimir_guiones(palabra_elegida)

while(vidas > 0):

    letra = pedir_letra()

    if (validar_letra(letra) == True):

        if True == validar_letra_en_palabra(letra, palabra_elegida, letras_invalidas, palabra_estatus):
            print(palabra_estatus)
            for n in palabra_estatus:
                if n == " _ ":
                    letras_faltantes += 1
                else:
                    pass

            if letras_faltantes > 0:
                letras_faltantes = 0

            else:
                print("\n")
                print("Ganaste!, fin del juego...")
                vidas = 0
                break

        else:
            print(letras_invalidas)
            vidas -= 1
            print("\n")
            print(f"Te quedan {vidas} vidas")

            if (vidas == 0):
                print("\n")
                print("Perdiste, fin del juego...")
                break
            else:
                pass

    else:
        pass



