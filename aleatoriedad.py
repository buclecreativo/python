import tkinter as tk
from tkinter import ttk, messagebox
import random
import math

# =============================================
# CONFIGURACIÓN INICIAL Y VARIABLES GLOBALES
# =============================================
ventana = None  # Ventana principal
frame_principal = None  # Frame principal para los widgets
color_fondo = "#f0f8ff"  # Color de fondo principal (azul claro)
color_boton = "#4a90e2"  # Color principal de botones
color_boton_hover = "#357abd"  # Color de botones al pasar el mouse
color_texto = "#333333"  # Color de texto principal

# Variables para seguimiento de estadísticas
lanzamientos_dados = 0
lanzamientos_moneda = 0
selecciones_ruleta = 0
cartas_repartidas = 0

# =============================================
# FUNCIONES DE UTILIDAD
# =============================================

def aplicar_estilo_boton(boton):
    """Aplica el estilo visual a un botón y añade efecto hover"""
    boton.config(
        bg=color_boton,
        fg="white",
        font=("Arial", 10, "bold"),
        relief="raised",
        padx=15,
        pady=8,
        cursor="hand2"
    )
    
    # Configurar efecto hover
    boton.bind("<Enter>", lambda e: boton.config(bg=color_boton_hover))
    boton.bind("<Leave>", lambda e: boton.config(bg=color_boton))

def crear_frame_titulo(parent, titulo, descripcion):
    """Crea un frame con un título y descripción para secciones"""
    frame = tk.Frame(parent, bg=color_fondo)
    
    label_titulo = tk.Label(
        frame,
        text=titulo,
        bg=color_fondo,
        fg="#2c3e50",
        font=("Arial", 14, "bold")
    )
    label_titulo.pack(pady=(0, 5))
    
    label_desc = tk.Label(
        frame,
        text=descripcion,
        bg=color_fondo,
        fg=color_texto,
        font=("Arial", 10),
        wraplength=550,
        justify="left"
    )
    label_desc.pack(pady=(0, 10))
    
    return frame

def mostrar_explicacion_random():
    """Muestra una explicación sobre la librería random"""
    explicacion = """
    La librería RANDOM en Python nos permite generar números aleatorios.
    
    Aleatorio significa que no podemos predecir con certeza el resultado.
    En programación, la aleatoriedad se usa para:
    • Juegos (dados, cartas, ruleta)
    • Simulaciones científicas
    • Muestreos estadísticos
    • Asignaciones aleatorias
    
    IMPORTANTE: En computación, los números "aleatorios" son en realidad
    pseudoaleatorios (generados por algoritmos), pero son lo suficientemente
    impredecibles para la mayoría de aplicaciones.
    """
    
    messagebox.showinfo("¿Qué es RANDOM?", explicacion)

# =============================================
# FUNCIONALIDADES PRINCIPALES DEL JUEGO
# =============================================

# ---------- FUNCIÓN 1: LANZAR DADO ----------
def lanzar_dado():
    """Simula el lanzamiento de un dado de 6 caras"""
    global lanzamientos_dados
    
    # Generar número aleatorio entre 1 y 6
    resultado = random.randint(1, 6)
    lanzamientos_dados += 1
    
    # Mostrar resultado visualmente
    mostrar_resultado(
        "🎲 Lanzamiento de Dado",
        f"Resultado: {resultado}",
        f"Has lanzado el dado {lanzamientos_dados} veces.\n"
        f"random.randint(1, 6) generó: {resultado}"
    )
    
    # Actualizar estadísticas
    actualizar_estadisticas()

# ---------- FUNCIÓN 2: LANZAR MONEDA ----------
def lanzar_moneda():
    """Simula el lanzamiento de una moneda (cara o cruz)"""
    global lanzamientos_moneda
    
    # Elegir aleatoriamente entre cara o cruz
    resultado = random.choice(["CARA", "CRUZ"])
    lanzamientos_moneda += 1
    
    # Determinar emoji para mostrar
    emoji = "😊" if resultado == "CARA" else "✖️"
    
    mostrar_resultado(
        f"{emoji} Lanzamiento de Moneda",
        f"Resultado: {resultado}",
        f"Has lanzado la moneda {lanzamientos_moneda} veces.\n"
        f"random.choice(['CARA', 'CRUZ']) seleccionó: {resultado}"
    )
    
    actualizar_estadisticas()

