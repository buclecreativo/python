import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Librería necesaria para archivos .jpg y redimensionamiento

# ---------------------------------------------------------
# VARIABLES GLOBALES Y CONFIGURACIÓN DE COLORES
# ---------------------------------------------------------
COLOR_FONDO = "#f0f4f8"
COLOR_PRIMARIO = "#2c3e50"
COLOR_BOTON = "#3498db"
COLOR_BOTON_HOVER = "#2980b9"
COLOR_TEXTO_BOTON = "white"

# Variables globales para mantener la referencia de las imágenes y evitar que desaparezcan
foto_picaflor = None
foto_delfin = None

# ---------------------------------------------------------
# FUNCIONES DE LÓGICA (PROGRAMACIÓN ESTRUCTURADA)
# ---------------------------------------------------------

def mostrar_ayuda(tema):
    """Muestra una ventana informativa sobre el componente seleccionado."""
    mensajes = {
        "label": "Aquí usamos 'picaflor.jpg' dentro de un Label. Los Labels son ideales para fotos decorativas que no requieren clics.",
        "button": "Aquí usamos 'delfin.png' dentro de un Button. Al hacer clic en el delfín, se ejecuta una función.",
        "picaflor": "Este es un archivo JPEG manejado con la librería PIL.",
        "delfin": "Este es un archivo PNG con transparencia aplicado a un botón interactivo."
    }
    messagebox.showinfo("Concepto Educativo", mensajes.get(tema, "Información no disponible"))

def al_entrar_boton(event):
    """Cambia el color del botón cuando el mouse está encima."""
    event.widget.config(bg=COLOR_BOTON_HOVER)

def al_salir_boton(event):
    """Restaura el color original del botón cuando el mouse se retira."""
    event.widget.config(bg=COLOR_BOTON)

def accion_delfin():
    """Función que se ejecuta al presionar el botón del delfín."""
    messagebox.showinfo("Interacción", "¡Has hecho clic en la imagen del delfín!")

def cargar_recursos():
    """Carga y procesa las imágenes de forma segura."""
    global foto_picaflor, foto_delfin
    try:
        # Procesamiento del Picaflor (JPG)
        img_p = Image.open("picaflor.jpg")
        img_p = img_p.resize((200, 150), Image.Resampling.LANCZOS) # Ajustamos tamaño
        foto_picaflor = ImageTk.PhotoImage(img_p)

        # Procesamiento del Delfín (PNG)
        img_d = Image.open("delfin.png")
        img_d = img_d.resize((100, 100), Image.Resampling.LANCZOS) # Ajustamos tamaño
        foto_delfin = ImageTk.PhotoImage(img_d)
        return True
    except Exception as e:
        print(f"Error al cargar imágenes: {e}")
        return False

# ---------------------------------------------------------
# CONSTRUCCIÓN DE LA INTERFAZ
# ---------------------------------------------------------

def crear_aplicación():
    ventana = tk.Tk()
    ventana.title("Aprendiendo Imágenes: Picaflor y Delfín")
    
    # Dimensiones y centrado
    ancho_v, alto_v = 750, 600
    pos_x = (ventana.winfo_screenwidth() // 2) - (ancho_v // 2)
    pos_y = (ventana.winfo_screenheight() // 2) - (alto_v // 2)
    ventana.geometry(f"{ancho_v}x{alto_v}+{pos_x}+{pos_y}")
    ventana.configure(bg=COLOR_FONDO)

    # Título principal
    tk.Label(
        ventana, text="Uso de Imágenes Reales en Tkinter", 
        font=("Helvetica", 20, "bold"), bg=COLOR_FONDO, fg=COLOR_PRIMARIO, pady=20
    ).pack()

    # Intentar cargar las imágenes
    imagenes_listas = cargar_recursos()

    # Contenedor principal para los ejemplos
    frame_principal = tk.Frame(ventana, bg=COLOR_FONDO)
    frame_principal.pack(expand=True, fill="both", padx=20)

    # --- SECCIÓN IZQUIERDA: LABEL (PICAFLOR) ---
    col_izq = tk.Frame(frame_principal, bg=COLOR_FONDO)
    col_izq.pack(side="left", expand=True)

    tk.Label(col_izq, text="Imagen en Label (JPG)", font=("Arial", 12, "bold"), bg=COLOR_FONDO).pack(pady=5)
    
    if imagenes_listas:
        lbl_img = tk.Label(col_izq, image=foto_picaflor, bg=COLOR_FONDO, relief="groove", borderwidth=2)
        lbl_img.pack(pady=10)
    else:
        tk.Label(col_izq, text="[Archivo picaflor.jpg no encontrado]", fg="red", bg=COLOR_FONDO).pack(pady=20)

    btn_help_p = tk.Button(col_izq, text="¿Cómo se carga el picaflor?", command=lambda: mostrar_ayuda("picaflor"),
                           bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON, relief="flat", padx=10, cursor="hand2")
    btn_help_p.pack(pady=5)
    btn_help_p.bind("<Enter>", al_entrar_boton)
    btn_help_p.bind("<Leave>", al_salir_boton)

    # --- SECCIÓN DERECHA: BUTTON (DELFÍN) ---
    col_der = tk.Frame(frame_principal, bg=COLOR_FONDO)
    col_der.pack(side="right", expand=True)

    tk.Label(col_der, text="Imagen en Button (PNG)", font=("Arial", 12, "bold"), bg=COLOR_FONDO).pack(pady=5)

    if imagenes_listas:
        btn_img = tk.Button(col_der, image=foto_delfin, command=accion_delfin, 
                            bg="#ffffff", activebackground="#e1e1e1", relief="raised", cursor="hand2")
        btn_img.pack(pady=10)
    else:
        tk.Label(col_der, text="[Archivo delfin.png no encontrado]", fg="red", bg=COLOR_FONDO).pack(pady=20)

    btn_help_d = tk.Button(col_der, text="¿Cómo funciona el delfín?", command=lambda: mostrar_ayuda("delfin"),
                           bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON, relief="flat", padx=10, cursor="hand2")
    btn_help_d.pack(pady=5)
    btn_help_d.bind("<Enter>", al_entrar_boton)
    btn_help_d.bind("<Leave>", al_salir_boton)

    # Instrucciones finales en el pie
    instrucciones = "Recuerda: Para usar JPG necesitas instalar Pillow con 'pip install Pillow'."
    tk.Label(ventana, text=instrucciones, font=("Arial", 9, "italic"), 
             bg=COLOR_FONDO, fg="#7f8c8d", pady=20).pack(side="bottom")

    ventana.mainloop()

if __name__ == "__main__":
    crear_aplicación()