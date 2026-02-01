#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APLICACIÓN EDUCATIVA: EXPLORANDO LA LIBRERÍA DATETIME
Versión: 1.0
Autor: Experto en Desarrollo de Software Educativo
Descripción: Aplicación interactiva para aprender sobre datetime en Python
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, date, time, timedelta
import time as time_module

# ============================================================================
# CONFIGURACIÓN DE COLORES - PALETA MODERNA Y ATRACTIVA
# ============================================================================
COLOR_PRINCIPAL = "#2C3E50"      # Azul oscuro elegante
COLOR_SECUNDARIO = "#3498DB"     # Azul brillante
COLOR_TERCIARIO = "#ECF0F1"      # Gris claro para fondos
COLOR_TEXTO = "#2C3E50"          # Texto oscuro
COLOR_BOTON = "#3498DB"          # Color base de botones
COLOR_BOTON_HOVER = "#2980B9"    # Color al pasar el cursor
COLOR_EXITO = "#2ECC71"          # Verde para operaciones exitosas
COLOR_RESALTADO = "#F1C40F"      # Amarillo para resaltar

# ============================================================================
# FUNCIONES DE UTILIDAD PARA LA INTERFAZ
# ============================================================================

def crear_boton_con_hover(parent, texto, comando, ancho=25):
    """Crea un botón con efecto hover personalizado"""
    boton = tk.Button(
        parent,
        text=texto,
        command=comando,
        bg=COLOR_BOTON,
        fg="white",
        font=("Arial", 10, "bold"),
        relief="flat",
        padx=15,
        pady=8,
        width=ancho,
        cursor="hand2"
    )
    
    # Efectos hover
    def on_enter(e):
        boton['background'] = COLOR_BOTON_HOVER
        boton['relief'] = "raised"
    
    def on_leave(e):
        boton['background'] = COLOR_BOTON
        boton['relief'] = "flat"
    
    boton.bind("<Enter>", on_enter)
    boton.bind("<Leave>", on_leave)
    
    return boton

def crear_etiqueta_titulo(parent, texto):
    """Crea una etiqueta de título estilizada"""
    return tk.Label(
        parent,
        text=texto,
        font=("Arial", 12, "bold"),
        bg=COLOR_TERCIARIO,
        fg=COLOR_PRINCIPAL,
        pady=10
    )

def crear_etiqueta_descripcion(parent, texto):
    """Crea una etiqueta de descripción"""
    return tk.Label(
        parent,
        text=texto,
        font=("Arial", 9),
        bg=COLOR_TERCIARIO,
        fg=COLOR_TEXTO,
        wraplength=500,
        justify="left"
    )

def crear_marco_con_borde(parent, titulo=""):
    """Crea un marco con borde y título opcional"""
    marco = tk.Frame(
        parent,
        bg=COLOR_TERCIARIO,
        highlightbackground=COLOR_SECUNDARIO,
        highlightthickness=2,
        relief="ridge",
        padx=15,
        pady=15
    )
    
    if titulo:
        titulo_label = tk.Label(
            marco,
            text=titulo,
            font=("Arial", 10, "bold"),
            bg=COLOR_TERCIARIO,
            fg=COLOR_SECUNDARIO
        )
        titulo_label.pack(anchor="w", pady=(0, 10))
    
    return marco

# ============================================================================
# FUNCIONALIDADES PRINCIPALES DE DATETIME
# ============================================================================

