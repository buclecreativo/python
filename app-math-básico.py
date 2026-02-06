"""
JUEGO EDUCATIVO: EXPLORANDO FUNCIONES MATEMÁTICAS
Autor: Experto en Desarrollo de Software Educativo
Descripción: Aplicación educativa para aprender sobre funciones matemáticas en Python
Funciones cubiertas: abs(), round(), math.sqrt(), math.pi, math.pow(), 
                     math.ceil(), math.floor(), math.trunc()
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math

# ==============================================
# CONFIGURACIÓN INICIAL Y VARIABLES GLOBALES
# ==============================================

# Configuración de colores (paleta moderna y atractiva)
COLOR_FONDO = "#1E1E2E"           # Azul oscuro elegante
COLOR_SECUNDARIO = "#2D2D44"      # Azul medio
COLOR_BOTON = "#6C63FF"           # Púrpura vibrante
COLOR_BOTON_HOVER = "#5753D9"     # Púrpura más oscuro para hover
COLOR_TEXTO = "#FFFFFF"           # Blanco para texto
COLOR_TEXTO_SECUNDARIO = "#CDD6F4"# Gris claro para texto secundario
COLOR_EXITO = "#4CAF50"           # Verde para resultados
COLOR_EXPLICACION = "#89B4FA"     # Azul claro para explicaciones

# Variables globales para los widgets que necesitan ser accedidos en múltiples funciones
ventana_principal = None
frame_contenido = None
texto_explicacion = None
label_resultado = None
entry_numero = None
entry_numero2 = None

# ==============================================
# FUNCIONES DE UTILIDAD Y ESTILO
# ==============================================

def configurar_estilo():
    """Configura el estilo visual de la aplicación"""
    estilo = ttk.Style()
    estilo.theme_use('clam')
    
    # Configurar estilo para los frames
    estilo.configure('TFrame', background=COLOR_FONDO)
    
    # Configurar estilo para las etiquetas
    estilo.configure('TLabel', 
                     background=COLOR_FONDO, 
                     foreground=COLOR_TEXTO,
                     font=('Arial', 10))
    
    # Configurar estilo para los botones
    estilo.configure('TButton',
                     background=COLOR_BOTON,
                     foreground=COLOR_TEXTO,
                     borderwidth=0,
                     focuscolor=COLOR_FONDO,
                     font=('Arial', 10, 'bold'))
    
    # Estilo para botones cuando el cursor está sobre ellos
    estilo.map('TButton',
               background=[('active', COLOR_BOTON_HOVER)],
               foreground=[('active', COLOR_TEXTO)])

def crear_boton_con_hover(parent, texto, comando, grid_info=None, pack_info=None):
    """
    Crea un botón con efecto hover personalizado
    
    Args:
        parent: Widget padre donde se colocará el botón
        texto: Texto que mostrará el botón
        comando: Función a ejecutar al hacer clic
        grid_info: Diccionario con parámetros para grid() (opcional)
        pack_info: Diccionario con parámetros para pack() (opcional)
    
    Returns:
        El botón creado
    """
    boton = tk.Button(parent,
                      text=texto,
                      command=comando,
                      bg=COLOR_BOTON,
                      fg=COLOR_TEXTO,
                      activebackground=COLOR_BOTON_HOVER,
                      activeforeground=COLOR_TEXTO,
                      font=('Arial', 10, 'bold'),
                      relief='flat',
                      padx=20,
                      pady=10,
                      cursor='hand2')
    
    # Añadir efecto hover manualmente
    def on_enter(event):
        boton['background'] = COLOR_BOTON_HOVER
    
    def on_leave(event):
        boton['background'] = COLOR_BOTON
    
    boton.bind("<Enter>", on_enter)
    boton.bind("<Leave>", on_leave)
    
    # Colocar el botón en su contenedor
    if grid_info:
        boton.grid(**grid_info)
    elif pack_info:
        boton.pack(**pack_info)
    
    return boton

def limpiar_contenido():
    """Limpia el área de contenido principal"""
    global frame_contenido
    
    # Destruir el frame de contenido existente
    if frame_contenido:
        frame_contenido.destroy()
    
    # Crear un nuevo frame de contenido
    frame_contenido = tk.Frame(ventana_principal, bg=COLOR_FONDO)
    frame_contenido.pack(fill='both', expand=True, padx=20, pady=20)

def mostrar_explicacion(texto):
    """Muestra una explicación en el área de texto de explicaciones"""
    global texto_explicacion
    texto_explicacion.config(state='normal')
    texto_explicacion.delete(1.0, tk.END)
    texto_explicacion.insert(tk.END, texto)
    texto_explicacion.config(state='disabled')

def mostrar_resultado(texto, color=COLOR_EXITO):
    """Muestra un resultado en la etiqueta de resultados"""
    global label_resultado
    label_resultado.config(text=texto, fg=color)

def validar_numero(entrada):
    """Valida si la entrada es un número válido"""
    try:
        # Intentar convertir a float
        float(entrada)
        return True
    except ValueError:
        return False

# ==============================================
# FUNCIONES PARA CADA OPERACIÓN MATEMÁTICA
# ==============================================

def explicar_abs():
    """Muestra la explicación y funcionalidad de abs()"""
    mostrar_explicacion(
        "FUNCIÓN ABS() - VALOR ABSOLUTO\n\n"
        "• ¿Qué hace?: Devuelve el valor absoluto de un número.\n"
        "• ¿Qué es valor absoluto?: Es la distancia de un número al cero, siempre positiva.\n"
        "• Ejemplos:\n"
        "   abs(-5) = 5\n"
        "   abs(3.2) = 3.2\n"
        "   abs(0) = 0\n\n"
        "• ¿Cuándo usarlo?: Cuando necesitas trabajar con distancias, magnitudes o "
        "cuando quieres ignorar el signo de un número."
    )
    
    # Limpiar y configurar la interfaz para abs()
    limpiar_contenido()
    
    # Título
    tk.Label(frame_contenido, 
             text="VALOR ABSOLUTO - abs()",
             bg=COLOR_FONDO,
             fg=COLOR_EXPLICACION,
             font=('Arial', 14, 'bold')).pack(pady=(0, 20))
    
    # Frame para entrada de datos
    frame_entrada = tk.Frame(frame_contenido, bg=COLOR_FONDO)
    frame_entrada.pack(pady=10)
    
    tk.Label(frame_entrada, 
             text="Ingresa un número (puede ser positivo o negativo):",
             bg=COLOR_FONDO,
             fg=COLOR_TEXTO_SECUNDARIO).pack()
    
    # Usar variable global para el entry
    global entry_numero
    entry_numero = tk.Entry(frame_entrada, 
                           font=('Arial', 12),
                           width=20,
                           justify='center')
    entry_numero.pack(pady=10)
    entry_numero.focus()
    
    # Botón para calcular
    crear_boton_con_hover(frame_entrada, 
                         "CALCULAR VALOR ABSOLUTO",
                         calcular_abs,
                         pack_info={'pady': 10})
    
    # Ejemplos
    frame_ejemplos = tk.Frame(frame_contenido, bg=COLOR_SECUNDARIO, padx=10, pady=10)
    frame_ejemplos.pack(pady=20)
    
    tk.Label(frame_ejemplos,
             text="Ejemplos para probar:",
             bg=COLOR_SECUNDARIO,
             fg=COLOR_TEXTO,
             font=('Arial', 10, 'bold')).pack()
    
    ejemplos = ["-15", "7.5", "-3.1416", "0", "-100"]
    for ejemplo in ejemplos:
        boton_ejemplo = tk.Button(frame_ejemplos,
                                  text=ejemplo,
                                  command=lambda e=ejemplo: entry_numero.insert(0, e),
                                  bg=COLOR_SECUNDARIO,
                                  fg=COLOR_EXPLICACION,
                                  relief='flat',
                                  cursor='hand2')
        boton_ejemplo.pack(side='left', padx=5)

def calcular_abs():
    """Calcula el valor absoluto del número ingresado"""
    global entry_numero
    
    entrada = entry_numero.get()
    
    if not entrada:
        mostrar_resultado("Por favor, ingresa un número", "red")
        return
    
    if not validar_numero(entrada):
        mostrar_resultado("¡Error! Debes ingresar un número válido", "red")
        return
    
    numero = float(entrada)
    resultado = abs(numero)
    
    mostrar_resultado(f"abs({numero}) = {resultado}")

def explicar_round():
    """Muestra la explicación y funcionalidad de round()"""
    mostrar_explicacion(
        "FUNCIÓN ROUND() - REDONDEO\n\n"
        "• ¿Qué hace?: Redondea un número a una cantidad específica de decimales.\n"
        "• ¿Cómo funciona?: Si el decimal es 5 o mayor, redondea hacia arriba. "
        "Si es menor que 5, redondea hacia abajo.\n"
        "• Ejemplos:\n"
        "   round(3.14159, 2) = 3.14\n"
        "   round(2.678, 1) = 2.7\n"
        "   round(5.5) = 6\n"
        "   round(4.2) = 4\n\n"
        "• ¿Cuándo usarlo?: Cuando necesitas limitar los decimales de un número, "
        "especialmente en cálculos financieros o para mostrar resultados más legibles."
    )
    
    # Limpiar y configurar la interfaz para round()
    limpiar_contenido()
    
    # Título
    tk.Label(frame_contenido, 
             text="REDONDEO - round()",
             bg=COLOR_FONDO,
             fg=COLOR_EXPLICACION,
             font=('Arial', 14, 'bold')).pack(pady=(0, 20))
    
    # Frame para entrada de datos
    frame_entrada = tk.Frame(frame_contenido, bg=COLOR_FONDO)
    frame_entrada.pack(pady=10)
    
    # Entrada para el número
    tk.Label(frame_entrada, 
             text="Número a redondear:",
             bg=COLOR_FONDO,
             fg=COLOR_TEXTO_SECUNDARIO).grid(row=0, column=0, padx=5, pady=5)
    
    global entry_numero
    entry_numero = tk.Entry(frame_entrada, 
                           font=('Arial', 12),
                           width=15,
                           justify='center')
    entry_numero.grid(row=0, column=1, padx=5, pady=5)
    
    # Entrada para decimales
    tk.Label(frame_entrada, 
             text="Decimales (opcional):",
             bg=COLOR_FONDO,
             fg=COLOR_TEXTO_SECUNDARIO).grid(row=1, column=0, padx=5, pady=5)
    
    global entry_numero2
    entry_numero2 = tk.Entry(frame_entrada, 
                            font=('Arial', 12),
                            width=15,
                            justify='center')
    entry_numero2.grid(row=1, column=1, padx=5, pady=5)
    entry_numero2.insert(0, "0")  # Valor por defecto
    
    # Botón para calcular
    crear_boton_con_hover(frame_entrada, 
                         "REDONDEAR",
                         calcular_round,
                         grid_info={'row': 2, 'column': 0, 'columnspan': 2, 'pady': 10})
    
    # Ejemplos
    frame_ejemplos = tk.Frame(frame_contenido, bg=COLOR_SECUNDARIO, padx=10, pady=10)
    frame_ejemplos.pack(pady=20)
    
    tk.Label(frame_ejemplos,
             text="Ejemplos (número, decimales):",
             bg=COLOR_SECUNDARIO,
             fg=COLOR_TEXTO,
             font=('Arial', 10, 'bold')).pack()
    
    ejemplos = [("3.14159", "2"), ("2.678", "1"), ("5.5", "0"), ("7.8888", "3")]
    
    for num, dec in ejemplos:
        frame_ejemplo = tk.Frame(frame_ejemplos, bg=COLOR_SECUNDARIO)
        frame_ejemplo.pack(pady=5)
        
        tk.Label(frame_ejemplo,
                 text=f"{num}, {dec}",
                 bg=COLOR_SECUNDARIO,
                 fg=COLOR_TEXTO_SECUNDARIO).pack(side='left', padx=5)
        
        boton_ejemplo = tk.Button(frame_ejemplo,
                                  text="Probar",
                                  command=lambda n=num, d=dec: cargar_ejemplo_round(n, d),
                                  bg=COLOR_SECUNDARIO,
                                  fg=COLOR_EXPLICACION,
                                  relief='flat',
                                  cursor='hand2')
        boton_ejemplo.pack(side='left', padx=5)

def cargar_ejemplo_round(numero, decimales):
    """Carga un ejemplo en los campos de round()"""
    global entry_numero, entry_numero2
    entry_numero.delete(0, tk.END)
    entry_numero.insert(0, numero)
    entry_numero2.delete(0, tk.END)
    entry_numero2.insert(0, decimales)

def calcular_round():
    """Calcula el redondeo del número ingresado"""
    global entry_numero, entry_numero2
    
    entrada_num = entry_numero.get()
    entrada_dec = entry_numero2.get()
    
    if not entrada_num:
        mostrar_resultado("Por favor, ingresa un número", "red")
        return
    
    if not validar_numero(entrada_num):
        mostrar_resultado("¡Error! El número no es válido", "red")
        return
    
    numero = float(entrada_num)
    
    if entrada_dec:
        if not entrada_dec.isdigit():
            mostrar_resultado("¡Error! Los decimales deben ser un número entero", "red")
            return
        
        decimales = int(entrada_dec)
        resultado = round(numero, decimales)
        mostrar_resultado(f"round({numero}, {decimales}) = {resultado}")
    else:
        resultado = round(numero)
        mostrar_resultado(f"round({numero}) = {resultado}")

def explicar_math_sqrt():
    """Muestra la explicación y funcionalidad de math.sqrt()"""
    mostrar_explicacion(
        "FUNCIÓN MATH.SQRT() - RAÍZ CUADRADA\n\n"
        "• ¿Qué hace?: Calcula la raíz cuadrada de un número.\n"
        "• ¿Qué es raíz cuadrada?: Es el número que multiplicado por sí mismo da el número original.\n"
        "• Ejemplos:\n"
        "   math.sqrt(25) = 5   (porque 5 × 5 = 25)\n"
        "   math.sqrt(9) = 3    (porque 3 × 3 = 9)\n"
        "   math.sqrt(2) ≈ 1.4142\n\n"
        "• Importante: No se puede calcular la raíz cuadrada de números negativos.\n"
        "• ¿Cuándo usarlo?: En geometría (para calcular lados de triángulos), "
        "física, estadística y cualquier cálculo que involucre potencias."
    )
    
    # Limpiar y configurar la interfaz para math.sqrt()
    limpiar_contenido()
    
    # Título
    tk.Label(frame_contenido, 
             text="RAÍZ CUADRADA - math.sqrt()",
             bg=COLOR_FONDO,
             fg=COLOR_EXPLICACION,
             font=('Arial', 14, 'bold')).pack(pady=(0, 20))
    
    # Frame para entrada de datos
    frame_entrada = tk.Frame(frame_contenido, bg=COLOR_FONDO)
    frame_entrada.pack(pady=10)
    
    tk.Label(frame_entrada, 
             text="Ingresa un número positivo:",
             bg=COLOR_FONDO,
             fg=COLOR_TEXTO_SECUNDARIO).pack()
    
    global entry_numero
    entry_numero = tk.Entry(frame_entrada, 
                           font=('Arial', 12),
                           width=20,
                           justify='center')
    entry_numero.pack(pady=10)
    entry_numero.focus()
    
    # Botón para calcular
    crear_boton_con_hover(frame_entrada, 
                         "CALCULAR RAÍZ CUADRADA",
                         calcular_sqrt,
                         pack_info={'pady': 10})
    
    # Ejemplos
    frame_ejemplos = tk.Frame(frame_contenido, bg=COLOR_SECUNDARIO, padx=10, pady=10)
    frame_ejemplos.pack(pady=20)
    
    tk.Label(frame_ejemplos,
             text="Ejemplos para probar:",
             bg=COLOR_SECUNDARIO,
             fg=COLOR_TEXTO,
             font=('Arial', 10, 'bold')).pack()
    
    ejemplos = ["25", "9", "2", "100", "16"]
    for ejemplo in ejemplos:
        boton_ejemplo = tk.Button(frame_ejemplos,
                                  text=ejemplo,
                                  command=lambda e=ejemplo: entry_numero.insert(0, e),
                                  bg=COLOR_SECUNDARIO,
                                  fg=COLOR_EXPLICACION,
                                  relief='flat',
                                  cursor='hand2')
        boton_ejemplo.pack(side='left', padx=5)

def calcular_sqrt():
    """Calcula la raíz cuadrada del número ingresado"""
    global entry_numero
    
    entrada = entry_numero.get()
    
    if not entrada:
        mostrar_resultado("Por favor, ingresa un número", "red")
        return
    
    if not validar_numero(entrada):
        mostrar_resultado("¡Error! Debes ingresar un número válido", "red")
        return
    
    numero = float(entrada)
    
    if numero < 0:
        mostrar_resultado("¡Error! No existe raíz cuadrada de números negativos", "red")
        return
    
    resultado = math.sqrt(numero)
    mostrar_resultado(f"math.sqrt({numero}) = {resultado}")

def explicar_math_pi():
    """Muestra la explicación de math.pi"""
    mostrar_explicacion(
        "CONSTANTE MATH.PI - NÚMERO π (PI)\n\n"
        "• ¿Qué es?: Es una constante matemática que representa la relación "
        "entre la circunferencia de un círculo y su diámetro.\n"
        "• Valor aproximado: π ≈ 3.141592653589793\n"
        "• ¿Por qué es importante?: Es fundamental en geometría, trigonometría, "
        "física, ingeniería y muchas otras áreas de la ciencia.\n"
        "• Ejemplos de uso:\n"
        "   - Área de un círculo: π × radio²\n"
        "   - Circunferencia: 2 × π × radio\n"
        "   - Volumen de una esfera: (4/3) × π × radio³\n\n"
        "• Curiosidad: π es un número irracional, lo que significa que tiene "
        "infinitos decimales que no siguen un patrón repetitivo."
    )
    
    # Limpiar y configurar la interfaz para math.pi
    limpiar_contenido()
    
    # Título
    tk.Label(frame_contenido, 
             text="CONSTANTE PI - math.pi",
             bg=COLOR_FONDO,
             fg=COLOR_EXPLICACION,
             font=('Arial', 14, 'bold')).pack(pady=(0, 20))
    
    # Mostrar el valor de pi
    frame_pi = tk.Frame(frame_contenido, bg=COLOR_SECUNDARIO, padx=20, pady=20)
    frame_pi.pack(pady=10)
    
    tk.Label(frame_pi,
             text="π ≈",
             bg=COLOR_SECUNDARIO,
             fg=COLOR_TEXTO,
             font=('Arial', 16, 'bold')).pack(side='left')
    
    tk.Label(frame_pi,
             text=str(math.pi),
             bg=COLOR_SECUNDARIO,
             fg=COLOR_EXPLICACION,
             font=('Arial', 16)).pack(side='left', padx=10)
    
    # Frame para cálculos con pi
    frame_calculos = tk.Frame(frame_contenido, bg=COLOR_FONDO)
    frame_calculos.pack(pady=20)
    
    tk.Label(frame_calculos,
             text="Calcula con π:",
             bg=COLOR_FONDO,
             fg=COLOR_TEXTO_SECUNDARIO,
             font=('Arial', 11, 'bold')).pack()
    
    # Botones para cálculos comunes con pi
    frame_botones_pi = tk.Frame(frame_calculos, bg=COLOR_FONDO)
    frame_botones_pi.pack(pady=10)
    
    def calcular_area_circulo():
        global entry_numero
        radio = entry_numero.get() if entry_numero else "1"
        
        if not validar_numero(radio):
            radio = 1
        else:
            radio = float(radio)
        
        area = math.pi * math.pow(radio, 2)
        mostrar_resultado(f"Área círculo (radio={radio}) = {area:.4f}")
    
    def calcular_circunferencia():
        global entry_numero
        radio = entry_numero.get() if entry_numero else "1"
        
        if not validar_numero(radio):
            radio = 1
        else:
            radio = float(radio)
        
        circunferencia = 2 * math.pi * radio
        mostrar_resultado(f"Circunferencia (radio={radio}) = {circunferencia:.4f}")
    
    # Entrada para radio
    tk.Label(frame_botones_pi,
             text="Radio:",
             bg=COLOR_FONDO,
             fg=COLOR_TEXTO_SECUNDARIO).grid(row=0, column=0, padx=5, pady=5)
    
    entry_numero = tk.Entry(frame_botones_pi, 
                           font=('Arial', 12),
                           width=10,
                           justify='center')
    entry_numero.grid(row=0, column=1, padx=5, pady=5)
    entry_numero.insert(0, "1")
    
    # Botones para cálculos
    crear_boton_con_hover(frame_botones_pi,
                         "Área del círculo",
                         calcular_area_circulo,
                         grid_info={'row': 1, 'column': 0, 'padx': 5, 'pady': 5})
    
    crear_boton_con_hover(frame_botones_pi,
                         "Circunferencia",
                         calcular_circunferencia,
                         grid_info={'row': 1, 'column': 1, 'padx': 5, 'pady': 5})

def explicar_math_pow():
    """Muestra la explicación y funcionalidad de math.pow()"""
    mostrar_explicacion(
        "FUNCIÓN MATH.POW() - POTENCIA\n\n"
        "• ¿Qué hace?: Calcula la potencia de un número.\n"
        "• ¿Qué es una potencia?: Es la multiplicación repetida de un número por sí mismo.\n"
        "• Sintaxis: math.pow(base, exponente)\n"
        "• Ejemplos:\n"
        "   math.pow(2, 3) = 8      (2 × 2 × 2 = 8)\n"
        "   math.pow(5, 2) = 25     (5 × 5 = 25)\n"
        "   math.pow(10, 0) = 1     (cualquier número elevado a 0 es 1)\n\n"
        "• ¿Cuándo usarlo?: En cálculos científicos, financieros (interés compuesto), "
        "geometría (áreas y volúmenes), y cualquier situación que involucre crecimiento exponencial."
    )
    
    # Limpiar y configurar la interfaz para math.pow()
    limpiar_contenido()
    
    # Título
    tk.Label(frame_contenido, 
             text="POTENCIA - math.pow()",
             bg=COLOR_FONDO,
             fg=COLOR_EXPLICACION,
             font=('Arial', 14, 'bold')).pack(pady=(0, 20))
    
    # Frame para entrada de datos
    frame_entrada = tk.Frame(frame_contenido, bg=COLOR_FONDO)
    frame_entrada.pack(pady=10)
    
    # Entrada para la base
    tk.Label(frame_entrada, 
             text="Base:",
             bg=COLOR_FONDO,
             fg=COLOR_TEXTO_SECUNDARIO).grid(row=0, column=0, padx=5, pady=5)
    
    global entry_numero
    entry_numero = tk.Entry(frame_entrada, 
                           font=('Arial', 12),
                           width=15,
                           justify='center')
    entry_numero.grid(row=0, column=1, padx=5, pady=5)
    
    # Entrada para el exponente
    tk.Label(frame_entrada, 
             text="Exponente:",
             bg=COLOR_FONDO,
             fg=COLOR_TEXTO_SECUNDARIO).grid(row=1, column=0, padx=5, pady=5)
    
    global entry_numero2
    entry_numero2 = tk.Entry(frame_entrada, 
                            font=('Arial', 12),
                            width=15,
                            justify='center')
    entry_numero2.grid(row=1, column=1, padx=5, pady=5)
    
    # Botón para calcular
    crear_boton_con_hover(frame_entrada, 
                         "CALCULAR POTENCIA",
                         calcular_pow,
                         grid_info={'row': 2, 'column': 0, 'columnspan': 2, 'pady': 10})
    
    # Ejemplos comunes
    frame_ejemplos = tk.Frame(frame_contenido, bg=COLOR_SECUNDARIO, padx=10, pady=10)
    frame_ejemplos.pack(pady=20)
    
    tk.Label(frame_ejemplos,
             text="Ejemplos comunes:",
             bg=COLOR_SECUNDARIO,
             fg=COLOR_TEXTO,
             font=('Arial', 10, 'bold')).pack()
    
    ejemplos = [("2", "3", "2³ = 8"), ("5", "2", "5² = 25"), ("10", "0", "10⁰ = 1"), ("3", "4", "3⁴ = 81")]
    
    for base, exp, texto in ejemplos:
        frame_ejemplo = tk.Frame(frame_ejemplos, bg=COLOR_SECUNDARIO)
        frame_ejemplo.pack(pady=5)
        
        tk.Label(frame_ejemplo,
                 text=texto,
                 bg=COLOR_SECUNDARIO,
                 fg=COLOR_TEXTO_SECUNDARIO).pack(side='left', padx=5)
        
        boton_ejemplo = tk.Button(frame_ejemplo,
                                  text="Probar",
                                  command=lambda b=base, e=exp: cargar_ejemplo_pow(b, e),
                                  bg=COLOR_SECUNDARIO,
                                  fg=COLOR_EXPLICACION,
                                  relief='flat',
                                  cursor='hand2')
        boton_ejemplo.pack(side='left', padx=5)

def cargar_ejemplo_pow(base, exponente):
    """Carga un ejemplo en los campos de pow()"""
    global entry_numero, entry_numero2
    entry_numero.delete(0, tk.END)
    entry_numero.insert(0, base)
    entry_numero2.delete(0, tk.END)
    entry_numero2.insert(0, exponente)

def calcular_pow():
    """Calcula la potencia de los números ingresados"""
    global entry_numero, entry_numero2
    
    entrada_base = entry_numero.get()
    entrada_exp = entry_numero2.get()
    
    if not entrada_base or not entrada_exp:
        mostrar_resultado("Por favor, ingresa base y exponente", "red")
        return
    
    if not validar_numero(entrada_base) or not validar_numero(entrada_exp):
        mostrar_resultado("¡Error! Ambos valores deben ser números", "red")
        return
    
    base = float(entrada_base)
    exponente = float(entrada_exp)
    
    resultado = math.pow(base, exponente)
    mostrar_resultado(f"math.pow({base}, {exponente}) = {resultado}")

def explicar_funciones_redondeo():
    """Muestra la explicación de ceil(), floor() y trunc()"""
    mostrar_explicacion(
        "FUNCIONES DE REDONDEO ESPECIALES\n\n"
        "1. MATH.CEIL() - REDONDEO HACIA ARRIBA\n"
        "   • ¿Qué hace?: Devuelve el entero más pequeño mayor o igual al número.\n"
        "   • Ejemplos:\n"
        "     math.ceil(3.2) = 4\n"
        "     math.ceil(5.9) = 6\n"
        "     math.ceil(-2.3) = -2\n\n"
        
        "2. MATH.FLOOR() - REDONDEO HACIA ABAJO\n"
        "   • ¿Qué hace?: Devuelve el entero más grande menor o igual al número.\n"
        "   • Ejemplos:\n"
        "     math.floor(3.8) = 3\n"
        "     math.floor(5.1) = 5\n"
        "     math.floor(-2.7) = -3\n\n"
        
        "3. MATH.TRUNC() - TRUNCAMIENTO\n"
        "   • ¿Qué hace?: Elimina la parte decimal sin redondear.\n"
        "   • Ejemplos:\n"
        "     math.trunc(3.8) = 3\n"
        "     math.trunc(5.1) = 5\n"
        "     math.trunc(-2.7) = -2\n\n"
        
        "• Diferencia clave: ceil() siempre redondea hacia arriba, "
        "floor() siempre hacia abajo, y trunc() simplemente quita los decimales."
    )
    
    # Limpiar y configurar la interfaz para las funciones de redondeo
    limpiar_contenido()
    
    # Título
    tk.Label(frame_contenido, 
             text="REDONDEO ESPECIAL - ceil(), floor(), trunc()",
             bg=COLOR_FONDO,
             fg=COLOR_EXPLICACION,
             font=('Arial', 14, 'bold')).pack(pady=(0, 20))
    
    # Frame para entrada de datos
    frame_entrada = tk.Frame(frame_contenido, bg=COLOR_FONDO)
    frame_entrada.pack(pady=10)
    
    tk.Label(frame_entrada, 
             text="Ingresa un número (puede tener decimales):",
             bg=COLOR_FONDO,
             fg=COLOR_TEXTO_SECUNDARIO).pack()
    
    global entry_numero
    entry_numero = tk.Entry(frame_entrada, 
                           font=('Arial', 12),
                           width=20,
                           justify='center')
    entry_numero.pack(pady=10)
    entry_numero.focus()
    
    # Frame para botones de funciones
    frame_botones = tk.Frame(frame_contenido, bg=COLOR_FONDO)
    frame_botones.pack(pady=10)
    
    # Botones para cada función
    crear_boton_con_hover(frame_botones,
                         "math.ceil()",
                         lambda: calcular_redondeo("ceil"),
                         pack_info={'side': 'left', 'padx': 5})
    
    crear_boton_con_hover(frame_botones,
                         "math.floor()",
                         lambda: calcular_redondeo("floor"),
                         pack_info={'side': 'left', 'padx': 5})
    
    crear_boton_con_hover(frame_botones,
                         "math.trunc()",
                         lambda: calcular_redondeo("trunc"),
                         pack_info={'side': 'left', 'padx': 5})
    
    # Ejemplos
    frame_ejemplos = tk.Frame(frame_contenido, bg=COLOR_SECUNDARIO, padx=10, pady=10)
    frame_ejemplos.pack(pady=20)
    
    tk.Label(frame_ejemplos,
             text="Comparación de funciones (usando 3.7 y -2.3):",
             bg=COLOR_SECUNDARIO,
             fg=COLOR_TEXTO,
             font=('Arial', 10, 'bold')).pack()
    
    # Tabla de comparación
    frame_tabla = tk.Frame(frame_ejemplos, bg=COLOR_SECUNDARIO)
    frame_tabla.pack(pady=10)
    
    # Encabezados
    encabezados = ["Función", "3.7", "-2.3"]
    for i, texto in enumerate(encabezados):
        tk.Label(frame_tabla,
                 text=texto,
                 bg=COLOR_SECUNDARIO,
                 fg=COLOR_TEXTO,
                 font=('Arial', 10, 'bold'),
                 width=15).grid(row=0, column=i, padx=5, pady=2)
    
    # Datos
    datos = [
        ("ceil()", "4", "-2"),
        ("floor()", "3", "-3"),
        ("trunc()", "3", "-2")
    ]
    
    for i, (funcion, val1, val2) in enumerate(datos, start=1):
        tk.Label(frame_tabla,
                 text=funcion,
                 bg=COLOR_SECUNDARIO,
                 fg=COLOR_EXPLICACION).grid(row=i, column=0, padx=5, pady=2)
        
        tk.Label(frame_tabla,
                 text=val1,
                 bg=COLOR_SECUNDARIO,
                 fg=COLOR_TEXTO_SECUNDARIO).grid(row=i, column=1, padx=5, pady=2)
        
        tk.Label(frame_tabla,
                 text=val2,
                 bg=COLOR_SECUNDARIO,
                 fg=COLOR_TEXTO_SECUNDARIO).grid(row=i, column=2, padx=5, pady=2)

def calcular_redondeo(funcion):
    """Calcula el redondeo según la función especificada"""
    global entry_numero
    
    entrada = entry_numero.get()
    
    if not entrada:
        mostrar_resultado("Por favor, ingresa un número", "red")
        return
    
    if not validar_numero(entrada):
        mostrar_resultado("¡Error! Debes ingresar un número válido", "red")
        return
    
    numero = float(entrada)
    
    if funcion == "ceil":
        resultado = math.ceil(numero)
        mostrar_resultado(f"math.ceil({numero}) = {resultado}")
    elif funcion == "floor":
        resultado = math.floor(numero)
        mostrar_resultado(f"math.floor({numero}) = {resultado}")
    elif funcion == "trunc":
        resultado = math.trunc(numero)
        mostrar_resultado(f"math.trunc({numero}) = {resultado}")

# ==============================================
# FUNCIONES PARA LA INTERFAZ PRINCIPAL
# ==============================================

def crear_interfaz():
    """Crea y configura la interfaz gráfica principal"""
    global ventana_principal, frame_contenido, texto_explicacion, label_resultado
    
    # Crear ventana principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Juego Educativo: Funciones Matemáticas en Python")
    ventana_principal.configure(bg=COLOR_FONDO)
    
    # Configurar el tamaño y centrar la ventana
    ancho_ventana = 1200
    alto_ventana = 700
    
    # Obtener dimensiones de la pantalla
    ancho_pantalla = ventana_principal.winfo_screenwidth()
    alto_pantalla = ventana_principal.winfo_screenheight()
    
    # Calcular posición para centrar
    x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    y = (alto_pantalla // 2) - (alto_ventana // 2)
    
    ventana_principal.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    ventana_principal.resizable(False, False)
    
    # Configurar estilo
    configurar_estilo()
    
    # ==============================================
    # CABECERA
    # ==============================================
    
    frame_cabecera = tk.Frame(ventana_principal, bg=COLOR_FONDO)
    frame_cabecera.pack(fill='x', padx=20, pady=10)
    
    # Título principal
    tk.Label(frame_cabecera,
             text="🎓 EXPLORANDO FUNCIONES MATEMÁTICAS 🎓",
             bg=COLOR_FONDO,
             fg=COLOR_TEXTO,
             font=('Arial', 18, 'bold')).pack()
    
    tk.Label(frame_cabecera,
             text="Aprende y practica con funciones matemáticas de Python",
             bg=COLOR_FONDO,
             fg=COLOR_TEXTO_SECUNDARIO,
             font=('Arial', 12)).pack(pady=(5, 0))
    
    # ==============================================
    # MENÚ LATERAL (FUNCIONES)
    # ==============================================
    
    frame_menu = tk.Frame(ventana_principal, bg=COLOR_SECUNDARIO)
    frame_menu.pack(side='left', fill='y', padx=(20, 10), pady=10)
    
    tk.Label(frame_menu,
             text="FUNCIONES DISPONIBLES",
             bg=COLOR_SECUNDARIO,
             fg=COLOR_TEXTO,
             font=('Arial', 12, 'bold')).pack(pady=(10, 20))
    
    # Lista de funciones con sus botones
    funciones = [
        ("abs() - Valor absoluto", explicar_abs),
        ("round() - Redondeo", explicar_round),
        ("math.sqrt() - Raíz cuadrada", explicar_math_sqrt),
        ("math.pi - Constante π", explicar_math_pi),
        ("math.pow() - Potencia", explicar_math_pow),
        ("ceil(), floor(), trunc()", explicar_funciones_redondeo)
    ]
    
    for texto, comando in funciones:
        crear_boton_con_hover(frame_menu,
                             texto,
                             comando,
                             pack_info={'fill': 'x', 'padx': 10, 'pady': 5})
    
    # ==============================================
    # ÁREA DE CONTENIDO PRINCIPAL
    # ==============================================
    
    # Frame principal para contenido
    frame_principal = tk.Frame(ventana_principal, bg=COLOR_FONDO)
    frame_principal.pack(side='left', fill='both', expand=True, padx=(0, 20), pady=10)
    
    # Área de explicación (con scrollbar)
    frame_explicacion = tk.Frame(frame_principal, bg=COLOR_SECUNDARIO)
    frame_explicacion.pack(fill='both', expand=True, pady=(0, 10))
    
    tk.Label(frame_explicacion,
             text="EXPLICACIÓN",
             bg=COLOR_SECUNDARIO,
             fg=COLOR_TEXTO,
             font=('Arial', 12, 'bold')).pack(pady=10)
    
    # Scrollbar para el texto de explicación
    scrollbar_explicacion = tk.Scrollbar(frame_explicacion)
    scrollbar_explicacion.pack(side='right', fill='y')
    
    # Texto de explicación
    texto_explicacion = tk.Text(frame_explicacion,
                                wrap='word',
                                height=8,
                                bg=COLOR_SECUNDARIO,
                                fg=COLOR_TEXTO_SECUNDARIO,
                                font=('Arial', 10),
                                relief='flat',
                                yscrollcommand=scrollbar_explicacion.set)
    texto_explicacion.pack(side='left', fill='both', expand=True, padx=10, pady=(0, 10))
    texto_explicacion.config(state='disabled')
    
    scrollbar_explicacion.config(command=texto_explicacion.yview)
    
    # Frame para contenido interactivo (se llenará dinámicamente)
    frame_contenido = tk.Frame(frame_principal, bg=COLOR_FONDO)
    frame_contenido.pack(fill='both', expand=True, pady=10)
    
    # Área de resultados
    frame_resultado = tk.Frame(frame_principal, bg=COLOR_SECUNDARIO, height=50)
    frame_resultado.pack(fill='x', pady=(10, 0))
    frame_resultado.pack_propagate(False)  # Mantener el tamaño fijo
    
    tk.Label(frame_resultado,
             text="RESULTADO",
             bg=COLOR_SECUNDARIO,
             fg=COLOR_TEXTO,
             font=('Arial', 12, 'bold')).pack(pady=(10, 5))
    
    label_resultado = tk.Label(frame_resultado,
                               text="Aquí aparecerán los resultados de tus cálculos",
                               bg=COLOR_SECUNDARIO,
                               fg=COLOR_EXITO,
                               font=('Arial', 11))
    label_resultado.pack(pady=(0, 10))
    
    # ==============================================
    # PIE DE PÁGINA
    # ==============================================
    
    frame_pie = tk.Frame(ventana_principal, bg=COLOR_FONDO)
    frame_pie.pack(side='bottom', fill='x', padx=20, pady=10)
    
    tk.Label(frame_pie,
             text="🎯 Objetivo educativo: Comprender y practicar funciones matemáticas esenciales en Python",
             bg=COLOR_FONDO,
             fg=COLOR_TEXTO_SECUNDARIO,
             font=('Arial', 9)).pack()
    
    tk.Label(frame_pie,
             text="Desarrollado para estudiantes de bachillerato | ¡Aprende divirtiéndote!",
             bg=COLOR_FONDO,
             fg=COLOR_TEXTO_SECUNDARIO,
             font=('Arial', 8)).pack(pady=(5, 0))
    
    # Mostrar explicación inicial
    mostrar_explicacion(
        "¡BIENVENIDO AL JUEGO EDUCATIVO DE FUNCIONES MATEMÁTICAS!\n\n"
        "Este juego te ayudará a comprender y practicar con las funciones matemáticas más importantes de Python.\n\n"
        "📚 ¿CÓMO USAR ESTA APLICACIÓN?\n"
        "1. Selecciona una función del menú lateral\n"
        "2. Lee la explicación detallada en esta área\n"
        "3. Ingresa valores en los campos correspondientes\n"
        "4. Haz clic en los botones para ver los resultados\n"
        "5. ¡Experimenta con diferentes valores!\n\n"
        "🎯 CONSEJO: No te limites a los ejemplos. Prueba tus propios números y observa qué sucede."
    )
    
    # Iniciar con la primera función
    explicar_abs()
    
    # Iniciar el bucle principal de la aplicación
    ventana_principal.mainloop()

# ==============================================
# PUNTO DE ENTRADA PRINCIPAL
# ==============================================

if __name__ == "__main__":
    crear_interfaz()