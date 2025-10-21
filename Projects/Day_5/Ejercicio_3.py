

def doble_cero(*args):
    lista = []
    retorno = False

    for contador, n in enumerate(args):
        lista.append(n)
        if (contador >=1) and (lista[contador-1] == 0) and (lista[contador] == 0):
            retorno = True
            break
        else:
            pass

    return retorno
         

print(f"{doble_cero(5,6,7,0,0,3,5,7)}")
print(f"{doble_cero(5,6,7,0,1,3,5,7)}")