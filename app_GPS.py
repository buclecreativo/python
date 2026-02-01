"""
APLICACIÓN EDUCATIVA: GPS PARA JÓVENES PENSADORES
Autor: Edwin Méndez J.
Descripción: Aplicación interactiva para enseñar los principios básicos del funcionamiento del GPS
             a estudiantes de bachillerato, utilizando Python y tkinter.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math
import random
import time

# ============================================================
# CLASE PRINCIPAL DE LA APLICACIÓN
# ============================================================

class AplicacionGPS:
    """
    Clase principal que contiene toda la aplicación educativa sobre GPS.
    Organizada en secciones para facilitar la comprensión por parte de estudiantes.
    """
    
    def __init__(self, ventana):
        """
        Inicializa la aplicación con todos sus componentes.
        
        Args:
            ventana: Ventana principal de tkinter
        """
        self.ventana = ventana
        self.ventana.title("GPS para Jóvenes Pensadores - Python para Pensadores")
        self.ventana.geometry("1100x900")
        self.ventana.configure(bg='#f0f8ff')
        
        # Configurar icono y título de ventana
        try:
            self.ventana.iconbitmap(default='')  # Se puede agregar un icono aquí
        except:
            pass
        
        # Configurar el estilo de la aplicación
        self.configurar_estilos()
        
        # Variables para simulación
        self.satelites = []
        self.receptor_pos = [0, 0]
        self.distancias = []
        self.simulando = False
        
        # Crear la interfaz
        self.crear_interfaz()
        
        # Inicializar satélites
        self.inicializar_satelites()
        
    def configurar_estilos(self):
        """Configura los estilos visuales para toda la aplicación."""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Colores para la aplicación (paleta amigable para estudiantes)
        self.color_fondo = '#f0f8ff'
        self.color_principal = '#2c3e50'
        self.color_secundario = '#3498db'
        self.color_acento = '#e74c3c'
        self.color_exito = '#2ecc71'
        self.color_texto = '#2c3e50'
        
        # Configurar estilos para widgets
        self.style.configure('Titulo.TLabel', 
                           font=('Arial', 18, 'bold'),
                           foreground=self.color_principal,
                           background=self.color_fondo)
        
        self.style.configure('Subtitulo.TLabel',
                           font=('Arial', 12, 'bold'),
                           foreground=self.color_secundario,
                           background=self.color_fondo)
        
        self.style.configure('Cuerpo.TLabel',
                           font=('Arial', 10),
                           foreground=self.color_texto,
                           background=self.color_fondo,
                           wraplength=500)
        
        self.style.configure('BotonPrincipal.TButton',
                           font=('Arial', 11, 'bold'),
                           foreground='white',
                           background=self.color_secundario,
                           borderwidth=2,
                           relief='raised')
        
        self.style.map('BotonPrincipal.TButton',
                      background=[('active', self.color_principal)])
        
        self.style.configure('Marco.TFrame',
                           background=self.color_fondo,
                           relief='solid',
                           borderwidth=1)
    
    def crear_interfaz(self):
        """Crea todos los elementos de la interfaz gráfica."""
        
        # ============================================================
        # ENCABEZADO DE LA APLICACIÓN
        # ============================================================
        encabezado_frame = ttk.Frame(self.ventana, style='Marco.TFrame')
        encabezado_frame.pack(fill='x', padx=10, pady=10)
        
        # Título principal
        titulo_label = ttk.Label(encabezado_frame, 
                                text="Python para pensadores",
                                style='Titulo.TLabel')
        titulo_label.pack(pady=5)
        
        # Subtítulo
        subtitulo_label = ttk.Label(encabezado_frame,
                                   text="Taller diseñado con el corazón de un docente y la mente de un programador.",
                                   style='Cuerpo.TLabel')
        subtitulo_label.pack(pady=5)
        
        # Reto
        reto_label = ttk.Label(encabezado_frame,
                              text='Reto "Tipo de jugador" - Comprendiendo el GPS',
                              style='Subtitulo.TLabel')
        reto_label.pack(pady=10)
        
        # ============================================================
        # CONTENIDO PRINCIPAL (Dividido en dos secciones)
        # ============================================================
        contenido_frame = ttk.Frame(self.ventana)
        contenido_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Panel izquierdo: Explicación y controles
        panel_izquierdo = ttk.Frame(contenido_frame, style='Marco.TFrame')
        panel_izquierdo.pack(side='left', fill='both', expand=True, padx=(0, 5))
        
        # Panel derecho: Visualización
        panel_derecho = ttk.Frame(contenido_frame, style='Marco.TFrame')
        panel_derecho.pack(side='right', fill='both', expand=True, padx=(5, 0))
        
        # ============================================================
        # PANEL IZQUIERDO: EXPLICACIÓN Y CONTROLES
        # ============================================================
        
        # Pestañas para organizar el contenido
        notebook = ttk.Notebook(panel_izquierdo)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Pestaña 1: Introducción al GPS
        tab_intro = ttk.Frame(notebook)
        notebook.add(tab_intro, text="Introducción")
        self.crear_tab_introduccion(tab_intro)
        
        # Pestaña 2: Cómo funciona
        tab_funcionamiento = ttk.Frame(notebook)
        notebook.add(tab_funcionamiento, text="Cómo funciona")
        self.crear_tab_funcionamiento(tab_funcionamiento)
        
        # Pestaña 3: Simulación
        tab_simulacion = ttk.Frame(notebook)
        notebook.add(tab_simulacion, text="Simulación")
        self.crear_tab_simulacion(tab_simulacion)
        
        # Pestaña 4: Práctica
        tab_practica = ttk.Frame(notebook)
        notebook.add(tab_practica, text="Práctica")
        self.crear_tab_practica(tab_practica)
        
        # ============================================================
        # PANEL DERECHO: VISUALIZACIÓN
        # ============================================================
        
        # Título del panel de visualización
        titulo_visualizacion = ttk.Label(panel_derecho,
                                        text="Visualización de Trilateración GPS",
                                        style='Subtitulo.TLabel')
        titulo_visualizacion.pack(pady=10)
        
        # Canvas para dibujar la simulación
        self.canvas = tk.Canvas(panel_derecho, bg='white', width=500, height=500,
                               highlightbackground=self.color_secundario,
                               highlightthickness=2)
        self.canvas.pack(pady=10, padx=10)
        
        # Información de la simulación
        self.info_label = ttk.Label(panel_derecho,
                                   text="Presiona 'Iniciar Simulación' para comenzar",
                                   style='Cuerpo.TLabel')
        self.info_label.pack(pady=5)
        
        # ============================================================
        # PIE DE PÁGINA
        # ============================================================
        pie_frame = ttk.Frame(self.ventana, style='Marco.TFrame')
        pie_frame.pack(fill='x', padx=10, pady=10)
        
        pie_label = ttk.Label(pie_frame,
                             text="Diseñado por: Edwin Méndez J.",
                             style='Cuerpo.TLabel')
        pie_label.pack(pady=5)
    
    def crear_tab_introduccion(self, contenedor):
        """Crea el contenido de la pestaña de introducción."""
        # Texto de introducción
        intro_texto = """
        ¡Bienvenido al taller de GPS para Jóvenes Pensadores!

        El Sistema de Posicionamiento Global (GPS) es una tecnología que
        usamos todos los días en nuestros teléfonos y dispositivos. 
        Pero, ¿sabes realmente cómo funciona?

        En este taller aprenderás:
        1. Los principios básicos del funcionamiento del GPS
        2. Cómo los satélites nos ayudan a determinar nuestra posición
        3. El concepto matemático de trilateración
        4. Cómo programar una simulación básica de GPS en Python

        Este conocimiento es útil no solo para tecnología, sino que 
        desarrolla tu pensamiento lógico y espacial.
        """
        
        intro_label = ttk.Label(contenedor, text=intro_texto,
                               style='Cuerpo.TLabel', justify='left')
        intro_label.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Imagen simbólica (usando texto ASCII para simplicidad)
        ascii_gps = """
           ╔══════════════════════════════╗
           ║      SISTEMA GPS             ║
           ╠══════════════════════════════╣
           ║   🛰️    🛰️                  ║
           ║                              ║
           ║      🛰️      🛰️             ║
           ║                              ║
           ║        📍 (TÚ)               ║
           ║                              ║
           ╚══════════════════════════════╝
        """
        
        ascii_label = ttk.Label(contenedor, text=ascii_gps,
                               font=('Courier', 9),
                               foreground=self.color_principal,
                               background=self.color_fondo)
        ascii_label.pack(pady=10)
    
    def crear_tab_funcionamiento(self, contenedor):
        """Crea el contenido de la pestaña de funcionamiento."""
        # Texto explicativo
        explicacion = """
        CÓMO FUNCIONA EL GPS - PASO A PASO:

        1. CONSTELACIÓN DE SATÉLITES
        • Hay 24+ satélites GPS orbitando la Tierra
        • Cada satélite transmite su posición y hora exacta

        2. RECEPCIÓN DE SEÑALES
        • Tu dispositivo GPS recibe señales de varios satélites
        • Mide el tiempo que tardó cada señal en llegar

        3. CÁLCULO DE DISTANCIAS
        • Velocidad de la luz = 300,000 km/segundo
        • Distancia = Velocidad × Tiempo
        • Cada distancia crea una "esfera" de posibles posiciones

        4. TRILATERACIÓN
        • Con 3 satélites: Posición 2D (latitud, longitud)
        • Con 4+ satélites: Posición 3D + corrección de tiempo
        • Intersección de esferas = tu posición exacta
        """
        
        explicacion_label = ttk.Label(contenedor, text=explicacion,
                                     style='Cuerpo.TLabel', justify='left')
        explicacion_label.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Ejemplo visual de trilateración
        ejemplo_frame = ttk.Frame(contenedor)
        ejemplo_frame.pack(pady=10)
        
        ejemplo_label = ttk.Label(ejemplo_frame,
                                 text="Ejemplo de Trilateración:",
                                 style='Subtitulo.TLabel')
        ejemplo_label.pack()
        
        ejemplo_texto = """
        Imaginemos que estamos en un campo:
        • Satélite 1 está a 100km → Dibujamos círculo de 100km
        • Satélite 2 está a 120km → Dibujamos círculo de 120km
        • Satélite 3 está a 90km → Dibujamos círculo de 90km
        
        Donde se cruzan los 3 círculos: ¡Ahí estás tú!
        """
        
        ejemplo_detalle = ttk.Label(ejemplo_frame, text=ejemplo_texto,
                                   style='Cuerpo.TLabel', justify='left')
        ejemplo_detalle.pack(pady=10)
    
    def crear_tab_simulacion(self, contenedor):
        """Crea el contenido de la pestaña de simulación."""
        # Controles de simulación
        controles_frame = ttk.Frame(contenedor)
        controles_frame.pack(pady=20, padx=20, fill='x')
        
        # Botón para iniciar simulación
        self.btn_iniciar = ttk.Button(controles_frame,
                                     text="Iniciar Simulación",
                                     style='BotonPrincipal.TButton',
                                     command=self.iniciar_simulacion)
        self.btn_iniciar.pack(pady=10, fill='x')
        
        # Botón para reiniciar
        self.btn_reiniciar = ttk.Button(controles_frame,
                                       text="Reiniciar Simulación",
                                       style='BotonPrincipal.TButton',
                                       command=self.reiniciar_simulacion)
        self.btn_reiniciar.pack(pady=10, fill='x')
        
        # Botón para paso a paso
        self.btn_paso = ttk.Button(controles_frame,
                                  text="Ejecutar Paso a Paso",
                                  style='BotonPrincipal.TButton',
                                  command=self.ejecutar_paso_a_paso)
        self.btn_paso.pack(pady=10, fill='x')
        
        # Configuración de satélites
        config_frame = ttk.LabelFrame(contenedor, text="Configuración de Satélites")
        config_frame.pack(pady=20, padx=20, fill='x')
        
        # Control para número de satélites
        ttk.Label(config_frame, text="Número de satélites:").pack(pady=5)
        self.num_satelites = tk.IntVar(value=4)
        
        spinbox_frame = ttk.Frame(config_frame)
        spinbox_frame.pack(pady=5)
        
        ttk.Spinbox(spinbox_frame, from_=3, to=8,
                   textvariable=self.num_satelites,
                   width=10).pack(side='left', padx=5)
        
        ttk.Button(spinbox_frame, text="Aplicar",
                  command=self.actualizar_satelites).pack(side='left', padx=5)
        
        # Instrucciones de simulación
        instrucciones = """
        INSTRUCCIONES DE SIMULACIÓN:

        1. Haz clic en 'Iniciar Simulación' para comenzar
        2. Observa cómo los satélites envían señales
        3. Mira cómo se calculan las distancias
        4. Observa el proceso de trilateración
        5. La posición calculada aparecerá en rojo
        6. La posición real aparecerá en verde
        """
        
        instrucciones_label = ttk.Label(contenedor, text=instrucciones,
                                       style='Cuerpo.TLabel', justify='left')
        instrucciones_label.pack(pady=20, padx=20, fill='both', expand=True)
    
    def crear_tab_practica(self, contenedor):
        """Crea el contenido de la pestaña de práctica."""
        # Ejercicio práctico
        ejercicio_texto = """
        EJERCICIO PRÁCTICO: RESUELVE LA POSICIÓN

        Dadas las siguientes distancias a 3 satélites:
        
        Satélite 1: Posición (100, 100) - Distancia: 141.42 km
        Satélite 2: Posición (300, 100) - Distancia: 180.28 km
        Satélite 3: Posición (200, 300) - Distancia: 111.80 km
        
        ¿Cuál es tu posición (x, y)?
        
        Usa la fórmula de distancia:
        d = √[(x₂ - x₁)² + (y₂ - y₁)²]
        
        Resuelve el sistema de ecuaciones:
        1. (x - 100)² + (y - 100)² = 141.42²
        2. (x - 300)² + (y - 100)² = 180.28²
        3. (x - 200)² + (y - 300)² = 111.80²
        """
        
        ejercicio_label = ttk.Label(contenedor, text=ejercicio_texto,
                                   style='Cuerpo.TLabel', justify='left')
        ejercicio_label.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Entrada para respuesta del estudiante
        respuesta_frame = ttk.Frame(contenedor)
        respuesta_frame.pack(pady=20, padx=20, fill='x')
        
        ttk.Label(respuesta_frame, text="Tu respuesta (x, y):").pack(pady=5)
        
        entrada_frame = ttk.Frame(respuesta_frame)
        entrada_frame.pack(pady=10)
        
        ttk.Label(entrada_frame, text="x =").pack(side='left', padx=5)
        self.entrada_x = ttk.Entry(entrada_frame, width=10)
        self.entrada_x.pack(side='left', padx=5)
        
        ttk.Label(entrada_frame, text="y =").pack(side='left', padx=5)
        self.entrada_y = ttk.Entry(entrada_frame, width=10)
        self.entrada_y.pack(side='left', padx=5)
        
        # Botón para verificar respuesta
        ttk.Button(respuesta_frame, text="Verificar Respuesta",
                  command=self.verificar_respuesta).pack(pady=10)
        
        # Resultado de verificación
        self.resultado_label = ttk.Label(respuesta_frame, text="")
        self.resultado_label.pack(pady=10)
        
        # Solución (oculta inicialmente)
        self.btn_mostrar_solucion = ttk.Button(contenedor,
                                              text="Mostrar Solución",
                                              command=self.mostrar_solucion)
        self.btn_mostrar_solucion.pack(pady=10)
        
        self.solucion_label = ttk.Label(contenedor, text="", foreground=self.color_exito)
        self.solucion_label.pack(pady=10)
    
    def inicializar_satelites(self):
        """Inicializa los satélites para la simulación."""
        self.satelites = []
        num_satelites = self.num_satelites.get()
        
        # Posiciones predefinidas para mejor visualización
        posiciones_predefinidas = [
            (100, 100), (400, 100), (100, 400), (400, 400),
            (250, 50), (250, 450), (50, 250), (450, 250)
        ]
        
        for i in range(num_satelites):
            if i < len(posiciones_predefinidas):
                x, y = posiciones_predefinidas[i]
            else:
                x = random.randint(50, 450)
                y = random.randint(50, 450)
            
            self.satelites.append({
                'id': i + 1,
                'x': x,
                'y': y,
                'distancia': 0
            })
        
        # Posición aleatoria para el receptor
        self.receptor_pos = [random.randint(150, 350), random.randint(150, 350)]
    
    def actualizar_satelites(self):
        """Actualiza el número de satélites según la configuración."""
        self.inicializar_satelites()
        self.dibujar_simulacion()
        self.info_label.config(text=f"Satélites actualizados: {self.num_satelites.get()}")
    
    def iniciar_simulacion(self):
        """Inicia la simulación completa."""
        if self.simulando:
            return
        
        self.simulando = True
        self.info_label.config(text="Simulación en progreso...")
        
        # Limpiar el canvas
        self.canvas.delete("all")
        
        # Dibujar elementos iniciales
        self.dibujar_simulacion()
        
        # Realizar la simulación paso a paso
        self.simular_paso_a_paso(0)
    
    def simular_paso_a_paso(self, paso):
        """Simula el proceso paso a paso."""
        if not self.simulando or paso > 4:
            self.simulando = False
            self.info_label.config(text="Simulación completada")
            return
        
        # Ejecutar el paso actual
        if paso == 0:
            self.mostrar_satelites()
        elif paso == 1:
            self.mostrar_receptor()
        elif paso == 2:
            self.calcular_distancias()
        elif paso == 3:
            self.mostrar_distancias()
        elif paso == 4:
            self.mostrar_trilateracion()
        
        # Programar el siguiente paso después de un delay
        self.ventana.after(1500, lambda: self.simular_paso_a_paso(paso + 1))
    
    def ejecutar_paso_a_paso(self):
        """Ejecuta un solo paso de la simulación."""
        if not hasattr(self, 'paso_actual'):
            self.paso_actual = 0
            self.canvas.delete("all")
        
        pasos = [
            ("Mostrando satélites...", self.mostrar_satelites),
            ("Mostrando receptor...", self.mostrar_receptor),
            ("Calculando distancias...", self.calcular_distancias),
            ("Mostrando distancias...", self.mostrar_distancias),
            ("Realizando trilateración...", self.mostrar_trilateracion)
        ]
        
        if self.paso_actual < len(pasos):
            texto, funcion = pasos[self.paso_actual]
            self.info_label.config(text=texto)
            funcion()
            self.paso_actual += 1
        else:
            self.info_label.config(text="Simulación completada")
            self.paso_actual = 0
    
    def reiniciar_simulacion(self):
        """Reinicia la simulación a su estado inicial."""
        self.simulando = False
        self.paso_actual = 0
        self.dibujar_simulacion()
        self.info_label.config(text="Simulación reiniciada. Presiona 'Iniciar Simulación' para comenzar.")
    
    def dibujar_simulacion(self):
        """Dibuja todos los elementos en el canvas."""
        self.canvas.delete("all")
        
        # Dibujar satélites
        for sat in self.satelites:
            x, y = sat['x'], sat['y']
            self.canvas.create_oval(x-10, y-10, x+10, y+10,
                                   fill=self.color_secundario,
                                   outline=self.color_principal,
                                   width=2)
            self.canvas.create_text(x, y-15,
                                   text=f"S{sat['id']}",
                                   fill=self.color_principal,
                                   font=('Arial', 10, 'bold'))
        
        # Dibujar receptor
        rx, ry = self.receptor_pos
        self.canvas.create_oval(rx-8, ry-8, rx+8, ry+8,
                               fill=self.color_exito,
                               outline=self.color_principal,
                               width=2,
                               tags="receptor")
        self.canvas.create_text(rx, ry+15,
                               text="TÚ (Real)",
                               fill=self.color_exito,
                               font=('Arial', 9, 'bold'))
    
    def mostrar_satelites(self):
        """Muestra los satélites con animación."""
        for sat in self.satelites:
            x, y = sat['x'], sat['y']
            
            # Destacar satélite
            self.canvas.create_oval(x-15, y-15, x+15, y+15,
                                   outline=self.color_acento,
                                   width=3,
                                   tags="destacado")
            
            # Información del satélite
            self.canvas.create_text(x, y+25,
                                   text=f"({x}, {y})",
                                   fill=self.color_principal,
                                   font=('Arial', 8))
        
        self.canvas.update()
    
    def mostrar_receptor(self):
        """Muestra la posición del receptor."""
        rx, ry = self.receptor_pos
        
        # Destacar receptor
        self.canvas.create_oval(rx-12, ry-12, rx+12, ry+12,
                               outline=self.color_acento,
                               width=3,
                               tags="destacado")
        
        # Información del receptor
        self.canvas.create_text(rx, ry-25,
                               text=f"Posición real: ({rx}, {ry})",
                               fill=self.color_exito,
                               font=('Arial', 9, 'bold'))
        
        self.canvas.update()
    
    def calcular_distancias(self):
        """Calcula las distancias desde cada satélite al receptor."""
        self.distancias = []
        rx, ry = self.receptor_pos
        
        for sat in self.satelites:
            # Calcular distancia euclidiana
            distancia = math.sqrt((sat['x'] - rx)**2 + (sat['y'] - ry)**2)
            sat['distancia'] = distancia
            self.distancias.append(distancia)
            
            # Mostrar cálculo
            info = f"Distancia S{sat['id']}: {distancia:.1f} km"
            self.canvas.create_text(sat['x'], sat['y']+40,
                                   text=info,
                                   fill=self.color_principal,
                                   font=('Arial', 8))
        
        self.canvas.update()
    
    def mostrar_distancias(self):
        """Muestra visualmente las distancias como círculos."""
        for sat in self.satelites:
            x, y = sat['x'], sat['y']
            distancia = sat['distancia']
            
            # Dibujar círculo de distancia
            self.canvas.create_oval(x-distancia, y-distancia,
                                   x+distancia, y+distancia,
                                   outline=self.color_secundario,
                                   width=1,
                                   dash=(5, 2))
        
        self.canvas.update()
    
    def mostrar_trilateracion(self):
        """Muestra el proceso de trilateración y calcula la posición."""
        # Para simplificar, usaremos un método aproximado
        # En un caso real, se resolvería el sistema de ecuaciones
        
        # Método simplificado: promedio ponderado
        total_x = 0
        total_y = 0
        total_peso = 0
        
        for sat in self.satelites:
            # Dar más peso a satélites más cercanos
            peso = 1 / (sat['distancia'] + 0.1)
            total_x += sat['x'] * peso
            total_y += sat['y'] * peso
            total_peso += peso
        
        # Calcular posición estimada
        if total_peso > 0:
            pos_estimada_x = total_x / total_peso
            pos_estimada_y = total_y / total_peso
            
            # Dibujar posición estimada
            self.canvas.create_oval(pos_estimada_x-10, pos_estimada_y-10,
                                   pos_estimada_x+10, pos_estimada_y+10,
                                   fill=self.color_acento,
                                   outline=self.color_principal,
                                   width=2)
            
            self.canvas.create_text(pos_estimada_x, pos_estimada_y+20,
                                   text="Posición estimada",
                                   fill=self.color_acento,
                                   font=('Arial', 9, 'bold'))
            
            # Mostrar error
            error = math.sqrt((pos_estimada_x - self.receptor_pos[0])**2 +
                             (pos_estimada_y - self.receptor_pos[1])**2)
            
            self.info_label.config(text=f"Simulación completada. Error: {error:.2f} km")
            
            # Mostrar línea entre posición real y estimada
            self.canvas.create_line(self.receptor_pos[0], self.receptor_pos[1],
                                   pos_estimada_x, pos_estimada_y,
                                   fill=self.color_acento,
                                   width=2,
                                   dash=(3, 2))
    
    def verificar_respuesta(self):
        """Verifica la respuesta del ejercicio práctico."""
        try:
            x_respuesta = float(self.entrada_x.get())
            y_respuesta = float(self.entrada_y.get())
            
            # Solución del ejercicio (aproximada)
            solucion_x = 200.0
            solucion_y = 200.0
            
            # Calcular error
            error = math.sqrt((x_respuesta - solucion_x)**2 + (y_respuesta - solucion_y)**2)
            
            if error < 10:  # Margen de error aceptable
                self.resultado_label.config(text="¡Correcto! Excelente trabajo.",
                                          foreground=self.color_exito)
            else:
                self.resultado_label.config(text=f"Buen intento. Error: {error:.2f}. ¡Sigue intentando!",
                                          foreground=self.color_acento)
                
        except ValueError:
            self.resultado_label.config(text="Por favor ingresa números válidos",
                                      foreground=self.color_acento)
    
    def mostrar_solucion(self):
        """Muestra la solución del ejercicio práctico."""
        solucion = """
        SOLUCIÓN:
        
        Resolviendo el sistema de ecuaciones:
        
        1. (x - 100)² + (y - 100)² = 20000
        2. (x - 300)² + (y - 100)² = 32500
        3. (x - 200)² + (y - 300)² = 12500
        
        Restando ecuación 2 - ecuación 1:
        (x-300)² - (x-100)² = 12500
        x² - 600x + 90000 - (x² - 200x + 10000) = 12500
        -400x + 80000 = 12500
        -400x = -67500
        x = 168.75
        
        Sustituyendo en ecuación 1:
        (168.75 - 100)² + (y - 100)² = 20000
        4726.56 + (y - 100)² = 20000
        (y - 100)² = 15273.44
        y - 100 = ±123.6
        y = 223.6  (tomamos la solución positiva)
        
        Posición aproximada: (169, 224)
        
        NOTA: En la práctica, se usarían métodos numéricos más precisos
        y al menos 4 satélites para mayor exactitud.
        """
        
        self.solucion_label.config(text=solucion, justify='left')
        self.btn_mostrar_solucion.config(state='disabled')


# ============================================================
# FUNCIÓN PRINCIPAL PARA EJECUTAR LA APLICACIÓN
# ============================================================

def main():
    """
    Función principal que inicia la aplicación GPS educativa.
    Esta función crea la ventana principal y la aplicación.
    """
    # Crear ventana principal
    ventana_principal = tk.Tk()
    
    # Crear la aplicación
    app = AplicacionGPS(ventana_principal)
    
    # Configurar cierre seguro
    ventana_principal.protocol("WM_DELETE_WINDOW", ventana_principal.quit)
    
    # Iniciar el loop principal
    ventana_principal.mainloop()


# ============================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================

if __name__ == "__main__":
    """
    Punto de entrada principal del programa.
    Esta parte del código se ejecuta cuando el programa inicia.
    """
    print("Iniciando aplicación educativa de GPS...")
    print("Taller: Python para Pensadores")
    print("Autor: Edwin Méndez J.")
    print("\nCargando interfaz gráfica...")
    
    # Ejecutar la aplicación
    main()