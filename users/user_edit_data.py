import random

from CTkMessagebox import CTkMessagebox

from data_estructure.list.list import List
import customtkinter
from users.user import User


class EditData:
    def __init__(self, usuarios_pred):
        self.ventana = self.cargar_datos()
        self.frame2 = self.frame_2(self.ventana)
        self.frame = self.frame1(self.ventana)
        self.usuarios_pred = usuarios_pred
        self.input_password = customtkinter.CTkEntry(master=self.frame, show='*', width=600)
        self.labels_parte1(self.frame, self.frame2)
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
        frame.pack(pady=0, padx=60, fill='both', ipady=80)
        return frame

    def frame_2(self, ventana):
        frame = customtkinter.CTkFrame(master=ventana)
        frame.pack(pady=10, padx=60, fill='both', ipady=0)

        return frame

    def labels_parte1(self, frame, frame2):
        lb_inbreso = customtkinter.CTkLabel(master=frame2, text='Actualizar Contraseña',
                                            font=("Times New Roman", 50, "bold"))
        lb_inbreso.pack(pady=400, padx=400, )
        lb_inbreso.place(x=10, y=0)

        lb_id = customtkinter.CTkLabel(master=frame2, text='Ingresar ID:',
                                       font=("Times New Roman", 15, "bold"))
        lb_id.pack(pady=400, padx=400, )
        lb_id.place(x=10, y=60)

        self.input_id = customtkinter.CTkEntry(master=frame2, placeholder_text="Codigo de Usuario", width=600)
        self.input_id.pack(padx=40, pady=40)
        self.input_id.place(x=120, y=60)

        bt_search = customtkinter.CTkButton(master=frame2, text='Buscar', command=self.search)
        bt_search.pack(padx=20, pady=10)
        bt_search.place(x=10, y=100)

        lb_name = customtkinter.CTkLabel(master=frame, text='Nombre:',
                                         font=("Times New Roman", 15, "bold"))
        lb_name.pack(pady=400, padx=400, )
        lb_name.place(x=10, y=60)

        self.input_name = customtkinter.CTkEntry(master=frame, placeholder_text="", width=600)
        self.input_name.pack(padx=40, pady=40)
        self.input_name.place(x=80, y=60)

        lb_email = customtkinter.CTkLabel(master=frame, text='Email:',
                                         font=("Times New Roman", 15, "bold"))
        lb_email.pack(pady=400, padx=400, )
        lb_email.place(x=10, y=100)

        self.input_email = customtkinter.CTkEntry(master=frame, placeholder_text="", width=600)
        self.input_email.pack(padx=40, pady=40)
        self.input_email.place(x=80, y=100)

        lb_password = customtkinter.CTkLabel(master=frame, text='Contraseña:',
                                          font=("Times New Roman", 15, "bold"))
        lb_password.pack(pady=400, padx=400, )
        lb_password.place(x=10, y=140)

        self.input_password.place(x=100, y=140)

        switch_password = customtkinter.CTkCheckBox(master=frame, text="Mostrar", command=self.show_password)
        switch_password.pack(padx=20, pady=10)
        switch_password.place(x=10, y=180)

        lb_puesto = customtkinter.CTkLabel(master=frame, text='Puesto:',
                                          font=("Times New Roman", 15, "bold"))
        lb_puesto.pack(pady=400, padx=400, )
        lb_puesto.place(x=10, y=220)

        self.input_puesto = customtkinter.CTkEntry(master=frame, placeholder_text="", width=600)
        self.input_puesto.pack(padx=40, pady=40)
        self.input_puesto.place(x=80, y=220)

        bt_registrar = customtkinter.CTkButton(master=frame, text='Actualizar', command=self.actualizar)
        bt_registrar.pack(padx=20, pady=10)
        bt_registrar.place(x=700, y=220)

    def show_password(self):
        if self.input_password.cget('show') == '':
            self.input_password.configure(show='*')
        else:
            self.input_password.configure(show='')

    def search(self):
        id = int(self.input_id.get())
        self.usuario_buscado = None
        for x in self.usuarios_pred:
            if id == x.codigo:
                self.usuario_buscado = x
                self.input_name.configure(placeholder_text=str(x.name))
                self.input_email.configure(placeholder_text=str(x.email))
                self.input_puesto.configure(placeholder_text=str(x.puesto))

    def actualizar(self):
        password = self.input_password.get()
        if password == self.usuario_buscado.password:
            name = self.input_name.get()
            email = self.input_email.get()
            puesto = self.input_puesto.get()
            self.usuario_buscado.name = name
            self.usuario_buscado.email = email
            self.usuario_buscado.puesto = puesto
            CTkMessagebox(title='', message='Realizado Correctamente')
        else:
            CTkMessagebox(title='', message='Contraseña Incorrecta')
