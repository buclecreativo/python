import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, date
import calendar

# ============================================
# CONFIGURACIÓN INICIAL Y CONSTANTES
# ============================================

# Paleta de colores 
COLOR_FONDO = "#F0F7FF"  # Azul muy claro
COLOR_PRIMARIO = "#4361EE"  # Azul vibrante
COLOR_SECUNDARIO = "#3A0CA3"  # Azul oscuro
COLOR_TERCIARIO = "#4CC9F0"  # Azul claro
COLOR_BOTON_NORMAL = "#7209B7"  # Púrpura
COLOR_BOTON_HOVER = "#560BAD"  # Púrpura oscuro
COLOR_TEXTO = "#2B2D42"  # Gris azulado oscuro
COLOR_RESALTADO = "#F72585"  # Rosa vibrante
COLOR_EXPLICACION = "#4A4E69"  # Gris medio

# Configuración de la ventana principal
ANCHO_VENTANA = 900
ALTO_VENTANA = 860

# ============================================
# FUNCIONES DE CÁLCULO
# ============================================

def calcular_edad_completa(fecha_nacimiento):
    """
    Calcula la edad exacta en años, meses y días.
    
    Args:
        fecha_nacimiento (datetime): Fecha de nacimiento
    
    Returns:
        dict: Diccionario con años, meses y días
    """
    hoy = date.today()
    
    # Calcular años
    anios = hoy.year - fecha_nacimiento.year
    
    # Calcular meses
    meses = hoy.month - fecha_nacimiento.month
    if meses < 0:
        meses += 12
        anios -= 1
    
    # Calcular días
    dias = hoy.day - fecha_nacimiento.day
    if dias < 0:
        # Obtener el número de días del mes anterior
        mes_anterior = hoy.month - 1 if hoy.month > 1 else 12
        año_anterior = hoy.year if hoy.month > 1 else hoy.year - 1
        dias_en_mes_anterior = calendar.monthrange(año_anterior, mes_anterior)[1]
        dias += dias_en_mes_anterior
        meses -= 1
        if meses < 0:
            meses += 12
            anios -= 1
    
    return {"años": anios, "meses": meses, "dias": dias}

def obtener_signo_zodiacal(dia, mes):
    """
    Determina el signo zodiacal según la fecha de nacimiento.
    
    Args:
        dia (int): Día de nacimiento
        mes (int): Mes de nacimiento
    
    Returns:
        str: Signo zodiacal
    """
    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Acuario ♒"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Piscis ♓"
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Aries ♈"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Tauro ♉"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Géminis ♊"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Cáncer ♋"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leo ♌"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgo ♍"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra ♎"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpio ♏"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitario ♐"
    else:
        return "Capricornio ♑"

def obtener_dia_semana(fecha):
    """
    Determina el día de la semana en que nació una persona.
    
    Args:
        fecha (datetime): Fecha de nacimiento
    
    Returns:
        str: Día de la semana en español
    """
    dias_semana = [
        "Lunes", "Martes", "Miércoles", "Jueves", 
        "Viernes", "Sábado", "Domingo"
    ]
    return dias_semana[fecha.weekday()]

def formatear_fecha_larga(fecha):
    """
    Formatea una fecha en un formato legible en español.
    
    Args:
        fecha (datetime): Fecha a formatear
    
    Returns:
        str: Fecha formateada
    """
    meses = [
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]
    return f"{fecha.day} de {meses[fecha.month-1]} de {fecha.year}"

# ============================================
# FUNCIONES DE INTERFAZ Y EVENTOS
# ============================================

def crear_estilo_botones():
    """Configura el estilo de los botones con efecto hover"""
    # Estilo para botones normales
    estilo_boton = ttk.Style()
    estilo_boton.configure(
        "Boton.TButton",
        background=COLOR_BOTON_NORMAL,
        foreground="white",
        font=("Arial", 11, "bold"),
        borderwidth=0,
        focuscolor="none",
        relief="flat",
        padding=10
    )
    
    # Estilo para botones cuando el cursor está sobre ellos
    estilo_boton.map(
        "Boton.TButton",
        background=[("active", COLOR_BOTON_HOVER), ("pressed", COLOR_BOTON_HOVER)],
        relief=[("pressed", "flat")]
    )

