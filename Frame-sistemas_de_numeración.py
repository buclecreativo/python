# -*- coding: utf-8 -*-
"""
CALCULADORA DE CONVERSIÓN DE SISTEMAS NUMÉRICOS
Aplicación educativa para estudiantes de bachillerato
Incluye sistema binario (base 2)
Autor: Experto en Desarrollo de Software Educativo
"""

import tkinter as tk
from tkinter import ttk, messagebox

# ============================================================================
# CONFIGURACIÓN INICIAL Y PALETA DE COLORES
# ============================================================================

# Paleta de colores moderna y atractiva
COLORES = {
    "fondo_principal": "#1e1e2e",        # Azul oscuro moderno
    "fondo_secundario": "#2d2d44",       # Azul medio
    "fondo_botones": "#4a4a6a",          # Azul grisáceo
    "hover_botones": "#6a6a9a",          # Azul más claro para hover
    "texto_principal": "#e0e0e0",        # Gris claro
    "texto_secundario": "#a0a0c0",       # Gris azulado
    "acento": "#7c3aed",                 # Violeta moderno
    "acento_binario": "#10b981",         # Verde esmeralda para binario
    "acento_octal": "#3b82f6",           # Azul para octal
    "acento_decimal": "#8b5cf6",         # Violeta para decimal
    "acento_hexadecimal": "#ef4444",     # Rojo para hexadecimal
    "bordes": "#3a3a5a",                 # Azul para bordes
    "entrada_fondo": "#2a2a3a",          # Fondo para campos de entrada
    "entrada_texto": "#ffffff"           # Texto blanco para entradas
}

# ============================================================================
# FUNCIONES DE CONVERSIÓN NUMÉRICA
# ============================================================================

def decimal_a_binario(decimal_str):
    """Convierte un número decimal a binario"""
    try:
        decimal_num = int(decimal_str)
        if decimal_num == 0:
            return "0"
        # Convertir a binario (sin el prefijo '0b')
        binario = bin(decimal_num)[2:]
        return binario
    except ValueError:
        return "ERROR: No es decimal válido"

def decimal_a_octal(decimal_str):
    """Convierte un número decimal a octal"""
    try:
        decimal_num = int(decimal_str)
        if decimal_num == 0:
            return "0"
        # Convertir a octal (sin el prefijo '0o')
        octal = oct(decimal_num)[2:]
        return octal
    except ValueError:
        return "ERROR: No es decimal válido"

def decimal_a_hexadecimal(decimal_str):
    """Convierte un número decimal a hexadecimal"""
    try:
        decimal_num = int(decimal_str)
        if decimal_num == 0:
            return "0"
        # Convertir a hexadecimal (sin el prefijo '0x')
        hexadecimal = hex(decimal_num)[2:].upper()
        return hexadecimal
    except ValueError:
        return "ERROR: No es decimal válido"

def binario_a_decimal(binario_str):
    """Convierte un número binario a decimal"""
    try:
        # Verificar que solo contenga 0 y 1
        if not all(c in '01' for c in binario_str):
            return "ERROR: No es binario válido"
        # Convertir a decimal (el segundo parámetro 2 indica base binaria)
        decimal = int(binario_str, 2)
        return str(decimal)
    except ValueError:
        return "ERROR: No es binario válido"

def octal_a_decimal(octal_str):
    """Convierte un número octal a decimal"""
    try:
        # Convertir a decimal (el segundo parámetro 8 indica base octal)
        decimal = int(octal_str, 8)
        return str(decimal)
    except ValueError:
        return "ERROR: No es octal válido"

def hexadecimal_a_decimal(hex_str):
    """Convierte un número hexadecimal a decimal"""
    try:
        # Convertir a decimal (el segundo parámetro 16 indica base hexadecimal)
        decimal = int(hex_str, 16)
        return str(decimal)
    except ValueError:
        return "ERROR: No es hexadecimal válido"

