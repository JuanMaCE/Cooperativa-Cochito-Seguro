import customtkinter
from gestion_asociados import menu_gestion_asociados
from gestion_prestamo import menu_prestamos
from users import user_login
from users.user import User
from data_estructure.list.list import List

user_pred = List[User]()
app = customtkinter.CTk()


def usuarios_predeterminados():
    user_pred.append(User(12345, 'Juan', 'juanmc228@gmail.com', 'Admin123', 'Administrador'))
    user_pred.append(User(54321, 'Roger', 'rogcl228@gmail.com', 'Admin123', 'Administrador'))
    user_pred.append(User(56789, 'Vyn', 'vynla228@gmail.com', 'Admin123', 'Administrador'))
    user_pred.append(User(98765, 'Chat', 'chatman228@gmail.com', 'Admin123', 'Administrador'))


def open_gestion():
    menu_gestion_asociados.main()

def open_prestamos():
    menu_prestamos.main()

def open_users():
    usuarios_predeterminados()
    user_login.Login(user_pred)


def main_window():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    app.title("MENU")
    app.geometry("1000x500")
    app.wm_attributes("-topmost", False)
    frame = customtkinter.CTkFrame(master=app)
    frame.pack(pady=10, padx=10, fill='both', expand=True)
    buttons(frame)
    # botones
    app.mainloop()


def buttons(frame):
    button_gestion = customtkinter.CTkButton(master=frame, text='Gestión de Asociados', height=100, width=150,
                                         font=("Arial", 20), fg_color="#3E4446", command=lambda: open_gestion())

    button_gestion.pack(pady=10, padx=10)
    button_gestion.place(x=50, y=10)

    bt_prestamos_bancarios = customtkinter.CTkButton(master=frame, text='Prestamos bancarios', height=100, width=160,
                                                     font=("Arial", 20), fg_color="#3E4446", command=lambda: open_prestamos())

    bt_prestamos_bancarios.pack(pady=10, padx=10)
    bt_prestamos_bancarios.place(x=50, y=150)

    bt_usuarios = customtkinter.CTkButton(master=frame, text='Usuarios', height=100, width=210,
                                          font=("Arial", 20), fg_color="#3E4446", command=lambda: open_users())

    bt_usuarios.pack(pady=10, padx=10)
    bt_usuarios.place(x=50, y=310)


main_window()
