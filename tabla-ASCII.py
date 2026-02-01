"""
Aplicación Educativa: Tabla ASCII Interactiva
Desarrollado para estudiantes de bachillerato
Autor: Experto en Desarrollo de Software Educativo
Descripción: Aplicación que ayuda a comprender la tabla ASCII mediante
             una interfaz interactiva con calculadora y visualizador.
"""

import tkinter as tk
from tkinter import ttk, messagebox

# ============================================
# CONFIGURACIÓN DE COLORES Y ESTILOS
# ============================================
COLOR_PRIMARIO = "#2C3E50"      # Azul oscuro
COLOR_SECUNDARIO = "#3498DB"    # Azul claro
COLOR_FONDO = "#ECF0F1"         # Gris claro
COLOR_BOTON_NORMAL = "#2980B9"  # Azul medio
COLOR_BOTON_HOVER = "#1ABC9C"   # Turquesa
COLOR_TEXTO = "#2C3E50"         # Azul oscuro
COLOR_TEXTO_CLARO = "#FFFFFF"   # Blanco
COLOR_RESALTADO = "#E74C3C"     # Rojo para resaltar

# ============================================
# FUNCIONES DE UTILIDAD
# ============================================

def crear_boton_con_hover(parent, texto, comando, fila, columna, 
                         ancho=15, alto=1, colspan=1, color_normal=COLOR_BOTON_NORMAL,
                         color_hover=COLOR_BOTON_HOVER):
    """
    Crea un botón con efecto hover (cambio de color al pasar el mouse)
    """
    boton = tk.Button(
        parent,
        text=texto,
        command=comando,
        bg=color_normal,
        fg=COLOR_TEXTO_CLARO,
        font=("Arial", 10, "bold"),
        relief="raised",
        borderwidth=2,
        width=ancho,
        height=alto,
        cursor="hand2"
    )
    
    boton.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew", columnspan=colspan)
    
    # Configurar efecto hover
    def entrar(event):
        boton.config(bg=color_hover)
    
    def salir(event):
        boton.config(bg=color_normal)
    
    boton.bind("<Enter>", entrar)
    boton.bind("<Leave>", salir)
    
    return boton

def crear_label_con_estilo(parent, texto, fila, columna, 
                          fuente=("Arial", 10), estilo="normal",
                          colspan=1, sticky="w", color_texto=COLOR_TEXTO):
    """
    Crea una etiqueta con un estilo consistente
    """
    label = tk.Label(
        parent,
        text=texto,
        bg=COLOR_FONDO,
        fg=color_texto,
        font=fuente,
        justify="left"
    )
    
    if estilo == "titulo":
        label.config(font=("Arial", 12, "bold"), fg=COLOR_PRIMARIO)
    elif estilo == "subtitulo":
        label.config(font=("Arial", 11, "bold"), fg=COLOR_SECUNDARIO)
    elif estilo == "resaltado":
        label.config(fg=COLOR_RESALTADO, font=("Arial", 10, "bold"))
    
    label.grid(row=fila, column=columna, padx=5, pady=2, sticky=sticky, columnspan=colspan)
    return label

def crear_entry_con_estilo(parent, fila, columna, ancho=20, colspan=1):
    """
    Crea un campo de entrada con estilo consistente
    """
    entry = tk.Entry(
        parent,
        width=ancho,
        font=("Arial", 10),
        relief="sunken",
        borderwidth=2,
        justify="center"
    )
    entry.grid(row=fila, column=columna, padx=5, pady=5, columnspan=colspan, sticky="ew")
    return entry