def mostrar_fecha_hora_actual():
    """Muestra la fecha y hora actual en diferentes formatos"""
    ahora = datetime.now()
    
    # Formateamos en diferentes estilos
    formatos = {
        "Completo (predeterminado)": ahora.strftime("%A, %d de %B de %Y - %H:%M:%S"),
        "Fecha corta (DD/MM/AAAA)": ahora.strftime("%d/%m/%Y"),
        "Fecha larga": ahora.strftime("%d de %B de %Y"),
        "Hora 24h": ahora.strftime("%H:%M:%S"),
        "Hora 12h": ahora.strftime("%I:%M:%S %p"),
        "ISO 8601": ahora.isoformat()
    }
    
    # Crear ventana de resultados
    ventana_resultado = tk.Toplevel(ventana_principal)
    ventana_resultado.title("Fecha y Hora Actual")
    ventana_resultado.configure(bg=COLOR_TERCIARIO)
    ventana_resultado.geometry("650x550")
    ventana_resultado.resizable(False, False)
    
    # Centrar ventana
    ventana_resultado.transient(ventana_principal)
    ventana_resultado.grab_set()
    
    # Título
    tk.Label(
        ventana_resultado,
        text="📅 FECHA Y HORA ACTUAL",
        font=("Arial", 14, "bold"),
        bg=COLOR_TERCIARIO,
        fg=COLOR_PRINCIPAL
    ).pack(pady=15)
    
    # Explicación
    tk.Label(
        ventana_resultado,
        text="Python obtiene la fecha y hora del sistema. Aquí la mostramos en diferentes formatos:",
        font=("Arial", 9),
        bg=COLOR_TERCIARIO,
        fg=COLOR_TEXTO,
        wraplength=450
    ).pack(pady=10)
    
    # Marco para resultados
    marco_resultados = tk.Frame(ventana_resultado, bg=COLOR_TERCIARIO)
    marco_resultados.pack(pady=10, padx=20, fill="both", expand=True)
    
    # Mostrar cada formato
    for formato_nombre, valor in formatos.items():
        frame_formato = tk.Frame(marco_resultados, bg=COLOR_TERCIARIO)
        frame_formato.pack(fill="x", pady=5)
        
        tk.Label(
            frame_formato,
            text=f"{formato_nombre}:",
            font=("Arial", 9, "bold"),
            bg=COLOR_TERCIARIO,
            fg=COLOR_SECUNDARIO,
            width=25,
            anchor="w"
        ).pack(side="left")
        
        tk.Label(
            frame_formato,
            text=valor,
            font=("Courier", 9),
            bg="white",
            fg=COLOR_TEXTO,
            relief="sunken",
            padx=10,
            pady=5,
            width=30
        ).pack(side="left", padx=(10, 0))
    
    # Botón para cerrar
    tk.Button(
        ventana_resultado,
        text="Cerrar",
        command=ventana_resultado.destroy,
        bg=COLOR_BOTON,
        fg="white",
        font=("Arial", 10),
        padx=20,
        pady=5
    ).pack(pady=20)