# ---------- FUNCIÓN 3: RULETA DE COLORES ----------
def girar_ruleta():
    """Simula una ruleta que selecciona un color aleatorio"""
    global selecciones_ruleta
    
    # Lista de colores disponibles
    colores = ["ROJO", "VERDE", "AZUL", "AMARILLO", "NARANJA", "MORADO"]
    
    # Seleccionar color aleatorio
    color_seleccionado = random.choice(colores)
    selecciones_ruleta += 1
    
    # Mapear colores a códigos hexadecimales para mostrar
    colores_hex = {
        "ROJO": "#ff6b6b",
        "VERDE": "#51cf66",
        "AZUL": "#339af0",
        "AMARILLO": "#ffd43b",
        "NARANJA": "#ff922b",
        "MORADO": "#cc5de8"
    }
    
    mostrar_resultado(
        "🎡 Ruleta de Colores",
        f"Color seleccionado: {color_seleccionado}",
        f"La ruleta ha girado {selecciones_ruleta} veces.\n"
        f"random.choice(colores) seleccionó: {color_seleccionado}",
        color_fondo=colores_hex[color_seleccionado]
    )
    
    actualizar_estadisticas()

# ---------- FUNCIÓN 4: REPARTIR CARTAS ----------
def repartir_carta():
    """Simula repartir una carta aleatoria de una baraja"""
    global cartas_repartidas
    
    # Definir palos y valores de cartas
    palos = ["♠️ Picas", "♥️ Corazones", "♦️ Diamantes", "♣️ Tréboles"]
    valores = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jota", "Reina", "Rey"]
    
    # Seleccionar palo y valor aleatorios
    palo = random.choice(palos)
    valor = random.choice(valores)
    cartas_repartidas += 1
    
    mostrar_resultado(
        "🃏 Repartir Carta",
        f"Carta: {valor} de {palo}",
        f"Se han repartido {cartas_repartidas} cartas.\n"
        f"random.choice() seleccionó: {valor} de {palo}"
    )
    
    actualizar_estadisticas()

# ---------- FUNCIÓN 5: GENERAR CONTRASEÑA ----------
def generar_contrasena():
    """Genera una contraseña aleatoria segura"""
    # Caracteres disponibles para la contraseña
    letras_min = "abcdefghijklmnopqrstuvwxyz"
    letras_may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    simbolos = "!@#$%^&*()"
    
    # Combinar todos los caracteres
    todos_caracteres = letras_min + letras_may + numeros + simbolos
    
    # Longitud aleatoria entre 8 y 12 caracteres
    longitud = random.randint(8, 12)
    
    # Generar contraseña aleatoria
    contrasena = ""
    for _ in range(longitud):
        contrasena += random.choice(todos_caracteres)
    
    mostrar_resultado(
        "🔒 Generador de Contraseñas",
        f"Contraseña generada: {contrasena}",
        f"Longitud: {longitud} caracteres\n"
        f"Se usó random.choice() para seleccionar cada carácter\n"
        f"NOTA: Esta es una contraseña de ejemplo. Para uso real,\n"
        f"considera usar métodos más seguros como secrets module."
    )

# ---------- FUNCIÓN 6: LOTERÍA NUMÉRICA ----------
def generar_loteria():
    """Genera números aleatorios para un juego de lotería"""
    # Generar 6 números únicos entre 1 y 49
    numeros_loteria = random.sample(range(1, 50), 6)
    numeros_loteria.sort()  # Ordenar de menor a mayor
    
    mostrar_resultado(
        "🎫 Números de Lotería",
        f"Números: {', '.join(map(str, numeros_loteria))}",
        f"Se usó random.sample() para obtener 6 números únicos\n"
        f"entre 1 y 49. random.sample() asegura que no haya\n"
        f"números repetidos, a diferencia de random.randint()."
    )