def realizar_conversion():
    """Función principal que ejecuta todas las conversiones"""
    # Obtener el valor ingresado por el usuario
    entrada = entrada_numero.get().strip()
    
    if not entrada:
        messagebox.showwarning("Entrada vacía", "Por favor, ingresa un número")
        return
    
    # Determinar el tipo de número ingresado
    tipo_ingresado = tipo_entrada.get()
    
    # Inicializar variables para los resultados
    decimal_result = ""
    binario_result = ""
    octal_result = ""
    hexadecimal_result = ""
    
    # Procesar según el tipo ingresado
    if tipo_ingresado == "decimal":
        if entrada.isdigit() or (entrada[0] == '-' and entrada[1:].isdigit()):
            decimal_result = entrada
            binario_result = decimal_a_binario(entrada)
            octal_result = decimal_a_octal(entrada)
            hexadecimal_result = decimal_a_hexadecimal(entrada)
        else:
            messagebox.showerror("Error", "¡Eso no es un número decimal válido!")
            return
            
    elif tipo_ingresado == "binario":
        # Verificar si es binario válido (solo dígitos 0 y 1)
        if all(c in '01' for c in entrada):
            decimal_result = binario_a_decimal(entrada)
            if "ERROR" in decimal_result:
                messagebox.showerror("Error", "¡Número binario inválido!")
                return
            binario_result = entrada
            octal_result = decimal_a_octal(decimal_result)
            hexadecimal_result = decimal_a_hexadecimal(decimal_result)
        else:
            messagebox.showerror("Error", "¡Eso no es un número binario válido!\nUsa solo dígitos 0 y 1")
            return
            
    elif tipo_ingresado == "octal":
        # Verificar si es octal válido (solo dígitos 0-7)
        if all(c in '01234567' for c in entrada):
            decimal_result = octal_a_decimal(entrada)
            if "ERROR" in decimal_result:
                messagebox.showerror("Error", "¡Número octal inválido!")
                return
            binario_result = decimal_a_binario(decimal_result)
            octal_result = entrada
            hexadecimal_result = decimal_a_hexadecimal(decimal_result)
        else:
            messagebox.showerror("Error", "¡Eso no es un número octal válido!\nUsa solo dígitos del 0 al 7")
            return
            
    elif tipo_ingresado == "hexadecimal":
        # Verificar si es hexadecimal válido (solo dígitos 0-9 y letras A-F)
        try:
            decimal_result = hexadecimal_a_decimal(entrada)
            if "ERROR" in decimal_result:
                raise ValueError
            binario_result = decimal_a_binario(decimal_result)
            octal_result = decimal_a_octal(decimal_result)
            hexadecimal_result = entrada.upper()
        except:
            messagebox.showerror("Error", "¡Eso no es un número hexadecimal válido!\nUsa solo 0-9 y A-F (mayúsculas o minúsculas)")
            return
    
    # Actualizar los campos de resultado
    resultado_decimal.set(decimal_result)
    resultado_binario.set(binario_result)
    resultado_octal.set(octal_result)
    resultado_hexadecimal.set(hexadecimal_result)
    
    # Mostrar explicación
    mostrar_explicacion(tipo_ingresado, entrada, decimal_result, binario_result, 
                       octal_result, hexadecimal_result)

