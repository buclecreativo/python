import tkinter as tk
import math
from tkinter import messagebox, ttk

# ============================================
# CONFIGURACIÓN DE COLORES Y APARIENCIA
# ============================================
COLOR_FONDO = "#2C3E50"           # Azul oscuro moderno
COLOR_PRIMARIO = "#3498DB"        # Azul brillante
COLOR_SECUNDARIO = "#1ABC9C"      # Turquesa
COLOR_TERCIARIO = "#E74C3C"       # Rojo suave
COLOR_TEXTO = "#ECF0F1"           # Blanco humo
COLOR_BOTON_NORMAL = "#3498DB"    # Azul
COLOR_BOTON_HOVER = "#2980B9"     # Azul más oscuro (hover)
COLOR_RESULTADO = "#2ECC71"       # Verde para resultados
COLOR_FRAME = "#34495E"           # Gris azulado para frames

# ============================================
# FUNCIONES MATEMÁTICAS BÁSICAS
# ============================================
def es_primo(n):
    """Determina si un número es primo de forma didáctica"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limite = int(math.sqrt(n)) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return False
    return True

def generar_primos_hasta(limite):
    """Genera todos los números primos hasta un límite (Criba de Eratóstenes simplificada)"""
    if limite < 2:
        return []
    
    primos = [2]
    # Solo verificamos números impares
    for num in range(3, limite + 1, 2):
        if es_primo(num):
            primos.append(num)
    return primos

def factorizacion_prima(n):
    """Realiza la factorización prima de un número"""
    if n < 2:
        return f"{n} = {n}"
    
    factores = []
    temp = n
    
    # División por 2 primero
    while temp % 2 == 0:
        factores.append(2)
        temp //= 2
    
    # Luego por impares
    divisor = 3
    while divisor * divisor <= temp:
        while temp % divisor == 0:
            factores.append(divisor)
            temp //= divisor
        divisor += 2
    
    if temp > 1:
        factores.append(temp)
    
    # Formatear resultado
    if len(factores) == 1:
        return f"{n} es primo!"
    else:
        resultado = f"{n} = "
        resultado += " × ".join(map(str, factores))
        return resultado

# ============================================
# FUNCIONES DE INTERFAZ Y EVENTOS
# ============================================
def crear_boton(parent, texto, comando, fila, columna, colspan=1):
    """Crea un botón estilizado con efecto hover"""
    boton = tk.Button(
        parent,
        text=texto,
        command=comando,
        bg=COLOR_BOTON_NORMAL,
        fg=COLOR_TEXTO,
        font=("Arial", 11, "bold"),
        relief="flat",
        padx=20,
        pady=10,
        cursor="hand2"
    )
    
    # Posicionamiento
    boton.grid(row=fila, column=columna, columnspan=colspan, pady=10, padx=5, sticky="ew")
    
    # Efecto hover
    def on_enter(e):
        boton.config(bg=COLOR_BOTON_HOVER)
    
    def on_leave(e):
        boton.config(bg=COLOR_BOTON_NORMAL)
    
    boton.bind("<Enter>", on_enter)
    boton.bind("<Leave>", on_leave)
    
    return boton

def verificar_primo():
    """Verifica si el número ingresado es primo"""
    try:
        num = int(entry_verificar.get())
        if num < 0:
            messagebox.showwarning("Advertencia", "Por favor, ingresa un número positivo.")
            return
        
        resultado = f"El número {num} "
        if es_primo(num):
            resultado += "ES PRIMO ✅\n\n"
            resultado += f"• Solo es divisible por 1 y por sí mismo.\n"
            resultado += f"• Es el {len(generar_primos_hasta(num))}° número primo."
            color = COLOR_RESULTADO
        else:
            resultado += "NO ES PRIMO ❌\n\n"
            resultado += f"• Factorización: {factorizacion_prima(num)}"
            color = COLOR_TERCIARIO
        
        label_resultado_verificar.config(text=resultado, fg=color)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")

def mostrar_primos_rango():
    """Muestra todos los primos en un rango dado"""
    try:
        inicio = int(entry_rango_min.get())
        fin = int(entry_rango_max.get())
        
        if inicio < 0 or fin < 0:
            messagebox.showwarning("Advertencia", "Por favor, ingresa números positivos.")
            return
        
        if inicio > fin:
            inicio, fin = fin, inicio
            entry_rango_min.delete(0, tk.END)
            entry_rango_min.insert(0, str(inicio))
            entry_rango_max.delete(0, tk.END)
            entry_rango_max.insert(0, str(fin))
        
        primos = generar_primos_hasta(fin)
        primos_rango = [p for p in primos if p >= inicio]
        
        resultado = f"Primos entre {inicio} y {fin}:\n\n"
        
        if not primos_rango:
            resultado += "No se encontraron números primos en este rango."
            color = COLOR_TERCIARIO
        else:
            # Mostrar máximo 20 primos por línea para mejor visualización
            for i in range(0, len(primos_rango), 20):
                linea = primos_rango[i:i+20]
                resultado += ", ".join(map(str, linea)) + "\n"
            
            resultado += f"\nTotal: {len(primos_rango)} números primos encontrados."
            color = COLOR_RESULTADO
        
        text_rango.delete("1.0", tk.END)
        text_rango.insert("1.0", resultado)
        text_rango.config(fg=color)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def factorizar_numero():
    """Muestra la factorización prima de un número"""
    try:
        num = int(entry_factorizar.get())
        if num < 2:
            messagebox.showwarning("Advertencia", "Ingresa un número mayor que 1.")
            return
        
        resultado = factorizacion_prima(num)
        
        # Explicación adicional
        explicacion = "\n\n¿Qué significa esto?\n"
        explicacion += "• Cada número de la multiplicación es primo\n"
        explicacion += "• Multiplicados dan el número original\n"
        explicacion += "• Es la 'huella digital' única del número"
        
        label_resultado_factorizar.config(text=resultado + explicacion, fg=COLOR_RESULTADO)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")

def mostrar_info():
    """Muestra información educativa sobre números primos"""
    info = """INFORMACIÓN SOBRE NÚMEROS PRIMOS

