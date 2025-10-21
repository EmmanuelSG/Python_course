
def ordenar_letras(palabra):
    lista = list(palabra)
    lista_ordenada = list(set(lista))
    lista_ordenada.sort()
    
    return lista_ordenada

print(ordenar_letras("entretenido"))