def crear_boton_con_hover(parent, texto, comando, row, column, padx=5, pady=5, columnspan=1):
    """
    Crea un botón con efecto hover personalizado usando grid para mejor posicionamiento.
    
    Args:
        parent: Widget padre
        texto (str): Texto del botón
        comando: Función a ejecutar al hacer clic
        row (int): Fila en grid
        column (int): Columna en grid
        padx (int): Espaciado horizontal
        pady (int): Espaciado vertical
        columnspan (int): Número de columnas que ocupa
    """
    boton = ttk.Button(
        parent, 
        text=texto, 
        command=comando, 
        style="Boton.TButton",
        width=20
    )
    boton.grid(row=row, column=column, padx=padx, pady=pady, columnspan=columnspan)
    
    return boton

def validar_fecha(dia_str, mes_str, año_str):
    """
    Valida que la fecha ingresada sea correcta.
    
    Args:
        dia_str (str): Día como string
        mes_str (str): Mes como string
        año_str (str): Año como string
    
    Returns:
        tuple: (bool, datetime o str) - Si es válida y la fecha o mensaje de error
    """
    try:
        # Convertir a enteros
        dia = int(dia_str)
        mes = int(mes_str)
        año = int(año_str)
        
        # Validar rango de años (entre 1900 y el año actual)
        año_actual = date.today().year
        if año < 1900 or año > año_actual:
            return False, f"El año debe estar entre 1900 y {año_actual}"
        
        # Validar mes
        if mes < 1 or mes > 12:
            return False, "El mes debe estar entre 1 y 12"
        
        # Validar día según el mes
        dias_en_mes = calendar.monthrange(año, mes)[1]
        if dia < 1 or dia > dias_en_mes:
            return False, f"Para el mes {mes}, el día debe estar entre 1 y {dias_en_mes}"
        
        # Validar que no sea una fecha futura
        fecha_ingresada = date(año, mes, dia)
        if fecha_ingresada > date.today():
            return False, "La fecha no puede ser futura"
        
        return True, fecha_ingresada
        
    except ValueError:
        return False, "Por favor, ingresa valores numéricos válidos"

def calcular_datos():
    """Función principal que calcula y muestra todos los datos"""
    # Obtener los valores de los campos de entrada
    dia = entrada_dia.get()
    mes = entrada_mes.get()
    anio = entrada_año.get()
    
    # Validar que todos los campos estén completos
    if not (dia and mes and anio):
        messagebox.showerror("Error", "Por favor, completa todos los campos")
        return
    
    # Validar la fecha
    es_valida, resultado = validar_fecha(dia, mes, anio)
    
    if not es_valida:
        messagebox.showerror("Error", resultado)
        return
    
    fecha_nacimiento = resultado
    
    # Calcular todos los datos
    edad = calcular_edad_completa(fecha_nacimiento)
    signo = obtener_signo_zodiacal(fecha_nacimiento.day, fecha_nacimiento.month)
    dia_semana = obtener_dia_semana(fecha_nacimiento)
    fecha_formateada = formatear_fecha_larga(fecha_nacimiento)
    
    # Mostrar resultados en las etiquetas correspondientes
    resultado_fecha.config(text=fecha_formateada)
    resultado_edad.config(
        text=f"{edad['años']} años, {edad['meses']} meses y {edad['dias']} días"
    )
    resultado_signo.config(text=signo)
    resultado_dia_semana.config(text=dia_semana)
    
    # Actualizar el título del área de resultados
    titulo_resultados.config(text=f"RESULTADOS PARA TU FECHA DE NACIMIENTO")

def limpiar_campos():
    """Limpia todos los campos de entrada y resultados"""
    entrada_dia.delete(0, tk.END)
    entrada_mes.delete(0, tk.END)
    entrada_año.delete(0, tk.END)
    
    resultado_fecha.config(text="---")
    resultado_edad.config(text="---")
    resultado_signo.config(text="---")
    resultado_dia_semana.config(text="---")
    
    # Restaurar el título del área de resultados
    titulo_resultados.config(text="INGRESA TU FECHA DE NACIMIENTO PARA VER LOS RESULTADOS")