def calcular_diferencia_fechas():
    """Calcula la diferencia entre dos fechas"""
    ventana_calculo = tk.Toplevel(ventana_principal)
    ventana_calculo.title("Calculadora de Diferencia entre Fechas")
    ventana_calculo.configure(bg=COLOR_TERCIARIO)
    ventana_calculo.geometry("500x500")
    ventana_calculo.resizable(False, False)
    ventana_calculo.transient(ventana_principal)
    ventana_calculo.grab_set()
    
    # Título
    tk.Label(
        ventana_calculo,
        text="📆 CALCULAR DIFERENCIA ENTRE FECHAS",
        font=("Arial", 14, "bold"),
        bg=COLOR_TERCIARIO,
        fg=COLOR_PRINCIPAL
    ).pack(pady=15)
    
    # Explicación
    explicacion = """
    Introduce dos fechas para calcular la diferencia entre ellas.
    Formato: DD/MM/AAAA (ejemplo: 25/12/2024)
    """
    tk.Label(
        ventana_calculo,
        text=explicacion,
        font=("Arial", 9),
        bg=COLOR_TERCIARIO,
        fg=COLOR_TEXTO,
        wraplength=450
    ).pack(pady=10)
    
    # Marco para entrada de fechas
    marco_entrada = tk.Frame(ventana_calculo, bg=COLOR_TERCIARIO)
    marco_entrada.pack(pady=20)
    
    # Fecha 1
    tk.Label(
        marco_entrada,
        text="Fecha 1 (inicio):",
        font=("Arial", 10, "bold"),
        bg=COLOR_TERCIARIO,
        fg=COLOR_TEXTO
    ).grid(row=0, column=0, pady=10, padx=5, sticky="w")
    
    entrada_fecha1 = tk.Entry(
        marco_entrada,
        font=("Arial", 10),
        width=15,
        justify="center"
    )
    entrada_fecha1.grid(row=0, column=1, pady=10, padx=5)
    entrada_fecha1.insert(0, "01/01/2024")
    
    # Fecha 2
    tk.Label(
        marco_entrada,
        text="Fecha 2 (fin):",
        font=("Arial", 10, "bold"),
        bg=COLOR_TERCIARIO,
        fg=COLOR_TEXTO
    ).grid(row=1, column=0, pady=10, padx=5, sticky="w")
    
    entrada_fecha2 = tk.Entry(
        marco_entrada,
        font=("Arial", 10),
        width=15,
        justify="center"
    )
    entrada_fecha2.grid(row=1, column=1, pady=10, padx=5)
    entrada_fecha2.insert(0, datetime.now().strftime("%d/%m/%Y"))
    
    # Área de resultados
    marco_resultado = tk.Frame(ventana_calculo, bg=COLOR_TERCIARIO)
    marco_resultado.pack(pady=20)
    
    resultado_texto = tk.StringVar()
    resultado_texto.set("Los resultados aparecerán aquí...")
    
    label_resultado = tk.Label(
        marco_resultado,
        textvariable=resultado_texto,
        font=("Arial", 10),
        bg="white",
        fg=COLOR_TEXTO,
        relief="sunken",
        width=50,
        height=8,
        wraplength=400,
        justify="left"
    )
    label_resultado.pack(pady=10)
    
    def calcular():
        """Función interna para realizar el cálculo"""
        try:
            # Convertir strings a objetos date
            fecha1 = datetime.strptime(entrada_fecha1.get(), "%d/%m/%Y")
            fecha2 = datetime.strptime(entrada_fecha2.get(), "%d/%m/%Y")
            
            # Asegurar que fecha1 sea anterior a fecha2
            if fecha1 > fecha2:
                fecha1, fecha2 = fecha2, fecha1
                entrada_fecha1.delete(0, tk.END)
                entrada_fecha1.insert(0, fecha1.strftime("%d/%m/%Y"))
                entrada_fecha2.delete(0, tk.END)
                entrada_fecha2.insert(0, fecha2.strftime("%d/%m/%Y"))
            
            # Calcular diferencia
            diferencia = fecha2 - fecha1
            
            # Formatear resultados
            resultado = f"""
            📊 RESULTADOS DE LA DIFERENCIA:
            
            • Días totales: {diferencia.days:,}
            • Semanas: {diferencia.days // 7} semanas y {diferencia.days % 7} días
            • Meses (aproximado): {diferencia.days // 30:.1f} meses
            • Años (aproximado): {diferencia.days / 365:.2f} años
            
            Fecha 1: {fecha1.strftime('%A, %d de %B de %Y')}
            Fecha 2: {fecha2.strftime('%A, %d de %B de %Y')}
            """
            
            resultado_texto.set(resultado)
            label_resultado.config(fg=COLOR_EXITO)
            
        except ValueError as e:
            resultado_texto.set(f"❌ ERROR: Formato de fecha incorrecto\n\nUse el formato DD/MM/AAAA\nEjemplo: 25/12/2024")
            label_resultado.config(fg="red")
    
    # Botones
    marco_botones = tk.Frame(ventana_calculo, bg=COLOR_TERCIARIO)
    marco_botones.pack(pady=10)
    
    crear_boton_con_hover(
        marco_botones,
        "🔢 Calcular Diferencia",
        calcular,
        ancho=20
    ).pack(side="left", padx=5)
    
    tk.Button(
        marco_botones,
        text="Cerrar",
        command=ventana_calculo.destroy,
        bg=COLOR_TERCIARIO,
        fg=COLOR_TEXTO,
        font=("Arial", 10),
        padx=20
    ).pack(side="left", padx=5)

