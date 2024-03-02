import customtkinter


class frame():
    def __init__(self, ventana):
        self.ventana = ventana

    def frame1(ventana):
        frame = customtkinter.CTkFrame(master=ventana)
        frame.pack(pady=10, padx=60, fill='both', ipady=60)
        return frame