def mostrar_explicacion(tipo_orig, entrada, decimal, binario, octal, hexa):
    """Muestra una explicación educativa del proceso de conversión"""
    explicaciones = {
        "decimal": f"""
CONVERSIÓN DESDE DECIMAL ({entrada}):

1. Decimal a Binario:
   • Dividimos {entrada} sucesivamente entre 2
   • Tomamos los restos de cada división
   • Leemos los restos de abajo hacia arriba
   • Resultado: {binario}₂

2. Decimal a Octal:
   • Dividimos {entrada} sucesivamente entre 8
   • Tomamos los restos de cada división
   • Resultado: {octal}₈

3. Decimal a Hexadecimal:
   • Dividimos {entrada} sucesivamente entre 16
   • Restos 10-15 se convierten a A-F
   • Resultado: {hexa}₁₆
""",
        "binario": f"""
CONVERSIÓN DESDE BINARIO ({entrada}):

1. Binario a Decimal:
   • Cada dígito se multiplica por 2^posición
   • Posición 0: dígito más a la derecha
   • Solo usamos dígitos 0 y 1
   • {entrada}₂ = {decimal}₁₀

2. Luego convertimos el decimal a:
   • Octal: {octal}₈
   • Hexadecimal: {hexa}₁₆

CONSEJO: Cada 3 bits binarios = 1 dígito octal
         Cada 4 bits binarios = 1 dígito hexadecimal
""",
        "octal": f"""
CONVERSIÓN DESDE OCTAL ({entrada}):

1. Octal a Decimal:
   • Cada dígito se multiplica por 8^posición
   • Solo usamos dígitos del 0 al 7
   • {entrada}₈ = {decimal}₁₀

2. Luego convertimos el decimal a:
   • Binario: {binario}₂
   • Hexadecimal: {hexa}₁₆

CONSEJO: Cada dígito octal = 3 bits binarios
""",
        "hexadecimal": f"""
CONVERSIÓN DESDE HEXADECIMAL ({entrada}):

1. Hexadecimal a Decimal:
   • Cada dígito se multiplica por 16^posición
   • Letras: A=10, B=11, C=12, D=13, E=14, F=15
   • {entrada}₁₆ = {decimal}₁₀

2. Luego convertimos el decimal a:
   • Binario: {binario}₂
   • Octal: {octal}₈

CONSEJO: Cada dígito hexadecimal = 4 bits binarios
"""
    }
    
    texto_explicacion.config(state=tk.NORMAL)
    texto_explicacion.delete(1.0, tk.END)
    texto_explicacion.insert(1.0, explicaciones[tipo_orig])
    texto_explicacion.config(state=tk.DISABLED)

def limpiar_campos():
    """Limpia todos los campos de entrada y resultados"""
    entrada_numero.delete(0, tk.END)
    resultado_decimal.set("")
    resultado_binario.set("")
    resultado_octal.set("")
    resultado_hexadecimal.set("")
    texto_explicacion.config(state=tk.NORMAL)
    texto_explicacion.delete(1.0, tk.END)
    texto_explicacion.insert(1.0, "Ingresa un número y selecciona su tipo para ver las conversiones y explicaciones.")
    texto_explicacion.config(state=tk.DISABLED)