def crear_texto_con_estilo(parent, fila, columna, alto=10, ancho=40, colspan=1):
    """
    Crea un widget de texto con barras de desplazamiento
    """
    # Frame para contener el texto y la barra de desplazamiento
    frame_texto = tk.Frame(parent, bg=COLOR_FONDO)
    frame_texto.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew", columnspan=colspan)
    
    # Barra de desplazamiento vertical
    scrollbar = tk.Scrollbar(frame_texto)
    scrollbar.pack(side="right", fill="y")
    
    # Widget de texto
    texto = tk.Text(
        frame_texto,
        height=alto,
        width=ancho,
        font=("Consolas", 10),
        bg="white",
        fg=COLOR_TEXTO,
        relief="sunken",
        borderwidth=2,
        wrap="word",
        yscrollcommand=scrollbar.set
    )
    texto.pack(side="left", fill="both", expand=True)
    
    # Configurar la barra de desplazamiento
    scrollbar.config(command=texto.yview)
    
    return texto

# ============================================
# FUNCIONES DE LA CALCULADORA ASCII
# ============================================

def convertir_caracter_a_ascii():
    """
    Convierte un carácter a su valor decimal, hexadecimal y binario
    """
    entrada = entry_caracter.get()
    
    if not entrada:
        messagebox.showwarning("Entrada vacía", "Por favor, ingresa un carácter.")
        return
    
    if len(entrada) > 1:
        messagebox.showwarning("Entrada inválida", "Por favor, ingresa solo un carácter.")
        return
    
    caracter = entrada[0]
    decimal = ord(caracter)
    hexadecimal = hex(decimal)
    binario = bin(decimal)
    
    # Mostrar resultados
    texto_resultados.delete(1.0, tk.END)
    texto_resultados.insert(tk.END, f"Carácter: '{caracter}'\n")
    texto_resultados.insert(tk.END, f"Decimal: {decimal}\n")
    texto_resultados.insert(tk.END, f"Hexadecimal: {hexadecimal}\n")
    texto_resultados.insert(tk.END, f"Binario: {binario}\n")
    
    # Resaltar en la tabla
    resaltar_en_tabla_ascii(decimal)

def convertir_numero_a_caracter():
    """
    Convierte un número decimal a su carácter ASCII correspondiente
    """
    entrada = entry_numero.get()
    
    if not entrada:
        messagebox.showwarning("Entrada vacía", "Por favor, ingresa un número.")
        return
    
    try:
        numero = int(entrada)
        
        if numero < 0 or numero > 255:
            messagebox.showwarning("Número fuera de rango", 
                                  "Por favor, ingresa un número entre 0 y 255.")
            return
        
        caracter = chr(numero)
        
        # Mostrar resultados
        texto_resultados.delete(1.0, tk.END)
        texto_resultados.insert(tk.END, f"Número: {numero}\n")
        texto_resultados.insert(tk.END, f"Carácter: '{caracter}'\n")
        texto_resultados.insert(tk.END, f"Hexadecimal: {hex(numero)}\n")
        texto_resultados.insert(tk.END, f"Binario: {bin(numero)}\n")
        
        # Resaltar en la tabla
        resaltar_en_tabla_ascii(numero)
        
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor, ingresa un número válido.")

def mostrar_tabla_ascii_completa():
    """
    Muestra la tabla ASCII completa en el área de texto
    """
    texto_tabla.delete(1.0, tk.END)
    
    # Encabezado
    texto_tabla.insert(tk.END, "="*60 + "\n")
    texto_tabla.insert(tk.END, "TABLA ASCII COMPLETA (0-127)\n")
    texto_tabla.insert(tk.END, "="*60 + "\n\n")
    
    texto_tabla.insert(tk.END, "Dec  Hex  Bin        Carácter       Descripción\n")
    texto_tabla.insert(tk.END, "-"*60 + "\n")
    
    # Generar la tabla
    for i in range(0, 128):
        # Solo mostrar caracteres imprimibles, los no imprimibles se muestran con descripción
        if i < 32 or i == 127:
            # Caracteres de control
            caracter = "[Ctrl]"
            descripcion = obtener_descripcion_caracter_control(i)
        else:
            caracter = chr(i)
            descripcion = ""
        
        # Formatear la línea
        linea = f"{i:3d}  {hex(i)[2:].upper():>3s}  {bin(i)[2:]:>8s}  "
        linea += f"     '{caracter}'       {descripcion}\n"
        
        texto_tabla.insert(tk.END, linea)
        
        # Separador cada 32 caracteres
        if (i + 1) % 32 == 0 and i < 127:
            texto_tabla.insert(tk.END, "-"*60 + "\n")

