"""
APLICACIÓN EDUCATIVA: INTERÉS COMPUESTO
Versión: 1.0
Autor: Experto en Desarrollo Educativo
Descripción: Aplicación para enseñar el concepto de interés compuesto
             a estudiantes de bachillerato usando Tkinter.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math

# ============================================================================
# CONFIGURACIÓN DE COLORES Y ESTILO
# ============================================================================
COLOR_FONDO = "#F0F7FF"          # Azul claro muy suave
COLOR_PRIMARIO = "#4A6FA5"       # Azul principal
COLOR_SECUNDARIO = "#166088"     # Azul más oscuro
COLOR_TERCIARIO = "#95B8D1"      # Azul pastel
COLOR_TEXTO = "#2C3E50"          # Gris azulado oscuro para texto
COLOR_BOTON = "#4A6FA5"          # Azul para botones
COLOR_BOTON_HOVER = "#166088"    # Azul oscuro para hover
COLOR_EXITO = "#2ECC71"          # Verde para resultados
COLOR_ENTRADA = "#FFFFFF"        # Blanco para campos de entrada

# ============================================================================
# FUNCIONES MATEMÁTICAS PARA INTERÉS COMPUESTO
# ============================================================================

def calcular_monto_final():
    """Calcula el monto final con interés compuesto y muestra explicación"""
    try:
        # Obtener valores de los campos de entrada
        capital = float(entrada_capital.get())
        tasa = float(entrada_tasa.get())
        tiempo = float(entrada_tiempo.get())
        periodos = int(entrada_periodos.get())
        
        # Validar valores positivos
        if capital <= 0 or tasa <= 0 or tiempo <= 0 or periodos <= 0:
            messagebox.showwarning("Valores inválidos", 
                                   "Todos los valores deben ser mayores que cero.")
            return
        
        # Calcular monto final
        tasa_decimal = tasa / 100
        monto_final = capital * ((1 + tasa_decimal/periodos) ** (periodos * tiempo))
        interes_generado = monto_final - capital
        
        # Mostrar resultados
        resultado_var.set(f"${monto_final:,.2f}")
        interes_var.set(f"${interes_generado:,.2f}")
        
        # Mostrar explicación paso a paso
        explicacion = f"""📈 CÁLCULO PASO A PASO:

1. Capital inicial: ${capital:,.2f}
2. Tasa anual: {tasa}% = {tasa_decimal}
3. Tiempo: {tiempo} años
4. Periodos por año: {periodos}

FÓRMULA:
M = C × (1 + r/n)^(n×t)

Donde:
M = Monto final
C = Capital inicial (${capital:,.2f})
r = Tasa de interés ({tasa_decimal})
n = Periodos por año ({periodos})
t = Tiempo en años ({tiempo})

CÁLCULO:
M = {capital:,.2f} × (1 + {tasa_decimal}/{periodos})^({periodos}×{tiempo})
M = {capital:,.2f} × (1 + {tasa_decimal/periodos:.4f})^({periodos*tiempo})
M = {capital:,.2f} × ({1 + tasa_decimal/periodos:.4f})^{periodos*tiempo}
M = {capital:,.2f} × {((1 + tasa_decimal/periodos) ** (periodos * tiempo)):.4f}
M = ${monto_final:,.2f}

💰 INTERÉS GENERADO: ${interes_generado:,.2f}
"""
        texto_explicacion.delete(1.0, tk.END)
        texto_explicacion.insert(1.0, explicacion)
        
        # Actualizar gráfico
        actualizar_grafico(capital, tasa_decimal, tiempo, periodos)
        
    except ValueError:
        messagebox.showerror("Error de entrada", 
                            "Por favor, ingresa valores numéricos válidos.")

def calcular_tiempo_objetivo():
    """Calcula el tiempo necesario para alcanzar un monto objetivo"""
    try:
        capital = float(entrada_capital.get())
        tasa = float(entrada_tasa.get())
        periodos = int(entrada_periodos.get())
        monto_objetivo = float(entrada_objetivo.get())
        
        if capital <= 0 or tasa <= 0 or periodos <= 0 or monto_objetivo <= capital:
            messagebox.showwarning("Valores inválidos", 
                                   "El monto objetivo debe ser mayor al capital inicial.")
            return
        
        # Calcular tiempo necesario
        tasa_decimal = tasa / 100
        tiempo = math.log(monto_objetivo/capital) / (periodos * math.log(1 + tasa_decimal/periodos))
        
        # Mostrar resultado
        tiempo_var.set(f"{tiempo:.2f} años")
        
        # Explicación
        explicacion = f"""⏰ TIEMPO PARA ALCANZAR OBJETIVO:

