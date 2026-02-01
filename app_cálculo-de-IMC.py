#!/usr/bin/env python3
"""
Aplicación Educativa de Cálculo de IMC
Para estudiantes de bachillerato
Desarrollado con Tkinter - Programación Estructurada
"""

import tkinter as tk
from tkinter import ttk, messagebox

# ============================================================================
# CONFIGURACIÓN INICIAL Y CONSTANTES
# ============================================================================

# Paleta de colores moderna y atractiva
COLORES = {
    'fondo_principal': '#F0F7FF',
    'fondo_secundario': '#FFFFFF',
    'azul_primario': '#4A6FA5',
    'azul_secundario': '#6B9AC4',
    'verde': '#4CAF50',
    'naranja': '#FF9800',
    'rojo': '#F44336',
    'texto_oscuro': '#2C3E50',
    'texto_claro': '#FFFFFF',
    'borde': '#D1E3FF'
}

# Categorías de IMC con rangos y colores
CATEGORIAS_IMC = [
    {"nombre": "Bajo peso", "rango": (0, 18.5), "color": COLORES['azul_primario'], "descripcion": "Tu peso está por debajo de lo recomendado para tu altura."},
    {"nombre": "Peso normal", "rango": (18.5, 24.9), "color": COLORES['verde'], "descripcion": "¡Excelente! Tu peso es saludable para tu altura."},
    {"nombre": "Sobrepeso", "rango": (25, 29.9), "color": COLORES['naranja'], "descripcion": "Tienes un ligero exceso de peso para tu altura."},
    {"nombre": "Obesidad grado I", "rango": (30, 34.9), "color": COLORES['rojo'], "descripcion": "Tu peso está significativamente por encima de lo recomendado."},
    {"nombre": "Obesidad grado II", "rango": (35, 39.9), "color": '#C62828', "descripcion": "Tu peso está muy por encima de lo recomendado."},
    {"nombre": "Obesidad grado III", "rango": (40, 100), "color": '#8B0000', "descripcion": "Tu peso está extremadamente por encima de lo recomendado."}
]

# ============================================================================
# FUNCIONES MATEMÁTICAS Y LÓGICA
# ============================================================================

