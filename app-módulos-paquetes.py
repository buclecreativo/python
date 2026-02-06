"""
JUEGO EDUCATIVO: EXPLORANDO MÓDULOS Y PAQUETES EN PYTHON
Autor: Experto en Desarrollo de Software Educativo
Objetivo: Enseñar conceptos de módulos y paquetes de Python a estudiantes de bachillerato
"""

import tkinter as tk
from tkinter import messagebox, font
import sys
import os

# ============================================================================
# CONFIGURACIÓN INICIAL Y CONSTANTES
# ============================================================================

# Paleta de colores moderna y atractiva
COLOR_FONDO = "#1a1a2e"
COLOR_PRIMARIO = "#16213e"
COLOR_SECUNDARIO = "#0f3460"
COLOR_ACENTO = "#e94560"
COLOR_TEXTO = "#ffffff"
COLOR_HOVER = "#2d4263"

# Dimensiones de la ventana
ANCHO_VENTANA = 900
ALTO_VENTANA = 750

# ============================================================================
# FUNCIONES DE UTILIDAD
# ============================================================================

def centrar_ventana(ventana, ancho, alto):
    """Centra la ventana en la pantalla"""
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def crear_boton(parent, texto, comando, x, y, ancho=20, alto=2):
    """Crea un botón con efecto hover"""
    boton = tk.Button(
        parent,
        text=texto,
        command=comando,
        bg=COLOR_SECUNDARIO,
        fg=COLOR_TEXTO,
        font=("Arial", 11, "bold"),
        width=ancho,
        height=alto,
        relief="flat",
        borderwidth=0,
        cursor="hand2"
    )
    
    # Posicionar el botón
    boton.place(x=x, y=y)
    
    # Efecto hover
    def on_enter(event):
        boton.config(bg=COLOR_HOVER)
    
    def on_leave(event):
        boton.config(bg=COLOR_SECUNDARIO)
    
    boton.bind("<Enter>", on_enter)
    boton.bind("<Leave>", on_leave)
    
    return boton

def crear_etiqueta(parent, texto, x, y, tamaño=12, negrita=False, color=COLOR_TEXTO):
    """Crea una etiqueta de texto estilizada"""
    fuente = ("Arial", tamaño, "bold" if negrita else "normal")
    etiqueta = tk.Label(
        parent,
        text=texto,
        bg=COLOR_FONDO,
        fg=color,
        font=fuente,
        justify="left"
    )
    etiqueta.place(x=x, y=y)
    return etiqueta

def crear_area_texto(parent, x, y, ancho, alto, editable=False):
    """Crea un área de texto con scrollbar"""
    marco = tk.Frame(parent, bg=COLOR_FONDO)
    marco.place(x=x, y=y, width=ancho, height=alto)
    
    # Crear scrollbar
    scrollbar = tk.Scrollbar(marco)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Crear área de texto
    texto = tk.Text(
        marco,
        bg=COLOR_PRIMARIO,
        fg=COLOR_TEXTO,
        font=("Consolas", 11),
        yscrollcommand=scrollbar.set,
        wrap=tk.WORD,
        state="normal" if editable else "disabled"
    )
    texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # Configurar scrollbar
    scrollbar.config(command=texto.yview)
    
    return texto

# ============================================================================
# FUNCIONES PRINCIPALES DEL JUEGO
# ============================================================================

def mostrar_introduccion():
    """Muestra la pantalla de introducción al juego"""
    limpiar_pantalla()
    
    # Título principal
    crear_etiqueta(
        ventana_principal, 
        "🎮 EXPLORANDO MÓDULOS Y PAQUETES EN PYTHON", 
        50, 40, 24, True, COLOR_ACENTO
    )
    
    # Explicación del juego
    explicacion = """
    ¡Hola estudiante! 👋
    
    En este juego interactivo aprenderás sobre:
    
    1. ¿QUÉ SON LOS MÓDULOS?
       Fragmentos de código Python reutilizables
    
    2. ¿QUÉ SON LOS PAQUETES?
       Colecciones organizadas de módulos
    
    3. ¿CÓMO IMPORTAR MÓDULOS?
       Diferentes formas de usar código de otros archivos
    
    4. PRÁCTICA INTERACTIVA
       Ejercicios para aplicar lo aprendido
    
    Al final del juego, podrás crear tus propios módulos
    y paquetes para organizar mejor tus proyectos.
    """
    
    area_texto = crear_area_texto(ventana_principal, 50, 100, 800, 300)
    area_texto.config(state="normal")
    area_texto.insert("1.0", explicacion)
    area_texto.config(state="disabled")
    
    # Botones de navegación
    crear_boton(ventana_principal, "Comenzar Aprendizaje", mostrar_modulos, 350, 450)