def operaciones_con_fechas():
    """Realiza operaciones de suma/resta de días a una fecha"""
    ventana_operaciones = tk.Toplevel(ventana_principal)
    ventana_operaciones.title("Operaciones con Fechas")
    ventana_operaciones.configure(bg=COLOR_TERCIARIO)
    ventana_operaciones.geometry("500x500")
    ventana_operaciones.resizable(False, False)
    ventana_operaciones.transient(ventana_principal)
    ventana_operaciones.grab_set()
    
    # Título
    tk.Label(
        ventana_operaciones,
        text="➕➖ OPERACIONES CON FECHAS",
        font=("Arial", 14, "bold"),
        bg=COLOR_TERCIARIO,
        fg=COLOR_PRINCIPAL
    ).pack(pady=15)
    
    # Explicación
    explicacion = """
    Puedes sumar o restar días a una fecha específica.
    Esto es útil para calcular fechas futuras o pasadas.
    """
    tk.Label(
        ventana_operaciones,
        text=explicacion,
        font=("Arial", 9),
        bg=COLOR_TERCIARIO,
        fg=COLOR_TEXTO,
        wraplength=450
    ).pack(pady=10)
    
    # Marco para entrada de datos
    marco_entrada = tk.Frame(ventana_operaciones, bg=COLOR_TERCIARIO)
    marco_entrada.pack(pady=20)
    
    # Fecha base
    tk.Label(
        marco_entrada,
        text="Fecha base (DD/MM/AAAA):",
        font=("Arial", 10, "bold"),
        bg=COLOR_TERCIARIO,
        fg=COLOR_TEXTO
    ).grid(row=0, column=0, pady=10, padx=5, sticky="w")
    
    entrada_fecha = tk.Entry(
        marco_entrada,
        font=("Arial", 10),
        width=15,
        justify="center"
    )
    entrada_fecha.grid(row=0, column=1, pady=10, padx=5)
    entrada_fecha.insert(0, datetime.now().strftime("%d/%m/%Y"))
    
    # Días a sumar/restar
    tk.Label(
        marco_entrada,
        text="Días a sumar/restar:",
        font=("Arial", 10, "bold"),
        bg=COLOR_TERCIARIO,
        fg=COLOR_TEXTO
    ).grid(row=1, column=0, pady=10, padx=5, sticky="w")
    
    entrada_dias = tk.Entry(
        marco_entrada,
        font=("Arial", 10),
        width=15,
        justify="center"
    )
    entrada_dias.grid(row=1, column=1, pady=10, padx=5)
    entrada_dias.insert(0, "30")
    
    # Área de resultados
    marco_resultado = tk.Frame(ventana_operaciones, bg=COLOR_TERCIARIO)
    marco_resultado.pack(pady=20)
    
    resultado_texto = tk.StringVar()
    resultado_texto.set("Los resultados aparecerán aquí...")
    
    label_resultado = tk.Label(
        marco_resultado,
        textvariable=resultado_texto,
        font=("Arial", 10),
        bg="white",
        fg=COLOR_TEXTO,
        relief="sunken",
        width=50,
        height=8,
        wraplength=400,
        justify="left"
    )
    label_resultado.pack(pady=10)
    
    def operar(operacion):
        """Realiza la operación de suma o resta"""
        try:
            fecha_base = datetime.strptime(entrada_fecha.get(), "%d/%m/%Y")
            dias = int(entrada_dias.get())
            
            if operacion == "sumar":
                nueva_fecha = fecha_base + timedelta(days=dias)
                operacion_texto = "sumado"
            else:
                nueva_fecha = fecha_base - timedelta(days=dias)
                operacion_texto = "restado"
            
            resultado = f"""
            📅 RESULTADO DE LA OPERACIÓN:
            
            Fecha base: {fecha_base.strftime('%A, %d de %B de %Y')}
            Días {operacion_texto}: {abs(dias):,}
            
            🔮 NUEVA FECHA:
            {nueva_fecha.strftime('%A, %d de %B de %Y')}
            
            Formato corto: {nueva_fecha.strftime('%d/%m/%Y')}
            Diferencia con hoy: {(nueva_fecha.date() - date.today()).days} días
            """
            
            resultado_texto.set(resultado)
            label_resultado.config(fg=COLOR_EXITO)
            
        except ValueError as e:
            resultado_texto.set(f"❌ ERROR: Datos incorrectos\n\n• Fecha: Use DD/MM/AAAA\n• Días: Use números enteros")
            label_resultado.config(fg="red")
    
    # Botones
    marco_botones = tk.Frame(ventana_operaciones, bg=COLOR_TERCIARIO)
    marco_botones.pack(pady=10)
    
    crear_boton_con_hover(
        marco_botones,
        "➕ Sumar Días",
        lambda: operar("sumar"),
        ancho=15
    ).pack(side="left", padx=5)
    
    crear_boton_con_hover(
        marco_botones,
        "➖ Restar Días",
        lambda: operar("restar"),
        ancho=15
    ).pack(side="left", padx=5)
    
    tk.Button(
        marco_botones,
        text="Cerrar",
        command=ventana_operaciones.destroy,
        bg=COLOR_TERCIARIO,
        fg=COLOR_TEXTO,
        font=("Arial", 10),
        padx=20
    ).pack(side="left", padx=5)

