import customtkinter
global texto_imagen
from gestion_prestamo.prestamo import visualizar


def main():
    ventana = cargar_datos()
    frame_1 = frame(ventana)
    labels_parte1(frame_1)
    color = "#3E4446"

    return

def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Aprobar prestamo")
    ventana.geometry('950x195')
    return ventana


def frame(ventana):
    frame_ = customtkinter.CTkFrame(master=ventana)
    frame_.pack(pady=0, padx=60, fill='both', ipady=80)
    return frame_


def labels_parte1(frame_u):
    lb_inbreso = customtkinter.CTkLabel(master=frame_u, text='Visualizar',
                                        font=("Times New Roman", 50, "bold"))
    lb_inbreso.pack(pady=400, padx=400)
    lb_inbreso.place(x=10, y=0)

    t = 70
    lista = visualizar()

    lb_ver = customtkinter.CTkLabel(master=frame_u, text=lista,
                                    font=("Times New Roman", 15))
    lb_ver.pack(pady=400, padx=400, )
    lb_ver.place(x=10, y=50)