def mostrar_modulos():
    """Explica el concepto de módulos"""
    limpiar_pantalla()
    
    crear_etiqueta(ventana_principal, "📦 ¿QUÉ SON LOS MÓDULOS?", 50, 40, 22, True, COLOR_ACENTO)
    
    explicacion = """
    UN MÓDULO ES SIMPLEMENTE UN ARCHIVO .PY
    
    Imagina que tienes un archivo llamado "matematicas.py" con estas funciones:
    
    --- matematicas.py ---
    def sumar(a, b):
        return a + b
    
    def restar(a, b):
        return a - b
    
    def multiplicar(a, b):
        return a * b
    ----------------------
    
    Puedes usar estas funciones en otro archivo IMPORTANDO el módulo:
    
    --- mi_programa.py ---
    import matematicas
    
    resultado = matematicas.sumar(5, 3)
    print(f"5 + 3 = {resultado}")
    
    resultado = matematicas.multiplicar(4, 6)
    print(f"4 × 6 = {resultado}")
    ----------------------
    
    VENTAJAS DE USAR MÓDULOS:
    • REUTILIZAR código sin copiar y pegar
    • ORGANIZAR mejor tus programas
    • MANTENER el código más limpio y ordenado
    • COLABORAR más fácilmente con otros programadores
    """
    
    area_texto = crear_area_texto(ventana_principal, 50, 80, 800, 350)
    area_texto.config(state="normal")
    area_texto.insert("1.0", explicacion)
    area_texto.config(state="disabled")
    
    # Ejemplo interactivo
    crear_etiqueta(ventana_principal, "PRUEBA ESTE EJEMPLO:", 50, 450, 14, True)
    
    # Botones de ejemplo
    crear_boton(ventana_principal, "Ver Ejemplo Simple", ejemplo_modulo_simple, 50, 490, 18)
    crear_boton(ventana_principal, "Siguiente: Paquetes", mostrar_paquetes, 650, 490, 18)
    crear_boton(ventana_principal, "Volver al Inicio", mostrar_introduccion, 350, 550, 18)

def ejemplo_modulo_simple():
    """Muestra un ejemplo práctico de módulos"""
    limpiar_pantalla()
    
    crear_etiqueta(ventana_principal, "🔍 EJEMPLO PRÁCTICO: MÓDULO SIMPLE", 50, 40, 20, True, COLOR_ACENTO)
    
    explicacion = """
    VAMOS A SIMULAR UN MÓDULO DE CÁLCULOS GEOMÉTRICOS:
    
    PASO 1: Creamos el módulo "geometria.py"
    ----------------------------------------
    # geometria.py
    
    PI = 3.1416
    
    def area_circulo(radio):
        return PI * radio * radio
    
    def perimetro_circulo(radio):
        return 2 * PI * radio
    
    def area_rectangulo(base, altura):
        return base * altura
    
    PASO 2: Usamos el módulo en nuestro programa principal
    -------------------------------------------------------
    """
    
    area_texto = crear_area_texto(ventana_principal, 50, 80, 800, 250)
    area_texto.config(state="normal")
    area_texto.insert("1.0", explicacion)
    area_texto.config(state="disabled")
    
    # Simulación interactiva
    crear_etiqueta(ventana_principal, "SIMULACIÓN INTERACTIVA:", 50, 350, 14, True)
    
    # Área para resultados
    marco_resultados = tk.Frame(ventana_principal, bg=COLOR_PRIMARIO)
    marco_resultados.place(x=50, y=380, width=800, height=150)
    
    resultados = tk.Text(
        marco_resultados,
        bg=COLOR_PRIMARIO,
        fg=COLOR_TEXTO,
        font=("Consolas", 11),
        height=8,
        width=70
    )
    resultados.pack(padx=10, pady=10)
    
    # Simular funciones del módulo
    PI = 3.1416
    
    def area_circulo(radio):
        return PI * radio * radio
    
    def perimetro_circulo(radio):
        return 2 * PI * radio
    
    def area_rectangulo(base, altura):
        return base * altura
    
    # Botones para probar las funciones
    def probar_area_circulo():
        resultados.delete("1.0", tk.END)
        radio = 5
        area = area_circulo(radio)
        resultados.insert("1.0", f"import geometria\n\n")
        resultados.insert(tk.END, f"radio = {radio}\n")
        resultados.insert(tk.END, f"area = geometria.area_circulo(radio)\n")
        resultados.insert(tk.END, f"print(f'Área del círculo: {area:.2f}')\n")
        resultados.insert(tk.END, f"\n>>> Área del círculo: {area:.2f}")
    
    def probar_perimetro_circulo():
        resultados.delete("1.0", tk.END)
        radio = 7
        perimetro = perimetro_circulo(radio)
        resultados.insert("1.0", f"import geometria\n\n")
        resultados.insert(tk.END, f"radio = {radio}\n")
        resultados.insert(tk.END, f"perimetro = geometria.perimetro_circulo(radio)\n")
        resultados.insert(tk.END, f"print(f'Perímetro del círculo: {perimetro:.2f}')\n")
        resultados.insert(tk.END, f"\n>>> Perímetro del círculo: {perimetro:.2f}")
    
    def probar_area_rectangulo():
        resultados.delete("1.0", tk.END)
        base, altura = 8, 4
        area = area_rectangulo(base, altura)
        resultados.insert("1.0", f"import geometria\n\n")
        resultados.insert(tk.END, f"base = {base}, altura = {altura}\n")
        resultados.insert(tk.END, f"area = geometria.area_rectangulo(base, altura)\n")
        resultados.insert(tk.END, f"print(f'Área del rectángulo: {area}')\n")
        resultados.insert(tk.END, f"\n>>> Área del rectángulo: {area}")
    
    # Botones de prueba
    crear_boton(ventana_principal, "Probar área círculo", probar_area_circulo, 50, 540, 18)
    crear_boton(ventana_principal, "Probar perímetro círculo", probar_perimetro_circulo, 300, 540, 18)
    crear_boton(ventana_principal, "Probar área rectángulo", probar_area_rectangulo, 550, 540, 18)
    
    # Botón de navegación
    crear_boton(ventana_principal, "Volver a Módulos", mostrar_modulos, 350, 580, 18)

