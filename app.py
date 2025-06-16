import customtkinter as ctk

def invertir_palabras(palabra: str) -> str:
    if len(palabra) <= 1:
        return palabra
    else:
        return palabra[-1] + invertir_palabras(palabra[:-1])

def invertir_palabras_frase(frase: str) -> str:
    palabras = frase.split()
    if len(palabras) == 0:
        return ''
    else:
        return ' '.join(invertir_palabras(palabra) for palabra in palabras)

def boton_invertir():
    frase = entrada.get()
    if not frase.strip():
        etiqueta_resultado.configure(text="Por favor, escribe algo.", text_color="#FF3B30")  # rojo suave iOS
        return
    resultado = invertir_palabras_frase(frase)
    etiqueta_resultado.configure(text=resultado, text_color="#1C1C1E")  # gris oscuro texto

def boton_borrar():
    entrada.delete(0, ctk.END)
    etiqueta_resultado.configure(text="")

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("Inversor iOS Style")
ventana.geometry("420x280")
ventana.resizable(False, False)
ventana.configure(fg_color="#F9F9F9")  # blanco casi puro iOS

titulo = ctk.CTkLabel(
    ventana,
    text="Inversor de Palabras",
    font=ctk.CTkFont(family="SF Pro Text", size=28, weight="bold"),
    text_color="#1C1C1E"
)
titulo.pack(pady=(30, 15))

entrada = ctk.CTkEntry(
    ventana,
    width=360,
    height=38,
    placeholder_text="Escribe tu frase aquí...",
    font=ctk.CTkFont(family="SF Pro Text", size=16),
    corner_radius=12,
    border_width=1,
    border_color="#C0C0C0",   # borde gris suave
    fg_color="#E5E5E5",       # gris clarito para fondo de la barra
    text_color="#1C1C1E"
)

entrada.pack(pady=(0, 25))

botones_frame = ctk.CTkFrame(ventana, fg_color="transparent")
botones_frame.pack(pady=(0, 20))

boton_invertir_btn = ctk.CTkButton(
    botones_frame,
    text="Invertir",
    width=140,
    height=44,
    corner_radius=14,
    fg_color="#007AFF",  # azul iOS oficial
    hover_color="#005BBB",
    font=ctk.CTkFont(family="SF Pro Text", size=16, weight="bold"),
    command=boton_invertir
)
boton_invertir_btn.grid(row=0, column=0, padx=18)

boton_borrar_btn = ctk.CTkButton(
    botones_frame,
    text="Borrar",
    width=140,
    height=44,
    corner_radius=14,
    fg_color="#E5E5EA",  # gris iOS muy claro
    hover_color="#CACACE",
    font=ctk.CTkFont(family="SF Pro Text", size=16, weight="bold"),
    command=boton_borrar,
    text_color="#1C1C1E"
)
boton_borrar_btn.grid(row=0, column=1, padx=18)

etiqueta_resultado = ctk.CTkLabel(
    ventana,
    text="",
    wraplength=380,
    justify="center",
    font=ctk.CTkFont(family="SF Pro Text", size=18),
    text_color="#1C1C1E"
)
etiqueta_resultado.pack(pady=(0, 10))

ventana.mainloop()
