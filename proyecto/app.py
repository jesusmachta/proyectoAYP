import random
import requests
from Discos import Discos
from Cliente import Cliente
from Staff import Staff

class App():
    def __init__(self):

        self.discos = []
        self.clientes = []
        self.staff = []

    def start(self):
        print("""
        --- ¡Bienvenido a Saman Musica! ---
        """)
        while True:
            s = (input("""
                    ¿Qué desea hacer?
                    Introduzca el número de su elección:

                        1. Clientes
                        2. Staff
                        3. Mostrar Discos Disponibles
                        
                        """))
            if s != "1" and s != "2" and s != "3":
                print("Error, intente de nuevo: ")
            elif s == "1":
                self.menu_clientes()
            elif s == "2":
                self.menu_staff()
            elif s == "3":
                self.mostrar_productos()
            else:
                print("Gracias por visitarnos!")
                break

    def menu_clientes(self):
        print("""
        --- ¡Bienvenido Estimado Cliente! ---
        --- De no tener una cuenta, por favor registrece ---
        --- De ya tener una cuenta, puede agregar al carrito ---
        """)
        while True:
            s = (input("""
                    ¿Qué desea hacer?
                    Introduzca el número de su elección:

                        1. Registrar Cliente
                        2. Carrito de Compras
                        3. Atras
                        
                        """))
            if s != "1" and s != "2" and s != "3":
                print("Error, intente de nuevo: ")
            elif s == "1":
                self.agregar_cliente()
            elif s == "2":
                pass
            else:
                print("Gracias por visitarnos!")
                break

    def menu_staff(self):
        print("""
        --- ¡Bienvenido Estimado Staff! ---
        """)
        while True:
            s = (input("""
                    ¿Qué desea hacer?
                    Introduzca el número de su elección:

                        1. Agregar Staff
                        2. Inventario
                        3. Atras
                        
                        """))
            if s != "1" and s != "2" and s != "3":
                print("Error, intente de nuevo: ")
            elif s == "1":
                self.agregar_staff()
            elif s == "2":
                self.inventario()
            else:
                break
    

    def inventario(self):
        print("""
        --- ¡Bienvenido Estimado Staff! ---
        """)
        while True:
            s = (input("""
                    ¿Qué desea hacer?
                    Introduzca el número de su elección:

                        1. Agregar al Inventario
                        2. Eliminar del Inventario
                        3. Mostrar Productos Disponibles
                        4. Atras
                        
                        """))
            if s != "1" and s != "2" and s != "3" and s != "4":
                print("Error, intente de nuevo: ")
            elif s == "1":
                self.agregar_disco()
            elif s == "2":
                self.eliminar_disco()
            elif s == "3":
                self.mostrar_productos()
            else:
                break

    def agregar_cliente(self):

        nombre = input("Por favor ingrese su nombre: ")
        while not nombre.isalpha():
            print("Error")
            nombre = input("Por favor introduzca su nombre: ")
        apellido = input("Por favor ingrese su apellido: ")
        while not apellido.isalpha():
            print("Error")
            apellido = input("Por favor ingrese su apellido: ")
        cedula = input("Por favor ingrese su cedula: ")
        while not cedula.isnumeric():
            print("Error")
            cedula = input("Por favor ingrese su cedula: ")
        cedula = int(cedula)
        
        cliente = {
            "Nombre": nombre,
            "Apellido": apellido,
            "Cedula": cedula
            }
        #cliente = Cliente(nombre, apellido, cedula)
        self.clientes.append(cliente)
        print("Cliente Agregado!")
    
    def agregar_staff(self):

        nombre = input("Por favor ingrese su nombre: ")
        while not nombre.isalpha():
            print("Error")
            nombre = input("Por favor introduzca su nombre: ")
        apellido = input("Por favor ingrese su apellido: ")
        while not apellido.isalpha():
            print("Error")
            apellido = input("Por favor ingrese su apellido: ")
        cedula = input("Por favor ingrese su cedula: ")
        while not cedula.isnumeric():
            print("Error")
            cedula = input("Por favor ingrese su cedula: ")
        cedula = int(cedula)

        staffs = {
            "Nombre": nombre,
            "Apellido": apellido,
            "Cedula": cedula
            }
        #staffs = Staff(nombre, apellido, cedula)
        self.staff.append(staffs)
        print("Staff Agregado")
    
    def agregar_disco(self):
        cedula = input("Por favor ingrese su cedula asociada al registro del staff: ")
        while not cedula.isnumeric():
            print("Error")
            cedula = input("Por favor ingrese su cedula asociada al registro del staff: ")
        cedula = int(cedula)

        for i, cedu in enumerate(self.staff):
            if cedu['Cedula'] == cedula:
                
                ids = random.randint(0,999)

                titulo = input("Por favor ingrese el tiutlo del album: ")
                while not titulo.isalpha():
                    print("Error")
                    titulo = input("Por favor ingrese el titulo del album: ")
                titulo = titulo.title()

                artista = input("Por favor ingrese el artista: ")
                while not artista.isalpha():
                    print("Error")
                    titulo = input("Por favor ingrese el artista: ")
                artista = artista.title()

                ano_publicacion = input("Por favor ingrese el año de publiación: ")
                while not ano_publicacion.isnumeric():
                    print("Error")
                    ano_publicacion = input("Por favor ingrese el año de publiación: ")
                ano_publicacion = int(ano_publicacion)

                costo = input("Por favor ingrese el costo: ")
                while not costo.isnumeric():
                    print("Error")
                    costo = input("Por favor ingrese el costo: ")
                costo = int(costo)

                precio_venta = input("Por favor ingrese el precio de venta: ")
                while not precio_venta.isnumeric():
                    print("Error")
                    precio_venta = input("Por favor ingrese el precio de venta: ")
                precio_venta = int(precio_venta)

                discos = {
                    "ids": ids,
                    "tiutlo": titulo,
                    "artista": artista,
                    "ano_publiacion": ano_publicacion,
                    "costo": costo,
                    "precio_venta": precio_venta
                }
                #discos = Discos(ids, titulo, artista, ano_publicacion, costo, precio_venta)
                self.discos.append(discos)
                print("Disco Agregado!")

    def mostrar_productos(self):
        for i in self.discos:
            print(i)

    def eliminar_disco(self):
        
        for i in self.discos:
            print(i)
            
        cedula = input("Por favor ingrese su cedula asociada al registro del staff: ")
        while not cedula.isnumeric():
            print("Error")
            cedula = input("Por favor ingrese su cedula asociada al registro del staff: ")
        cedula = int(cedula)

        for i, cedu in enumerate(self.staff):
            if cedu['Cedula'] == cedula:
                ids = input("Por favor ingrese el id del disco: ")
                while not ids.isnumeric():
                    print("Error el id no esta en el inventario o es incorrecto")
                    ids = input("Por favor ingrese el id del disco: ")

                ids = int(ids)

                for i, disco in enumerate(self.discos):
                        if disco['ids'] == ids:
                            del self.discos[i]

                print("Disco Eliminado!")