def obtener_descripcion_caracter_control(codigo):
    """
    Devuelve la descripción de los caracteres de control ASCII
    """
    descripciones = {
        0: "NUL (null)",
        1: "SOH (start of heading)",
        2: "STX (start of text)",
        3: "ETX (end of text)",
        4: "EOT (end of transmission)",
        5: "ENQ (enquiry)",
        6: "ACK (acknowledge)",
        7: "BEL (bell)",
        8: "BS  (backspace)",
        9: "TAB (horizontal tab)",
        10: "LF  (line feed, new line)",
        11: "VT  (vertical tab)",
        12: "FF  (form feed, new page)",
        13: "CR  (carriage return)",
        14: "SO  (shift out)",
        15: "SI  (shift in)",
        16: "DLE (data link escape)",
        17: "DC1 (device control 1)",
        18: "DC2 (device control 2)",
        19: "DC3 (device control 3)",
        20: "DC4 (device control 4)",
        21: "NAK (negative acknowledge)",
        22: "SYN (synchronous idle)",
        23: "ETB (end of trans. block)",
        24: "CAN (cancel)",
        25: "EM  (end of medium)",
        26: "SUB (substitute)",
        27: "ESC (escape)",
        28: "FS  (file separator)",
        29: "GS  (group separator)",
        30: "RS  (record separator)",
        31: "US  (unit separator)",
        127: "DEL (delete)"
    }
    
    return descripciones.get(codigo, "")

def resaltar_en_tabla_ascii(codigo):
    """
    Resalta un código específico en la tabla ASCII
    """
    # Primero, mostrar la tabla completa
    mostrar_tabla_ascii_completa()
    
    # Encontrar la línea correspondiente al código
    contenido = texto_tabla.get(1.0, tk.END)
    lineas = contenido.split('\n')
    
    for i, linea in enumerate(lineas):
        if linea.startswith(f"{codigo:3d}"):
            # Calcular la posición de inicio de la línea
            inicio = f"1.{sum(len(l) + 1 for l in lineas[:i])}"
            fin = f"{inicio}+{len(linea)}c"
            
            # Resaltar la línea
            texto_tabla.tag_add("resaltado", inicio, fin)
            texto_tabla.tag_config("resaltado", background="#FFF3CD", foreground="#856404")
            
            # Hacer scroll para que la línea sea visible
            texto_tabla.see(inicio)
            break

