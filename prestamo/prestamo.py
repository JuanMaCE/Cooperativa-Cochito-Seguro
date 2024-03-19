class Prestamo:
    def __init__(self, id_prestamo: int, id_credito: int, status: str, monto_solicitado: int,
                 cuotas: int, monto_aprobado: int, ingresos: int, garantia: str,
                 archivos, plan_pagos, historial_pagos):
        self.id_prestamo = id_prestamo
        self.id_credito = id_credito
        self.status = status
        self.monto_solicitado = monto_solicitado
        self.coutas = cuotas
        self.monto_aprobado = monto_aprobado
        self.ingresos = ingresos
        self.garantia = garantia
        self.archivos = archivos
        self.plan = plan_pagos
        self.historial_pagos = historial_pagos

    def solicitar(self):
        pass

    def generar_plan(self):
        pass

    def aprobar(self):
        pass

    def visualizar(self):
        pass

    def realizar_pago(self):
        pass

