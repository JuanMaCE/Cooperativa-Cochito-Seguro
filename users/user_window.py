import customtkinter
from users import user_delete, user_edit, usuarios, user_registro


color = "#3E4446"


def main():
    ventana = cargar_datos()
    frame = frame1(ventana)
    labels_parte1(frame)

    ventana.mainloop()

    return


def open_ver():
    usuarios.main()


def open_registro():
    user_registro.UserRegistro()


def open_edit():
    user_edit.main()


def open_delete():
    user_delete.main()


def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Menú Usuarios")
    ventana.geometry("1000x300")

    # buttons

    return ventana


def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=60, fill='both', ipady=60)
    return frame


def labels_parte1(frame, ):
    lb_inbreso = customtkinter.CTkLabel(master=frame, text='Menú Usuarios',
                                        font=("Times New Roman", 50, "bold"))
    lb_inbreso.pack(pady=400, padx=400, )
    lb_inbreso.place(x=10, y=0)

    button_registro = customtkinter.CTkButton(master=frame, text="Registrar", fg_color=color, height=100, width=210,
                                              command=open_registro)
    button_registro.pack(pady=100, padx=10)
    button_registro.place(x=10, y=100)

    button_usuarios = customtkinter.CTkButton(master=frame, text="Ver Usuarios", fg_color=color, height=100, width=210,
                                             command=open_ver)
    button_usuarios.pack(pady=100, padx=10)
    button_usuarios.place(x=225, y=100)

    button_editar = customtkinter.CTkButton(master=frame, text="Actualizar", fg_color=color, height=100, width=210,
                                            command=open_edit)
    button_editar.pack(pady=100, padx=10)
    button_editar.place(x=440, y=100)

    button_deshabilitar = customtkinter.CTkButton(master=frame, text="Eliminar", fg_color=color, height=100, width=210,
                                              command=open_delete)
    button_deshabilitar.pack(pady=100, padx=10)
    button_deshabilitar.place(x=655, y=100)
