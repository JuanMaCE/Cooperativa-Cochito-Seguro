import customtkinter


class ShowUser:
    def __init__(self, user):
        self.ventana = self.cargar_datos()
        self.frame = self.frame1(self.ventana)
        self.user = user
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
        ventana.title("Usuarios Existentes")
        ventana.geometry("1000x300")

        # buttons

        return ventana

    def frame1(self, ventana):
        frame = customtkinter.CTkFrame(master=ventana)
        frame.pack(pady=10, padx=60, fill='both', ipady=60)
        return frame

    def labels_parte1(self, frame):
        lb_inbreso = customtkinter.CTkLabel(master=frame, text='Usuarios Registrados',
                                            font=("Times New Roman", 50, "bold"))
        lb_inbreso.pack(pady=400, padx=400, )
        lb_inbreso.place(x=10, y=0)

        lb_titulo = customtkinter.CTkLabel(master=frame, text='Código | Datos del Usuario', font=('Times New Roman', 15, 'bold'))
        lb_titulo.pack(pady=400, padx=400)
        lb_titulo.place(x=10, y=50)

        t = 70
        for x in self.user:
            lb_ver = customtkinter.CTkLabel(master=frame, text=x,
                                                font=("Times New Roman", 15))
            lb_ver.pack(pady=400, padx=400, )
            lb_ver.place(x=10, y=t)
            t += 30
