"""
Aplicación Educativa: Calculadora de Interés Simple
Autor: Experto en Desarrollo de Software Educativo
Descripción: Aplicación educativa para estudiantes de bachillerato que explica
             y calcula el interés simple de forma interactiva.
Versión: 1.0
"""

import tkinter as tk
from tkinter import ttk, messagebox

# ============================================================================
# CONFIGURACIÓN INICIAL Y VARIABLES GLOBALES
# ============================================================================

# Configuración de colores (paleta moderna y atractiva)
COLOR_FONDO = "#F0F7FF"           # Azul claro muy suave
COLOR_PRIMARIO = "#4A6FA5"        # Azul principal
COLOR_SECUNDARIO = "#166088"      # Azul oscuro
COLOR_ACENTO = "#7B9E89"          # Verde azulado suave
COLOR_TEXTO = "#2C3E50"           # Gris azulado oscuro
COLOR_BOTON_NORMAL = "#4A6FA5"    # Azul
COLOR_BOTON_HOVER = "#3A5A8C"     # Azul más oscuro para hover
COLOR_ENTRADA = "#FFFFFF"         # Blanco para campos de entrada

# Variables globales para almacenar los widgets
widgets = {}

# ============================================================================
# FUNCIONES DE CÁLCULO MATEMÁTICO
# ============================================================================

def calcular_interes_simple(principal, tasa, tiempo):
    """
    Calcula el interés simple usando la fórmula: I = P * r * t
    
    Donde:
        I = Interés
        P = Capital principal
        r = Tasa de interés (en decimal)
        t = Tiempo (en años)
    
    Retorna el interés calculado.
    """
    try:
        principal = float(principal)
        tasa = float(tasa) / 100  # Convertir porcentaje a decimal
        tiempo = float(tiempo)
        
        if principal < 0 or tasa < 0 or tiempo < 0:
            raise ValueError("Los valores no pueden ser negativos")
            
        interes = principal * tasa * tiempo
        return round(interes, 2)
    except ValueError as e:
        raise ValueError(f"Error en los datos ingresados: {str(e)}")

def calcular_monto_total(principal, tasa, tiempo):
    """
    Calcula el monto total (capital + interés) usando la fórmula:
    Monto = P + (P * r * t) = P * (1 + r * t)
    """
    try:
        interes = calcular_interes_simple(principal, tasa, tiempo)
        principal_float = float(principal)
        monto_total = principal_float + interes
        return round(monto_total, 2)
    except ValueError as e:
        raise ValueError(str(e))

def calcular_capital_necesario(monto_deseado, tasa, tiempo):
    """
    Calcula el capital necesario para alcanzar un monto deseado.
    Fórmula: P = Monto / (1 + r * t)
    """
    try:
        monto_deseado = float(monto_deseado)
        tasa = float(tasa) / 100
        tiempo = float(tiempo)
        
        if monto_deseado < 0 or tasa < 0 or tiempo < 0:
            raise ValueError("Los valores no pueden ser negativos")
            
        if tiempo == 0 and tasa == 0:
            raise ValueError("Tiempo y tasa no pueden ser ambos cero")
            
        capital = monto_deseado / (1 + tasa * tiempo)
        return round(capital, 2)
    except ValueError as e:
        raise ValueError(str(e))

# ============================================================================
# FUNCIONES DE INTERFAZ Y EVENTOS
# ============================================================================

def configurar_estilos():
    """Configura los estilos visuales de la aplicación."""
    estilo = ttk.Style()
    
    # Configurar estilo para etiquetas
    estilo.configure("Titulo.TLabel", 
                    font=("Arial", 16, "bold"),
                    foreground=COLOR_SECUNDARIO,
                    background=COLOR_FONDO)
    
    estilo.configure("Subtitulo.TLabel",
                    font=("Arial", 12),
                    foreground=COLOR_TEXTO,
                    background=COLOR_FONDO)
    
    estilo.configure("Normal.TLabel",
                    font=("Arial", 10),
                    foreground=COLOR_TEXTO,
                    background=COLOR_FONDO)

