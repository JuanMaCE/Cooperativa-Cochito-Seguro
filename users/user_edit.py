import customtkinter
from users import user_edit_data, user_edit_password


class UserEdit:
    def __init__(self, user_pred):
        self.ventana = self.cargar_datos()
        self.frame = self.frame1(self.ventana)
        self.users = user_pred
        self.labels_parte1(self.frame)
        print(" ")
        self.ventana.mainloop()

        return

    def cargar_datos(self):
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('dark-blue')
        # root
        ventana = customtkinter.CTkToplevel()
        ventana.grab_set()
        ventana.title("Edición de Usuarios")
        ventana.geometry("1000x300")

        # buttons

        return ventana

    def frame1(self, ventana):
        frame = customtkinter.CTkFrame(master=ventana)
        frame.pack(pady=10, padx=60, fill='both', ipady=60)
        return frame

    def labels_parte1(self, frame):
        lb_inbreso = customtkinter.CTkLabel(master=frame, text='Actualizar Datos',
                                            font=("Times New Roman", 50, "bold"))
        lb_inbreso.pack(pady=400, padx=400, )
        lb_inbreso.place(x=10, y=0)

        bt_data = customtkinter.CTkButton(master=frame, text='Datos', height=100, width=210,
                                          font=("Arial", 20), fg_color="#3E4446", command=self.open_edit_data)
        bt_data.pack(pady=100, padx=10)
        bt_data.place(x=10, y=100)

        bt_password = customtkinter.CTkButton(master=frame, text='Contraseña', height=100, width=210,
                                              font=("Arial", 20), fg_color="#3E4446", command=self.open_edit_password)

        bt_password.pack(pady=100, padx=10)
        bt_password.place(x=340, y=100)

    def open_edit_data(self):
        user_edit_data.EditData(self.users)

    def open_edit_password(self):
        user_edit_password.EditPassword(self.users)
