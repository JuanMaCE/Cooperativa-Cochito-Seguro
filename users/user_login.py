import customtkinter
from CTkMessagebox import CTkMessagebox
from users import user_window


class Login:
    def __init__(self):
        self.ventana = self.cargar_datos()
        self.frame = self.frame1(self.ventana)
        self.input_password = customtkinter.CTkEntry(master=self.frame, show='*', width=600)
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
        lb_inbreso = customtkinter.CTkLabel(master=frame, text='Iniciar Sesión',
                                            font=("Times New Roman", 50, "bold"))
        lb_inbreso.pack(pady=400, padx=400, )
        lb_inbreso.place(x=10, y=0)

        lb_name = customtkinter.CTkLabel(master=frame, text='Nombre:',
                                         font=("Times New Roman", 15, "bold"))
        lb_name.pack(pady=400, padx=400, )
        lb_name.place(x=10, y=60)

        self.input_name = customtkinter.CTkEntry(master=frame, placeholder_text="Nombre Completo", width=600)
        self.input_name.pack(padx=40, pady=40)
        self.input_name.place(x=80, y=60)

        lb_password = customtkinter.CTkLabel(master=frame, text='Contraseña:',
                                          font=("Times New Roman", 15, "bold"))
        lb_password.pack(pady=400, padx=400, )
        lb_password.place(x=10, y=100)

        self.input_password.place(x=100, y=100)

        switch_password = customtkinter.CTkCheckBox(master=frame, text="Mostrar", command=self.show_password)
        switch_password.pack(padx=20, pady=10)
        switch_password.place(x=10, y=140)

        bt_registrar = customtkinter.CTkButton(master=frame, text='Log In', command=self.login)
        bt_registrar.pack(padx=20, pady=10)
        bt_registrar.place(x=700, y=220)

    def show_password(self):
        if self.input_password.cget('show') == '':
            self.input_password.configure(show='*')
        else:
            self.input_password.configure(show='')

    def login(self):
        name = self.input_name.get()
        password = self.input_password.get()
        if name == '':
            if password == '+':
                user_window.main()
            else:
                CTkMessagebox(title='Advertencia', message='Contraseña Incorrecta')
        else:
            CTkMessagebox(title='Advertencia', message='No se Encuentra el Usuario')