def mostrar_tabla_conversion():
    """Muestra una tabla de conversión básica de 0 a 15"""
    ventana_tabla = tk.Toplevel(ventana)
    ventana_tabla.title("Tabla de Conversión (0-15)")
    ventana_tabla.configure(bg=COLORES["fondo_principal"])
    ventana_tabla.geometry("600x600")
    
    # Centrar ventana
    ventana_tabla.transient(ventana)
    ventana_tabla.grab_set()
    
    # Título
    tk.Label(
        ventana_tabla,
        text="📊 TABLA DE CONVERSIÓN RÁPIDA (0-15)",
        font=("Arial", 16, "bold"),
        fg=COLORES["acento"],
        bg=COLORES["fondo_principal"]
    ).pack(pady=10)
    
    # Frame para la tabla
    frame_tabla = tk.Frame(ventana_tabla, bg=COLORES["fondo_secundario"])
    frame_tabla.pack(pady=10, padx=20)
    
    # Encabezados
    encabezados = ["Decimal", "Binario", "Octal", "Hexadecimal"]
    for i, encabezado in enumerate(encabezados):
        tk.Label(
            frame_tabla,
            text=encabezado,
            font=("Arial", 11, "bold"),
            fg=COLORES["acento"],
            bg=COLORES["fondo_secundario"],
            width=15
        ).grid(row=0, column=i, padx=2, pady=2)
    
    # Datos de la tabla
    for num in range(16):
        # Fila con diferentes colores según paridad
        color_fondo = COLORES["fondo_secundario"] if num % 2 == 0 else COLORES["fondo_principal"]
        
        # Decimal
        tk.Label(
            frame_tabla,
            text=str(num),
            font=("Arial", 10),
            fg=COLORES["texto_principal"],
            bg=color_fondo,
            width=15
        ).grid(row=num+1, column=0, padx=2, pady=1)
        
        # Binario
        binario = bin(num)[2:].zfill(4)  # 4 bits con ceros a la izquierda
        tk.Label(
            frame_tabla,
            text=binario,
            font=("Arial", 10, "bold"),
            fg=COLORES["acento_binario"],
            bg=color_fondo,
            width=15
        ).grid(row=num+1, column=1, padx=2, pady=1)
        
        # Octal
        octal = oct(num)[2:]
        tk.Label(
            frame_tabla,
            text=octal,
            font=("Arial", 10),
            fg=COLORES["acento_octal"],
            bg=color_fondo,
            width=15
        ).grid(row=num+1, column=2, padx=2, pady=1)
        
        # Hexadecimal
        hexadecimal = hex(num)[2:].upper()
        tk.Label(
            frame_tabla,
            text=hexadecimal,
            font=("Arial", 10),
            fg=COLORES["acento_hexadecimal"],
            bg=color_fondo,
            width=15
        ).grid(row=num+1, column=3, padx=2, pady=1)
    
    # Información adicional
    tk.Label(
        ventana_tabla,
        text="💡 Consejo: Observa cómo los números cambian de representación en cada sistema.",
        font=("Arial", 10),
        fg=COLORES["texto_secundario"],
        bg=COLORES["fondo_principal"]
    ).pack(pady=10)
    
    # Botón para cerrar
    tk.Button(
        ventana_tabla,
        text="Cerrar Tabla",
        command=ventana_tabla.destroy,
        bg=COLORES["fondo_botones"],
        fg=COLORES["texto_principal"],
        font=("Arial", 10),
        width=15
    ).pack(pady=10)

def crear_efecto_hover(boton, color_normal, color_hover):
    """Crea efecto hover para un botón"""
    def entrar(event):
        boton.config(bg=color_hover)
    
    def salir(event):
        boton.config(bg=color_normal)
    
    boton.bind("<Enter>", entrar)
    boton.bind("<Leave>", salir)

# ============================================================================
# CONFIGURACIÓN DE LA VENTANA PRINCIPAL
# ============================================================================

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Sistemas Numéricos - Incluye Binario")
ventana.configure(bg=COLORES["fondo_principal"])

# Centrar ventana en pantalla
ancho_ventana = 1000
alto_ventana = 900
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

# Evitar que la ventana sea redimensionable
ventana.resizable(False, False)

# ============================================================================
# CREACIÓN DE FRAMES (CONTENEDORES)
# ============================================================================

# Frame para el título
frame_titulo = tk.Frame(
    ventana, 
    bg=COLORES["fondo_principal"],
    height=100
)
frame_titulo.pack(fill=tk.X, padx=20, pady=(20, 10))

# Frame para entrada de datos
frame_entrada = tk.Frame(
    ventana,
    bg=COLORES["fondo_secundario"],
    relief=tk.RAISED,
    bd=2
)
frame_entrada.pack(fill=tk.X, padx=20, pady=10)

# Frame para resultados
frame_resultados = tk.Frame(
    ventana,
    bg=COLORES["fondo_secundario"],
    relief=tk.RAISED,
    bd=2
)
frame_resultados.pack(fill=tk.X, padx=20, pady=10)