def crear_boton_con_hover(parent, texto, comando, fila, columna, colspan=1):
    """
    Crea un botón con efecto hover (cambio de color al pasar el mouse).
    
    Args:
        parent: Widget padre donde se colocará el botón
        texto: Texto que mostrará el botón
        comando: Función a ejecutar al hacer clic
        fila: Fila en la grid
        columna: Columna en la grid
        colspan: Número de columnas que ocupará
    """
    # Crear el botón
    boton = tk.Button(parent,
                     text=texto,
                     command=comando,
                     bg=COLOR_BOTON_NORMAL,
                     fg="white",
                     font=("Arial", 10, "bold"),
                     relief="flat",
                     padx=20,
                     pady=10,
                     cursor="hand2")
    
    # Colocar en la grid
    boton.grid(row=fila, column=columna, columnspan=colspan, 
              padx=5, pady=10, sticky="ew")
    
    # Funciones para el efecto hover
    def on_enter(event):
        boton.config(bg=COLOR_BOTON_HOVER)
    
    def on_leave(event):
        boton.config(bg=COLOR_BOTON_NORMAL)
    
    # Asignar eventos de hover
    boton.bind("<Enter>", on_enter)
    boton.bind("<Leave>", on_leave)
    
    return boton

def limpiar_resultados():
    """Limpia todos los campos de resultados."""
    for key in ['resultado_interes', 'resultado_monto', 'resultado_capital']:
        if key in widgets:
            widgets[key].config(text="")

def mostrar_explicacion_interes():
    """Muestra la explicación del interés simple en un cuadro de diálogo."""
    explicacion = """INTERÉS SIMPLE - EXPLICACIÓN

El interés simple es una forma de calcular el interés sobre un préstamo o inversión.

FÓRMULA PRINCIPAL:
I = P × r × t

Donde:
• I = Interés ganado o pagado
• P = Capital principal (cantidad inicial)
• r = Tasa de interés anual (en decimal, ej: 5% = 0.05)
• t = Tiempo en años

EJEMPLO PRÁCTICO:
Si inviertes $1,000 al 5% anual por 3 años:
I = 1000 × 0.05 × 3 = $150
Monto total = $1,000 + $150 = $1,150

CARACTERÍSTICAS:
• El interés se calcula siempre sobre el capital original
• No hay interés sobre el interés (compuesto)
• Es lineal y predecible
• Usado en préstamos a corto plazo y algunos tipos de inversiones"""

    messagebox.showinfo("Explicación del Interés Simple", explicacion)

