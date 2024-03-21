import customtkinter
from gestion_prestamo import v_aprobar, v_generar, v_pagar, v_solicitar, v_visualizar, prestamo
from gestion_prestamo.prestamo import solicitar, generar_plan, aprobar, visualizar, realizar_pago


color = "#3E4446"


def main(list_asociados):
    ventana = cargar_datos()
    frame = frame1(ventana)
    labels_parte1(frame, list_asociados)

    ventana.mainloop()

    return


def open_solicitar(list_asociados):
    v_solicitar.main(list_asociados)


def open_generar():
    v_generar.main()


def open_aprobar():
    v_aprobar.main()

def open_pagar():
    v_pagar.main()

def open_visualizar():
    v_visualizar.main()
def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Menú Gestión Prestamos")
    ventana.geometry("1000x400")

    # buttons

    return ventana


def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=60, fill='both', ipady=90)
    return frame


def labels_parte1(frame, lista_asociados):
    lb_inbreso = customtkinter.CTkLabel(master=frame, text='Menú Gestión Prestamos',
                                        font=("Times New Roman", 50, "bold"))
    lb_inbreso.pack(pady=400, padx=400, )
    lb_inbreso.place(x=10, y=0)

    button_solicitar = customtkinter.CTkButton(master=frame, text="Solicitar", fg_color=color, height=100, width=210,
                                               command=lambda: open_solicitar(lista_asociados))
    button_solicitar.pack(pady=100, padx=10)
    button_solicitar.place(x=10, y=100)

    button_generar = customtkinter.CTkButton(master=frame, text="Generar planes", fg_color=color, height=100, width=210,
                                            command=open_generar)
    button_generar.pack(pady=100, padx=10)
    button_generar.place(x=340, y=100)

    button_aprobar = customtkinter.CTkButton(master=frame, text="Aprobar", fg_color=color, height=100, width=210,
                                              command=open_aprobar)
    button_aprobar.pack(pady=100, padx=10)
    button_aprobar.place(x=650, y=100)

    button_visualizar = customtkinter.CTkButton(master=frame, text="Visualizar", fg_color=color, height=100, width=210,
                                              command=open_visualizar)
    button_visualizar.pack(pady=100, padx=10)
    button_visualizar.place(x=10, y=230)

    button_pagos = customtkinter.CTkButton(master=frame, text="Pagos", fg_color=color, height=100, width=210,
                                                command=open_pagar)
    button_pagos.pack(pady=100, padx=10)
    button_pagos.place(x=340, y=230)