def mostrar_explicacion_signos():
    """Muestra una ventana emergente con la explicación de los signos zodiacales"""
    explicacion = """
    LOS SIGNOS ZODIACALES:
    
    • Aries ♈ (21 mar - 19 abr): Energético y decidido
    • Tauro ♉ (20 abr - 20 may): Práctico y confiable
    • Géminis ♊ (21 may - 20 jun): Adaptable y comunicativo
    • Cáncer ♋ (21 jun - 22 jul): Emocional y protector
    • Leo ♌ (23 jul - 22 ago): Creativo y extrovertido
    • Virgo ♍ (23 ago - 22 sep): Analítico y meticuloso
    • Libra ♎ (23 sep - 22 oct): Diplomático y social
    • Escorpio ♏ (23 oct - 21 nov): Intenso y apasionado
    • Sagitario ♐ (22 nov - 21 dic): Optimista y aventurero
    • Capricornio ♑ (22 dic - 19 ene): Disciplinado y ambicioso
    • Acuario ♒ (20 ene - 18 feb): Innovador e independiente
    • Piscis ♓ (19 feb - 20 mar): Empático e intuitivo
    
    Cada signo zodiacal corresponde a un período del año 
    basado en la posición del Sol en el momento del nacimiento.
    """
    
    ventana_explicacion = tk.Toplevel(ventana)
    ventana_explicacion.title("Explicación de Signos Zodiacales")
    ventana_explicacion.geometry("500x500")
    ventana_explicacion.configure(bg=COLOR_FONDO)
    ventana_explicacion.resizable(False, False)
    
    # Centrar la ventana emergente
    ventana_explicacion.update_idletasks()
    ancho = ventana_explicacion.winfo_width()
    alto = ventana_explicacion.winfo_height()
    x = (ventana_explicacion.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana_explicacion.winfo_screenheight() // 2) - (alto // 2)
    ventana_explicacion.geometry(f"{ancho}x{alto}+{x}+{y}")
    
    # Título
    titulo = tk.Label(
        ventana_explicacion,
        text="EXPLICACIÓN DE SIGNOS ZODIACALES",
        font=("Arial", 16, "bold"),
        bg=COLOR_PRIMARIO,
        fg="white",
        pady=10
    )
    titulo.pack(fill=tk.X, padx=10, pady=(10, 0))
    
    # Texto de explicación
    texto = tk.Label(
        ventana_explicacion,
        text=explicacion,
        font=("Arial", 11),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO,
        justify=tk.LEFT,
        padx=20,
        pady=20
    )
    texto.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Botón para cerrar
    boton_cerrar = ttk.Button(
        ventana_explicacion,
        text="Cerrar",
        command=ventana_explicacion.destroy,
        style="Boton.TButton",
        width=15
    )
    boton_cerrar.pack(pady=(0, 15))

# ============================================
# CONFIGURACIÓN DE LA VENTANA PRINCIPAL
# ============================================

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Educativa: Edad, Signo Zodiacal y Día de Nacimiento")
ventana.geometry(f"{ANCHO_VENTANA}x{ALTO_VENTANA}")
ventana.configure(bg=COLOR_FONDO)
ventana.resizable(False, False)

# Centrar la ventana en la pantalla
ventana.update_idletasks()
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
x = (ancho_pantalla // 2) - (ANCHO_VENTANA // 2)
y = (alto_pantalla // 2) - (ALTO_VENTANA // 2)
ventana.geometry(f"{ANCHO_VENTANA}x{ALTO_VENTANA}+{x}+{y}")

# Configurar estilo de botones
crear_estilo_botones()

# ============================================
# INTERFAZ GRÁFICA
# ============================================

# Título principal
titulo_principal = tk.Label(
    ventana,
    text="CALCULADORA EDUCATIVA DE DATOS PERSONALES",
    font=("Arial", 20, "bold"),
    bg=COLOR_PRIMARIO,
    fg="white",
    pady=15
)
titulo_principal.pack(fill=tk.X, padx=10, pady=10)

# Marco para la entrada de datos
marco_entrada = tk.Frame(
    ventana,
    bg=COLOR_FONDO,
    highlightbackground=COLOR_SECUNDARIO,
    highlightthickness=2
)
marco_entrada.pack(pady=20, padx=50, fill=tk.BOTH, expand=True)

# Título del área de entrada
titulo_entrada = tk.Label(
    marco_entrada,
    text="INGRESA TU FECHA DE NACIMIENTO",
    font=("Arial", 16, "bold"),
    bg=COLOR_FONDO,
    fg=COLOR_SECUNDARIO,
    pady=10
)
titulo_entrada.pack()

# Instrucciones
instrucciones = tk.Label(
    marco_entrada,
    text="Ingresa el día, mes y año de tu nacimiento en los siguientes campos:",
    font=("Arial", 11),
    bg=COLOR_FONDO,
    fg=COLOR_EXPLICACION,
    pady=5
)
instrucciones.pack()

# Marco para los campos de entrada
marco_campos = tk.Frame(marco_entrada, bg=COLOR_FONDO)
marco_campos.pack(pady=15)

# Campo para el día
tk.Label(
    marco_campos,
    text="DÍA (1-31):",
    font=("Arial", 11, "bold"),
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO
).grid(row=0, column=0, padx=5, pady=5, sticky="e")

entrada_dia = tk.Entry(
    marco_campos,
    font=("Arial", 12),
    width=10,
    justify="center",
    bg="white",
    fg=COLOR_TEXTO,
    relief="solid",
    bd=1
)
entrada_dia.grid(row=0, column=1, padx=5, pady=5)

# Campo para el mes
tk.Label(
    marco_campos,
    text="MES (1-12):",
    font=("Arial", 11, "bold"),
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO
).grid(row=0, column=2, padx=5, pady=5, sticky="e")

entrada_mes = tk.Entry(
    marco_campos,
    font=("Arial", 12),
    width=10,
    justify="center",
    bg="white",
    fg=COLOR_TEXTO,
    relief="solid",
    bd=1
)
entrada_mes.grid(row=0, column=3, padx=5, pady=5)

# Campo para el año
tk.Label(
    marco_campos,
    text="AÑO (1900-actual):",
    font=("Arial", 11, "bold"),
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO
).grid(row=0, column=4, padx=5, pady=5, sticky="e")

entrada_año = tk.Entry(
    marco_campos,
    font=("Arial", 12),
    width=15,
    justify="center",
    bg="white",
    fg=COLOR_TEXTO,
    relief="solid",
    bd=1
)
entrada_año.grid(row=0, column=5, padx=5, pady=5)

# Marco para botones de acción
marco_botones_accion = tk.Frame(marco_entrada, bg=COLOR_FONDO)
marco_botones_accion.pack(pady=20)

# Botón Calcular
boton_calcular = ttk.Button(
    marco_botones_accion,
    text="📊 CALCULAR DATOS",
    command=calcular_datos,
    style="Boton.TButton",
    width=25
)
boton_calcular.grid(row=0, column=0, padx=15, pady=5)

# Botón Limpiar
boton_limpiar = ttk.Button(
    marco_botones_accion,
    text="🔄 LIMPIAR CAMPOS",
    command=limpiar_campos,
    style="Boton.TButton",
    width=25
)
boton_limpiar.grid(row=0, column=1, padx=15, pady=5)

# Marco para los resultados
marco_resultados = tk.Frame(
    ventana,
    bg=COLOR_FONDO,
    highlightbackground=COLOR_TERCIARIO,
    highlightthickness=2
)
marco_resultados.pack(pady=20, padx=50, fill=tk.BOTH, expand=True)

# Título del área de resultados
titulo_resultados = tk.Label(
    marco_resultados,
    text="INGRESA TU FECHA DE NACIMIENTO PARA VER LOS RESULTADOS",
    font=("Arial", 16, "bold"),
    bg=COLOR_TERCIARIO,
    fg="white",
    pady=10
)
titulo_resultados.pack(fill=tk.X, padx=10, pady=(10, 0))

# Marco para mostrar los resultados
marco_datos_resultados = tk.Frame(marco_resultados, bg=COLOR_FONDO)
marco_datos_resultados.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Resultado: Fecha de nacimiento
frame_fecha = tk.Frame(marco_datos_resultados, bg=COLOR_FONDO)
frame_fecha.pack(fill=tk.X, pady=10)

tk.Label(
    frame_fecha,
    text="Fecha de nacimiento:",
    font=("Arial", 12, "bold"),
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO,
    width=20,
    anchor="w"
).pack(side=tk.LEFT)

resultado_fecha = tk.Label(
    frame_fecha,
    text="---",
    font=("Arial", 12),
    bg=COLOR_FONDO,
    fg=COLOR_RESALTADO,
    anchor="w"
)
resultado_fecha.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Resultado: Edad exacta
frame_edad = tk.Frame(marco_datos_resultados, bg=COLOR_FONDO)
frame_edad.pack(fill=tk.X, pady=10)

tk.Label(
    frame_edad,
    text="Edad exacta:",
    font=("Arial", 12, "bold"),
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO,
    width=20,
    anchor="w"
).pack(side=tk.LEFT)

resultado_edad = tk.Label(
    frame_edad,
    text="---",
    font=("Arial", 12),
    bg=COLOR_FONDO,
    fg=COLOR_RESALTADO,
    anchor="w"
)
resultado_edad.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Resultado: Signo zodiacal
frame_signo = tk.Frame(marco_datos_resultados, bg=COLOR_FONDO)
frame_signo.pack(fill=tk.X, pady=10)

tk.Label(
    frame_signo,
    text="Signo zodiacal:",
    font=("Arial", 12, "bold"),
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO,
    width=20,
    anchor="w"
).pack(side=tk.LEFT)

resultado_signo = tk.Label(
    frame_signo,
    text="---",
    font=("Arial", 12),
    bg=COLOR_FONDO,
    fg=COLOR_RESALTADO,
    anchor="w"
)
resultado_signo.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Resultado: Día de la semana
frame_dia_semana = tk.Frame(marco_datos_resultados, bg=COLOR_FONDO)
frame_dia_semana.pack(fill=tk.X, pady=10)

tk.Label(
    frame_dia_semana,
    text="Día de la semana:",
    font=("Arial", 12, "bold"),
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO,
    width=20,
    anchor="w"
).pack(side=tk.LEFT)

resultado_dia_semana = tk.Label(
    frame_dia_semana,
    text="---",
    font=("Arial", 12),
    bg=COLOR_FONDO,
    fg=COLOR_RESALTADO,
    anchor="w"
)
resultado_dia_semana.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Marco para el botón de explicación
marco_boton_explicacion = tk.Frame(marco_resultados, bg=COLOR_FONDO)
marco_boton_explicacion.pack(pady=15)

# Botón para explicación de signos zodiacales
boton_explicacion = ttk.Button(
    marco_boton_explicacion,
    text="📚 EXPLICACIÓN SIGNOS ZODIACALES",
    command=mostrar_explicacion_signos,
    style="Boton.TButton",
    width=30
)
boton_explicacion.pack()

# Información educativa
marco_info = tk.Frame(
    ventana,
    bg=COLOR_FONDO,
    highlightbackground=COLOR_PRIMARIO,
    highlightthickness=1
)
marco_info.pack(pady=10, padx=50, fill=tk.X)

info_texto = tk.Label(
    marco_info,
    text="💡 Esta aplicación te ayuda a comprender conceptos de calendario, astronomía y cálculo de edades",
    font=("Arial", 10),
    bg=COLOR_FONDO,
    fg=COLOR_EXPLICACION,
    pady=5
)
info_texto.pack()

# ============================================
# EJECUCIÓN DE LA APLICACIÓN
# ============================================

# Iniciar el bucle principal de la aplicación
ventana.mainloop()