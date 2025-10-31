#Decorador
def decorar_turno(funcion_imprimir_turno):

    def decorador(funcion_obtener_turno):
        print("Tu turno es: ")
        funcion_imprimir_turno(funcion_obtener_turno)
        print("aguarde un momento y sera atendido...")
    return decorador

#Funcion para obtener turno de perfumería
def obtener_turno_perfumeria():
    cont = 1 
    while True:
        yield f"P - {cont}"
        cont += 1

#Funcion para obtener turno de farmacia
def obtener_turno_farmacia():
    cont = 1 
    while True:
        yield f"F - {cont}"
        cont += 1

#Funcion para obtener turno de cosmética
def obtener_turno_cosmetica():
    cont = 1 
    while True:
        yield f"C - {cont}"
        cont += 1

#Funcion para imprimir el turno
@decorar_turno
def imprimir_turno(funcion):
    print(next(funcion))


