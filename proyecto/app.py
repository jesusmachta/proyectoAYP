import random
import requests
import copy
from Discos import Discos
from Cliente import Cliente
from Staff import Staff
from collections import Counter

class App():
    def __init__(self):

        self.discos = []
        self.clientes = []
        self.staff = []
        self.carrito = []
        self.ids = []

    def start(self):
        print("""
        --- ¡Bienvenido a Saman Musica! ---
        """)
        while True:
            s = (input("""
                    ¿Qué desea hacer?
                    Introduzca el número de su elección:

                        1. Staff
                        2. Clientes
                        3. Mostrar Discos Disponibles
                        4. Estadisticas
                        
                        """))
            if s != "1" and s != "2" and s != "3" and s == "4":
                print("Error, intente de nuevo: ")
            elif s == "1":
                self.menu_staff()
            elif s == "2":
                self.menu_clientes()
            elif s == "3":
                self.mostrar_productos()
            elif s == "4":
                self.estadisticas()
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
                        2. Agregar al Carrito de Compras
                        3. Elimnar del Carrito de Compras
                        4. CheckOut
                        5. Regalo
                        6. Atras
                        
                        """))
            if s != "1" and s != "2" and s != "3" and s != "4" and s != "5" and s != "6":
                print("Error, intente de nuevo: ")
            elif s == "1":
                self.agregar_cliente()
            elif s == "2":
                self.carrito_agregar()
            elif s == "3":
                self.carrito_eliminar()
            elif s == "4":
                self.checkout()
            elif s == "5":
                self.regalo()
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
                if ids in self.ids:
                    print("Error el id ya esta registrado")
                    ids = random.randint(0,999)
                    self.ids.append(ids)
                else:
                    self.ids.append(ids)
                print(self.ids)


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

    def carrito_agregar(self):
        cedula = input("Por favor ingrese su cedula asociada a su registro como cliente: ")
        while not cedula.isnumeric():
            print("Error")
            cedula = input("Por favor ingrese su cedula asociada a su registro como cliente: ")
        cedula = int(cedula)

        for i, cedu in enumerate(self.clientes):
            if cedu['Cedula'] == cedula:
                print(self.discos)
                ids = input("Por favor ingrese el id del disco: ")
                while not ids.isnumeric():
                    print("Error el id no esta en el inventario o es incorrecto")
                    ids = input("Por favor ingrese el id del disco: ")

                ids = int(ids)

                for disco in self.discos:
                        if disco['ids'] == ids:
                            carritos = copy.deepcopy(disco)                         
                            self.carrito.append(carritos)
                            del self.discos[i]
                print("Disco Agregado a su Carrito!")
                print(self.carrito)

    def carrito_eliminar(self):
        cedula = input("Por favor ingrese su cedula asociada a su registro como cliente: ")
        while not cedula.isnumeric():
            print("Error")
            cedula = input("Por favor ingrese su cedula asociada a su registro como cliente: ")
        cedula = int(cedula)

        for i, cedu in enumerate(self.clientes):
            if cedu['Cedula'] == cedula:
                print(self.carrito)
                ids = input("Por favor ingrese el id del disco: ")
                while not ids.isnumeric():
                    print("Error el id no esta en el inventario o es incorrecto")
                    ids = input("Por favor ingrese el id del disco: ")

                ids = int(ids)

                for i, disco in enumerate(self.carrito):
                        if disco['ids'] == ids:
                            del self.carrito[i]

                print("Disco Eliminado de su carrito")
                print(self.carrito)

    def checkout(self):

        cedula = input("Por favor ingrese su cedula asociada a su registro como cliente: ")
        while not cedula.isnumeric():
            print("Error")
            cedula = input("Por favor ingrese su cedula asociada a su registro como cliente: ")
        cedula = int(cedula)

        for i, cedu in enumerate(self.clientes):
            if cedu['Cedula'] == cedula:
                costo_compra_cliente = sum(i['precio_venta'] for i in self.carrito)
                costo_con_iva = costo_compra_cliente + costo_compra_cliente * 0.03
                print(f'El cliente debe cancelar: {costo_con_iva}$')

    def regalo(self):
        res = []
        for ele in self.ids:
            sum = 0
            for digit in str(ele):
                sum += int(digit)
            res.append(sum)
        print ("La Suma de los digitos del id es: " + str(res))    
        for num in res:
            if num == 7:
                print("Querido cliente, su pedido es un regalo por parte de la Tienda")
            else:
                print("No se aplica la oferta del regalo")
    
    def estadisticas(self):
        cedula = input("Por favor ingrese su cedula asociada al registro del staff: ")
        while not cedula.isnumeric():
            print("Error")
            cedula = input("Por favor ingrese su cedula asociada al registro del staff: ")
        cedula = int(cedula)

        for i, cedu in enumerate(self.staff):
            if cedu['Cedula'] == cedula:
                print("""
                --- ¡Bienvenido Estimado Staff! ---
                --- ¡Aqui estan las Estadisticas de la Tienda! ---
                """)
                while True:
                    s = (input("""
                            ¿Qué desea hacer?
                            Introduzca el número de su elección:
        
                                1. Clientes mas Fieles
                                2. Clientes que mas han Gastado
                                3. Géneros mas Vendido
                                4. Artistas mas Vendidos
                                5. Clientes Sin finiquitar compra
                                6. Ingreso Bruto
                                7. Ganancia Neta
                                8. Discos Regalados
                                9. Atras
                                
                                """))
                    if s != "1" and s != "2" and s != "3" and s != "4" and s != "5" and s != "6" and s != "7" and s != "8" and s != "9":
                        print("Error, intente de nuevo: ")
                    elif s == "1":
                        pass
                    elif s == "2":
                        pass
                    elif s == "3":
                        pass
                    elif s == "4":
                        pass
                    elif s == "5":
                        pass
                    elif s == "6":
                        pass
                    elif s == "7":
                        pass
                    elif s == "8":
                        pass
                    else:
                        break