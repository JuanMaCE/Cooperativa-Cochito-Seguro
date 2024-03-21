import os.path
import customtkinter
from tkinter import filedialog
import shutil
import os
global texto_imagen
from data_estructure.circular_list.circular_list import CircularList
from gestion_asociados.datos_asociados.asociado import Asociado
global asociado_a_cambiar


def main(lista: CircularList):
    ventana = cargar_datos()
    frame2 = frame1(ventana)
    frame = frame_2(ventana)
    color = "#3E4446"
    labels_parte1(frame, frame2)
    posicion_a_editar = 0

    # IB
    ib_id = customtkinter.CTkEntry(master=frame2, placeholder_text='Ingrese Codigo')
    ib_id.pack(pady=12, padx=10)
    ib_id.place(x=330, y=65)

    # buscar entre la lista
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
        ib_name = customtkinter.CTkEntry(master=frame, placeholder_text=str(asociado_a_cambiar.devolver_nomre()),
                                         width=400,
                                         height=35)
        ib_name.pack(pady=100, padx=10)
        ib_name.place(x=130, y=23)
        ib_direccion = customtkinter.CTkEntry(master=frame,
                                              placeholder_text=str(asociado_a_cambiar.devolver_direccion()),
                                              width=580,
                                              height=35)
        ib_direccion.pack(pady=100, padx=10)
        ib_direccion.place(x=230, y=66)

        ib_tel = customtkinter.CTkEntry(master=frame, placeholder_text=str(asociado_a_cambiar.devolver_telefono()))
        ib_tel.pack(pady=100, padx=10)
        ib_tel.place(x=75, y=113)

        ib_num_dpi = customtkinter.CTkEntry(master=frame, placeholder_text=str(asociado_a_cambiar.devolver_dpi()),
                                            width=180, height=35)
        ib_num_dpi.pack(pady=100, padx=10)
        ib_num_dpi.place(x=300, y=113)

        ib_nit = customtkinter.CTkEntry(master=frame, placeholder_text=str(asociado_a_cambiar.devolver_nit()),
                                        width=180,
                                        height=35)
        ib_nit.pack(pady=100, padx=10)
        ib_nit.place(x=580, y=110)

        ib_ref_personales = customtkinter.CTkEntry(master=frame,
                                                   placeholder_text="str(asociado_a_cambiar.referencias_personales())",
                                                   width=400)
        ib_ref_personales.pack(pady=100, padx=10)
        ib_ref_personales.place(x=210, y=210)

        cb_busqueda = customtkinter.CTkComboBox(master=frame, font=("Times New Roman", 20),
                                                values=['Recibo De Luz', 'Telefono', 'Estados de cuenta'], width=200)
        cb_busqueda.pack(pady=400, padx=400, )
        cb_busqueda.place(x=150, y=160)

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
                texto_alrevez += texto_final[-i - 1]
            texto_final_alrevez = ""
            for i in range(len(texto_alrevez)):
                if texto_alrevez[i] == "/":
                    break
                texto_final_alrevez += texto_alrevez[i]
            texto_image = ""
            for i in range(len(texto_final_alrevez)):
                texto_image += texto_final_alrevez[-i - 1]
            global texto_imagen
            texto_imagen = texto_image

        # botones

        button_select_img = customtkinter.CTkButton(master=frame, text="Seleccionar", fg_color=color,
                                                    command=seleccionar_imagen)
        button_select_img.pack(pady=100, padx=10)
        button_select_img.place(x=630, y=167)
        ventana.geometry('950x530')

        def cambiar_datos():
            name = ib_name.get()
            adress = ib_direccion.get()
            phone = ib_tel.get()
            dpi = ib_num_dpi.get()
            nit = ib_nit.get()
            referencias = ib_ref_personales.get()
            asociado = Asociado(name, adress, phone, dpi, nit, referencias)
            print("se elimino:  ", lista.delete_at(posicion_a_editar))
            asociado.cambiar_codigo(ib_id.get())
            lista.insert_at(asociado, posicion_a_editar)

        # confirmación
        button_confirm_2 = customtkinter.CTkButton(master=frame, text="Confirmar", fg_color=color, width=180, height=45
                                                   , command=cambiar_datos)
        button_confirm_2.pack(pady=100, padx=10)
        button_confirm_2.place(x=630, y=200)

    button_busqueda = customtkinter.CTkButton(master=frame2, text="Confirmar", fg_color=color, width=180, height=45,
                                              command=buscar)
    button_busqueda.pack(pady=100, padx=10)
    button_busqueda.place(x=10, y=100)

    ventana.mainloop()

    return


def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Edicicion de asociados")
    ventana.geometry('950x220')
    return ventana


def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=60, fill='both', ipady=0)
    return frame


def frame_2(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=0, padx=60, fill='both', ipady=80)
    return frame


def labels_parte1(frame, frame2):

    lb_inbreso = customtkinter.CTkLabel(master=frame2, text='Edicion asociados',
                                        font=("Times New Roman", 50, "bold"))
    lb_inbreso.pack(pady=400, padx=400)
    lb_inbreso.place(x=10, y=0)

    lb_tipo = customtkinter.CTkLabel(master=frame2, text='Ingrese el ID de asociado', font=("Times New Roman", 30))
    lb_tipo.pack(pady=400, padx=400)
    lb_tipo.place(x=10, y=60)

    lb_nombre = customtkinter.CTkLabel(master=frame, text='Nombre', font=("Times New Roman", 30))
    lb_nombre.pack(pady=400, padx=400)
    lb_nombre.place(x=10, y=20)

    lb_direccion_actual = customtkinter.CTkLabel(master=frame, text='Dirección Actual', font=("Times New Roman", 30))
    lb_direccion_actual.pack(pady=400, padx=400)
    lb_direccion_actual.place(x=10, y=65)

    lb_telefonos = customtkinter.CTkLabel(master=frame, text='Tel.', font=("Times New Roman", 30))
    lb_telefonos.pack(pady=400, padx=400)
    lb_telefonos.place(x=10, y=110)

    lb_dpi = customtkinter.CTkLabel(master=frame, text='DPI', font=("Times New Roman", 30))
    lb_dpi.pack(pady=400, padx=400)
    lb_dpi.place(x=240, y=113)

    lb_select_img = customtkinter.CTkLabel(master=frame, text='Seleccionar Imagen', font=("Times New Roman", 30))
    lb_select_img.pack(pady=400, padx=400)
    lb_select_img.place(x=370, y=160)

    lb_nit = customtkinter.CTkLabel(master=frame, text='NIT', font=("Times New Roman", 30))
    lb_nit.pack(pady=400, padx=400)
    lb_nit.place(x=512, y=110)

    lb_ref_personales = customtkinter.CTkLabel(master=frame, text='Ref. Personales', font=("Times New Roman", 30))
    lb_ref_personales.pack(pady=400, padx=400)
    lb_ref_personales.place(x=10, y=205)

    lb_tipo = customtkinter.CTkLabel(master=frame, text='Tipo Doc.', font=("Times New Roman", 30))
    lb_tipo.pack(pady=400, padx=400)
    lb_tipo.place(x=10, y=160)