def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC)
    Fórmula: IMC = peso (kg) / (altura (m) * altura (m))
    
    Args:
        peso: Peso en kilogramos
        altura: Altura en metros
    
    Returns:
        Valor del IMC redondeado a 2 decimales
    """
    if altura <= 0:
        return 0
    imc = peso / (altura ** 2)
    return round(imc, 2)

def determinar_categoria(imc):
    """
    Determina la categoría del IMC basándose en los rangos establecidos
    
    Args:
        imc: Valor del IMC calculado
    
    Returns:
        Diccionario con información de la categoría
    """
    for categoria in CATEGORIAS_IMC:
        if categoria["rango"][0] <= imc < categoria["rango"][1]:
            return categoria
    # Por si acaso no encuentra categoría
    return CATEGORIAS_IMC[-1]

def validar_entrada(peso_texto, altura_texto):
    """
    Valida que las entradas sean números positivos
    
    Returns:
        Tuple (peso_valido, altura_valida) o (None, None) si hay error
    """
    try:
        peso = float(peso_texto)
        altura = float(altura_texto)
        
        if peso <= 0 or altura <= 0:
            messagebox.showwarning("Datos inválidos", 
                                 "Por favor, ingresa valores positivos para peso y altura.")
            return None, None
        
        # Validar altura razonable (entre 0.5 y 2.5 metros)
        if altura < 0.5 or altura > 2.5:
            messagebox.showwarning("Altura inválida",
                                 "Por favor, ingresa una altura entre 0.5 y 2.5 metros.")
            return None, None
        
        # Validar peso razonable (entre 20 y 300 kg)
        if peso < 20 or peso > 300:
            messagebox.showwarning("Peso inválido",
                                 "Por favor, ingresa un peso entre 20 y 300 kg.")
            return None, None
            
        return peso, altura
    except ValueError:
        messagebox.showerror("Error de entrada", 
                           "Por favor, ingresa números válidos para peso y altura.")
        return None, None

# ============================================================================
# FUNCIONES DE INTERFAZ GRÁFICA
# ============================================================================

def crear_estilos():
    """Configura estilos personalizados para la aplicación"""
    estilo = ttk.Style()
    
    # Configurar estilo para botones normales
    estilo.configure('TButton',
                    font=('Segoe UI', 10, 'bold'),
                    padding=10,
                    borderwidth=1,
                    relief='flat')
    
    # Configurar estilo para botones con efecto hover
    estilo.map('TButton',
              background=[('active', COLORES['azul_primario'])],
              foreground=[('active', COLORES['texto_claro'])])

def centrar_ventana(ventana, ancho, alto):
    """Centra la ventana en la pantalla"""
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')

def crear_boton_con_hover(parent, texto, comando, color_normal, color_hover):
    """
    Crea un botón con efecto hover personalizado
    
    Args:
        parent: Widget padre
        texto: Texto del botón
        comando: Función a ejecutar al hacer clic
        color_normal: Color normal del botón
        color_hover: Color cuando el mouse está encima
    """
    def on_enter(event):
        boton.config(bg=color_hover)
    
    def on_leave(event):
        boton.config(bg=color_normal)
    
    boton = tk.Button(parent,
                     text=texto,
                     font=('Segoe UI', 10, 'bold'),
                     bg=color_normal,
                     fg=COLORES['texto_claro'],
                     activebackground=color_hover,
                     activeforeground=COLORES['texto_claro'],
                     relief='flat',
                     padx=20,
                     pady=10,
                     cursor='hand2',
                     command=comando)
    
    boton.bind('<Enter>', on_enter)
    boton.bind('<Leave>', on_leave)
    
    return boton

# ============================================================================
# FUNCIONES PRINCIPALES DE LA APLICACIÓN
# ============================================================================

def ejecutar_calculo():
    """Función principal que ejecuta el cálculo y muestra los resultados"""
    # Obtener valores de entrada
    peso_texto = entrada_peso.get()
    altura_texto = entrada_altura.get()
    
    # Validar entrada
    peso, altura = validar_entrada(peso_texto, altura_texto)
    if peso is None or altura is None:
        return
    
    # Calcular IMC
    imc = calcular_imc(peso, altura)
    categoria = determinar_categoria(imc)
    
    # Mostrar resultados
    etiqueta_resultado.config(text=f"IMC: {imc}", fg=categoria["color"])
    etiqueta_categoria.config(text=categoria["nombre"], fg=categoria["color"])
    etiqueta_descripcion.config(text=categoria["descripcion"])
    
    # Actualizar barra de progreso
    actualizar_barra_progreso(imc)
    
    # Actualizar tabla de categorías
    resaltar_categoria_actual(imc)
    
    # Mostrar detalles adicionales
    mostrar_detalles_adicionales(peso, altura, imc)

def actualizar_barra_progreso(imc):
    """Actualiza la barra de progreso según el IMC calculado"""
    # Normalizar el IMC para la barra (0-50 es el rango visible)
    valor_barra = min(imc, 50) * 2  # Convertir a escala 0-100
    
    barra_progreso['value'] = valor_barra
    barra_progreso.configure(style='TProgressbar')
    
    # Cambiar color según categoría
    estilo_barra = ttk.Style()
    categoria = determinar_categoria(imc)
    estilo_barra.configure('TProgressbar', 
                          troughcolor=COLORES['fondo_secundario'],
                          background=categoria["color"])

def resaltar_categoria_actual(imc):
    """Resalta la categoría actual en la tabla de referencias"""
    categoria_actual = determinar_categoria(imc)
    
    # Resetear todos los frames
    for widget in frame_tabla.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.config(bg=COLORES['fondo_secundario'])
    
    # Resaltar categoría actual
    for i, categoria in enumerate(CATEGORIAS_IMC):
        if categoria["nombre"] == categoria_actual["nombre"]:
            # Encontrar el frame correspondiente y resaltarlo
            for widget in frame_tabla.winfo_children():
                if isinstance(widget, tk.Frame):
                    etiquetas = widget.winfo_children()
                    if etiquetas and etiquetas[0].cget("text") == categoria["nombre"]:
                        widget.config(bg=categoria["color"], relief='solid', borderwidth=1)
                        for etiqueta in etiquetas:
                            etiqueta.config(bg=categoria["color"], fg=COLORES['texto_claro'])
                        break

def mostrar_detalles_adicionales(peso, altura, imc):
    """Muestra información detallada y educativa"""
    categoria = determinar_categoria(imc)
    
    detalles = f"""
    📊 **Detalles del cálculo:**
    • Peso ingresado: {peso} kg
    • Altura ingresada: {altura} m
    • IMC calculado: {imc}
    
    📈 **Interpretación:**
    • Categoría: {categoria['nombre']}
    • Rango saludable: 18.5 - 24.9
    
    💡 **Recuerda:**
    El IMC es una referencia general. Para una 
    evaluación precisa de tu salud, consulta a un 
    profesional médico.
    """
    
    etiqueta_detalles.config(text=detalles)

def mostrar_informacion_imc():
    """Muestra información educativa sobre el IMC"""
    info_texto = """
    🤔 **¿Qué es el IMC?**
    
    El Índice de Masa Corporal (IMC) es una medida que 
    relaciona tu peso con tu altura. Se utiliza como una 
    referencia general para evaluar si tu peso es saludable.
    
    🧮 **Fórmula:**
    IMC = Peso (kg) ÷ Altura² (m)
    
    📊 **Categorías:**
    • Bajo peso: IMC < 18.5
    • Peso normal: 18.5 - 24.9
    • Sobrepeso: 25 - 29.9
    • Obesidad: IMC ≥ 30
    
    ⚠️ **Limitaciones:**
    El IMC no considera la composición corporal (músculo vs grasa),
    por lo que debe usarse como referencia, no como diagnóstico.
    
    Siempre consulta a un profesional de la salud para una
    evaluación personalizada.
    """
    
    messagebox.showinfo("Información sobre IMC", info_texto)

def limpiar_campos():
    """Limpia todos los campos y restablece la interfaz"""
    entrada_peso.delete(0, tk.END)
    entrada_altura.delete(0, tk.END)
    etiqueta_resultado.config(text="IMC: --", fg=COLORES['texto_oscuro'])
    etiqueta_categoria.config(text="Categoría", fg=COLORES['texto_oscuro'])
    etiqueta_descripcion.config(text="Ingresa tus datos para calcular tu IMC")
    etiqueta_detalles.config(text="")
    barra_progreso['value'] = 0
    
    # Resetear tabla
    for widget in frame_tabla.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.config(bg=COLORES['fondo_secundario'], relief='flat')
            for etiqueta in widget.winfo_children():
                if isinstance(etiqueta, tk.Label):
                    etiqueta.config(bg=COLORES['fondo_secundario'], fg=COLORES['texto_oscuro'])

# ============================================================================
# CONFIGURACIÓN DE LA INTERFAZ PRINCIPAL
# ============================================================================

def configurar_interfaz():
    """Configura todos los elementos de la interfaz gráfica"""
    global ventana_principal, entrada_peso, entrada_altura
    global etiqueta_resultado, etiqueta_categoria, etiqueta_descripcion, etiqueta_detalles
    global barra_progreso, frame_tabla
    
    # Crear ventana principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Calculadora Educativa de IMC")
    ventana_principal.configure(bg=COLORES['fondo_principal'])
    
    # Centrar ventana
    centrar_ventana(ventana_principal, 900, 900)
    ventana_principal.resizable(False, False)
    
    # Configurar estilos
    crear_estilos()
    
    # ========== CABECERA ==========
    frame_cabecera = tk.Frame(ventana_principal, bg=COLORES['fondo_principal'])
    frame_cabecera.pack(pady=20, fill='x')
    
    titulo = tk.Label(frame_cabecera,
                     text="📊 Calculadora de Índice de Masa Corporal",
                     font=('Segoe UI', 20, 'bold'),
                     bg=COLORES['fondo_principal'],
                     fg=COLORES['azul_primario'])
    titulo.pack()
    
    subtitulo = tk.Label(frame_cabecera,
                        text="Aplicación educativa para estudiantes de bachillerato",
                        font=('Segoe UI', 11),
                        bg=COLORES['fondo_principal'],
                        fg=COLORES['texto_oscuro'])
    subtitulo.pack(pady=(5, 0))
    
    # ========== ENTRADAS DE DATOS ==========
    frame_entradas = tk.Frame(ventana_principal, 
                             bg=COLORES['fondo_secundario'],
                             relief='solid',
                             borderwidth=1,
                             padx=20,
                             pady=20)
    frame_entradas.pack(pady=10, padx=20, fill='x')
    
    # Etiqueta de instrucciones
    instrucciones = tk.Label(frame_entradas,
                           text="Ingresa tus datos para calcular tu IMC:",
                           font=('Segoe UI', 11, 'bold'),
                           bg=COLORES['fondo_secundario'],
                           fg=COLORES['texto_oscuro'])
    instrucciones.pack(anchor='w', pady=(0, 15))
    
    # Frame para entradas
    frame_datos = tk.Frame(frame_entradas, bg=COLORES['fondo_secundario'])
    frame_datos.pack(fill='x')
    
    # Entrada de peso
    tk.Label(frame_datos,
            text="Peso (kg):",
            font=('Segoe UI', 10),
            bg=COLORES['fondo_secundario'],
            fg=COLORES['texto_oscuro']).grid(row=0, column=0, sticky='w', padx=(0, 10))
    
    entrada_peso = tk.Entry(frame_datos,
                          font=('Segoe UI', 11),
                          width=15,
                          relief='solid',
                          borderwidth=1)
    entrada_peso.grid(row=0, column=1, padx=(0, 30))
    entrada_peso.insert(0, "65")  # Valor por defecto
    
    # Entrada de altura
    tk.Label(frame_datos,
            text="Altura (m):",
            font=('Segoe UI', 10),
            bg=COLORES['fondo_secundario'],
            fg=COLORES['texto_oscuro']).grid(row=0, column=2, sticky='w', padx=(0, 10))
    
    entrada_altura = tk.Entry(frame_datos,
                            font=('Segoe UI', 11),
                            width=15,
                            relief='solid',
                            borderwidth=1)
    entrada_altura.grid(row=0, column=3)
    entrada_altura.insert(0, "1.70")  # Valor por defecto
    
    # Botones de acción
    frame_botones = tk.Frame(frame_entradas, bg=COLORES['fondo_secundario'])
    frame_botones.pack(pady=(20, 0))
    
    btn_calcular = crear_boton_con_hover(frame_botones,
                                        "🎯 Calcular IMC",
                                        ejecutar_calculo,
                                        COLORES['azul_secundario'],
                                        COLORES['azul_primario'])
    btn_calcular.pack(side='left', padx=5)
    
    btn_info = crear_boton_con_hover(frame_botones,
                                    "📚 ¿Qué es el IMC?",
                                    mostrar_informacion_imc,
                                    COLORES['verde'],
                                    '#45a049')
    btn_info.pack(side='left', padx=5)
    
    btn_limpiar = crear_boton_con_hover(frame_botones,
                                       "🗑️ Limpiar",
                                       limpiar_campos,
                                       COLORES['naranja'],
                                       '#e68900')
    btn_limpiar.pack(side='left', padx=5)
    
    # ========== RESULTADOS ==========
    frame_resultados = tk.Frame(ventana_principal,
                               bg=COLORES['fondo_secundario'],
                               relief='solid',
                               borderwidth=1,
                               padx=20,
                               pady=20)
    frame_resultados.pack(pady=10, padx=20, fill='x')
    
    # IMC numérico
    etiqueta_resultado = tk.Label(frame_resultados,
                                 text="IMC: --",
                                 font=('Segoe UI', 32, 'bold'),
                                 bg=COLORES['fondo_secundario'],
                                 fg=COLORES['texto_oscuro'])
    etiqueta_resultado.pack()
    
    # Categoría
    etiqueta_categoria = tk.Label(frame_resultados,
                                 text="Categoría",
                                 font=('Segoe UI', 16),
                                 bg=COLORES['fondo_secundario'],
                                 fg=COLORES['texto_oscuro'])
    etiqueta_categoria.pack()
    
    # Descripción
    etiqueta_descripcion = tk.Label(frame_resultados,
                                   text="Ingresa tus datos para calcular tu IMC",
                                   font=('Segoe UI', 11),
                                   bg=COLORES['fondo_secundario'],
                                   fg=COLORES['texto_oscuro'],
                                   wraplength=600)
    etiqueta_descripcion.pack(pady=(10, 0))
    
    # Barra de progreso
    barra_progreso = ttk.Progressbar(frame_resultados,
                                    length=600,
                                    mode='determinate',
                                    maximum=100)
    barra_progreso.pack(pady=20)
    
    # Etiquetas de rango en la barra
    frame_rangos = tk.Frame(frame_resultados, bg=COLORES['fondo_secundario'])
    frame_rangos.pack(fill='x')
    
    tk.Label(frame_rangos,
            text="Bajo peso",
            font=('Segoe UI', 8),
            bg=COLORES['fondo_secundario'],
            fg=COLORES['texto_oscuro']).pack(side='left')
    
    tk.Label(frame_rangos,
            text="Normal",
            font=('Segoe UI', 8),
            bg=COLORES['fondo_secundario'],
            fg=COLORES['texto_oscuro']).pack(side='left', expand=True)
    
    tk.Label(frame_rangos,
            text="Sobrepeso",
            font=('Segoe UI', 8),
            bg=COLORES['fondo_secundario'],
            fg=COLORES['texto_oscuro']).pack(side='left', expand=True)
    
    tk.Label(frame_rangos,
            text="Obesidad",
            font=('Segoe UI', 8),
            bg=COLORES['fondo_secundario'],
            fg=COLORES['texto_oscuro']).pack(side='right')
    
    # ========== TABLA DE REFERENCIA ==========
    frame_tabla_titulo = tk.Frame(ventana_principal, bg=COLORES['fondo_principal'])
    frame_tabla_titulo.pack(pady=(20, 5), fill='x')
    
    tk.Label(frame_tabla_titulo,
            text="📋 Tabla de Referencia del IMC",
            font=('Segoe UI', 14, 'bold'),
            bg=COLORES['fondo_principal'],
            fg=COLORES['azul_primario']).pack()
    
    frame_tabla = tk.Frame(ventana_principal, bg=COLORES['fondo_principal'])
    frame_tabla.pack(pady=(0, 20), padx=20, fill='x')
    
    # Crear filas de la tabla
    for categoria in CATEGORIAS_IMC:
        frame_fila = tk.Frame(frame_tabla, 
                             bg=COLORES['fondo_secundario'],
                             relief='solid',
                             borderwidth=1)
        frame_fila.pack(fill='x', pady=2)
        
        # Nombre de la categoría
        tk.Label(frame_fila,
                text=categoria["nombre"],
                font=('Segoe UI', 10, 'bold'),
                bg=COLORES['fondo_secundario'],
                fg=categoria["color"],
                width=20,
                anchor='w').pack(side='left', padx=10, pady=5)
        
        # Rango
        rango_texto = f"{categoria['rango'][0]} - {categoria['rango'][1]}"
        tk.Label(frame_fila,
                text=rango_texto,
                font=('Segoe UI', 10),
                bg=COLORES['fondo_secundario'],
                fg=COLORES['texto_oscuro'],
                width=15).pack(side='left', padx=10)
        
        # Descripción
        tk.Label(frame_fila,
                text=categoria["descripcion"],
                font=('Segoe UI', 9),
                bg=COLORES['fondo_secundario'],
                fg=COLORES['texto_oscuro'],
                wraplength=400,
                justify='left').pack(side='left', padx=10, pady=5, expand=True, fill='x')
    
    # ========== DETALLES ADICIONALES ==========
    frame_detalles = tk.Frame(ventana_principal,
                             bg=COLORES['fondo_secundario'],
                             relief='solid',
                             borderwidth=1,
                             padx=20,
                             pady=20)
    frame_detalles.pack(pady=(0, 20), padx=20, fill='x')
    
    etiqueta_detalles = tk.Label(frame_detalles,
                                text="",
                                font=('Segoe UI', 10),
                                bg=COLORES['fondo_secundario'],
                                fg=COLORES['texto_oscuro'],
                                justify='left',
                                wraplength=800)
    etiqueta_detalles.pack()
    
    # ========== PIE DE PÁGINA ==========
    frame_pie = tk.Frame(ventana_principal, bg=COLORES['fondo_principal'])
    frame_pie.pack(pady=10, fill='x')
    
    tk.Label(frame_pie,
            text="🔬 Aplicación Educativa - Cálculo del IMC | Para estudiantes de bachillerato",
            font=('Segoe UI', 9),
            bg=COLORES['fondo_principal'],
            fg=COLORES['texto_oscuro']).pack()
    
    tk.Label(frame_pie,
            text="⚠️ Esta herramienta es educativa. Consulta a un profesional de la salud para diagnóstico.",
            font=('Segoe UI', 8),
            bg=COLORES['fondo_principal'],
            fg=COLORES['rojo']).pack(pady=(5, 0))

# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """Función principal que inicia la aplicación"""
    configurar_interfaz()
    
    # Ejecutar el bucle principal de la aplicación
    ventana_principal.mainloop()

# ============================================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================================

if __name__ == "__main__":
    print("🚀 Iniciando Aplicación Educativa de IMC...")
    print("📚 Destinada a estudiantes de bachillerato")
    print("🎯 Objetivo: Facilitar la comprensión práctica del Índice de Masa Corporal")
    print("=" * 60)
    
    main()