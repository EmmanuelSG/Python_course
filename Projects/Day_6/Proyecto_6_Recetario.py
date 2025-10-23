import os
from pathlib import Path 

############# Variables #######################
ruta_recetas = Path("C:/Users/hjg45m/Desktop/Python_course/Python_course/Anexos/Recetas")
inicio_programa = True
opciones = 0
categoria = 0


############ Funciones auxiliares ##############

def Encabezado(titulo):
    print(90*"*" + "\n")
    print(30*"*" + "___________" + titulo + "__________" + 30*"*" + "\n")

# Funcion para contar recetas
def contar_recetas(ruta):      
    contador = 0
    contador = len(list(ruta.rglob("*.txt")))
    return contador

# Funcion para elegir una categoria
def elegir_categoria(ruta):
    index_categoria = -1
    contador = 0
    directorios = [item for item in ruta.iterdir() if item.is_dir()]

    for index,item in enumerate(directorios, start=1):
        print(f"_{index}_  " + item.name + "\n")
        contador += 1
    
    while not ((contador >= index_categoria) and (0 <= index_categoria)):
        index_categoria = int(input("Elige una opción:  "))
    print("\n\n\n")

    return str(index_categoria)

# Funcion para elegir una receta dentro de la categoría seleccionada
def elegir_receta(ruta, index_categoria):
    index_receta = -1
    dic_recetas = dict()
    directorios = [item for item in ruta.iterdir() if item.is_dir()]

    for index,item in enumerate(directorios, start=1):
        if index_categoria == str(index):
            recetas = item.glob("*.txt")
        else:
            pass
    
    for index,receta in enumerate(recetas, start=1):
        print(f"_{index}_  " + receta.name + "\n")
        dic_recetas[str(index)] = str(receta)

    while not (len(dic_recetas) >= int(index_receta) and 0 <= int(index_receta)):
        index_receta = int(input("Elige una opción:  "))
    print("\n\n\n")

    return dic_recetas[str(index_receta)]

# Funcion para mostrar receta
def mostrar_receta(ruta):
    with open(ruta, "r") as f:
        contenido = f.read()
        print(contenido)

    print("\n\n_(1)_ Regresar a Leer receta\n")
    print("_(Cualquier numero)_ Regresar a Inicio\n")
    retorno = input("\nSelecciona una opcion:  ")
    if ("1" == retorno):
        pass
    else:
        retorno = "7"
    return retorno

# Obtener el nombre y la ruta del archivo
def nombre_y_ruta(ruta, index_categoria):
    directorio_seleccionado = ""
    directorios = [item for item in ruta.iterdir() if item.is_dir()]

    for index,item in enumerate(directorios, start=1):
        if index_categoria == str(index):
            directorio_seleccionado = item
        else:
            pass

    nombre = input("Ingresa un nombre para tu receta: ")
    return nombre, directorio_seleccionado

# Funcion para crear receta
def crear_archivo(ruta, nombre):
    contenido = input("Ingresa tu receta:..... \n")

    with open(str(Path(ruta)/nombre) + ".txt", "w") as archivo:
        archivo.write(contenido)

    print("\n\n_(2)_ Regresar a Crear receta\n")
    print("_(Cualquier numero)_ Regresar a Inicio\n")
    retorno = input("\nSelecciona una opcion:  ")
    if ("2" == retorno):
        pass
    else:
        retorno = "7"
    return retorno

# Funcion para crear nuevo directorio
def Elegir_nombre_crear_directorio(ruta):
    nombre_directorio = input("\nElige un nombre para tu nueva categoría: ")

    nueva_ruta = Path(str(ruta) + "/" + nombre_directorio)
    nueva_ruta.mkdir(exist_ok=True)
    print("\nTu nueva categoria fue creada")

    print("\n\n_(3)_ Regresar a Crear categoria\n")
    print("_(Cualquier numero)_ Regresar a Inicio\n")
    retorno = input("\nSelecciona una opcion:  ")
    if ("3" == retorno):
        pass
    else:
        retorno = "7"
    return retorno

def Eliminar_archivo(ruta):
    archivo = Path(ruta)
    nombre = archivo.name.upper()

    if archivo.exists():
        archivo.unlink()

    print("               RECETA " + nombre + " ELIMINADA \n")
    print("\n\n_(4)_ Regresar a Eliminar receta\n")
    print("_(Cualquier numero)_ Regresar a Inicio\n")
    retorno = input("\nSelecciona una opcion:  ")
    if ("4" == retorno):
        pass
    else:
        retorno = "7"
    return retorno