def informacion_dia_semana():
    """Muestra información sobre un día específico de la semana"""
    ventana_dia = tk.Toplevel(ventana_principal)
    ventana_dia.title("Información del Día de la Semana")
    ventana_dia.configure(bg=COLOR_TERCIARIO)
    ventana_dia.geometry("450x550")
    ventana_dia.resizable(False, False)
    ventana_dia.transient(ventana_principal)
    ventana_dia.grab_set()
    
    # Título
    tk.Label(
        ventana_dia,
        text="📅 DÍA DE LA SEMANA",
        font=("Arial", 14, "bold"),
        bg=COLOR_TERCIARIO,
        fg=COLOR_PRINCIPAL
    ).pack(pady=15)
    
    # Explicación
    explicacion = """
    Introduce una fecha para conocer qué día de la semana fue o será.
    También mostraremos información adicional sobre esa fecha.
    """
    tk.Label(
        ventana_dia,
        text=explicacion,
        font=("Arial", 9),
        bg=COLOR_TERCIARIO,
        fg=COLOR_TEXTO,
        wraplength=400
    ).pack(pady=10)
    
    # Entrada de fecha
    marco_entrada = tk.Frame(ventana_dia, bg=COLOR_TERCIARIO)
    marco_entrada.pack(pady=15)
    
    tk.Label(
        marco_entrada,
        text="Fecha (DD/MM/AAAA):",
        font=("Arial", 10, "bold"),
        bg=COLOR_TERCIARIO,
        fg=COLOR_TEXTO
    ).pack(pady=5)
    
    entrada_fecha = tk.Entry(
        marco_entrada,
        font=("Arial", 10),
        width=15,
        justify="center"
    )
    entrada_fecha.pack(pady=5)
    entrada_fecha.insert(0, datetime.now().strftime("%d/%m/%Y"))
    
    # Área de resultados
    marco_resultado = tk.Frame(ventana_dia, bg=COLOR_TERCIARIO)
    marco_resultado.pack(pady=20)
    
    resultado_texto = tk.StringVar()
    resultado_texto.set("La información aparecerá aquí...")
    
    label_resultado = tk.Label(
        marco_resultado,
        textvariable=resultado_texto,
        font=("Arial", 10),
        bg="white",
        fg=COLOR_TEXTO,
        relief="sunken",
        width=40,
        height=6,
        wraplength=350,
        justify="center"
    )
    label_resultado.pack(pady=10)
    
    def calcular_dia():
        """Calcula el día de la semana"""
        try:
            fecha = datetime.strptime(entrada_fecha.get(), "%d/%m/%Y")
            hoy = datetime.now()
            
            # Días de la semana en español
            dias_semana = [
                "Lunes", "Martes", "Miércoles", "Jueves", 
                "Viernes", "Sábado", "Domingo"
            ]
            
            # Meses en español
            meses = [
                "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
            ]
            
            dia_semana = dias_semana[fecha.weekday()]
            nombre_mes = meses[fecha.month - 1]
            
            # Determinar si es pasado, presente o futuro
            if fecha.date() < hoy.date():
                tiempo = f"Hace {(hoy.date() - fecha.date()).days} días"
                estado = "🕒 FECHA PASADA"
            elif fecha.date() > hoy.date():
                tiempo = f"Dentro de {(fecha.date() - hoy.date()).days} días"
                estado = "🔮 FECHA FUTURA"
            else:
                tiempo = "¡HOY MISMO!"
                estado = "🎉 ¡HOY!"
            
            resultado = f"""
            {estado}
            
            📅 {dia_semana}, {fecha.day} de {nombre_mes} de {fecha.year}
            
            {tiempo}
            
            Día {fecha.timetuple().tm_yday} del año
            Semana {fecha.isocalendar()[1]} del año
            """
            
            resultado_texto.set(resultado)
            label_resultado.config(fg=COLOR_EXITO)
            
        except ValueError:
            resultado_texto.set("❌ ERROR: Formato de fecha incorrecto\nUse DD/MM/AAAA")
            label_resultado.config(fg="red")
    
    # Botones
    marco_botones = tk.Frame(ventana_dia, bg=COLOR_TERCIARIO)
    marco_botones.pack(pady=10)
    
    crear_boton_con_hover(
        marco_botones,
        "🔍 Calcular Día",
        calcular_dia,
        ancho=15
    ).pack(side="left", padx=5)
    
    tk.Button(
        marco_botones,
        text="Cerrar",
        command=ventana_dia.destroy,
        bg=COLOR_TERCIARIO,
        fg=COLOR_TEXTO,
        font=("Arial", 10),
        padx=20
    ).pack(side="left", padx=5)

