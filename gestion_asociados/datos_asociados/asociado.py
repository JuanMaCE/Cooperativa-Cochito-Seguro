from data_estructure.list_double.list_double import ListD
import random


class Asociado:
    def __init__(self, nombre, direccion, telefono, dpi, nit, referencias_personales):
        codigo = random.randint(999, 9999)
        self.codigo_asociado = codigo
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.dpi = dpi
        self.nit = nit
        self.archivos_adjuntos = ListD()
        self.referencias_personales = referencias_personales

    def cambiar_codigo(self, new_codigo: int):
        self.codigo_asociado = new_codigo

    def agregar_referencais(self, referencias):
        self.referencias_personales = referencias

    def eliminar_referencias(self):
        self.referencias_personales = None

    def almacenar_archivos_adjuntos(self, archivo):
        self.archivos_adjuntos.append(archivo)

    def actualizar_datos(self, nombre, direccion, dpi, nit, referencias_personales):
        self.nombre = nombre
        self.direccion = direccion
        self.dpi = dpi
        self.nit = nit
        self.archivos_adjuntos = ListD()
        self.referencias_personales = referencias_personales

    def devolver_nomre(self):
        return str(self.nombre)

    def __str__(self):
        return str(self.nombre)

    def devolver_id(self):
        return str(self.codigo_asociado)

    def devolver_direccion(self):
        return str(self.direccion)

    def devolver_telefono(self):
        return str(self.telefono)

    def devolver_dpi(self):
        return str(self.dpi)

    def devolver_nit(self):
        return str(self.nit)

    def referencias_personales(self):
        return str(self.referencias_personales())