def mostrar_paquetes():
    """Explica el concepto de paquetes"""
    limpiar_pantalla()
    
    crear_etiqueta(ventana_principal, "📁 ¿QUÉ SON LOS PAQUETES?", 50, 40, 22, True, COLOR_ACENTO)
    
    explicacion = """
    UN PAQUETE ES UNA COLECCIÓN DE MÓDULOS ORGANIZADOS EN CARPETAS
    
    Estructura de un paquete llamado "matematicas":
    
    matematicas/          <-- Esta es la carpeta del paquete
    ├── __init__.py      <-- Archivo especial que indica que es un paquete
    ├── basico.py        <-- Módulo con operaciones básicas
    ├── avanzado.py      <-- Módulo con operaciones avanzadas
    └── utilidades.py    <-- Módulo con funciones auxiliares
    
    CONTENIDO DE LOS ARCHIVOS:
    
    --- matematicas/__init__.py ---
    # Puede estar vacío o contener configuración
    print("Paquete matemáticas cargado")
    
    --- matematicas/basico.py ---
    def sumar(a, b):
        return a + b
    
    def restar(a, b):
        return a - b
    
    --- matematicas/avanzado.py ---
    def potencia(base, exponente):
        return base ** exponente
    
    def raiz_cuadrada(numero):
        return numero ** 0.5
    
    CÓMO USAR EL PAQUETE:
    
    --- mi_programa.py ---
    # Importar módulo específico del paquete
    from matematicas import basico
    
    resultado = basico.sumar(10, 20)
    print(f"10 + 20 = {resultado}")
    
    # Importar función específica
    from matematicas.avanzado import potencia
    
    resultado = potencia(2, 8)
    print(f"2⁸ = {resultado}")
    
    # Importar todo el paquete
    import matematicas.basico as mb
    
    resultado = mb.restar(50, 25)
    print(f"50 - 25 = {resultado}")
    """
    
    area_texto = crear_area_texto(ventana_principal, 50, 80, 800, 400)
    area_texto.config(state="normal")
    area_texto.insert("1.0", explicacion)
    area_texto.config(state="disabled")
    
    # Botones de navegación
    crear_boton(ventana_principal, "Anterior: Módulos", mostrar_modulos, 50, 500, 18)
    crear_boton(ventana_principal, "Siguiente: Importaciones", mostrar_importaciones, 350, 500, 18)
    crear_boton(ventana_principal, "Volver al Inicio", mostrar_introduccion, 650, 500, 18)

