import customtkinter
from CTkMessagebox import CTkMessagebox

global texto_imagen
global asociado_a_cambiar


def main(lista):
    ventana = cargar_datos()
    frame_1 = frame(ventana)
    labels_parte1(frame_1)
    color = "#3E4446"
    # IB
    ib_id = customtkinter.CTkEntry(master=frame_1, placeholder_text='Ingrese Codigo')
    ib_id.pack(pady=12, padx=10)
    ib_id.place(x=330, y=65)
    posicion_a_editar = 0

    def buscar():
        id_a_buscar = ib_id.get()
        contador = 0
        for dato in lista:
            if id_a_buscar == dato.devolver_id():
                global asociado_a_cambiar
                asociado_a_cambiar = dato
                posicion_a_editar = contador
                break
            contador += 1

        def eliminar():
            eliminado = lista.delete_at(posicion_a_editar)
            CTkMessagebox(title='APROBADO', message='SE ELIMINO CORRECTAMENTE A ' + str(eliminado))

        button_deleate = customtkinter.CTkButton(master=frame_1, text="Eliminar", fg_color=color, width=180, height=45,
                                                 command=eliminar)
        button_deleate.pack(pady=100, padx=10)
        button_deleate.place(x=10, y=150)

    button_busqueda = customtkinter.CTkButton(master=frame_1, text="Buscar", fg_color=color, width=180, height=45
                                              , command=buscar)
    button_busqueda.pack(pady=100, padx=10)
    button_busqueda.place(x=10, y=100)

    return


def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Edicicion de asociados")
    ventana.geometry('950x200')
    return ventana


def frame(ventana):
    frame_ = customtkinter.CTkFrame(master=ventana)
    frame_.pack(pady=0, padx=60, fill='both', ipady=80)
    return frame_


def labels_parte1(frame_u):
    lb_inbreso = customtkinter.CTkLabel(master=frame_u, text='Eliminación asociados',
                                        font=("Times New Roman", 50, "bold"))
    lb_inbreso.pack(pady=400, padx=400)
    lb_inbreso.place(x=10, y=0)

    lb_tipo = customtkinter.CTkLabel(master=frame_u, text='Ingrese el ID de asociado', font=("Times New Roman", 30))
    lb_tipo.pack(pady=400, padx=400)
    lb_tipo.place(x=10, y=60)

