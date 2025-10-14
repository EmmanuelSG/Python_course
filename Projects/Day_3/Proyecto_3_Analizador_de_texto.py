print("Ingrese un texto: ")

texto = "En un rincón olvidado del bosque, python donde los árboles susurran secretos al viento y la luz del sol apenas se filtra entre las hojas, vivía una criatura diminuta llamada Elio. No era un duende ni un hada, sino algo más antiguo, más curioso. Cada mañana, Elio despertaba con el canto de los pájaros y recorría los senderos cubiertos de musgo, recolectando gotas de rocío en una pequeña copa de pétalos. Su misión era simple: mantener viva la chispa de la magia que aún quedaba en ese rincón del mundo."

print(texto)

print("""Ingresa 3 letras... 
""")
print("Letra 1: ")
#Letra_1 = input()
Letra_1 = "a"
print("Letra 2: ")
#Letra_2 = input()
Letra_2 = "b"
print("Letra 3: ")
#Letra_3 = input()
Letra_3 = "c"

texto_minus = texto.lower()
Letra_1_minus = Letra_1.lower()
Letra_2_minus = Letra_2.lower()
Letra_3_minus = Letra_3.lower()

Letra_1_count = texto_minus.count(Letra_1_minus)
Letra_2_count = texto_minus.count(Letra_2_minus)
Letra_3_count = texto_minus.count(Letra_3_minus)

print("Hay '" + str(Letra_1_count) + "' letras " + Letra_1)
print("Hay '" + str(Letra_2_count) + "' letras " + Letra_2)
print("Hay '" + str(Letra_3_count) + "' letras " + Letra_3)

texto_lista = texto.split()
texto_lista_invert = texto_lista[::-1]
texto_invert = " ".join(texto_lista_invert)

texto_palabras_count = len(texto_lista)

print("El numero total de palabras es " + str(texto_palabras_count))

print("La primera letra es '" + texto[0] + "' y la última es " + texto[-1])

print(texto_invert)

print("Existe la palabra python en el texto?: " + str(texto.find("python")!= -1))