def mostrar_importaciones():
    """Muestra diferentes formas de importar módulos y paquetes"""
    limpiar_pantalla()
    
    crear_etiqueta(ventana_principal, "🔗 FORMAS DE IMPORTAR MÓDULOS Y PAQUETES", 50, 40, 20, True, COLOR_ACENTO)
    
    explicacion = """
    PYTHON OFRECE DIFERENTES FORMAS DE IMPORTAR:
    
    1. IMPORTAR MÓDULO COMPLETO
       -------------------------
       import modulo
       
       Uso: modulo.funcion()
    
    2. IMPORTAR CON ALIAS
       ------------------
       import modulo as md
       
       Uso: md.funcion()
    
    3. IMPORTAR FUNCIÓN ESPECÍFICA
       ---------------------------
       from modulo import funcion
       
       Uso: funcion()
    
    4. IMPORTAR MÚLTIPLES FUNCIONES
       -----------------------------
       from modulo import funcion1, funcion2, funcion3
       
       Uso: funcion1(), funcion2()
    
    5. IMPORTAR TODO (NO RECOMENDADO)
       -------------------------------
       from modulo import *
       
       Uso: funcion()
    
    EJEMPLOS PRÁCTICOS:
    
    # Opción 1: Importación completa
    import math
    raiz = math.sqrt(25)           # Resultado: 5.0
    
    # Opción 2: Importación con alias
    import math as m
    seno = m.sin(m.pi/2)           # Resultado: 1.0
    
    # Opción 3: Importación específica
    from math import sqrt, pi
    circulo = sqrt(16) * pi        # Resultado: 12.566...
    
    # Opción 4: Importación múltiple
    from math import sin, cos, tan
    angulo = sin(0) + cos(0)       # Resultado: 1.0
    
    RECOMENDACIÓN:
    • Usa alias para módulos con nombres largos
    • Importa solo lo que necesitas
    • Evita "import *" (puede causar conflictos)
    """
    
    area_texto = crear_area_texto(ventana_principal, 50, 80, 800, 380)
    area_texto.config(state="normal")
    area_texto.insert("1.0", explicacion)
    area_texto.config(state="disabled")
    
    # Demostración interactiva
    crear_etiqueta(ventana_principal, "DEMOSTRACIÓN INTERACTIVA:", 50, 480, 14, True)
    
    marco_demo = tk.Frame(ventana_principal, bg=COLOR_PRIMARIO)
    marco_demo.place(x=50, y=510, width=800, height=100)
    
    demo_texto = tk.Text(
        marco_demo,
        bg=COLOR_PRIMARIO,
        fg=COLOR_TEXTO,
        font=("Consolas", 10),
        height=5,
        width=80
    )
    demo_texto.pack(padx=10, pady=10)
    
    def demostrar_import_completo():
        import math
        demo_texto.delete("1.0", tk.END)
        demo_texto.insert("1.0", "import math\n\n")
        demo_texto.insert(tk.END, f"math.sqrt(49) = {math.sqrt(49)}\n")
        demo_texto.insert(tk.END, f"math.pi = {math.pi:.4f}\n")
        demo_texto.insert(tk.END, f"math.cos(math.pi) = {math.cos(math.pi):.2f}")
    
    def demostrar_import_alias():
        import math as m
        demo_texto.delete("1.0", tk.END)
        demo_texto.insert("1.0", "import math as m\n\n")
        demo_texto.insert(tk.END, f"m.sqrt(64) = {m.sqrt(64)}\n")
        demo_texto.insert(tk.END, f"m.pi = {m.pi:.4f}")
    
    def demostrar_import_especifico():
        from math import sqrt, pi
        demo_texto.delete("1.0", tk.END)
        demo_texto.insert("1.0", "from math import sqrt, pi\n\n")
        demo_texto.insert(tk.END, f"sqrt(81) = {sqrt(81)}\n")
        demo_texto.insert(tk.END, f"pi = {pi:.4f}")
    
    # Botones de demostración
    crear_boton(ventana_principal, "Import completo", demostrar_import_completo, 50, 620, 16)
    crear_boton(ventana_principal, "Import con alias", demostrar_import_alias, 250, 620, 16)
    crear_boton(ventana_principal, "Import específico", demostrar_import_especifico, 450, 620, 16)
    crear_boton(ventana_principal, "Siguiente: Práctica", mostrar_practica, 650, 620, 16)
    
    # Botones de navegación
    crear_boton(ventana_principal, "Anterior: Paquetes", mostrar_paquetes, 350, 570, 18)

