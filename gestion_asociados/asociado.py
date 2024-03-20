from data_estructure.list_double.list_double import ListD
import random
class Asociado():
    def __init__(self,nombre,direccion,telefono,dpi,nit,referencias_personales):
        self.codigo_asociado = None
        self.nombre = nombre
        self.direccion = direccion
        self.telefonos = ListD()
        self.telefonos.append(telefono)
        self.dpi = dpi
        self.nit = nit
        self.archivos_adjuntos = ListD()
        self.referencias_personales = referencias_personales
        self.generar_codigo()

    def generar_codigo(self):
        codigo = ""
        codigo += self.nombre[0] + self.nombre[1]
        for i in range(0,4):
            num = random.randint(0,9)
            codigo += str(num)
        self.codigo_asociado = codigo

    def agregar_referencais(self,referencias):
        self.referencias_personales = referencias

    def eliminar_referencias(self):
        self.referencias_personales = None

    def almacenar_archivos_adjuntos(self,archivo):
        self.archivos_adjuntos.append(archivo)

    def actualizar_datos(self,nombre,direccion,dpi,nit,referencias_personales):
        self.nombre = nombre
        self.direccion = direccion
        self.dpi = dpi
        self.nit = nit
        self.archivos_adjuntos = ListD()
        self.referencias_personales = referencias_personales