def mostrar_info_datetime():
    """Muestra información educativa sobre la librería datetime"""
    ventana_info = tk.Toplevel(ventana_principal)
    ventana_info.title("Información sobre datetime")
    ventana_info.configure(bg=COLOR_TERCIARIO)
    ventana_info.geometry("550x500")
    ventana_info.resizable(False, False)
    ventana_info.transient(ventana_principal)
    ventana_info.grab_set()
    
    # Título
    tk.Label(
        ventana_info,
        text="📚 INFORMACIÓN SOBRE DATETIME",
        font=("Arial", 14, "bold"),
        bg=COLOR_TERCIARIO,
        fg=COLOR_PRINCIPAL
    ).pack(pady=15)
    
    # Crear widget Text con scrollbar
    marco_texto = tk.Frame(ventana_info, bg=COLOR_TERCIARIO)
    marco_texto.pack(fill="both", expand=True, padx=20, pady=10)
    
    scrollbar = tk.Scrollbar(marco_texto)
    scrollbar.pack(side="right", fill="y")
    
    texto_info = tk.Text(
        marco_texto,
        wrap="word",
        font=("Arial", 10),
        bg="white",
        fg=COLOR_TEXTO,
        relief="sunken",
        yscrollcommand=scrollbar.set,
        padx=15,
        pady=15
    )
    texto_info.pack(side="left", fill="both", expand=True)
    
    scrollbar.config(command=texto_info.yview)
    
    # Contenido educativo
    contenido = """
    📖 QUÉ ES LA LIBRERÍA DATETIME?
    
    La librería datetime es parte de la biblioteca estándar de Python
    y proporciona clases para manipular fechas y horas de manera eficiente.
    
    ⚙️ CLASES PRINCIPALES:
    
    1. datetime - Combina fecha y hora
    2. date - Solo fecha (año, mes, día)
    3. time - Solo hora (hora, minuto, segundo, microsegundo)
    4. timedelta - Diferencia entre dos fechas/horas
    5. tzinfo - Zonas horarias (abstracta)
    
    🎯 USOS COMUNES:
    
    • Obtener la fecha y hora actual del sistema
    • Formatear fechas en diferentes estilos
    • Calcular diferencias entre fechas
    • Sumar o restar días a una fecha
    • Validar fechas ingresadas por usuarios
    • Programar tareas en aplicaciones
    
    📝 EJEMPLOS DE CÓDIGO:
    
    from datetime import datetime, date, timedelta
    
    # Fecha y hora actual
    ahora = datetime.now()
    
    # Solo fecha actual
    hoy = date.today()
    
    # Crear una fecha específica
    navidad = date(2024, 12, 25)
    
    # Sumar días a una fecha
    futuro = hoy + timedelta(days=30)
    
    # Calcular diferencia
    dias_para_navidad = (navidad - hoy).days
    
    # Formatear fechas
    fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M")
    
    🎨 FORMATOS DE STRFTIME:
    
    %Y - Año con 4 dígitos (2024)
    %m - Mes con 2 dígitos (01-12)
    %d - Día con 2 dígitos (01-31)
    %H - Hora 24h (00-23)
    %M - Minutos (00-59)
    %S - Segundos (00-59)
    %A - Día de semana completo (Lunes)
    %B - Mes completo (Enero)
    
    💡 CONSEJOS PARA ESTUDIANTES:
    
    1. Siempre importa lo que necesites: from datetime import datetime
    2. Usa strftime() para formatear y strptime() para parsear
    3. timedelta es útil para cálculos con fechas
    4. Las fechas son inmutables, se crean nuevos objetos
    5. Practica con diferentes formatos de entrada/salida
    
    Esta aplicación te permite explorar todas estas funcionalidades
    de manera interactiva y visual.
    """
    
    texto_info.insert("1.0", contenido)
    texto_info.config(state="disabled")  # Hacer el texto de solo lectura
    
    # Botón para cerrar
    tk.Button(
        ventana_info,
        text="Cerrar",
        command=ventana_info.destroy,
        bg=COLOR_BOTON,
        fg="white",
        font=("Arial", 10),
        padx=20,
        pady=5
    ).pack(pady=15)

