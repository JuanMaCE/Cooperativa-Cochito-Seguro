import datetime
import random

from CTkMessagebox import CTkMessagebox
from data_estructure.list.list import List
from data_estructure.list_double.list_double import ListD
from datetime import date

prestamos = ListD()


class Prestamo:
    def __init__(self, id_prestamo: int, id_asociado: int, status: str, monto_solicitado: float,
                 cuotas: int, monto_aprobado: float, ingresos: float, garantia,
                 archivos, plan_pagos: tuple, historial_pagos):
        self.id_prestamo = id_prestamo
        self.id_asociado = id_asociado
        self.status = status
        self.monto_solicitado = monto_solicitado
        self.coutas = cuotas
        self.monto_aprobado = monto_aprobado
        self.ingresos = ingresos
        self.garantia = garantia
        self.archivos = archivos
        self.plan = plan_pagos
        self.historial_pagos = historial_pagos

    def transversal(self) -> str:
        result = f"Id prestamo: {self.id_prestamo}, "
        result += f"asociado: {self.id_asociado}, "
        result += f"status: {self.status}, "
        result += f"monto sol: {self.monto_solicitado}, "
        result += f"cuotas: {self.coutas}, "
        result += f"monto aprobado: {self.monto_aprobado}, "
        result += f"ingresos: {self.ingresos}, "
        result += f"garantia: {self.garantia}, "
        result += f"archivos: {self.archivos}, "
        result += f"plan: {self.plan}, "
        return result

    def change_status(self, status):
        self.status = status

    def search_id(self):
        return int(self.id_prestamo)

    def historial(self):
        result = ""
        for i in self.historial_pagos:
            result += str(i)
        return result

    def __str__(self):
        result = f"Id prestamo: {self.id_prestamo}, "
        result += f"asociado: {self.id_asociado}, "
        result += f"status: {self.status}, "
        result += f"monto sol: {self.monto_solicitado}, "
        result += f"cuotas: {self.coutas}, "
        result += f"monto aprobado: {self.monto_aprobado}, "
        result += f"ingresos: {self.ingresos}, "
        result += f"garantia: {self.garantia}, "
        result += f"archivos: {self.archivos}, "
        result += f"plan: {self.plan}, "
        return result


class HistorialPagos:
    def __init__(self, cuotas, restante, pago):
        self.cuota = 0
        self.cuotas_restantes = cuotas
        self.pago = pago
        self.acumulado = 0
        self.restante = restante
        self.fecha_pago = datetime.date
        self.historial = List()
        self.saldo_original = restante

    def pagar(self):
        x = self.acumulado + self.pago
        if x >= self.saldo_original:
            self.acumulado = self.saldo_original
            self.pago = x - self.acumulado
            self.cuota += 1
            self.fecha_pago = datetime.date
            self.restante = 0
        else:
            self.acumulado += self.pago
            self.cuotas_restantes -= 1
            self.cuota += 1
            self.fecha_pago = datetime.date.today()
            self.restante -= self.pago
        result = f"Cuota No.{self.cuota}, "
        result += f"Pago Q.{self.pago}, "
        result += f"Fecha .{self.fecha_pago}, "
        result += f"Acumulado Q.{self.acumulado}, "
        result += f"Restante Q. {self.restante}, "
        self.historial.append(result)
        print("pago")

    def imprimir_historial(self):
        for i in self.historial:
            print(i)


def solicitar(monto_solicitado, ingresos, cuotas, garantia, archivo, asociado, lista_asociados):
    lista_usuarios = lista_asociados
    en_lista_o_no = False
    for x in lista_usuarios:
        if asociado == str(x.codigo_asociado):
            en_lista_o_no = True
            ingresos = float(ingresos)
            cuotas = int(cuotas)
            monto_solicitado = float(monto_solicitado)
            num_prestamo = random.randint(100, 999)
            capacidad_de_pago = ingresos * 0.1 * cuotas
            monto_solicitado_interes = ((monto_solicitado * ((cuotas // 3) * 0.01)) + monto_solicitado)
            if capacidad_de_pago >= monto_solicitado_interes:
                monto_aprobado = monto_solicitado
            else:
                monto_aprobado = capacidad_de_pago
            pago_cuota = (monto_aprobado // cuotas) + 1
            plan_pagos = "Numero de Pagos: ", cuotas, "Pago minimo en cuota: ", str(pago_cuota)
            historial_pagos = HistorialPagos(cuotas, monto_aprobado, pago_cuota)
            x = Prestamo(num_prestamo, asociado, "Generado", monto_solicitado, cuotas, monto_aprobado, ingresos,
                         garantia, archivo, plan_pagos, historial_pagos)
            print(x.transversal())
            prestamos.append(x)
            CTkMessagebox(title='APROBADO', message='SE APROBO SU PRESTAMO')
            break
    if not en_lista_o_no:
        CTkMessagebox(title='Advertencia', message='No se encontro el usuario')






def generar_plan(ingresos,tiempo):
    ingresos = float(ingresos)
    tiempo = int(tiempo)
    capacidad_pago = ingresos * 0.1
    cuotas = tiempo
    # actualizar(cuotas, capacidad_pago, ingresos):
    interes_pagar = (cuotas * capacidad_pago) * ((cuotas // 3) * 0.01)
    monto_maximo = cuotas * capacidad_pago - ((cuotas * capacidad_pago) * ((cuotas // 3) * 0.01))
    pago_realizar = monto_maximo / cuotas
    print(monto_maximo, " maximo Boton en layout")
    print(pago_realizar, "pagos Boton en layout")
    print(interes_pagar, "interes a pagar text")
    print(monto_maximo - interes_pagar, "solicitar")


def aprobar(codigo):
    for i in prestamos:
        if i.search_id() == int(codigo):
            i.change_status("Aprobado")


def visualizar():
    texto = " "
    for i in prestamos:
        texto += str(i) + '\n'
    return texto



def realizar_pago(codigo):
    for i in prestamos:
        if i.search_id() == codigo:
            i.historial_pagos.pagar()