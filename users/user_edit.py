import customtkinter


def main():
    ventana = cargar_datos()
    frame = frame1(ventana)
    labels_parte1(frame)
    print(" ")
    ventana.mainloop()

    return


def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Edición de Usuarios")
    ventana.geometry("1000x300")

    # buttons

    return ventana


def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=60, fill='both', ipady=60)
    return frame


def labels_parte1(frame, ):
    lb_inbreso = customtkinter.CTkLabel(master=frame, text='Actualizar Datos',
                                        font=("Times New Roman", 50, "bold"))
    lb_inbreso.pack(pady=400, padx=400, )
    lb_inbreso.place(x=10, y=0)

    bt_data = customtkinter.CTkButton(master=frame, text='Datos', height=100, width=210,
                                          font=("Arial", 20), fg_color="#3E4446")
    bt_data.pack(pady=100, padx=10)
    bt_data.place(x=10, y=100)

    bt_password = customtkinter.CTkButton(master=frame, text='Contraseña', height=100, width=160,
                                                    font=("Arial", 20), fg_color="#3E4446")

    bt_password.pack(pady=100, padx=10)
    bt_password.place(x=340, y=100)