Capital inicial: ${capital:,.2f}
Tasa anual: {tasa}%
Monto objetivo: ${monto_objetivo:,.2f}

FÓRMULA:
t = log(M/C) ÷ [n × log(1 + r/n)]

CÁLCULO:
t = log({monto_objetivo/capital:.4f}) ÷ [{periodos} × log(1 + {tasa_decimal}/{periodos})]
t = {math.log(monto_objetivo/capital):.4f} ÷ [{periodos} × {math.log(1 + tasa_decimal/periodos):.4f}]
t = {math.log(monto_objetivo/capital):.4f} ÷ {periodos * math.log(1 + tasa_decimal/periodos):.4f}
t = {tiempo:.2f} años

Con interés compuesto, necesitas aproximadamente {tiempo:.1f} años
para que ${capital:,.2f} se conviertan en ${monto_objetivo:,.2f}.
"""
        texto_explicacion.delete(1.0, tk.END)
        texto_explicacion.insert(1.0, explicacion)
        
    except ValueError:
        messagebox.showerror("Error", "Ingresa valores válidos en todos los campos.")

def actualizar_grafico(capital, tasa, tiempo, periodos):
    """Genera datos para mostrar crecimiento en el tiempo"""
    # Limpiar gráfico anterior
    for item in canvas_grafico.find_all():
        canvas_grafico.delete(item)
    
    # Configurar área del gráfico
    ancho = 400
    alto = 200
    margen = 40
    
    # Dibujar ejes
    canvas_grafico.create_line(margen, alto-margen, ancho-margen, alto-margen, width=2)  # Eje X
    canvas_grafico.create_line(margen, margen, margen, alto-margen, width=2)  # Eje Y
    
    # Etiquetas de ejes
    canvas_grafico.create_text(ancho//2, alto-10, text="Años", fill=COLOR_TEXTO)
    canvas_grafico.create_text(15, alto//2, text="Monto ($)", angle=90, fill=COLOR_TEXTO)
    
    # Generar puntos del gráfico
    puntos = []
    for año in range(int(tiempo) + 1):
        monto = capital * ((1 + tasa/periodos) ** (periodos * año))
        x = margen + (año/tiempo) * (ancho - 2*margen) if tiempo > 0 else margen
        y = alto - margen - (monto/(capital*3)) * (alto - 2*margen) if monto > 0 else alto-margen
        puntos.append((x, y))
        
        # Marcar cada año
        if año <= tiempo:
            canvas_grafico.create_text(x, alto-margen+10, text=str(año), fill=COLOR_TEXTO)
            canvas_grafico.create_line(x, alto-margen-5, x, alto-margen+5, fill=COLOR_TEXTO)
    
    # Dibujar línea del gráfico
    for i in range(len(puntos)-1):
        canvas_grafico.create_line(puntos[i][0], puntos[i][1], 
                                  puntos[i+1][0], puntos[i+1][1], 
                                  fill=COLOR_PRIMARIO, width=3)
    
    # Puntos de datos
    for x, y in puntos:
        canvas_grafico.create_oval(x-4, y-4, x+4, y+4, 
                                  fill=COLOR_SECUNDARIO, outline=COLOR_SECUNDARIO)

def limpiar_campos():
    """Limpia todos los campos de entrada y resultados"""
    entrada_capital.delete(0, tk.END)
    entrada_tasa.delete(0, tk.END)
    entrada_tiempo.delete(0, tk.END)
    entrada_periodos.delete(0, tk.END)
    entrada_objetivo.delete(0, tk.END)
    resultado_var.set("$0.00")
    interes_var.set("$0.00")
    tiempo_var.set("0 años")
    texto_explicacion.delete(1.0, tk.END)
    
    # Limpiar gráfico
    for item in canvas_grafico.find_all():
        canvas_grafico.delete(item)

def crear_efecto_hover(boton, color_normal, color_hover):
    """Crea efecto hover para un botón"""
    def entrar(event):
        boton.config(bg=color_hover)
    def salir(event):
        boton.config(bg=color_normal)
    
    boton.bind("<Enter>", entrar)
    boton.bind("<Leave>", salir)

def mostrar_info_interes():
    """Muestra información educativa sobre interés compuesto"""
    info = """💡 ¿QUÉ ES EL INTERÉS COMPUESTO?