# ============================================================================
# CONFIGURACIÓN DE LA VENTANA PRINCIPAL
# ============================================================================

# Crear ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Explorador Interactivo de datetime - Para Estudiantes")
ventana_principal.configure(bg=COLOR_TERCIARIO)

# Obtener dimensiones de pantalla y centrar ventana
ancho_pantalla = ventana_principal.winfo_screenwidth()
alto_pantalla = ventana_principal.winfo_screenheight()
ancho_ventana = 800
alto_ventana = 700
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)
ventana_principal.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
ventana_principal.resizable(False, False)

# ============================================================================
# INTERFAZ PRINCIPAL - CABECERA
# ============================================================================

# Marco de cabecera
marco_cabecera = tk.Frame(
    ventana_principal,
    bg=COLOR_PRINCIPAL,
    height=150
)
marco_cabecera.pack(fill="x")
marco_cabecera.pack_propagate(False)

# Título principal
titulo_principal = tk.Label(
    marco_cabecera,
    text="🕒 EXPLORADOR INTERACTIVO DE DATETIME",
    font=("Arial", 18, "bold"),
    bg=COLOR_PRINCIPAL,
    fg="white",
    pady=20
)
titulo_principal.pack()

# Subtítulo
subtitulo = tk.Label(
    marco_cabecera,
    text="Aplicación educativa para aprender a trabajar con fechas y horas en Python",
    font=("Arial", 11),
    bg=COLOR_PRINCIPAL,
    fg="#BDC3C7",
    pady=5
)
subtitulo.pack()

# Mensaje para estudiantes
mensaje = tk.Label(
    marco_cabecera,
    text="Para estudiantes de bachillerato - Desarrolla habilidades prácticas en programación",
    font=("Arial", 9, "italic"),
    bg=COLOR_PRINCIPAL,
    fg="#ECF0F1"
)
mensaje.pack(pady=(5, 0))