def mostrar_practica():
    """Pantalla de práctica interactiva"""
    limpiar_pantalla()
    
    crear_etiqueta(ventana_principal, "💻 PRÁCTICA INTERACTIVA", 50, 40, 22, True, COLOR_ACENTO)
    
    explicacion = """
    AHORA ES TU TURNO DE PRACTICAR
    
    Imagina que tienes estos archivos:
    
    mi_paquete/
    ├── __init__.py
    ├── calculos.py
    └── texto.py
    
    calculos.py contiene:
    def promedio(a, b, c):
        return (a + b + c) / 3
    
    def maximo(a, b, c):
        return max(a, b, c)
    
    texto.py contiene:
    def invertir(texto):
        return texto[::-1]
    
    def mayusculas(texto):
        return texto.upper()
    
    COMPLETA LOS IMPORT NECESARIOS:
    """
    
    area_texto = crear_area_texto(ventana_principal, 50, 80, 800, 200)
    area_texto.config(state="normal")
    area_texto.insert("1.0", explicacion)
    area_texto.config(state="disabled")
    
    # Ejercicios interactivos
    crear_etiqueta(ventana_principal, "EJERCICIO 1: Importa la función 'promedio'", 50, 300, 14, True)
    
    ejercicio1 = tk.Entry(
        ventana_principal,
        bg=COLOR_PRIMARIO,
        fg=COLOR_TEXTO,
        font=("Consolas", 12),
        width=60
    )
    ejercicio1.place(x=50, y=330)
    
    crear_etiqueta(ventana_principal, "EJERCICIO 2: Importa todo el módulo 'texto' con alias 'txt'", 50, 370, 14, True)
    
    ejercicio2 = tk.Entry(
        ventana_principal,
        bg=COLOR_PRIMARIO,
        fg=COLOR_TEXTO,
        font=("Consolas", 12),
        width=60
    )
    ejercicio2.place(x=50, y=400)
    
    # Área de retroalimentación
    marco_feedback = tk.Frame(ventana_principal, bg=COLOR_PRIMARIO)
    marco_feedback.place(x=50, y=450, width=800, height=100)
    
    feedback = tk.Text(
        marco_feedback,
        bg=COLOR_PRIMARIO,
        fg=COLOR_TEXTO,
        font=("Arial", 11),
        height=4,
        width=80
    )
    feedback.pack(padx=10, pady=10)
    
    def verificar_respuestas():
        resp1 = ejercicio1.get().strip()
        resp2 = ejercicio2.get().strip()
        
        feedback.delete("1.0", tk.END)
        
        # Verificar primera respuesta
        respuestas_correctas1 = [
            "from mi_paquete.calculos import promedio",
            "from mi_paquete import calculos",
            "import mi_paquete.calculos"
        ]
        
        correcto1 = False
        for respuesta in respuestas_correctas1:
            if resp1.lower() == respuesta.lower():
                correcto1 = True
                break
        
        # Verificar segunda respuesta
        correcto2 = resp2.lower() == "import mi_paquete.texto as txt"
        
        if correcto1 and correcto2:
            feedback.insert("1.0", "✅ ¡EXCELENTE! Ambas respuestas son correctas.\n\n")
            feedback.insert(tk.END, "Has demostrado que comprendes cómo importar módulos y paquetes.")
            feedback.config(fg="#4CAF50")
        elif correcto1:
            feedback.insert("1.0", "⚠️ Respuesta 1: ✅ Correcta\n")
            feedback.insert(tk.END, "Respuesta 2: ❌ Incorrecta\n\n")
            feedback.insert(tk.END, "Recuerda: 'import mi_paquete.texto as txt'")
            feedback.config(fg="#FF9800")
        elif correcto2:
            feedback.insert("1.0", "⚠️ Respuesta 1: ❌ Incorrecta\n")
            feedback.insert(tk.END, "Respuesta 2: ✅ Correcta\n\n")
            feedback.insert(tk.END, "Recuerda: 'from mi_paquete.calculos import promedio'")
            feedback.config(fg="#FF9800")
        else:
            feedback.insert("1.0", "❌ Ambas respuestas necesitan corrección.\n\n")
            feedback.insert(tk.END, "Pista 1: Usa 'from mi_paquete.calculos import promedio'\n")
            feedback.insert(tk.END, "Pista 2: Usa 'import mi_paquete.texto as txt'")
            feedback.config(fg=COLOR_ACENTO)
    
    def mostrar_soluciones():
        feedback.delete("1.0", tk.END)
        feedback.insert("1.0", "SOLUCIONES RECOMENDADAS:\n\n")
        feedback.insert(tk.END, "Ejercicio 1: from mi_paquete.calculos import promedio\n")
        feedback.insert(tk.END, "Ejercicio 2: import mi_paquete.texto as txt\n\n")
        feedback.insert(tk.END, "Otras soluciones válidas también son aceptables.")
        feedback.config(fg="#2196F3")
    
    # Botones de práctica
    crear_boton(ventana_principal, "Verificar Respuestas", verificar_respuestas, 50, 560, 18)
    crear_boton(ventana_principal, "Mostrar Soluciones", mostrar_soluciones, 300, 560, 18)
    crear_boton(ventana_principal, "Finalizar Juego", mostrar_conclusion, 550, 560, 18)
    
    # Botón de navegación
    crear_boton(ventana_principal, "Anterior: Importaciones", mostrar_importaciones, 350, 500, 18)

