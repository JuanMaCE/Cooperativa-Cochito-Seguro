import customtkinter
global texto_imagen
from gestion_prestamo.prestamo import solicitar


def main(list_asociados):
    ventana = cargar_datos()
    frame_1 = frame(ventana)
    labels_parte1(frame_1)
    color = "#3E4446"
    # IB
    ib_id = customtkinter.CTkEntry(master=frame_1, placeholder_text='Ingrese Monto')
    ib_id.pack(pady=12, padx=10)
    ib_id.place(x=330, y=65)

    ib_ingresos = customtkinter.CTkEntry(master=frame_1, placeholder_text='Ingresos')
    ib_ingresos.pack(pady=12, padx=10)
    ib_ingresos.place(x=330, y=105)

    ib_cuotas = customtkinter.CTkEntry(master=frame_1, placeholder_text='Cuotas')
    ib_cuotas.pack(pady=12, padx=10)
    ib_cuotas.place(x=330, y=145)

    ib_garantia = customtkinter.CTkEntry(master=frame_1, placeholder_text='Garantia')
    ib_garantia.pack(pady=12, padx=10)
    ib_garantia.place(x=330, y=185)

    ib_archivo = customtkinter.CTkEntry(master=frame_1, placeholder_text='Archivo')
    ib_archivo.pack(pady=12, padx=10)
    ib_archivo.place(x=330, y=225)

    ib_asociado = customtkinter.CTkEntry(master=frame_1, placeholder_text='Codigo de asociado')
    ib_asociado.pack(pady=12, padx=10)
    ib_asociado.place(x=330, y=265)

    button_solicitar = customtkinter.CTkButton(master=frame_1, text="Solicitar", fg_color=color, width=180, height=45,
                                               command=lambda: solicitar(ib_id.get(), ib_ingresos.get(), ib_cuotas.get()
                                                                         , ib_garantia.get(), ib_archivo.get(),
                                                                         ib_asociado.get(), list_asociados))
    button_solicitar.pack(pady=100, padx=10)
    button_solicitar.place(x=10, y=300)
    return

def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Solicitar prestamo")
    ventana.geometry('950x350')
    return ventana


def frame(ventana):
    frame_ = customtkinter.CTkFrame(master=ventana)
    frame_.pack(pady=0, padx=60, fill='both', ipady=80)
    return frame_


def labels_parte1(frame_u):
    lb_inbreso = customtkinter.CTkLabel(master=frame_u, text='Aprobar prestamo',
                                        font=("Times New Roman", 50, "bold"))
    lb_inbreso.pack(pady=400, padx=400)
    lb_inbreso.place(x=10, y=0)

    lb_tipo = customtkinter.CTkLabel(master=frame_u, text='Ingrese el Monto:', font=("Times New Roman", 30))
    lb_tipo.pack(pady=400, padx=400)
    lb_tipo.place(x=10, y=60)

    lb_ingresos = customtkinter.CTkLabel(master=frame_u, text='Ingresos:', font=("Times New Roman", 30))
    lb_ingresos.pack(pady=400, padx=400)
    lb_ingresos.place(x=10, y=100)

    lb_cuotas = customtkinter.CTkLabel(master=frame_u, text='Cuotas:', font=("Times New Roman", 30))
    lb_cuotas.pack(pady=400, padx=400)
    lb_cuotas.place(x=10, y=140)

    lb_garantia = customtkinter.CTkLabel(master=frame_u, text='Garantia:', font=("Times New Roman", 30))
    lb_garantia.pack(pady=400, padx=400)
    lb_garantia.place(x=10, y=180)

    lb_archivo = customtkinter.CTkLabel(master=frame_u, text='Archivo:', font=("Times New Roman", 30))
    lb_archivo.pack(pady=400, padx=400)
    lb_archivo.place(x=10, y=220)

    lb_asociado = customtkinter.CTkLabel(master=frame_u, text='Codigo de Asociado:', font=("Times New Roman", 30))
    lb_asociado.pack(pady=400, padx=400)
    lb_asociado.place(x=10, y=260)