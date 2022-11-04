class Discos:
    def __init__(self, ids, titulo, artista, ano_publicacion, costo, precio_venta):
        self.ids = ids
        self.titulo = titulo
        self.artista = artista
        self.ano_publiacion = ano_publicacion
        self.costo = costo
        self.precio_venta = precio_venta

    def show_attr(self):
        print (f"""
                ids: {self.ids}
                titulo: {self.titulo}
                artista: {self.artista}
                ano_publicacion: {self.ano_publiacion}
                costo: {self.costo}
                precio_venta: {self.precio_venta}
                """)