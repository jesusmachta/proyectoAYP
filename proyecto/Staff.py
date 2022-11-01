class Staff:
    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
    
    def show_attr(self):
        return f"""
                Nombre: {self.nombre}
                Apellido: {self.apellido}
                Cedula: {self.cedula}
                """