El interés compuesto es el interés calculado sobre el capital inicial 
Y también sobre el interés acumulado de periodos anteriores.

📊 FÓRMULA PRINCIPAL:
M = C × (1 + r/n)^(n×t)

Donde:
• M = Monto final
• C = Capital inicial
• r = Tasa de interés anual (en decimal)
• n = Número de veces que se capitaliza por año
• t = Tiempo en años

🎯 EJEMPLO PRÁCTICO:
Si inviertes $1,000 al 5% anual durante 10 años:
• Interés simple: $1,500
• Interés compuesto: $1,628.89

El interés compuesto hace que tu dinero crezca más rápido porque
los intereses generan nuevos intereses. ¡Es como una bola de nieve financiera!

💭 REGLA DEL 72:
Para saber cuánto tiempo tarda en duplicarse tu dinero:
72 ÷ tasa de interés = años aproximados
Ej: al 6% anual, se duplica en ≈ 12 años.
"""
    messagebox.showinfo("Concepto: Interés Compuesto", info)

# ============================================================================
# CONFIGURACIÓN DE LA VENTANA PRINCIPAL
# ============================================================================

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Educativa de Interés Compuesto")
ventana.geometry("900x900")
ventana.configure(bg=COLOR_FONDO)
ventana.resizable(False, False)

# Centrar ventana en pantalla
ventana.update_idletasks()
ancho_ventana = ventana.winfo_width()
alto_ventana = ventana.winfo_height()
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)
ventana.geometry(f'{ancho_ventana}x{alto_ventana}+{x}+{y}')

# ============================================================================
# WIDGETS DE LA INTERFAZ
# ============================================================================

# Título principal
frame_titulo = tk.Frame(ventana, bg=COLOR_FONDO)
frame_titulo.pack(pady=20)

titulo = tk.Label(frame_titulo, 
                  text="💸 CALCULADORA DE INTERÉS COMPUESTO", 
                  font=("Arial", 20, "bold"),
                  bg=COLOR_FONDO,
                  fg=COLOR_SECUNDARIO)
titulo.pack()

subtitulo = tk.Label(frame_titulo,
                     text="Herramienta educativa para estudiantes de bachillerato",
                     font=("Arial", 12),
                     bg=COLOR_FONDO,
                     fg=COLOR_TEXTO)
subtitulo.pack(pady=5)

# Frame principal con dos columnas
frame_principal = tk.Frame(ventana, bg=COLOR_FONDO)
frame_principal.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# Columna izquierda - Entradas y controles
frame_izquierda = tk.Frame(frame_principal, bg=COLOR_FONDO)
frame_izquierda.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

# Frame de entrada de datos
frame_entradas = tk.LabelFrame(frame_izquierda, 
                               text="📝 DATOS DE ENTRADA",
                               font=("Arial", 11, "bold"),
                               bg=COLOR_FONDO,
                               fg=COLOR_SECUNDARIO,
                               padx=15,
                               pady=15)
frame_entradas.pack(fill=tk.X, pady=(0, 15))

# Función para crear filas de entrada
def crear_fila_entrada(parent, texto, variable, row):
    tk.Label(parent, text=texto, bg=COLOR_FONDO, fg=COLOR_TEXTO, 
             font=("Arial", 10)).grid(row=row, column=0, sticky="w", pady=5)
    entrada = tk.Entry(parent, width=20, font=("Arial", 10), 
                      bg=COLOR_ENTRADA, relief=tk.SOLID, borderwidth=1)
    entrada.grid(row=row, column=1, padx=10, pady=5)
    return entrada

# Crear campos de entrada
entrada_capital = crear_fila_entrada(frame_entradas, "Capital inicial ($):", "", 0)
entrada_tasa = crear_fila_entrada(frame_entradas, "Tasa de interés anual (%):", "", 1)
entrada_tiempo = crear_fila_entrada(frame_entradas, "Tiempo (años):", "", 2)
entrada_periodos = crear_fila_entrada(frame_entradas, "Periodos por año:", "", 3)

# Configurar valores por defecto
entrada_capital.insert(0, "1000")
entrada_tasa.insert(0, "5")
entrada_tiempo.insert(0, "10")
entrada_periodos.insert(0, "12")

# Campo para objetivo (tiempo)
frame_objetivo = tk.Frame(frame_izquierda, bg=COLOR_FONDO)
frame_objetivo.pack(fill=tk.X, pady=(0, 15))

tk.Label(frame_objetivo, text="Objetivo - Calcular tiempo para:", 
         bg=COLOR_FONDO, fg=COLOR_TEXTO, font=("Arial", 10, "bold")).pack(anchor="w")
frame_obj_input = tk.Frame(frame_objetivo, bg=COLOR_FONDO)
frame_obj_input.pack(fill=tk.X, pady=5)

tk.Label(frame_obj_input, text="Monto objetivo ($):", bg=COLOR_FONDO, 
         fg=COLOR_TEXTO, font=("Arial", 10)).pack(side=tk.LEFT)
entrada_objetivo = tk.Entry(frame_obj_input, width=20, font=("Arial", 10), 
                           bg=COLOR_ENTRADA, relief=tk.SOLID, borderwidth=1)
entrada_objetivo.pack(side=tk.LEFT, padx=10)
entrada_objetivo.insert(0, "2000")

# Frame de botones
frame_botones = tk.Frame(frame_izquierda, bg=COLOR_FONDO)
frame_botones.pack(fill=tk.X, pady=(0, 15))

# Botones principales
btn_calcular = tk.Button(frame_botones, text="Calcular Monto Final", 
                        font=("Arial", 10, "bold"),
                        bg=COLOR_BOTON,
                        fg="white",
                        relief=tk.RAISED,
                        borderwidth=2,
                        width=20,
                        height=2,
                        command=calcular_monto_final)
btn_calcular.pack(side=tk.LEFT, padx=5, pady=5)

btn_tiempo = tk.Button(frame_botones, text="Calcular Tiempo", 
                      font=("Arial", 10, "bold"),
                      bg=COLOR_TERCIARIO,
                      fg=COLOR_TEXTO,
                      relief=tk.RAISED,
                      borderwidth=2,
                      width=20,
                      height=2,
                      command=calcular_tiempo_objetivo)
btn_tiempo.pack(side=tk.LEFT, padx=5, pady=5)

btn_limpiar = tk.Button(frame_botones, text="Limpiar Todo", 
                       font=("Arial", 10, "bold"),
                       bg="#E74C3C",
                       fg="white",
                       relief=tk.RAISED,
                       borderwidth=2,
                       width=20,
                       height=2,
                       command=limpiar_campos)
btn_limpiar.pack(side=tk.LEFT, padx=5, pady=5)

# Aplicar efectos hover
crear_efecto_hover(btn_calcular, COLOR_BOTON, COLOR_BOTON_HOVER)
crear_efecto_hover(btn_tiempo, COLOR_TERCIARIO, COLOR_SECUNDARIO)
crear_efecto_hover(btn_limpiar, "#E74C3C", "#C0392B")

# Frame de resultados
frame_resultados = tk.LabelFrame(frame_izquierda, 
                                text="📊 RESULTADOS",
                                font=("Arial", 11, "bold"),
                                bg=COLOR_FONDO,
                                fg=COLOR_SECUNDARIO,
                                padx=15,
                                pady=15)
frame_resultados.pack(fill=tk.BOTH, expand=True)

# Variables para resultados
resultado_var = tk.StringVar(value="$0.00")
interes_var = tk.StringVar(value="$0.00")
tiempo_var = tk.StringVar(value="0 años")

# Mostrar resultados
tk.Label(frame_resultados, text="Monto Final:", bg=COLOR_FONDO, 
         fg=COLOR_TEXTO, font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
tk.Label(frame_resultados, textvariable=resultado_var, bg=COLOR_FONDO, 
         fg=COLOR_EXITO, font=("Arial", 12, "bold")).grid(row=0, column=1, sticky="w", padx=10)

tk.Label(frame_resultados, text="Interés Generado:", bg=COLOR_FONDO, 
         fg=COLOR_TEXTO, font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
tk.Label(frame_resultados, textvariable=interes_var, bg=COLOR_FONDO, 
         fg=COLOR_EXITO, font=("Arial", 12, "bold")).grid(row=1, column=1, sticky="w", padx=10)

tk.Label(frame_resultados, text="Tiempo Necesario:", bg=COLOR_FONDO, 
         fg=COLOR_TEXTO, font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
tk.Label(frame_resultados, textvariable=tiempo_var, bg=COLOR_FONDO, 
         fg=COLOR_EXITO, font=("Arial", 12, "bold")).grid(row=2, column=1, sticky="w", padx=10)

# Gráfico simple
frame_grafico = tk.Frame(frame_resultados, bg="white", relief=tk.SUNKEN, borderwidth=2)
frame_grafico.grid(row=3, column=0, columnspan=2, pady=15, sticky="nsew")
frame_resultados.grid_rowconfigure(3, weight=1)
frame_resultados.grid_columnconfigure(0, weight=1)
frame_resultados.grid_columnconfigure(1, weight=1)

canvas_grafico = tk.Canvas(frame_grafico, bg="white", width=400, height=200)
canvas_grafico.pack(padx=5, pady=5)

# Columna derecha - Explicación
frame_derecha = tk.Frame(frame_principal, bg=COLOR_FONDO)
frame_derecha.pack(side=tk.RIGHT, padx=10, fill=tk.BOTH, expand=True)

frame_explicacion = tk.LabelFrame(frame_derecha,
                                 text="📚 EXPLICACIÓN PASO A PASO",
                                 font=("Arial", 11, "bold"),
                                 bg=COLOR_FONDO,
                                 fg=COLOR_SECUNDARIO,
                                 padx=15,
                                 pady=15)
frame_explicacion.pack(fill=tk.BOTH, expand=True)

# Área de texto para explicación
texto_explicacion = tk.Text(frame_explicacion,
                           wrap=tk.WORD,
                           width=45,
                           height=20,
                           font=("Arial", 10),
                           bg="#FFFFFF",
                           fg=COLOR_TEXTO,
                           relief=tk.SOLID,
                           borderwidth=1,
                           padx=10,
                           pady=10)
texto_explicacion.pack(fill=tk.BOTH, expand=True)

# Barra de desplazamiento para el texto
scrollbar = tk.Scrollbar(texto_explicacion)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
texto_explicacion.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=texto_explicacion.yview)

# Insertar texto introductorio
intro_texto = """👋 BIENVENIDO A LA CALCULADORA DE INTERÉS COMPUESTO

