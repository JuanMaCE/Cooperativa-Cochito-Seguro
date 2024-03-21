import datetime
import random
from data_estructure.list.list import List
from datetime import date

prestamos = List()


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
        result += f"ingrresos: {self.ingresos}, "
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


class HistorialPagos:
    def __init__(self, cuotas, restante):
        self.cuota = 0
        self.cuotas_restantes = cuotas
        self.pago = 0
        self.acumulado = 0
        self.restante = restante
        self.fecha_pago = datetime.date
        self.historial = List()

    def pagar(self, pago):
        self.pago = pago
        self.acumulado += pago
        self.cuotas_restantes -= 1
        self.cuota += 1
        self.fecha_pago = datetime.date
        self.restante -= pago
        result = f"Cuota {self.cuota}, "
        result += f"Pago Q.{self.pago}, "
        result += f"Fecha .{self.fecha_pago}, "
        result += f"Acumulado Q.{self.acumulado}, "
        result += f"Restante Q. {self.restante}, "
        self.historial.append(result)

    def imprimir_historial(self):
        for i in self.historial:
            print(i.transversal())


def solicitar():
    monto_solicitado = float(input("Monto solicitado, LAYUOT: "))
    num_prestamo = random.randint(100, 999)
    ingresos = float(input("Ingresos mensuales, LAYOUT: "))
    cuotas = int(input("Coutas solicitadas, LAYOUT: "))
    capacidad_de_pago = ingresos * 0.1 * cuotas
    monto_solicitado_interes = ((monto_solicitado * ((cuotas//3) * 0.01)) + monto_solicitado)
    if capacidad_de_pago >= monto_solicitado_interes:
        monto_aprobado = monto_solicitado
    else:
        monto_aprobado = capacidad_de_pago
    garantia = input("GARANTIA, LAYOUT: ")
    archivo = input("ARCHIVOS, LAYOUT: ")
    plan_pagos = "Numero de Pagos: ", cuotas, "Pago minimo en cuota: ", str(int(monto_aprobado // cuotas)+1)
    historial_pagos = HistorialPagos(cuotas, monto_aprobado)
    x = Prestamo(num_prestamo, 10001, "Generado",  monto_solicitado, cuotas, monto_aprobado, ingresos,
             garantia, archivo, plan_pagos, historial_pagos)
    print(x.transversal())
    prestamos.append(x)



def generar_plan():
    ingresos = float(input("Ingresos mensuales, LAYOUT: "))
    tiempo = float(input("Tiempo de pago en meses, LAYOUT: "))
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


solicitar()


def aprobar():
    codigo = float(input("Codigo, LAYOUT: "))
    for i in prestamos:
        if i.search_id() == codigo:
            i.change_status("Aprobado")


def visualizar():
    for i in prestamos:
        print(i.transversal())


def realizar_pago():
    codigo = float(input("Codigo, LAYOUT: "))
    for i in prestamos:
        if i.search_id() == codigo:
            print(i.historial())

realizar_pago()