# ============================================================================
# INTERFAZ PRINCIPAL - CONTENIDO
# ============================================================================

# Marco principal para contenido
marco_contenido = tk.Frame(
    ventana_principal,
    bg=COLOR_TERCIARIO,
    padx=30,
    pady=30
)
marco_contenido.pack(fill="both", expand=True)

# Sección de información
crear_etiqueta_titulo(
    marco_contenido,
    "🎯 ¿QUÉ VAS A APRENDER HOY?"
).pack(anchor="w", pady=(0, 10))

crear_etiqueta_descripcion(
    marco_contenido,
    "La librería datetime de Python te permite trabajar con fechas y horas. "
    "Con esta aplicación interactiva podrás explorar sus funcionalidades principales "
    "de manera práctica y visual. ¡Haz clic en cualquier botón para comenzar!"
).pack(anchor="w", pady=(0, 20))

# Marco para las funcionalidades
marco_funcionalidades = crear_marco_con_borde(
    marco_contenido,
    "✨ FUNCIONALIDADES DISPONIBLES"
)
marco_funcionalidades.pack(fill="both", expand=True, pady=(0, 20))

# Crear botones de funcionalidades (2 columnas)
marco_botones_func = tk.Frame(marco_funcionalidades, bg=COLOR_TERCIARIO)
marco_botones_func.pack(fill="both", expand=True)

# Columna izquierda
columna_izquierda = tk.Frame(marco_botones_func, bg=COLOR_TERCIARIO)
columna_izquierda.pack(side="left", fill="both", expand=True, padx=10)

# Columna derecha
columna_derecha = tk.Frame(marco_botones_func, bg=COLOR_TERCIARIO)
columna_derecha.pack(side="right", fill="both", expand=True, padx=10)

# Botones columna izquierda
crear_boton_con_hover(
    columna_izquierda,
    "📅 FECHA Y HORA ACTUAL",
    mostrar_fecha_hora_actual
).pack(pady=10)

crear_boton_con_hover(
    columna_izquierda,
    "📆 DIFERENCIA ENTRE FECHAS",
    calcular_diferencia_fechas
).pack(pady=10)

crear_boton_con_hover(
    columna_izquierda,
    "➕➖ OPERACIONES CON FECHAS",
    operaciones_con_fechas
).pack(pady=10)

# Botones columna derecha
crear_boton_con_hover(
    columna_derecha,
    "🔍 DÍA DE LA SEMANA",
    informacion_dia_semana
).pack(pady=10)

crear_boton_con_hover(
    columna_derecha,
    "📚 INFORMACIÓN SOBRE DATETIME",
    mostrar_info_datetime
).pack(pady=10)

# Botón de salida
crear_boton_con_hover(
    columna_derecha,
    "🚪 SALIR DE LA APLICACIÓN",
    ventana_principal.destroy
).pack(pady=20)

# ============================================================================
# PIE DE PÁGINA
# ============================================================================

marco_pie = tk.Frame(
    ventana_principal,
    bg=COLOR_PRINCIPAL,
    height=60
)
marco_pie.pack(fill="x", side="bottom")
marco_pie.pack_propagate(False)

# Información del pie
info_pie = tk.Label(
    marco_pie,
    text="Aplicación educativa desarrollada para el aprendizaje de Python - Librería datetime",
    font=("Arial", 9),
    bg=COLOR_PRINCIPAL,
    fg="#BDC3C7"
)
info_pie.pack(pady=10)

# ============================================================================
# INICIAR APLICACIÓN
# ============================================================================

if __name__ == "__main__":
    # Mostrar mensaje de bienvenida
    messagebox.showinfo(
        "¡Bienvenido/a!",
        "Explorador Interactivo de datetime\n\n"
        "Esta aplicación te ayudará a aprender y practicar con la librería datetime de Python.\n"
        "Selecciona cualquier funcionalidad para comenzar tu aprendizaje."
    )
    
    # Iniciar el bucle principal de la aplicación
    ventana_principal.mainloop()