
def devolver_distintos(int1, int2, int3):
    suma = int1 + int2 + int3
    lista = [int1, int2, int3]
    lista.sort()

    if (suma > 15):
        return lista[2]
    
    elif(suma < 10):
        return lista[0]
    
    else:
        return lista[1]
    
print(f"El valor obtenido es {devolver_distintos(4, 8, 2)}")