Esta herramienta te ayudará a entender cómo funciona el interés compuesto, uno de los conceptos más importantes en finanzas.

📝 INSTRUCCIONES:
1. Ingresa los valores en los campos de la izquierda
2. Haz clic en "Calcular Monto Final" para ver el resultado
3. Usa "Calcular Tiempo" para saber cuánto tiempo necesitas para alcanzar un monto objetivo
4. Lee la explicación detallada aquí

💡 CONSEJO:
Prueba diferentes valores para ver cómo cambian los resultados:
• Mayor tasa = crecimiento más rápido
• Más tiempo = más interés generado
• Más periodos = mayor capitalización

¡Comienza ingresando tus valores y haz clic en calcular!"""
texto_explicacion.insert(1.0, intro_texto)

# Frame inferior con botón de información
frame_inferior = tk.Frame(ventana, bg=COLOR_FONDO)
frame_inferior.pack(pady=10)

btn_info = tk.Button(frame_inferior, text="📖 ¿Qué es el Interés Compuesto?", 
                    font=("Arial", 10, "bold"),
                    bg=COLOR_PRIMARIO,
                    fg="white",
                    relief=tk.RAISED,
                    borderwidth=2,
                    width=30,
                    height=2,
                    command=mostrar_info_interes)
btn_info.pack(pady=5)
crear_efecto_hover(btn_info, COLOR_PRIMARIO, COLOR_SECUNDARIO)

# Pie de página
pie = tk.Label(ventana, 
               text="Herramienta educativa para bachillerato - © 2024",
               font=("Arial", 9),
               bg=COLOR_FONDO,
               fg=COLOR_TEXTO)
pie.pack(pady=10)

# ============================================================================
# INICIALIZAR APLICACIÓN
# ============================================================================

# Ejecutar cálculos iniciales para mostrar ejemplo
ventana.after(100, calcular_monto_final)

# Iniciar loop principal
ventana.mainloop()