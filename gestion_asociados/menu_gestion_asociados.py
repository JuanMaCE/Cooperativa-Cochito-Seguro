import customtkinter
from gestion_asociados import agregar, edit, delete
from data_estructure.circular_list.circular_list import CircularList
from typing import TypeVar

T = TypeVar("T")
asociados = CircularList[T]()
color = "#3E4446"


def main():
    ventana = cargar_datos()
    frame = frame1(ventana)
    labels_parte1(frame)

    ventana.mainloop()

    return


def open_registro():
    a = agregar.main()
    asociados.prepend(a)
    for dato in asociados:
        print(dato)

def open_edit():
    for dato in asociados:
        print(dato)
        print(" jeje ")
    edit.main(asociados)


def open_delete():
    delete.main()


def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Menú Gestión Asociados")
    ventana.geometry("1000x300")

    # buttons

    return ventana


def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=60, fill='both', ipady=60)
    return frame


def labels_parte1(frame, ):
    lb_inbreso = customtkinter.CTkLabel(master=frame, text='Menú Gestión Asociados',
                                        font=("Times New Roman", 50, "bold"))
    lb_inbreso.pack(pady=400, padx=400, )
    lb_inbreso.place(x=10, y=0)

    button_agregar = customtkinter.CTkButton(master=frame, text="Agregar", fg_color=color, height=100, width=210,
                                             command=open_registro)
    button_agregar.pack(pady=100, padx=10)
    button_agregar.place(x=10, y=100)

    button_editar = customtkinter.CTkButton(master=frame, text="Editar", fg_color=color, height=100, width=210,
                                            command=open_edit)
    button_editar.pack(pady=100, padx=10)
    button_editar.place(x=340, y=100)

    button_eliminar = customtkinter.CTkButton(master=frame, text="Eliminar  ", fg_color=color, height=100, width=210,
                                              command=open_delete)
    button_eliminar.pack(pady=100, padx=10)
    button_eliminar.place(x=650, y=100)