# Frame para explicaciones
frame_explicacion = tk.Frame(
    ventana,
    bg=COLORES["fondo_secundario"],
    relief=tk.RAISED,
    bd=2
)
frame_explicacion.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# Frame para botones principales
frame_botones = tk.Frame(
    ventana,
    bg=COLORES["fondo_principal"]
)
frame_botones.pack(fill=tk.X, padx=20, pady=(10, 10))

# Frame para botones adicionales
frame_botones_adicionales = tk.Frame(
    ventana,
    bg=COLORES["fondo_principal"]
)
frame_botones_adicionales.pack(fill=tk.X, padx=20, pady=(0, 20))

# ============================================================================
# WIDGETS - TÍTULO
# ============================================================================

titulo = tk.Label(
    frame_titulo,
    text="🧮 CALCULADORA DE 4 SISTEMAS NUMÉRICOS",
    font=("Arial", 24, "bold"),
    fg=COLORES["acento"],
    bg=COLORES["fondo_principal"]
)
titulo.pack(pady=10)

subtitulo = tk.Label(
    frame_titulo,
    text="Conversiones entre Decimal, Binario, Octal y Hexadecimal",
    font=("Arial", 12),
    fg=COLORES["texto_secundario"],
    bg=COLORES["fondo_principal"]
)
subtitulo.pack()

# ============================================================================
# WIDGETS - ENTRADA DE DATOS
# ============================================================================

# Título del frame de entrada
tk.Label(
    frame_entrada,
    text="INGRESA TU NÚMERO",
    font=("Arial", 14, "bold"),
    fg=COLORES["texto_principal"],
    bg=COLORES["fondo_secundario"]
).pack(pady=(10, 5))

# Frame para organizar entrada y tipo
frame_entrada_interior = tk.Frame(
    frame_entrada,
    bg=COLORES["fondo_secundario"]
)
frame_entrada_interior.pack(pady=10)

# Campo de entrada
tk.Label(
    frame_entrada_interior,
    text="Número:",
    font=("Arial", 11),
    fg=COLORES["texto_principal"],
    bg=COLORES["fondo_secundario"]
).grid(row=0, column=0, padx=(10, 5), pady=5, sticky="e")

entrada_numero = tk.Entry(
    frame_entrada_interior,
    font=("Arial", 12),
    width=30,
    bg=COLORES["entrada_fondo"],
    fg=COLORES["entrada_texto"],
    insertbackground=COLORES["texto_principal"],
    relief=tk.SUNKEN,
    bd=2
)
entrada_numero.grid(row=0, column=1, padx=5, pady=5)

# Selector de tipo
tk.Label(
    frame_entrada_interior,
    text="Tipo:",
    font=("Arial", 11),
    fg=COLORES["texto_principal"],
    bg=COLORES["fondo_secundario"]
).grid(row=0, column=2, padx=(20, 5), pady=5, sticky="e")

tipo_entrada = tk.StringVar(value="decimal")
opciones_tipo = ["decimal", "binario", "octal", "hexadecimal"]

menu_tipo = ttk.Combobox(
    frame_entrada_interior,
    textvariable=tipo_entrada,
    values=opciones_tipo,
    state="readonly",
    width=15,
    font=("Arial", 11)
)
menu_tipo.grid(row=0, column=3, padx=5, pady=5)

# ============================================================================
# WIDGETS - RESULTADOS
# ============================================================================

# Título del frame de resultados
tk.Label(
    frame_resultados,
    text="RESULTADOS DE CONVERSIÓN",
    font=("Arial", 14, "bold"),
    fg=COLORES["texto_principal"],
    bg=COLORES["fondo_secundario"]
).pack(pady=(10, 5))

# Frame para organizar resultados
frame_resultados_interior = tk.Frame(
    frame_resultados,
    bg=COLORES["fondo_secundario"]
)
frame_resultados_interior.pack(pady=10)

# Variables para resultados
resultado_decimal = tk.StringVar()
resultado_binario = tk.StringVar()
resultado_octal = tk.StringVar()
resultado_hexadecimal = tk.StringVar()

