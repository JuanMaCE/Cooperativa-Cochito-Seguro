import customtkinter
from users import user_delete, user_edit, usuarios, user_registro

color = "#3E4446"


class UserWindow:
    def __init__(self, users_pred):
        self.ventana = self.cargar_datos()
        self.frame = self.frame1(self.ventana)
        self.labels_parte1(self.frame)
        self.usuarios_predeterminados = users_pred

        self.ventana.mainloop()

        return

    def open_ver(self):
        usuarios.ShowUser(self.usuarios_predeterminados)

    def open_registro(self):
        user_registro.UserRegistro(self.usuarios_predeterminados)

    def open_edit(self):
        user_edit.UserEdit(self.usuarios_predeterminados)

    def open_delete(self):
        user_delete.UserDelete(self.usuarios_predeterminados)

    def cargar_datos(self):
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('dark-blue')
        # root
        ventana = customtkinter.CTkToplevel()
        ventana.grab_set()
        ventana.title("Menú Usuarios")
        ventana.geometry("1000x300")

        # buttons

        return ventana

    def frame1(self, ventana):
        frame = customtkinter.CTkFrame(master=ventana)
        frame.pack(pady=10, padx=60, fill='both', ipady=60)
        return frame

    def labels_parte1(self, frame):
        lb_inbreso = customtkinter.CTkLabel(master=frame, text='Menú Usuarios',
                                            font=("Times New Roman", 50, "bold"))
        lb_inbreso.pack(pady=400, padx=400, )
        lb_inbreso.place(x=10, y=0)

        button_registro = customtkinter.CTkButton(master=frame, text="Registrar", fg_color=color, height=100, width=210,
                                                  command=self.open_registro)
        button_registro.pack(pady=100, padx=10)
        button_registro.place(x=10, y=100)

        button_usuarios = customtkinter.CTkButton(master=frame, text="Ver Usuarios", fg_color=color, height=100, width=210,
                                                 command=self.open_ver)
        button_usuarios.pack(pady=100, padx=10)
        button_usuarios.place(x=225, y=100)

        button_editar = customtkinter.CTkButton(master=frame, text="Actualizar", fg_color=color, height=100, width=210,
                                                command=self.open_edit)
        button_editar.pack(pady=100, padx=10)
        button_editar.place(x=440, y=100)

        button_deshabilitar = customtkinter.CTkButton(master=frame, text="Eliminar", fg_color=color, height=100, width=210,
                                                  command=self.open_delete)
        button_deshabilitar.pack(pady=100, padx=10)
        button_deshabilitar.place(x=655, y=100)
