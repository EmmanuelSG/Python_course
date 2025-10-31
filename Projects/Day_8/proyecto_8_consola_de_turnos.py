from paquete_auxiliares import consola
import os

def Encabezado(titulo):
    os.system('cls')
    string = 30*"*" + "________   " + titulo + "   _______" + 30*"*" + "\n"
    for s in string:
        print("*", end="")
    print("\n", end="")
    print(string, end="")
    for s in string:
        print("*", end="")
    print("\n")

def menu_opciones(menu):
    Encabezado("Consola de turnos - menu")

    print(f"""\nElige una opción:...
          
    _(1)_ Turno para perfumeria
    _(2)_ Turno para farmacia
    _(3)_ Turno para cosmetica
    _(4)_ Salir
\n""")
    
    while True:
        try:
            menu = int(input(f"->  "))
            [1,2,3,4].index(menu)
        except ValueError:
            print("Entrada inválida. Por favor, ingresa una opcion valida.")
        else:
            break

    return menu


def entrada_opciones(valor_esperado, variable):
    while True:
        try:
            variable = int(input(f"Ingresa {valor_esperado} para salir: "))
            if variable == valor_esperado:
                break
            else:
                print(f"Ingresaste: {variable}, ingresa 0 para salir")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")


menu = 0 
turno_perfumeria = consola.obtener_turno_perfumeria()
turno_farmacia = consola.obtener_turno_farmacia()
turno_cosmetica = consola.obtener_turno_cosmetica()

while(4 != menu):
    menu = menu_opciones(menu)

    if (1 == menu):
        Encabezado("Turno perfumeria")
        consola.imprimir_turno(turno_perfumeria)
        entrada_opciones(0, menu)

    elif(2 == menu):
        Encabezado("Turno farmacia")
        consola.imprimir_turno(turno_farmacia)
        entrada_opciones(0, menu)

    elif(3 == menu):
        Encabezado("Turno cosmetica")
        consola.imprimir_turno(turno_cosmetica)
        entrada_opciones(0, menu)

    else:
        pass
