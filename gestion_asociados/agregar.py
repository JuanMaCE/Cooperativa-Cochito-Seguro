import os.path
import customtkinter
from tkinter import filedialog
import shutil
import os
global texto_imagen


def main():
    ventana = cargar_datos()
    frame = frame1(ventana)
    color = "#3E4446"
    labels_parte1(frame)

    # IB
    ib_id = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese Codigo')
    ib_id.pack(pady=12, padx=10)
    ib_id.place(x=110, y=67)

    ib_name = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese Nombre del producto', width=400,
                                     height=35)
    ib_name.pack(pady=100, padx=10)
    ib_name.place(x=410, y=63)
    ib_direccion = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese su dirección actual', width=580,
                                          height=35)
    ib_direccion.pack(pady=100, padx=10)
    ib_direccion.place(x=230, y=106)

    ib_tel = customtkinter.CTkEntry(master=frame, placeholder_text='Ingreso Num')
    ib_tel.pack(pady=100, padx=10)
    ib_tel.place(x=75, y=153)

    ib_num_dpi = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese El DPI', width=180, height=35)
    ib_num_dpi.pack(pady=100, padx=10)
    ib_num_dpi.place(x=300, y=153)

    ib_nit = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese el NIT', width=180,
                                    height=35)
    ib_nit.pack(pady=100, padx=10)
    ib_nit.place(x=580, y=150)

    ib_ref_personales = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese referencias personales',
                                               width=400)
    ib_ref_personales.pack(pady=100, padx=10)
    ib_ref_personales.place(x=210, y=250)

    def seleccionar_imagen():
        get_image = filedialog.askopenfilenames(title="SELECT IMAGE",
                                                filetypes=(("png", "*.png"), ("jpg", "*.jpg"), ("Allfile", "*.*")))

        texto = str(get_image)
        texto_final = ""
        for i in range(2, len(texto) - 3):
            texto_final += texto[i]
        print(texto_final)
        ruta_imagen_origen = str(texto_final)
        ruta_carpeta_destino = 'imagenes'
        if not os.path.exists(ruta_carpeta_destino):
            os.makedirs(ruta_carpeta_destino)

        shutil.copy(ruta_imagen_origen, ruta_carpeta_destino)
        texto_alrevez = ""
        for i in range(len(texto_final)):
            texto_alrevez += texto_final[-i-1]
        texto_final_alrevez = ""
        for i in range(len(texto_alrevez)):
            if texto_alrevez[i] == "/":
                break
            texto_final_alrevez += texto_alrevez[i]
        texto_image = ""
        for i in range(len(texto_final_alrevez)):
            texto_image += texto_final_alrevez[-i-1]
        global texto_imagen
        texto_imagen = texto_image

    # botones

    button_select_img = customtkinter.CTkButton(master=frame, text="Seleccionar", fg_color=color,
                                                command=seleccionar_imagen)
    button_select_img.pack(pady=100, padx=10)
    button_select_img.place(x=260, y=207)

    # confirmación
    button_confirm_1 = customtkinter.CTkButton(master=frame, text="Confirmar", fg_color=color, width=180, height=45)
    button_confirm_1.pack(pady=100, padx=10)
    button_confirm_1.place(x=630, y=240)
    ventana.mainloop()

    return


def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Registro de nuevos asociados")
    ventana.geometry('950x350')
    return ventana


def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=60, fill='both', ipady=60)
    return frame


def labels_parte1(frame):

    lb_inbreso = customtkinter.CTkLabel(master=frame, text='Registro de nuevos asociados',
                                        font=("Times New Roman", 50, "bold"))
    lb_inbreso.pack(pady=400, padx=400, )
    lb_inbreso.place(x=10, y=0)

    lb_id = customtkinter.CTkLabel(master=frame, text='Codigo', font=("Times New Roman", 30))
    lb_id.pack(pady=400, padx=400, )
    lb_id.place(x=10, y=60)

    lb_nombre = customtkinter.CTkLabel(master=frame, text='Nombre', font=("Times New Roman", 30))
    lb_nombre.pack(pady=400, padx=400)
    lb_nombre.place(x=290, y=60)

    lb_direccion_actual = customtkinter.CTkLabel(master=frame, text='Dirección Actual', font=("Times New Roman", 30))
    lb_direccion_actual.pack(pady=400, padx=400)
    lb_direccion_actual.place(x=10, y=105)

    lb_telefonos = customtkinter.CTkLabel(master=frame, text='Tel.', font=("Times New Roman", 30))
    lb_telefonos.pack(pady=400, padx=400)
    lb_telefonos.place(x=10, y=150)

    lb_dpi = customtkinter.CTkLabel(master=frame, text='DPI', font=("Times New Roman", 30))
    lb_dpi.pack(pady=400, padx=400)
    lb_dpi.place(x=240, y=153)

    lb_select_img = customtkinter.CTkLabel(master=frame, text='Seleccionar Imagen', font=("Times New Roman", 30))
    lb_select_img.pack(pady=400, padx=400)
    lb_select_img.place(x=10, y=200)

    lb_nit = customtkinter.CTkLabel(master=frame, text='NIT', font=("Times New Roman", 30))
    lb_nit.pack(pady=400, padx=400)
    lb_nit.place(x=512, y=150)

    lb_ref_personales = customtkinter.CTkLabel(master=frame, text='Ref. Personales', font=("Times New Roman", 30))
    lb_ref_personales.pack(pady=400, padx=400)
    lb_ref_personales.place(x=10, y=245)
