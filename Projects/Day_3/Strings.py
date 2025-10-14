#Metodo index

mi_texto = "Esta es una prueba una"
resultado = mi_texto[0]
resultado2 = mi_texto.index("n")
resultado3 = mi_texto.find("4")
print("resulado: " + str(resultado))
print("resulado2: " + str(resultado2))
print("resulado3: " + str(resultado3))

#Slice o extraer texto
texto = "ABCDEFGHIJKLMNOPQ"
fragmento = texto[2:15:2]
print(fragmento)


#metodos de strings
texto2 = "Este es el texto de Emmanuel"

resul = texto2[1:].upper()
resul2 = texto2.lower()
resul3 = texto2.split("t")

print(resul3)

a = "Aprender"
b = "es"
c = "genial"
resul4 = " ".join([a,b,c])
print(resul4)