def mostrar_conclusion():
    """Muestra la pantalla de conclusión"""
    limpiar_pantalla()
    
    crear_etiqueta(ventana_principal, "🎓 ¡FELICITACIONES!", 50, 40, 24, True, COLOR_ACENTO)
    
    conclusion = """
    HAS COMPLETADO EL JUEGO EDUCATIVO SOBRE MÓDULOS Y PAQUETES
    
    RESUMEN DE LO APRENDIDO:
    
    ✅ MÓDULOS: Archivos .py con código reutilizable
       • Ayudan a organizar el código
       • Facilitan la reutilización
       • Mejoran la mantenibilidad
    
    ✅ PAQUETES: Carpetas con múltiples módulos
       • Tienen un archivo __init__.py
       • Organizan módulos relacionados
       • Permiten estructuras complejas
    
    ✅ IMPORTACIONES: Diferentes formas de usar módulos
       • import modulo
       • import modulo as alias
       • from modulo import funcion
       • from paquete.modulo import funcion
    
    PRÓXIMOS PASOS RECOMENDADOS:
    
    1. Crea tu propio módulo con funciones útiles
    2. Organiza varios módulos en un paquete
    3. Explora módulos estándar de Python (math, random, os, etc.)
    4. Comparte tus paquetes con otros programadores
    
    RECUERDA: La práctica constante es clave para dominar 
    estos conceptos. ¡Sigue programando y explorando!
    """
    
    area_texto = crear_area_texto(ventana_principal, 50, 100, 800, 400)
    area_texto.config(state="normal")
    area_texto.insert("1.0", conclusion)
    area_texto.config(state="disabled")
    
    # Botones finales
    crear_boton(ventana_principal, "Repetir Juego", mostrar_introduccion, 250, 530, 20)
    crear_boton(ventana_principal, "Salir", salir_aplicacion, 500, 530, 20)
    
    # Créditos
    crear_etiqueta(
        ventana_principal,
        "Juego educativo creado para enseñar Python a estudiantes de bachillerato",
        50, 600, 10, False, "#AAAAAA"
    )

def limpiar_pantalla():
    """Elimina todos los widgets de la ventana principal"""
    for widget in ventana_principal.winfo_children():
        widget.destroy()

def salir_aplicacion():
    """Cierra la aplicación"""
    ventana_principal.quit()

# ============================================================================
# CONFIGURACIÓN DE LA VENTANA PRINCIPAL
# ============================================================================

def configurar_ventana_principal():
    """Configura la ventana principal de la aplicación"""
    global ventana_principal
    
    # Crear ventana principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Juego Educativo: Módulos y Paquetes en Python")
    ventana_principal.configure(bg=COLOR_FONDO)
    
    # Centrar ventana
    centrar_ventana(ventana_principal, ANCHO_VENTANA, ALTO_VENTANA)
    
    # Evitar redimensionamiento
    ventana_principal.resizable(False, False)
    
    # Mostrar pantalla de inicio
    mostrar_introduccion()
    
    return ventana_principal

# ============================================================================
# PUNTO DE INICIO DE LA APLICACIÓN
# ============================================================================

if __name__ == "__main__":
    # Configurar y mostrar la ventana principal
    ventana = configurar_ventana_principal()
    
    # Iniciar el bucle principal de la aplicación
    ventana.mainloop()