# ---------- FUNCIÓN 7: CAMINATA ALEATORIA ----------
def caminata_aleatoria():
    """Simula una caminata aleatoria en 2D"""
    # Iniciar en el centro (0, 0)
    x, y = 0, 0
    pasos = 20
    historial = [(x, y)]
    
    # Explicación de la caminata aleatoria
    explicacion = "Una caminata aleatoria es un proceso donde cada paso\n"
    explicacion += "se toma en dirección aleatoria. Se usa en:\n"
    explicacion += "• Física (movimiento browniano)\n"
    explicacion += "• Finanzas (mercados bursátiles)\n"
    explicacion += "• Biología (movimiento de bacterias)\n\n"
    explicacion += "Simulando 20 pasos:\n"
    
    # Realizar la caminata
    for paso in range(pasos):
        # Elegir dirección aleatoria
        direccion = random.choice(["ARRIBA", "ABAJO", "IZQUIERDA", "DERECHA"])
        
        # Mover según la dirección
        if direccion == "ARRIBA":
            y += 1
        elif direccion == "ABAJO":
            y -= 1
        elif direccion == "IZQUIERDA":
            x -= 1
        else:  # DERECHA
            x += 1
            
        historial.append((x, y))
        explicacion += f"Paso {paso+1}: {direccion} → Posición: ({x}, {y})\n"
    
    # Calcular distancia desde el origen
    distancia = math.sqrt(x**2 + y**2)
    explicacion += f"\nDistancia desde el origen: {distancia:.2f} unidades"
    
    mostrar_resultado(
        "🚶 Caminata Aleatoria",
        f"Posición final: ({x}, {y})",
        explicacion
    )

# =============================================
# FUNCIONES AUXILIARES (CORREGIDAS)
# =============================================

def mostrar_resultado(titulo, resultado, explicacion, color_fondo="#e9ecef"):
    """Muestra el resultado de una operación en un cuadro de diálogo personalizado"""
    # Crear ventana de resultados
    ventana_resultado = tk.Toplevel(ventana)
    ventana_resultado.title(titulo)
    ventana_resultado.geometry("600x400")
    ventana_resultado.configure(bg=color_fondo)
    ventana_resultado.resizable(False, False)
    
    # Centrar ventana
    ventana_resultado.transient(ventana)
    ventana_resultado.grab_set()
    
    # Título
    titulo_label = tk.Label(
        ventana_resultado,
        text=titulo,
        bg=color_fondo,
        fg="#2c3e50",
        font=("Arial", 16, "bold")
    )
    titulo_label.pack(pady=(20, 10))
    
    # Resultado (más grande y destacado)
    resultado_label = tk.Label(
        ventana_resultado,
        text=resultado,
        bg=color_fondo,
        fg="#1864ab",
        font=("Arial", 20, "bold")
    )
    resultado_label.pack(pady=(0, 20))
    
    # Explicación
    explicacion_label = tk.Label(
        ventana_resultado,
        text=explicacion,
        bg=color_fondo,
        fg=color_texto,
        font=("Arial", 10),
        justify="left",
        wraplength=450
    )
    explicacion_label.pack(pady=(0, 20), padx=20)
    
    # Botón para cerrar
    btn_cerrar = tk.Button(
        ventana_resultado,
        text="Cerrar",
        command=ventana_resultado.destroy,
        bg=color_boton,
        fg="white",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=5
    )
    btn_cerrar.pack(pady=(0, 20))
    
    # Aplicar efecto hover al botón
    aplicar_estilo_boton(btn_cerrar)

def actualizar_estadisticas():
    """Actualiza el contador de estadísticas en la interfaz"""
    if 'label_estadisticas' in globals():
        estadisticas_texto = (
            f"Lanzamientos de dado: {lanzamientos_dados} | "
            f"Lanzamientos de moneda: {lanzamientos_moneda} | "
            f"Giros de ruleta: {selecciones_ruleta} | "
            f"Cartas repartidas: {cartas_repartidas}"
        )
        label_estadisticas.config(text=estadisticas_texto)