# Funcion para eliminar directorio
def Eliminar_directorio(ruta, index_categoria):
    directorios = [item for item in ruta.iterdir() if item.is_dir()]

    for index,item in enumerate(directorios, start=1):
        if index_categoria == str(index):
            nombre_directorio = Path(item).name
        else:
            pass
        
    eliminar_ruta = Path(str(ruta) + "/" + nombre_directorio)
    nombre = eliminar_ruta.name
    
    if eliminar_ruta.exists() and eliminar_ruta.is_dir():
        eliminar_ruta.rmdir()

    print("\nLa categoria " + nombre + " fue eliminada")

    print("\n\n_(5)_ Regresar a Eliminar categoria\n")
    print("_(Cualquier numero)_ Regresar a Inicio\n")
    retorno = input("\nSelecciona una opcion:  ")
    if ("5" == retorno):
        pass
    else:
        retorno = "7"
    return retorno



############ Funciones principales #############

def Inicio(ruta, op):
    os.system('cls')
    Encabezado("RECETARIO")
    print("Las recetas estan en: " + str(ruta) + "\n")
    print(f"El número de recetas que hay es: {contar_recetas(ruta)}" + "\n\n")

    print("_(1)_  Leer receta \n")
    print("_(2)_  Crear receta \n")
    print("_(3)_  Crear categoría \n")
    print("_(4)_  Eliminar receta \n")
    print("_(5)_  Eliminar categoría \n")
    print("_(6)_  Finalizar programa \n\n")

    op = input("Elige una opción:  ")
    print("\n\n\n")

    return op

def Leer_recetas(ruta, op):
    os.system('cls')
    Encabezado("LEER RECETA")
    Encabezado("CATEGORIAS")
    categoria = elegir_categoria(ruta)

    os.system('cls')
    Encabezado("RECETAS")
    ruta_receta = elegir_receta(ruta, categoria)

    os.system('cls')
    Encabezado("RECETA DE" + str(Path(ruta_receta).name).upper())
    op = mostrar_receta(ruta_receta)
    
    return op

def Crear_receta(ruta, op):
    os.system('cls')
    Encabezado("CREAR RECETA")
    Encabezado("CATEGORIAS")
    categoria = elegir_categoria(ruta)

    os.system('cls')
    Encabezado("ELEGIR NOMBRE")
    nombre_receta, directorio = nombre_y_ruta(ruta, categoria)

    os.system('cls')
    Encabezado("CREAR RECETA")
    op = crear_archivo(directorio, nombre_receta)

    return op

def Crear_categoria(ruta, op):
    os.system('cls')
    Encabezado("CREAR CATEGORIA")
    Encabezado("ELEGIR NOMBRE")
    op = Elegir_nombre_crear_directorio(ruta)

    return op

def Eliminar_receta(ruta, op):
    os.system('cls')
    Encabezado("ELIMINAR RECETA")
    Encabezado("CATEGORIAS")
    categoria = elegir_categoria(ruta)

    os.system('cls')
    Encabezado("RECETAS")
    ruta_receta = elegir_receta(ruta, categoria)

    os.system('cls')
    op = Eliminar_archivo(ruta_receta)
    
    return op

def Eliminar_categoria(ruta, op):
    os.system('cls')
    Encabezado("ELIMINAR CATEGORIA")
    Encabezado("CATEGORIAS")
    categoria = elegir_categoria(ruta)

    os.system('cls')
    Encabezado("ELEGIR NOMBRE")
    op = Eliminar_directorio(ruta, categoria)

    return op



while("6" != opciones):

    opciones = Inicio(ruta_recetas, opciones)

    while("1" == opciones):
        opciones = Leer_recetas(ruta_recetas, opciones)

    while("2" == opciones):
        opciones = Crear_receta(ruta_recetas, opciones)

    while("3" == opciones):
        opciones = Crear_categoria(ruta_recetas, opciones)

    while("4" == opciones):
        opciones = Eliminar_receta(ruta_recetas, opciones)

    while("5" == opciones):
        opciones = Eliminar_categoria(ruta_recetas, opciones)
        pass