# Etiquetas y campos para resultados
sistemas = [
    ("Sistema Decimal", resultado_decimal, "10", COLORES["acento_decimal"], "Número en base 10 (0-9)"),
    ("Sistema Binario", resultado_binario, "2", COLORES["acento_binario"], "Número en base 2 (0-1)"),
    ("Sistema Octal", resultado_octal, "8", COLORES["acento_octal"], "Número en base 8 (0-7)"),
    ("Sistema Hexadecimal", resultado_hexadecimal, "16", COLORES["acento_hexadecimal"], "Número en base 16 (0-9, A-F)")
]

for i, (nombre, variable, base, color, descripcion) in enumerate(sistemas):
    # Frame para cada sistema
    frame_sistema = tk.Frame(
        frame_resultados_interior,
        bg=COLORES["fondo_secundario"]
    )
    frame_sistema.grid(row=0, column=i, padx=10, pady=5)
    
    # Nombre del sistema
    tk.Label(
        frame_sistema,
        text=nombre,
        font=("Arial", 11, "bold"),
        fg=color,
        bg=COLORES["fondo_secundario"]
    ).pack()
    
    # Base del sistema
    tk.Label(
        frame_sistema,
        text=f"(Base {base})",
        font=("Arial", 9),
        fg=COLORES["texto_secundario"],
        bg=COLORES["fondo_secundario"]
    ).pack()
    
    # Campo de resultado
    resultado_entry = tk.Entry(
        frame_sistema,
        textvariable=variable,
        font=("Arial", 12, "bold"),
        width=18,
        state="readonly",
        readonlybackground=COLORES["entrada_fondo"],
        fg=color,
        relief=tk.SUNKEN,
        bd=2,
        justify="center"
    )
    resultado_entry.pack(pady=5)
    
    # Descripción
    tk.Label(
        frame_sistema,
        text=descripcion,
        font=("Arial", 8),
        fg=COLORES["texto_secundario"],
        bg=COLORES["fondo_secundario"],
        wraplength=150
    ).pack()

# ============================================================================
# WIDGETS - EXPLICACIONES
# ============================================================================

# Título del frame de explicación
tk.Label(
    frame_explicacion,
    text="📚 EXPLICACIÓN DEL PROCESO DE CONVERSIÓN",
    font=("Arial", 14, "bold"),
    fg=COLORES["texto_principal"],
    bg=COLORES["fondo_secundario"]
).pack(pady=(10, 5))

# Widget Text para explicaciones
texto_explicacion = tk.Text(
    frame_explicacion,
    height=10,
    width=80,
    font=("Arial", 11),
    bg=COLORES["entrada_fondo"],
    fg=COLORES["texto_principal"],
    wrap=tk.WORD,
    relief=tk.SUNKEN,
    bd=2,
    padx=10,
    pady=10
)
texto_explicacion.pack(padx=10, pady=(0, 10), fill=tk.BOTH, expand=True)

# Insertar texto inicial
texto_explicacion.insert(1.0, "Ingresa un número y selecciona su tipo para ver las conversiones y explicaciones.")
texto_explicacion.config(state=tk.DISABLED)

# Barra de desplazamiento para el texto
scrollbar = tk.Scrollbar(texto_explicacion)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
texto_explicacion.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=texto_explicacion.yview)

# ============================================================================
# WIDGETS - BOTONES PRINCIPALES
# ============================================================================

# Botón de conversión
boton_convertir = tk.Button(
    frame_botones,
    text="🔁 REALIZAR CONVERSIÓN",
    font=("Arial", 12, "bold"),
    bg=COLORES["fondo_botones"],
    fg=COLORES["texto_principal"],
    activebackground=COLORES["hover_botones"],
    activeforeground=COLORES["texto_principal"],
    relief=tk.RAISED,
    bd=3,
    width=25,
    height=2,
    command=realizar_conversion
)
boton_convertir.pack(side=tk.LEFT, padx=10)

