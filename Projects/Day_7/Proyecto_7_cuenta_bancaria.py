from random import randint
import os


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Hola {self.nombre} {self.apellido}, tu número de cuenta es {self.numero_cuenta} y tienes {self.balance} pesos."
    
    def depositar(self):
        os.system('cls')
        Encabezado("Cuenta bancaria - Depositar")

        self.balance = self.balance + int(input("Ingrese el monto que quiere depositar:  "))

    def retirar(self):
        os.system('cls')
        Encabezado("Cuenta bancaria - Retirar")

        retiro = int(input("Ingrese el monto que quiere retirar:  "))
        while (retiro > self.balance):
            retiro = int(input(f"Tienes {self.balance}, ingresa un monto válido:  "))

        self.balance = self.balance - retiro

def Encabezado(titulo):
    string = 30*"*" + "________   " + titulo + "   _______" + 30*"*" + "\n"
    for s in string:
        print("*", end="")
    print("\n", end="")
    print(string, end="")
    for s in string:
        print("*", end="")
    print("\n")

def crear_cliente(usuario):
    numero_de_cuenta = randint(1000,2000)
    balance = 0
    os.system('cls')
    Encabezado("Cuenta bancaria - Crear cliente")

    nombre_completo = input("Ingrese su nombre completo: ").split()
    while(len(nombre_completo) < 2):
        nombre_completo = input("Ingrese su nombre completo: ").split()

    nombre = nombre_completo[0]
    apellido = nombre_completo[1]

    usuario = Cliente(nombre, apellido, numero_de_cuenta, balance)

    return usuario

def menu_opciones(menu, usuario):
    os.system('cls')
    Encabezado("Cuenta bancaria - menu")

    print("\n" + str(usuario) + "\n")

    print(f"""\nElige una opción:...
          
    _(1)_ Depositar a la cuenta {usuario.numero_cuenta}
    _(2)_ Retirar a la cuenta {usuario.numero_cuenta}
    _(3)_ Salir
\n""")
    menu = int(input("->"))
    return menu





menu = 0 
cliente = Cliente("","",0,0)

cliente = crear_cliente(cliente)

while(3 != menu):
    menu = menu_opciones(menu, cliente)

    if (1 == menu):
        cliente.depositar()

    elif(2 == menu):
        cliente.retirar()

    else:
        menu = 3