def reiniciar_estadisticas():
    """Reinicia todas las estadísticas a cero"""
    global lanzamientos_dados, lanzamientos_moneda, selecciones_ruleta, cartas_repartidas
    
    lanzamientos_dados = 0
    lanzamientos_moneda = 0
    selecciones_ruleta = 0
    cartas_repartidas = 0
    
    actualizar_estadisticas()
    messagebox.showinfo("Estadísticas Reiniciadas", "¡Todas las estadísticas se han reiniciado a cero!")

# =============================================
# INTERFAZ GRÁFICA PRINCIPAL
# =============================================

def crear_interfaz():
    """Crea y configura la interfaz gráfica principal"""
    global ventana, frame_principal, label_estadisticas
    
    # Crear ventana principal
    ventana = tk.Tk()
    ventana.title("Juego Educativo: Explorando la Aleatoriedad con Random")
    ventana.geometry("900x700")
    ventana.configure(bg=color_fondo)
    
    # Centrar ventana en pantalla
    ventana.update_idletasks()
    ancho_ventana = ventana.winfo_width()
    alto_ventana = ventana.winfo_height()
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    y = (alto_pantalla // 2) - (alto_ventana // 2)
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    
    # Evitar que la ventana sea redimensionada
    ventana.resizable(False, False)
    
    # Título principal
    titulo_principal = tk.Label(
        ventana,
        text="🎲 EXPLORANDO LA ALEATORIEDAD CON RANDOM 🎲",
        bg=color_fondo,
        fg="#2c3e50",
        font=("Arial", 18, "bold")
    )
    titulo_principal.pack(pady=(20, 10))
    
    # Subtítulo
    subtitulo = tk.Label(
        ventana,
        text="Un juego educativo para entender la aleatoriedad en programación",
        bg=color_fondo,
        fg=color_texto,
        font=("Arial", 12)
    )
    subtitulo.pack(pady=(0, 20))
    
    # Frame principal con scrollbar
    canvas = tk.Canvas(ventana, bg=color_fondo, highlightthickness=0)
    scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
    frame_principal = tk.Frame(canvas, bg=color_fondo)
    
    frame_principal.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=frame_principal, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True, padx=(20, 0), pady=(0, 20))
    scrollbar.pack(side="right", fill="y", pady=(0, 20))
    
    # Sección 1: Introducción
    frame_intro = crear_frame_titulo(
        frame_principal,
        "¿Qué es la ALEATORIEDAD en programación?",
        "La aleatoriedad nos permite generar resultados impredecibles en nuestros programas. "
        "En la vida real, usamos aleatoriedad cuando lanzamos un dado, una moneda o "
        "cuando mezclamos una baraja de cartas. En programación, la librería RANDOM "
        "de Python nos brinda herramientas para simular estos fenómenos."
    )
    frame_intro.pack(fill="x", padx=20, pady=(0, 10))
    
    # Botón de explicación
    btn_explicacion = tk.Button(
        frame_principal,
        text="📚 Aprende sobre RANDOM",
        command=mostrar_explicacion_random,
        bg="#6c5ce7",
        fg="white",
        font=("Arial", 11, "bold"),
        padx=20,
        pady=10
    )
    aplicar_estilo_boton(btn_explicacion)
    btn_explicacion.pack(pady=(0, 20))
    
    # Sección 2: Juegos de azar básicos
    frame_juegos_azar = crear_frame_titulo(
        frame_principal,
        "🎯 JUEGOS DE AZAR BÁSICOS",
        "Estas son las formas más comunes de usar aleatoriedad en juegos:"
    )
    frame_juegos_azar.pack(fill="x", padx=20, pady=(0, 10))
    
    # Botones para juegos de azar
    frame_botones_azar = tk.Frame(frame_principal, bg=color_fondo)
    frame_botones_azar.pack(fill="x", padx=20, pady=(0, 20))
    
    botones_azar = [
        ("🎲 Lanzar Dado", lanzar_dado),
        ("🪙 Lanzar Moneda", lanzar_moneda),
        ("🎡 Girar Ruleta", girar_ruleta),
        ("🃏 Repartir Carta", repartir_carta)
    ]
    
    for texto, comando in botones_azar:
        btn = tk.Button(
            frame_botones_azar,
            text=texto,
            command=comando,
            width=20
        )
        aplicar_estilo_boton(btn)
        btn.pack(side="left", padx=5, pady=5)
    
    # Sección 3: Aplicaciones prácticas
    frame_aplicaciones = crear_frame_titulo(
        frame_principal,
        "🔧 APLICACIONES PRÁCTICAS",
        "La aleatoriedad también tiene usos prácticos en programación:"
    )
    frame_aplicaciones.pack(fill="x", padx=20, pady=(0, 10))
    
    # Botones para aplicaciones prácticas
    frame_botones_aplicaciones = tk.Frame(frame_principal, bg=color_fondo)
    frame_botones_aplicaciones.pack(fill="x", padx=20, pady=(0, 20))
    
    botones_aplicaciones = [
        ("🔒 Generar Contraseña", generar_contrasena),
        ("🎫 Números de Lotería", generar_loteria),
        ("🚶 Caminata Aleatoria", caminata_aleatoria)
    ]
    
    for texto, comando in botones_aplicaciones:
        btn = tk.Button(
            frame_botones_aplicaciones,
            text=texto,
            command=comando,
            width=25
        )
        aplicar_estilo_boton(btn)
        btn.pack(side="left", padx=5, pady=5)
    
    # Sección 4: Estadísticas
    frame_estadisticas = crear_frame_titulo(
        frame_principal,
        "📊 ESTADÍSTICAS",
        "Lleva un registro de cuántas veces has usado cada función:"
    )
    frame_estadisticas.pack(fill="x", padx=20, pady=(0, 10))
    
    # Etiqueta de estadísticas
    label_estadisticas = tk.Label(
        frame_principal,
        text="Lanzamientos de dado: 0 | Lanzamientos de moneda: 0 | Giros de ruleta: 0 | Cartas repartidas: 0",
        bg=color_fondo,
        fg="#495057",
        font=("Arial", 10),
        wraplength=700
    )
    label_estadisticas.pack(pady=(0, 10))
    
    # Botón para reiniciar estadísticas
    btn_reiniciar = tk.Button(
        frame_principal,
        text="🔄 Reiniciar Estadísticas",
        command=reiniciar_estadisticas,
        bg="#e74c3c",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=15,
        pady=8
    )
    aplicar_estilo_boton(btn_reiniciar)
    btn_reiniciar.pack(pady=(0, 20))
    
    # Pie de página
    frame_pie = tk.Frame(frame_principal, bg=color_fondo)
    frame_pie.pack(fill="x", padx=20, pady=(20, 40))
    
    linea_separadora = tk.Frame(frame_pie, height=2, bg="#dee2e6")
    linea_separadora.pack(fill="x", pady=(0, 15))
    
    texto_pie = tk.Label(
        frame_pie,
        text="🎓 Juego Educativo para Bachillerato - Aleatoriedad con Python 🎓\n"
             "Conceptos: random.randint(), random.choice(), random.sample()\n"
             "Presiona F1 en cualquier momento para ver ayuda sobre la función utilizada",
        bg=color_fondo,
        fg="#6c757d",
        font=("Arial", 9),
        justify="center"
    )
    texto_pie.pack()
    
    # Configurar tecla F1 para mostrar ayuda
    ventana.bind("<F1>", lambda e: mostrar_explicacion_random())
    
    # Inicializar estadísticas
    actualizar_estadisticas()
    
    # Ejecutar la aplicación
    ventana.mainloop()

# =============================================
# INICIO DE LA APLICACIÓN
# =============================================

if __name__ == "__main__":
    # Configuración inicial
    print("Iniciando Juego Educativo: Explorando la Aleatoriedad...")
    
    # Crear y mostrar la interfaz
    crear_interfaz()