¿Qué es un número primo?
• Solo es divisible por 1 y por sí mismo
• Ejemplos: 2, 3, 5, 7, 11, 13...

Curiosidades:
✓ El 2 es el único primo par
✓ Los primos son infinitos (Euclides)
✓ Base de la criptografía moderna
✓ 'Átomos' de las matemáticas

Aplicaciones:
• Criptografía (seguridad en internet)
• Ciencias de la computación
• Teoría de números
"""
    
    ventana_info = tk.Toplevel(ventana)
    ventana_info.title("Información sobre Números Primos")
    ventana_info.geometry("500x400")
    ventana_info.configure(bg=COLOR_FONDO)
    ventana_info.resizable(False, False)
    
    # Centrar ventana
    ventana_info.update_idletasks()
    ancho = ventana_info.winfo_width()
    alto = ventana_info.winfo_height()
    x = (ventana_info.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana_info.winfo_screenheight() // 2) - (alto // 2)
    ventana_info.geometry(f'{ancho}x{alto}+{x}+{y}')
    
    # Widgets de información
    label_titulo = tk.Label(
        ventana_info,
        text="📚 INFORMACIÓN EDUCATIVA",
        font=("Arial", 14, "bold"),
        bg=COLOR_FONDO,
        fg=COLOR_SECUNDARIO
    )
    label_titulo.pack(pady=10)
    
    text_info = tk.Text(
        ventana_info,
        height=20,
        width=60,
        bg=COLOR_FRAME,
        fg=COLOR_TEXTO,
        font=("Arial", 11),
        wrap="word",
        relief="flat",
        padx=10,
        pady=10
    )
    text_info.pack(pady=10, padx=10)
    text_info.insert("1.0", info)
    text_info.config(state="disabled")

def limpiar_todo():
    """Limpia todos los campos de la aplicación"""
    entry_verificar.delete(0, tk.END)
    entry_rango_min.delete(0, tk.END)
    entry_rango_max.delete(0, tk.END)
    entry_factorizar.delete(0, tk.END)
    label_resultado_verificar.config(text="", fg=COLOR_TEXTO)
    label_resultado_factorizar.config(text="", fg=COLOR_TEXTO)
    text_rango.delete("1.0", tk.END)

def centrar_ventana(ventana, ancho, alto):
    """Centra la ventana en la pantalla"""
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')

# ============================================
# CONFIGURACIÓN DE LA VENTANA PRINCIPAL
# ============================================
ventana = tk.Tk()
ventana.title("Explorador de Números Primos - Herramienta Educativa")
ventana.configure(bg=COLOR_FONDO)

# Tamaño y centrado
ancho_ventana = 900
alto_ventana = 700
centrar_ventana(ventana, ancho_ventana, alto_ventana)
ventana.resizable(False, False)

# ============================================
# TÍTULO PRINCIPAL
# ============================================
frame_titulo = tk.Frame(ventana, bg=COLOR_FONDO)
frame_titulo.pack(pady=20)

label_titulo = tk.Label(
    frame_titulo,
    text="🔢 EXPLORADOR DE NÚMEROS PRIMOS",
    font=("Arial", 22, "bold"),
    bg=COLOR_FONDO,
    fg=COLOR_SECUNDARIO
)
label_titulo.pack()

label_subtitulo = tk.Label(
    frame_titulo,
    text="Una herramienta educativa para aprender sobre los 'átomos' de las matemáticas",
    font=("Arial", 12),
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO
)
label_subtitulo.pack(pady=5)

# ============================================
# NOTEBOOK (PESTAÑAS) PARA ORGANIZAR FUNCIONALIDADES
# ============================================
style = ttk.Style()
style.theme_create('custom', parent='clam', settings={
    'TNotebook': {'configure': {'tabmargins': [2, 5, 2, 0], 'background': COLOR_FRAME}},
    'TNotebook.Tab': {
        'configure': {'padding': [10, 5], 'background': COLOR_FONDO, 'foreground': COLOR_TEXTO},
        'map': {'background': [('selected', COLOR_PRIMARIO)], 'expand': [('selected', [1, 1, 1, 0])]}
    }
})
style.theme_use('custom')

notebook = ttk.Notebook(ventana)
notebook.pack(fill="both", expand=True, padx=20, pady=10)

# ============================================
# PESTAÑA 1: VERIFICAR PRIMO
# ============================================
tab1 = tk.Frame(notebook, bg=COLOR_FRAME)
notebook.add(tab1, text="Verificar Primo")

# Contenido de la pestaña 1
frame_tab1 = tk.Frame(tab1, bg=COLOR_FRAME)
frame_tab1.pack(pady=20, padx=20)

# Instrucciones
label_inst1 = tk.Label(
    frame_tab1,
    text="Verifica si un número es primo o compuesto",
    font=("Arial", 13, "bold"),
    bg=COLOR_FRAME,
    fg=COLOR_TEXTO
)
label_inst1.grid(row=0, column=0, columnspan=3, pady=(0, 20))

label_inst2 = tk.Label(
    frame_tab1,
    text="Ingresa un número positivo:",
    font=("Arial", 11),
    bg=COLOR_FRAME,
    fg=COLOR_TEXTO
)
label_inst2.grid(row=1, column=0, sticky="w", pady=10)

# Entrada de número
entry_verificar = tk.Entry(
    frame_tab1,
    font=("Arial", 14),
    width=20,
    relief="flat",
    bg="#ECF0F1",
    fg="#2C3E50"
)
entry_verificar.grid(row=1, column=1, pady=10, padx=10)

# Botón de verificación
btn_verificar = crear_boton(frame_tab1, "Verificar Primo", verificar_primo, 1, 2, 1)

# Área de resultados
label_resultado_verificar = tk.Label(
    frame_tab1,
    text="",
    font=("Arial", 12),
    bg=COLOR_FRAME,
    fg=COLOR_TEXTO,
    justify="left",
    wraplength=600,
    padx=10,
    pady=10
)
label_resultado_verificar.grid(row=2, column=0, columnspan=3, pady=20, sticky="w")

# ============================================
# PESTAÑA 2: GENERAR PRIMOS EN RANGO
# ============================================
tab2 = tk.Frame(notebook, bg=COLOR_FRAME)
notebook.add(tab2, text="Generar en Rango")

# Contenido de la pestaña 2
frame_tab2 = tk.Frame(tab2, bg=COLOR_FRAME)
frame_tab2.pack(pady=20, padx=20)

# Instrucciones
label_inst3 = tk.Label(
    frame_tab2,
    text="Genera todos los números primos en un rango específico",
    font=("Arial", 13, "bold"),
    bg=COLOR_FRAME,
    fg=COLOR_TEXTO
)
label_inst3.grid(row=0, column=0, columnspan=4, pady=(0, 20))

# Entradas para el rango
tk.Label(frame_tab2, text="Desde:", font=("Arial", 11), bg=COLOR_FRAME, fg=COLOR_TEXTO).grid(row=1, column=0, sticky="w", pady=10)
entry_rango_min = tk.Entry(frame_tab2, font=("Arial", 12), width=15, relief="flat", bg="#ECF0F1", fg="#2C3E50")
entry_rango_min.grid(row=1, column=1, pady=10, padx=5)

tk.Label(frame_tab2, text="Hasta:", font=("Arial", 11), bg=COLOR_FRAME, fg=COLOR_TEXTO).grid(row=1, column=2, sticky="w", pady=10, padx=(20,0))
entry_rango_max = tk.Entry(frame_tab2, font=("Arial", 12), width=15, relief="flat", bg="#ECF0F1", fg="#2C3E50")
entry_rango_max.grid(row=1, column=3, pady=10, padx=5)

# Botón para generar
btn_generar = crear_boton(frame_tab2, "Generar Primos", mostrar_primos_rango, 2, 0, 4)

# Área de texto para resultados
text_rango = tk.Text(
    frame_tab2,
    height=15,
    width=70,
    font=("Consolas", 10),
    bg="#1C2833",
    fg=COLOR_TEXTO,
    wrap="word",
    relief="flat",
    padx=10,
    pady=10
)
text_rango.grid(row=3, column=0, columnspan=4, pady=20)

# ============================================
# PESTAÑA 3: FACTORIZACIÓN PRIMA
# ============================================
tab3 = tk.Frame(notebook, bg=COLOR_FRAME)
notebook.add(tab3, text="Factorización Prima")

# Contenido de la pestaña 3
frame_tab3 = tk.Frame(tab3, bg=COLOR_FRAME)
frame_tab3.pack(pady=20, padx=20)

# Instrucciones
label_inst4 = tk.Label(
    frame_tab3,
    text="Descompone un número en sus factores primos",
    font=("Arial", 13, "bold"),
    bg=COLOR_FRAME,
    fg=COLOR_TEXTO
)
label_inst4.grid(row=0, column=0, columnspan=3, pady=(0, 20))

tk.Label(
    frame_tab3,
    text="Ingresa un número (>1):",
    font=("Arial", 11),
    bg=COLOR_FRAME,
    fg=COLOR_TEXTO
).grid(row=1, column=0, sticky="w", pady=10)

entry_factorizar = tk.Entry(
    frame_tab3,
    font=("Arial", 14),
    width=20,
    relief="flat",
    bg="#ECF0F1",
    fg="#2C3E50"
)
entry_factorizar.grid(row=1, column=1, pady=10, padx=10)

btn_factorizar = crear_boton(frame_tab3, "Factorizar", factorizar_numero, 1, 2, 1)

# Área de resultados de factorización
label_resultado_factorizar = tk.Label(
    frame_tab3,
    text="",
    font=("Arial", 12),
    bg=COLOR_FRAME,
    fg=COLOR_TEXTO,
    justify="left",
    wraplength=600,
    padx=10,
    pady=10
)
label_resultado_factorizar.grid(row=2, column=0, columnspan=3, pady=20, sticky="w")

# ============================================
# BOTONES INFERIORES (GLOBALES)
# ============================================
frame_botones = tk.Frame(ventana, bg=COLOR_FONDO)
frame_botones.pack(pady=20)

# Botón de información
btn_info = crear_boton(frame_botones, "📚 Información Educativa", mostrar_info, 0, 0)

# Botón de limpiar
btn_limpiar = crear_boton(frame_botones, "🧹 Limpiar Todo", limpiar_todo, 0, 1)

# Botón de salir
btn_salir = crear_boton(frame_botones, "🚪 Salir", ventana.quit, 0, 2)

# ============================================
# PIE DE PÁGINA
# ============================================
frame_footer = tk.Frame(ventana, bg=COLOR_FONDO)
frame_footer.pack(pady=10)

label_footer = tk.Label(
    frame_footer,
    text="Herramienta educativa para Bachillerato • Matemáticas • Números Primos",
    font=("Arial", 10),
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO
)
label_footer.pack()

# ============================================
# INICIALIZACIÓN
# ============================================
# Establecer pestaña inicial
notebook.select(tab1)

# Configurar entrada inicial
entry_verificar.focus_set()

# Ejecutar aplicación
ventana.mainloop()