# Botón de limpiar
boton_limpiar = tk.Button(
    frame_botones,
    text="🗑️ LIMPIAR TODO",
    font=("Arial", 12, "bold"),
    bg=COLORES["fondo_botones"],
    fg=COLORES["texto_principal"],
    activebackground=COLORES["hover_botones"],
    activeforeground=COLORES["texto_principal"],
    relief=tk.RAISED,
    bd=3,
    width=25,
    height=2,
    command=limpiar_campos
)
boton_limpiar.pack(side=tk.RIGHT, padx=10)

# ============================================================================
# WIDGETS - BOTONES ADICIONALES
# ============================================================================

# Botón para mostrar tabla de conversión
boton_tabla = tk.Button(
    frame_botones_adicionales,
    text="📊 VER TABLA DE CONVERSIÓN (0-15)",
    font=("Arial", 11),
    bg=COLORES["acento_binario"],
    fg=COLORES["texto_principal"],
    activebackground="#34d399",
    relief=tk.RAISED,
    bd=2,
    width=30,
    height=1,
    command=mostrar_tabla_conversion
)
boton_tabla.pack(pady=5)

# Aplicar efecto hover a todos los botones
crear_efecto_hover(boton_convertir, COLORES["fondo_botones"], COLORES["hover_botones"])
crear_efecto_hover(boton_limpiar, COLORES["fondo_botones"], COLORES["hover_botones"])
crear_efecto_hover(boton_tabla, COLORES["acento_binario"], "#34d399")

# ============================================================================
# INFORMACIÓN ADICIONAL
# ============================================================================

# Frame para información adicional
frame_info = tk.Frame(
    ventana,
    bg=COLORES["fondo_principal"]
)
frame_info.pack(fill=tk.X, padx=20, pady=(0, 10))

# Información sobre sistemas numéricos
info_texto = """
💡 LOS 4 SISTEMAS NUMÉRICOS: 
• BINARIO (Base 2): Solo usa 0 y 1. Fundamental en computación.
• OCTAL (Base 8): Usa dígitos 0-7. Relación directa con binario (3 bits = 1 dígito octal).
• DECIMAL (Base 10): Usa dígitos 0-9. Sistema que usamos diariamente.
• HEXADECIMAL (Base 16): Usa dígitos 0-9 y A-F. Muy usado en programación (4 bits = 1 dígito hex).
"""

tk.Label(
    frame_info,
    text=info_texto,
    font=("Arial", 10),
    fg=COLORES["texto_secundario"],
    bg=COLORES["fondo_principal"],
    justify=tk.LEFT
).pack()

# ============================================================================
# CONSEJO PARA ESTUDIANTES
# ============================================================================

consejo = tk.Label(
    ventana,
    text="🎓 Consejo educativo: Observa las relaciones: Binario → Octal (agrupa 3 bits), Binario → Hexadecimal (agrupa 4 bits)",
    font=("Arial", 10, "italic"),
    fg=COLORES["acento"],
    bg=COLORES["fondo_principal"]
)
consejo.pack(pady=(0, 10))

# ============================================================================
# PIE DE PÁGINA
# ============================================================================

pie_pagina = tk.Label(
    ventana,
    text="Herramienta educativa para estudiantes de bachillerato - © 2024",
    font=("Arial", 9),
    fg=COLORES["texto_secundario"],
    bg=COLORES["fondo_principal"]
)
pie_pagina.pack(pady=(0, 5))

# ============================================================================
# CONFIGURACIÓN FINAL Y EJECUCIÓN
# ============================================================================

# Configurar el evento Enter para el campo de entrada
entrada_numero.bind('<Return>', lambda event: realizar_conversion())

# Configurar focus inicial
entrada_numero.focus_set()

# Ejecutar la aplicación
ventana.mainloop()