def mostrar_informacion_ascii():
    """
    Muestra información educativa sobre la tabla ASCII
    """
    info_ventana = tk.Toplevel(ventana_principal)
    info_ventana.title("Información sobre ASCII")
    info_ventana.geometry("600x500")
    info_ventana.configure(bg=COLOR_FONDO)
    info_ventana.resizable(False, False)
    
    # Centrar la ventana
    info_ventana.update_idletasks()
    ancho = info_ventana.winfo_width()
    alto = info_ventana.winfo_height()
    x = (info_ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (info_ventana.winfo_screenheight() // 2) - (alto // 2)
    info_ventana.geometry(f'{ancho}x{alto}+{x}+{y}')
    
    # Frame principal
    frame_info = tk.Frame(info_ventana, bg=COLOR_FONDO)
    frame_info.pack(fill="both", expand=True, padx=20, pady=20)
    
    # Título
    titulo = crear_label_con_estilo(frame_info, "¿Qué es la tabla ASCII?", 0, 0, 
                                   estilo="titulo", colspan=2)
    
    # Contenido informativo
    info_texto = tk.Text(
        frame_info,
        height=20,
        width=70,
        font=("Arial", 10),
        bg="white",
        fg=COLOR_TEXTO,
        relief="flat",
        wrap="word",
        padx=10,
        pady=10
    )
    info_texto.grid(row=1, column=0, columnspan=2, pady=10, sticky="nsew")
    
    # Configurar columnas para expansión
    frame_info.columnconfigure(0, weight=1)
    frame_info.columnconfigure(1, weight=1)
    
    # Insertar información
    informacion = """
¿QUÉ ES ASCII?

ASCII (American Standard Code for Information Interchange) es un estándar de codificación de caracteres que asigna un número único a cada carácter, dígito o símbolo utilizado en la comunicación digital.

HISTORIA

ASCII fue desarrollado en la década de 1960 para estandarizar la representación de texto en computadoras y dispositivos de comunicación. Originalmente tenía 7 bits (128 caracteres), pero luego se extendió a 8 bits (256 caracteres).

RANGOS PRINCIPALES

• 0-31: Caracteres de control (no imprimibles)
• 32-127: Caracteres imprimibles estándar
  - 32: Espacio
  - 48-57: Dígitos (0-9)
  - 65-90: Letras mayúsculas (A-Z)
  - 97-122: Letras minúsculas (a-z)
• 128-255: Caracteres extendidos (dependen de la codificación)

USOS PRÁCTICOS

1. Almacenamiento de texto en computadoras
2. Comunicación entre sistemas
3. Programación (manejo de strings)
4. Codificación de datos

CURIOSIDADES

• La 'A' mayúscula tiene el código 65
• La 'a' minúscula tiene el código 97
• La diferencia entre mayúsculas y minúsculas es siempre 32
• El código 32 corresponde al espacio en blanco
"""
    
    info_texto.insert(tk.END, informacion)
    info_texto.config(state="disabled")  # Hacer el texto de solo lectura
    
    # Botón para cerrar
    boton_cerrar = crear_boton_con_hover(frame_info, "Cerrar", info_ventana.destroy, 
                                        2, 0, ancho=10, colspan=2)

def limpiar_resultados():
    """
    Limpia los resultados y campos de entrada
    """
    entry_caracter.delete(0, tk.END)
    entry_numero.delete(0, tk.END)
    texto_resultados.delete(1.0, tk.END)
    mostrar_tabla_ascii_completa()

def salir_aplicacion():
    """
    Sale de la aplicación después de confirmación
    """
    respuesta = messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?")
    if respuesta:
        ventana_principal.destroy()

# ============================================
# CONFIGURACIÓN DE LA VENTANA PRINCIPAL
# ============================================

def configurar_ventana_principal():
    """
    Configura y crea la ventana principal de la aplicación
    """
    global ventana_principal, entry_caracter, entry_numero, texto_resultados, texto_tabla
    
    # Crear ventana principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Tabla ASCII Educativa - Para Estudiantes de Bachillerato")
    ventana_principal.configure(bg=COLOR_FONDO)
    
    # Establecer tamaño y centrar ventana
    ancho_ventana = 1000
    alto_ventana = 700
    ventana_principal.geometry(f"{ancho_ventana}x{alto_ventana}")
    
    # Centrar la ventana en la pantalla
    ventana_principal.update_idletasks()
    x = (ventana_principal.winfo_screenwidth() // 2) - (ancho_ventana // 2)
    y = (ventana_principal.winfo_screenheight() // 2) - (alto_ventana // 2)
    ventana_principal.geometry(f'{ancho_ventana}x{alto_ventana}+{x}+{y}')
    
    # Evitar redimensionamiento
    ventana_principal.resizable(False, False)
    
    # Configurar icono de la ventana (si está disponible)
    try:
        ventana_principal.iconbitmap("ascii_icon.ico")
    except:
        pass
    
    return ventana_principal

def crear_interfaz():
    """
    Crea todos los widgets de la interfaz gráfica
    """
    # ============================================
    # FRAME SUPERIOR - TÍTULO
    # ============================================
    frame_titulo = tk.Frame(ventana_principal, bg=COLOR_PRIMARIO, height=80)
    frame_titulo.pack(fill="x", padx=10, pady=(10, 5))
    frame_titulo.pack_propagate(False)  # Mantener el tamaño fijo
    
    # Título principal
    titulo_principal = tk.Label(
        frame_titulo,
        text="APLICACIÓN EDUCATIVA: TABLA ASCII INTERACTIVA",
        bg=COLOR_PRIMARIO,
        fg=COLOR_TEXTO_CLARO,
        font=("Arial", 16, "bold")
    )
    titulo_principal.pack(expand=True)
    
    # Subtítulo
    subtitulo = tk.Label(
        frame_titulo,
        text="Para estudiantes de bachillerato - Aprende sobre codificación de caracteres",
        bg=COLOR_PRIMARIO,
        fg=COLOR_TEXTO_CLARO,
        font=("Arial", 10)
    )
    subtitulo.pack(expand=True)
    
    # ============================================
    # FRAME PRINCIPAL CON DOS COLUMNAS
    # ============================================
    frame_principal = tk.Frame(ventana_principal, bg=COLOR_FONDO)
    frame_principal.pack(fill="both", expand=True, padx=10, pady=5)
    
    # Configurar peso de columnas
    frame_principal.columnconfigure(0, weight=1)
    frame_principal.columnconfigure(1, weight=1)
    
    # ============================================
    # COLUMNA IZQUIERDA - CALCULADORA ASCII
    # ============================================
    frame_calculadora = tk.Frame(frame_principal, bg=COLOR_FONDO, relief="raised", borderwidth=2)
    frame_calculadora.grid(row=0, column=0, padx=(0, 5), pady=5, sticky="nsew")
    
    # Título de la calculadora
    crear_label_con_estilo(frame_calculadora, "CALCULADORA ASCII", 0, 0, 
                          estilo="titulo", colspan=2)
    
    # Instrucciones
    instrucciones = "Esta herramienta te permite convertir entre caracteres y códigos ASCII."
    crear_label_con_estilo(frame_calculadora, instrucciones, 1, 0, 
                          colspan=2, sticky="w")
    
    # Separador
    ttk.Separator(frame_calculadora, orient="horizontal").grid(
        row=2, column=0, columnspan=2, pady=10, sticky="ew"
    )
    
    # Sección 1: Carácter a ASCII
    crear_label_con_estilo(frame_calculadora, "1. CONVERTIR CARÁCTER A CÓDIGO ASCII", 3, 0,
                          estilo="subtitulo", colspan=2)
    
    crear_label_con_estilo(frame_calculadora, "Ingresa un carácter:", 4, 0)
    
    global entry_caracter
    entry_caracter = crear_entry_con_estilo(frame_calculadora, 4, 1, ancho=15)
    
    crear_boton_con_hover(frame_calculadora, "Convertir a ASCII", 
                         convertir_caracter_a_ascii, 5, 0, ancho=15, colspan=2)
    
    # Separador
    ttk.Separator(frame_calculadora, orient="horizontal").grid(
        row=6, column=0, columnspan=2, pady=10, sticky="ew"
    )
    
    # Sección 2: Número a carácter
    crear_label_con_estilo(frame_calculadora, "2. CONVERTIR NÚMERO A CARÁCTER ASCII", 7, 0,
                          estilo="subtitulo", colspan=2)
    
    crear_label_con_estilo(frame_calculadora, "Ingresa un número (0-255):", 8, 0)
    
    global entry_numero
    entry_numero = crear_entry_con_estilo(frame_calculadora, 8, 1, ancho=15)
    
    crear_boton_con_hover(frame_calculadora, "Convertir a Carácter", 
                         convertir_numero_a_caracter, 9, 0, ancho=15, colspan=2)
    
    # Separador
    ttk.Separator(frame_calculadora, orient="horizontal").grid(
        row=10, column=0, columnspan=2, pady=10, sticky="ew"
    )
    
    # Sección 3: Resultados
    crear_label_con_estilo(frame_calculadora, "RESULTADOS:", 11, 0,
                          estilo="subtitulo", colspan=2)
    
    global texto_resultados
    texto_resultados = crear_texto_con_estilo(frame_calculadora, 12, 0, 
                                             alto=6, ancho=30, colspan=2)
    
    # Botones de acción en la calculadora
    crear_boton_con_hover(frame_calculadora, "Limpiar", limpiar_resultados, 
                         13, 0, ancho=12, color_normal="#95A5A6")
    crear_boton_con_hover(frame_calculadora, "Información ASCII", 
                         mostrar_informacion_ascii, 13, 1, ancho=12, color_normal="#95A5A6")
    
    # ============================================
    # COLUMNA DERECHA - TABLA ASCII
    # ============================================
    frame_tabla = tk.Frame(frame_principal, bg=COLOR_FONDO, relief="raised", borderwidth=2)
    frame_tabla.grid(row=0, column=1, padx=(5, 0), pady=5, sticky="nsew")
    
    # Título de la tabla
    crear_label_con_estilo(frame_tabla, "TABLA ASCII COMPLETA", 0, 0,
                          estilo="titulo", colspan=2)
    
    # Instrucciones
    instrucciones_tabla = "Tabla de códigos ASCII estándar (0-127). Los caracteres resaltados aparecen en amarillo."
    crear_label_con_estilo(frame_tabla, instrucciones_tabla, 1, 0,
                          colspan=2, sticky="w")
    
    # Botón para refrescar tabla
    crear_boton_con_hover(frame_tabla, "Mostrar Tabla Completa", 
                         mostrar_tabla_ascii_completa, 2, 0, ancho=20, colspan=2)
    
    # Área de texto para la tabla
    global texto_tabla
    texto_tabla = crear_texto_con_estilo(frame_tabla, 3, 0, 
                                        alto=20, ancho=50, colspan=2)
    
    # Nota informativa
    nota = "Nota: Los códigos 0-31 y 127 son caracteres de control no imprimibles."
    crear_label_con_estilo(frame_tabla, nota, 4, 0, estilo="resaltado", 
                          colspan=2, sticky="w")
    
    # ============================================
    # FRAME INFERIOR - BOTONES DE CONTROL
    # ============================================
    frame_control = tk.Frame(ventana_principal, bg=COLOR_FONDO, height=60)
    frame_control.pack(fill="x", padx=10, pady=(5, 10))
    frame_control.pack_propagate(False)  # Mantener el tamaño fijo
    
    # Configurar columnas para centrar botones
    frame_control.columnconfigure(0, weight=1)
    frame_control.columnconfigure(1, weight=1)
    frame_control.columnconfigure(2, weight=1)
    
    # Botones de control
    crear_boton_con_hover(frame_control, "Información", mostrar_informacion_ascii, 
                         0, 0, ancho=15, color_normal="#95A5A6")
    
    crear_boton_con_hover(frame_control, "Limpiar Todo", limpiar_resultados, 
                         0, 1, ancho=15, color_normal="#95A5A6")
    
    crear_boton_con_hover(frame_control, "Salir", salir_aplicacion, 
                         0, 2, ancho=15, color_normal="#E74C3C")

# ============================================
# FUNCIÓN PRINCIPAL
# ============================================

def main():
    """
    Función principal que inicia la aplicación
    """
    global ventana_principal
    
    # Configurar ventana principal
    ventana_principal = configurar_ventana_principal()
    
    # Crear la interfaz
    crear_interfaz()
    
    # Mostrar la tabla ASCII al iniciar
    mostrar_tabla_ascii_completa()
    
    # Iniciar el bucle principal de la aplicación
    ventana_principal.mainloop()

# ============================================
# EJECUCIÓN DEL PROGRAMA
# ============================================

if __name__ == "__main__":
    main()