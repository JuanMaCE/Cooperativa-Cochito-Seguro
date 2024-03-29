import customtkinter
from gestion_asociados import menu_gestion_asociados
from users import user_login
from data_estructure.list.list import List
from gestion_prestamo import menu_prestamos

app = customtkinter.CTk()


def open_gestion(list_asociaods):
    menu_gestion_asociados.main(list_asociaods)


def open_users(user_pred):
    user_login.Login(user_pred)


def open_prestamo(asociados):
    menu_prestamos.main(asociados)


def main_window(list_usuarios, list_asociaods):
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    app.title("MENU")
    app.geometry("1000x500")
    app.wm_attributes("-topmost", False)
    frame = customtkinter.CTkFrame(master=app)
    frame.pack(pady=10, padx=10, fill='both', expand=True)
    buttons(frame, list_usuarios, list_asociaods)

    # botones
    app.mainloop()


def buttons(frame, list_usuarios, list_asociaods):
    button_gestion = customtkinter.CTkButton(master=frame, text='Gestión de Asociados', height=100, width=150,
                                             font=("Arial", 20), fg_color="#3E4446",
                                             command=lambda: open_gestion(list_asociaods))

    button_gestion.pack(pady=10, padx=10)
    button_gestion.place(x=50, y=10)

    bt_prestamos_bancarios = customtkinter.CTkButton(master=frame, text='Prestamos bancarios', height=100, width=160,
                                                     font=("Arial", 20), fg_color="#3E4446",
                                                     command=lambda: open_prestamo(list_asociaods))

    bt_prestamos_bancarios.pack(pady=10, padx=10)
    bt_prestamos_bancarios.place(x=50, y=150)

    bt_usuarios = customtkinter.CTkButton(master=frame, text='Usuarios', height=100, width=210,
                                          font=("Arial", 20), fg_color="#3E4446",
                                          command=lambda: open_users(list_usuarios))

    bt_usuarios.pack(pady=10, padx=10)
    bt_usuarios.place(x=50, y=310)


