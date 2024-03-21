import random
from data_estructure.list.list import List

prestamo = List()


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
        result += f"historial: {self.historial_pagos}, "
        return result


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
    historial_pagos = 0
    x = Prestamo(num_prestamo, 10001, "Generado",  monto_solicitado, cuotas, monto_aprobado, ingresos,
             garantia, archivo, plan_pagos, historial_pagos)
    print(x.transversal())


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


generar_plan()
solicitar()


def aprobar():
    codigo = float(input("Codigo, LAYOUT: "))


def visualizar():
    pass


def realizar_pago():
    pass