def mostrar_formula_interactiva():
    """Muestra la fórmula del interés simple de forma visual."""
    # Crear ventana emergente
    ventana_formula = tk.Toplevel(widgets['ventana_principal'])
    ventana_formula.title("Fórmula Interactiva")
    ventana_formula.geometry("500x300")
    ventana_formula.configure(bg=COLOR_FONDO)
    ventana_formula.resizable(False, False)
    
    # Centrar ventana
    ventana_formula.update_idletasks()
    ancho = ventana_formula.winfo_width()
    alto = ventana_formula.winfo_height()
    x = (ventana_formula.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana_formula.winfo_screenheight() // 2) - (alto // 2)
    ventana_formula.geometry(f'{ancho}x{alto}+{x}+{y}')
    
    # Título
    titulo = tk.Label(ventana_formula,
                     text="FÓRMULA DEL INTERÉS SIMPLE",
                     font=("Arial", 14, "bold"),
                     bg=COLOR_FONDO,
                     fg=COLOR_SECUNDARIO)
    titulo.pack(pady=20)
    
    # Fórmula principal
    formula_frame = tk.Frame(ventana_formula, bg=COLOR_FONDO)
    formula_frame.pack(pady=10)
    
    tk.Label(formula_frame,
            text="I = P × r × t",
            font=("Arial", 24, "bold"),
            bg=COLOR_FONDO,
            fg=COLOR_PRIMARIO).pack()
    
    # Explicación de variables
    explicacion_frame = tk.Frame(ventana_formula, bg=COLOR_FONDO)
    explicacion_frame.pack(pady=20)
    
    variables = [
        ("I = Interés total", COLOR_SECUNDARIO),
        ("P = Capital principal (monto inicial)", COLOR_TEXTO),
        ("r = Tasa de interés anual (en decimal)", COLOR_TEXTO),
        ("t = Tiempo en años", COLOR_TEXTO)
    ]
    
    for texto, color in variables:
        tk.Label(explicacion_frame,
                text=texto,
                font=("Arial", 11),
                bg=COLOR_FONDO,
                fg=color).pack(pady=5)
    
    # Fórmula del monto total
    tk.Label(ventana_formula,
            text="Monto Total = P + I = P × (1 + r × t)",
            font=("Arial", 14),
            bg=COLOR_FONDO,
            fg=COLOR_ACENTO).pack(pady=15)

def calcular_y_mostrar_interes():
    """Calcula y muestra el interés simple."""
    try:
        # Obtener valores de los campos de entrada
        principal = widgets['entry_principal'].get()
        tasa = widgets['entry_tasa'].get()
        tiempo = widgets['entry_tiempo'].get()
        
        # Validar que todos los campos estén completos
        if not principal or not tasa or not tiempo:
            raise ValueError("Por favor, complete todos los campos")
        
        # Calcular interés
        interes = calcular_interes_simple(principal, tasa, tiempo)
        monto_total = calcular_monto_total(principal, tasa, tiempo)
        
        # Mostrar resultados
        widgets['resultado_interes'].config(
            text=f"Interés ganado: ${interes:,.2f}\n"
                 f"Monto total: ${monto_total:,.2f}",
            fg=COLOR_SECUNDARIO
        )
        
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        widgets['resultado_interes'].config(text="", fg="red")

def calcular_y_mostrar_monto_deseado():
    """Calcula el capital necesario para un monto deseado."""
    try:
        # Obtener valores
        monto_deseado = widgets['entry_monto_deseado'].get()
        tasa = widgets['entry_tasa_monto'].get()
        tiempo = widgets['entry_tiempo_monto'].get()
        
        # Validar campos
        if not monto_deseado or not tasa or not tiempo:
            raise ValueError("Por favor, complete todos los campos")
        
        # Calcular capital necesario
        capital = calcular_capital_necesario(monto_deseado, tasa, tiempo)
        interes = float(monto_deseado) - capital
        
        # Mostrar resultados
        widgets['resultado_capital'].config(
            text=f"Capital necesario: ${capital:,.2f}\n"
                 f"Interés generado: ${interes:,.2f}",
            fg=COLOR_SECUNDARIO
        )
        
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        widgets['resultado_capital'].config(text="", fg="red")

def crear_seccion_entrada(parent, titulo, fila_inicial):
    """
    Crea una sección de entrada de datos con etiquetas y campos.
    
    Args:
        parent: Widget padre
        titulo: Título de la sección
        fila_inicial: Fila inicial para colocar los widgets
    
    Returns:
        Diccionario con las referencias a los campos creados
    """
    # Título de la sección
    tk.Label(parent,
            text=titulo,
            font=("Arial", 12, "bold"),
            bg=COLOR_FONDO,
            fg=COLOR_PRIMARIO).grid(row=fila_inicial, column=0, columnspan=3, 
                                   pady=(10, 5), sticky="w")
    
    campos = {}
    
    return campos

def crear_campo_entrada(parent, texto, fila, variable=None):
    """
    Crea un campo de entrada con su etiqueta.
    
    Args:
        parent: Widget padre
        texto: Texto de la etiqueta
        fila: Fila en la grid
        variable: Variable tkinter para el campo (opcional)
    
    Returns:
        El widget Entry creado
    """
    # Crear etiqueta
    tk.Label(parent,
            text=texto + ":",
            font=("Arial", 10),
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO).grid(row=fila, column=0, padx=5, pady=5, sticky="w")
    
    # Crear campo de entrada
    entry = tk.Entry(parent,
                    font=("Arial", 10),
                    bg=COLOR_ENTRADA,
                    fg=COLOR_TEXTO,
                    relief="solid",
                    borderwidth=1,
                    width=20)
    
    entry.grid(row=fila, column=1, padx=5, pady=5, sticky="w")
    
    return entry

# ============================================================================
# FUNCIÓN PRINCIPAL - CONSTRUCCIÓN DE LA INTERFAZ
# ============================================================================

def crear_interfaz():
    """Crea y configura la interfaz gráfica principal de la aplicación."""
    
    # Crear ventana principal
    ventana = tk.Tk()
    ventana.title("Calculadora Educativa - Interés Simple")
    ventana.configure(bg=COLOR_FONDO)
    
    # Establecer tamaño y centrar ventana
    ancho_ventana = 800
    alto_ventana = 700
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}")
    
    # Centrar ventana en pantalla
    ventana.update_idletasks()
    x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
    ventana.geometry(f'{ancho_ventana}x{alto_ventana}+{x}+{y}')
    
    ventana.resizable(False, False)
    widgets['ventana_principal'] = ventana
    
    # Configurar estilos
    configurar_estilos()
    
    # ========================================================================
    # ENCABEZADO DE LA APLICACIÓN
    # ========================================================================
    
    encabezado_frame = tk.Frame(ventana, bg=COLOR_PRIMARIO)
    encabezado_frame.pack(fill="x", pady=(0, 20))
    
    # Título principal
    titulo = tk.Label(encabezado_frame,
                     text="CALCULADORA EDUCATIVA: INTERÉS SIMPLE",
                     font=("Arial", 18, "bold"),
                     bg=COLOR_PRIMARIO,
                     fg="white",
                     pady=15)
    titulo.pack()
    
    # Subtítulo
    subtitulo = tk.Label(encabezado_frame,
                        text="Para estudiantes de bachillerato - Aprende practicando",
                        font=("Arial", 11),
                        bg=COLOR_PRIMARIO,
                        fg="#E0E0E0")
    subtitulo.pack(pady=(0, 10))
    
    # ========================================================================
    # CONTENEDOR PRINCIPAL CON SCROLL
    # ========================================================================
    
    # Crear un canvas y scrollbar para contenido desplazable
    canvas = tk.Canvas(ventana, bg=COLOR_FONDO, highlightthickness=0)
    scrollbar = tk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg=COLOR_FONDO)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True, padx=20)
    scrollbar.pack(side="right", fill="y")
    
    # Configurar scroll con rueda del mouse
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
    # ========================================================================
    # SECCIÓN 1: EXPLICACIÓN Y FÓRMULA
    # ========================================================================
    
    seccion_explicacion = tk.Frame(scrollable_frame, bg=COLOR_FONDO)
    seccion_explicacion.pack(fill="x", pady=(0, 20))
    
    # Título de sección
    tk.Label(seccion_explicacion,
            text="📚 CONCEPTOS BÁSICOS",
            font=("Arial", 14, "bold"),
            bg=COLOR_FONDO,
            fg=COLOR_SECUNDARIO).pack(anchor="w", pady=(0, 10))
    
    # Explicación breve
    explicacion_texto = """
El interés simple es el beneficio que se obtiene al prestar o invertir dinero durante un tiempo determinado.
Se llama 'simple' porque el interés se calcula siempre sobre la cantidad inicial, sin acumular los intereses
generados en periodos anteriores."""
    
    tk.Label(seccion_explicacion,
            text=explicacion_texto,
            font=("Arial", 10),
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO,
            justify="left",
            wraplength=700).pack(anchor="w", pady=(0, 15))
    
    # Botones de explicación
    botones_frame = tk.Frame(seccion_explicacion, bg=COLOR_FONDO)
    botones_frame.pack(fill="x", pady=(0, 10))
    
    crear_boton_con_hover(botones_frame, "📖 Ver Explicación Completa", 
                         mostrar_explicacion_interes, 0, 0)
    
    crear_boton_con_hover(botones_frame, "🧮 Ver Fórmula Interactiva", 
                         mostrar_formula_interactiva, 0, 1)
    
    crear_boton_con_hover(botones_frame, "🗑️ Limpiar Resultados", 
                         limpiar_resultados, 0, 2)
    
    # Separador
    ttk.Separator(scrollable_frame, orient="horizontal").pack(fill="x", pady=20)
    
    # ========================================================================
    # SECCIÓN 2: CÁLCULO DE INTERÉS SIMPLE
    # ========================================================================
    
    seccion_calculo = tk.Frame(scrollable_frame, bg=COLOR_FONDO)
    seccion_calculo.pack(fill="x", pady=(0, 20))
    
    tk.Label(seccion_calculo,
            text="🔢 CALCULAR INTERÉS SIMPLE",
            font=("Arial", 14, "bold"),
            bg=COLOR_FONDO,
            fg=COLOR_SECUNDARIO).grid(row=0, column=0, columnspan=3, 
                                     sticky="w", pady=(0, 15))
    
    # Campos de entrada para cálculo básico
    tk.Label(seccion_calculo,
            text="Capital Principal ($):",
            font=("Arial", 10),
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO).grid(row=1, column=0, padx=5, pady=5, sticky="w")
    
    widgets['entry_principal'] = tk.Entry(seccion_calculo,
                                         font=("Arial", 10),
                                         bg=COLOR_ENTRADA,
                                         width=25)
    widgets['entry_principal'].grid(row=1, column=1, padx=5, pady=5, sticky="w")
    
    tk.Label(seccion_calculo,
            text="Tasa de interés anual (%):",
            font=("Arial", 10),
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO).grid(row=2, column=0, padx=5, pady=5, sticky="w")
    
    widgets['entry_tasa'] = tk.Entry(seccion_calculo,
                                    font=("Arial", 10),
                                    bg=COLOR_ENTRADA,
                                    width=25)
    widgets['entry_tasa'].grid(row=2, column=1, padx=5, pady=5, sticky="w")
    
    tk.Label(seccion_calculo,
            text="Tiempo (años):",
            font=("Arial", 10),
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO).grid(row=3, column=0, padx=5, pady=5, sticky="w")
    
    widgets['entry_tiempo'] = tk.Entry(seccion_calculo,
                                      font=("Arial", 10),
                                      bg=COLOR_ENTRADA,
                                      width=25)
    widgets['entry_tiempo'].grid(row=3, column=1, padx=5, pady=5, sticky="w")
    
    # Botón para calcular
    btn_calcular_interes = crear_boton_con_hover(seccion_calculo,
                                                "Calcular Interés",
                                                calcular_y_mostrar_interes,
                                                4, 0, colspan=2)
    
    # Área de resultados
    widgets['resultado_interes'] = tk.Label(seccion_calculo,
                                           text="",
                                           font=("Arial", 11, "bold"),
                                           bg=COLOR_FONDO,
                                           fg=COLOR_SECUNDARIO,
                                           justify="left")
    widgets['resultado_interes'].grid(row=5, column=0, columnspan=3, 
                                     pady=15, sticky="w")
    
    # Separador
    ttk.Separator(scrollable_frame, orient="horizontal").pack(fill="x", pady=20)
    
    # ========================================================================
    # SECCIÓN 3: CÁLCULO DE MONTO DESEADO
    # ========================================================================
    
    seccion_monto = tk.Frame(scrollable_frame, bg=COLOR_FONDO)
    seccion_monto.pack(fill="x", pady=(0, 20))
    
    tk.Label(seccion_monto,
            text="🎯 CALCULAR CAPITAL PARA MONTO DESEADO",
            font=("Arial", 14, "bold"),
            bg=COLOR_FONDO,
            fg=COLOR_SECUNDARIO).grid(row=0, column=0, columnspan=3, 
                                     sticky="w", pady=(0, 15))
    
    # Explicación de esta sección
    explicacion_monto = "¿Cuánto necesito invertir hoy para tener un monto específico en el futuro?"
    tk.Label(seccion_monto,
            text=explicacion_monto,
            font=("Arial", 10),
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO,
            wraplength=700).grid(row=1, column=0, columnspan=3, 
                                sticky="w", pady=(0, 15))
    
    # Campos para cálculo de monto deseado
    tk.Label(seccion_monto,
            text="Monto deseado ($):",
            font=("Arial", 10),
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO).grid(row=2, column=0, padx=5, pady=5, sticky="w")
    
    widgets['entry_monto_deseado'] = tk.Entry(seccion_monto,
                                             font=("Arial", 10),
                                             bg=COLOR_ENTRADA,
                                             width=25)
    widgets['entry_monto_deseado'].grid(row=2, column=1, padx=5, pady=5, sticky="w")
    
    tk.Label(seccion_monto,
            text="Tasa de interés anual (%):",
            font=("Arial", 10),
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO).grid(row=3, column=0, padx=5, pady=5, sticky="w")
    
    widgets['entry_tasa_monto'] = tk.Entry(seccion_monto,
                                          font=("Arial", 10),
                                          bg=COLOR_ENTRADA,
                                          width=25)
    widgets['entry_tasa_monto'].grid(row=3, column=1, padx=5, pady=5, sticky="w")
    
    tk.Label(seccion_monto,
            text="Tiempo (años):",
            font=("Arial", 10),
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO).grid(row=4, column=0, padx=5, pady=5, sticky="w")
    
    widgets['entry_tiempo_monto'] = tk.Entry(seccion_monto,
                                            font=("Arial", 10),
                                            bg=COLOR_ENTRADA,
                                            width=25)
    widgets['entry_tiempo_monto'].grid(row=4, column=1, padx=5, pady=5, sticky="w")
    
    # Botón para calcular
    btn_calcular_monto = crear_boton_con_hover(seccion_monto,
                                              "Calcular Capital Necesario",
                                              calcular_y_mostrar_monto_deseado,
                                              5, 0, colspan=2)
    
    # Área de resultados
    widgets['resultado_capital'] = tk.Label(seccion_monto,
                                           text="",
                                           font=("Arial", 11, "bold"),
                                           bg=COLOR_FONDO,
                                           fg=COLOR_SECUNDARIO,
                                           justify="left")
    widgets['resultado_capital'].grid(row=6, column=0, columnspan=3, 
                                     pady=15, sticky="w")
    
    # ========================================================================
    # SECCIÓN 4: EJEMPLOS PRÁCTICOS
    # ========================================================================
    
    ttk.Separator(scrollable_frame, orient="horizontal").pack(fill="x", pady=20)
    
    seccion_ejemplos = tk.Frame(scrollable_frame, bg=COLOR_FONDO)
    seccion_ejemplos.pack(fill="x", pady=(0, 30))
    
    tk.Label(seccion_ejemplos,
            text="💡 EJEMPLOS PRÁCTICOS",
            font=("Arial", 14, "bold"),
            bg=COLOR_FONDO,
            fg=COLOR_SECUNDARIO).pack(anchor="w", pady=(0, 10))
    
    ejemplos = [
        ("Préstamo personal:", "$1,000 al 8% por 2 años → Interés: $160"),
        ("Inversión en CDT:", "$5,000 al 6% por 3 años → Interés: $900"),
        ("Ahorro para meta:", "$300 al 4% por 5 años → Monto total: $360"),
        ("Préstamo estudiantil:", "$2,000 al 5% por 4 años → Interés: $400")
    ]
    
    for ejemplo, resultado in ejemplos:
        frame_ejemplo = tk.Frame(seccion_ejemplos, bg=COLOR_FONDO)
        frame_ejemplo.pack(fill="x", pady=5)
        
        tk.Label(frame_ejemplo,
                text=ejemplo,
                font=("Arial", 10, "bold"),
                bg=COLOR_FONDO,
                fg=COLOR_PRIMARIO,
                width=25,
                anchor="w").pack(side="left")
        
        tk.Label(frame_ejemplo,
                text=resultado,
                font=("Arial", 10),
                bg=COLOR_FONDO,
                fg=COLOR_TEXTO).pack(side="left", padx=(10, 0))
    
    # ========================================================================
    # PIE DE PÁGINA
    # ========================================================================
    
    pie_frame = tk.Frame(scrollable_frame, bg=COLOR_FONDO)
    pie_frame.pack(fill="x", pady=(20, 30))
    
    tk.Label(pie_frame,
            text="© Aplicación Educativa para Bachillerato - Interés Simple",
            font=("Arial", 9),
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO).pack()
    
    tk.Label(pie_frame,
            text="Herramienta didáctica para comprender conceptos financieros básicos",
            font=("Arial", 8),
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO).pack(pady=5)
    
    # Configurar columnas para que se expandan
    for seccion in [seccion_calculo, seccion_monto]:
        seccion.columnconfigure(0, weight=1)
        seccion.columnconfigure(1, weight=1)
        seccion.columnconfigure(2, weight=1)
    
    return ventana

# ============================================================================
# PUNTO DE ENTRADA DE LA APLICACIÓN
# ============================================================================

def main():
    """Función principal que inicia la aplicación."""
    try:
        # Crear la interfaz gráfica
        ventana = crear_interfaz()
        
        # Establecer ícono (si está disponible)
        try:
            ventana.iconbitmap(default='icono.ico')
        except:
            pass  # Si no hay ícono, continuar sin él
        
        # Iniciar el loop principal de Tkinter
        ventana.mainloop()
        
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")
        messagebox.showerror("Error Crítico", 
                           f"No se pudo iniciar la aplicación:\n{str(e)}")

# ============================================================================
# EJECUCIÓN DEL PROGRAMA
# ============================================================================

if __name__ == "__main__":
    print("Iniciando aplicación educativa de Interés Simple...")
    print("Versión 1.0 - Para estudiantes de bachillerato")
    main()