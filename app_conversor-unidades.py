import tkinter as tk
from tkinter import ttk, messagebox

# ============================================
# CONFIGURACIÓN INICIAL Y VARIABLES GLOBALES
# ============================================

# Paleta de colores moderna y atractiva
COLORES = {
    "fondo": "#F0F4F8",
    "fondo_widget": "#FFFFFF",
    "primario": "#4361EE",
    "secundario": "#3A0CA3",
    "acento": "#7209B7",
    "texto": "#2B2D42",
    "texto_claro": "#8D99AE",
    "exito": "#4CC9F0",
    "hover": "#4895EF",
    "borde": "#D1D9E6"
}

# Tasas de conversión de monedas (valores de ejemplo para fines educativos)
TASAS_CAMBIO = {
    "USD": {"EUR": 0.92, "GBP": 0.79, "JPY": 150.0, "COP": 3900.0, "MXN": 17.0},
    "EUR": {"USD": 1.09, "GBP": 0.86, "JPY": 163.0, "COP": 4230.0, "MXN": 18.4},
    "GBP": {"USD": 1.27, "EUR": 1.16, "JPY": 189.0, "COP": 4920.0, "MXN": 21.4},
    "JPY": {"USD": 0.0067, "EUR": 0.0061, "GBP": 0.0053, "COP": 26.0, "MXN": 0.11},
    "COP": {"USD": 0.00026, "EUR": 0.00024, "GBP": 0.00020, "JPY": 0.038, "MXN": 0.0044},
    "MXN": {"USD": 0.059, "EUR": 0.054, "GBP": 0.047, "JPY": 8.9, "COP": 229.0}
}

# Variables para almacenar los valores de entrada
valor_entrada = None
resultado_label = None
tipo_conversion_actual = None

# ============================================
# FUNCIONES DE CONVERSIÓN
# ============================================

def convertir_temperatura(valor, de_unidad, a_unidad):
    """Convierte entre Celsius, Fahrenheit y Kelvin"""
    try:
        valor = float(valor)
        
        # Primero convertir todo a Celsius
        if de_unidad == "Celsius":
            celsius = valor
        elif de_unidad == "Fahrenheit":
            celsius = (valor - 32) * 5/9
        elif de_unidad == "Kelvin":
            celsius = valor - 273.15
        
        # Convertir de Celsius a la unidad destino
        if a_unidad == "Celsius":
            resultado = celsius
        elif a_unidad == "Fahrenheit":
            resultado = (celsius * 9/5) + 32
        elif a_unidad == "Kelvin":
            resultado = celsius + 273.15
            
        return round(resultado, 4)
    except ValueError:
        return None

def convertir_longitud(valor, de_unidad, a_unidad):
    """Convierte entre metros, kilómetros, millas y pies"""
    try:
        valor = float(valor)
        
        # Factores de conversión a metros
        factores = {
            "Metros": 1,
            "Kilómetros": 1000,
            "Millas": 1609.34,
            "Pies": 0.3048
        }
        
        # Convertir a metros primero
        metros = valor * factores[de_unidad]
        
        # Convertir de metros a la unidad destino
        resultado = metros / factores[a_unidad]
        
        return round(resultado, 4)
    except ValueError:
        return None

def convertir_moneda(valor, de_moneda, a_moneda):
    """Convierte entre diferentes monedas usando tasas de cambio predefinidas"""
    try:
        valor = float(valor)
        
        # Si es la misma moneda, no hay conversión
        if de_moneda == a_moneda:
            return round(valor, 4)
        
        # Usar las tasas de cambio definidas
        if de_moneda in TASAS_CAMBIO and a_moneda in TASAS_CAMBIO[de_moneda]:
            tasa = TASAS_CAMBIO[de_moneda][a_moneda]
            resultado = valor * tasa
            return round(resultado, 4)
        else:
            # Si no hay conversión directa, convertir a USD primero y luego a la moneda destino
            if de_moneda != "USD" and "USD" in TASAS_CAMBIO.get(de_moneda, {}):
                valor_usd = valor * TASAS_CAMBIO[de_moneda]["USD"]
                if a_moneda != "USD" and a_moneda in TASAS_CAMBIO.get("USD", {}):
                    resultado = valor_usd * TASAS_CAMBIO["USD"][a_moneda]
                    return round(resultado, 4)
        
        return None
    except ValueError:
        return None

def convertir_peso(valor, de_unidad, a_unidad):
    """Convierte entre kilogramos, gramos, libras y onzas"""
    try:
        valor = float(valor)
        
        # Factores de conversión a kilogramos
        factores = {
            "Kilogramos": 1,
            "Gramos": 0.001,
            "Libras": 0.453592,
            "Onzas": 0.0283495
        }
        
        # Convertir a kilogramos primero
        kilogramos = valor * factores[de_unidad]
        
        # Convertir de kilogramos a la unidad destino
        resultado = kilogramos / factores[a_unidad]
        
        return round(resultado, 4)
    except ValueError:
        return None

# ============================================
# FUNCIONES DE INTERFAZ Y EVENTOS
# ============================================

def aplicar_estilo_boton(boton, color_normal, color_hover):
    """Aplica efecto hover a un botón"""
    def entrar(event):
        boton.config(bg=color_hover)
    
    def salir(event):
        boton.config(bg=color_normal)
    
    boton.bind("<Enter>", entrar)
    boton.bind("<Leave>", salir)

def limpiar_area_conversion():
    """Limpia el área de conversión para mostrar nuevos controles"""
    global resultado_label
    
    # Limpiar el frame de conversión
    for widget in frame_conversion.winfo_children():
        widget.destroy()
    
    # Crear un nuevo frame para contenido de conversión
    global frame_contenido
    frame_contenido = tk.Frame(frame_conversion, bg=COLORES["fondo_widget"], 
                               relief="solid", bd=1, highlightbackground=COLORES["borde"])
    frame_contenido.pack(fill="both", expand=True, padx=10, pady=10)
    
    # Reiniciar la etiqueta de resultado
    resultado_label = None

def mostrar_conversion_temperatura():
    """Muestra la interfaz para conversión de temperatura"""
    global tipo_conversion_actual
    tipo_conversion_actual = "temperatura"
    limpiar_area_conversion()
    
    # Título explicativo
    titulo = tk.Label(frame_contenido, text="Conversor de Temperatura", 
                      font=("Arial", 16, "bold"), bg=COLORES["fondo_widget"], fg=COLORES["primario"])
    titulo.pack(pady=(10, 5))
    
    explicacion = tk.Label(frame_contenido, 
                           text="Convierte entre Celsius, Fahrenheit y Kelvin.\nCelsius (°C) es la escala más usada en el mundo.\nFahrenheit (°F) se usa principalmente en Estados Unidos.\nKelvin (K) es la escala científica absoluta.",
                           font=("Arial", 10), bg=COLORES["fondo_widget"], fg=COLORES["texto_claro"],
                           justify="center")
    explicacion.pack(pady=(0, 15))
    
    # Frame para controles de entrada
    frame_controles = tk.Frame(frame_contenido, bg=COLORES["fondo_widget"])
    frame_controles.pack(pady=10)
    
    # Etiqueta y campo de entrada
    tk.Label(frame_controles, text="Valor a convertir:", 
             font=("Arial", 11), bg=COLORES["fondo_widget"], fg=COLORES["texto"]).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    
    entrada_valor = tk.Entry(frame_controles, font=("Arial", 11), width=15, 
                            relief="solid", bd=1, highlightbackground=COLORES["borde"])
    entrada_valor.grid(row=0, column=1, padx=5, pady=5)
    entrada_valor.insert(0, "0")
    
    # Unidades de origen
    tk.Label(frame_controles, text="De unidad:", 
             font=("Arial", 11), bg=COLORES["fondo_widget"], fg=COLORES["texto"]).grid(row=1, column=0, padx=5, pady=5, sticky="w")
    
    de_unidad = ttk.Combobox(frame_controles, values=["Celsius", "Fahrenheit", "Kelvin"], 
                            state="readonly", width=13)
    de_unidad.grid(row=1, column=1, padx=5, pady=5)
    de_unidad.current(0)
    
    # Unidades de destino
    tk.Label(frame_controles, text="A unidad:", 
             font=("Arial", 11), bg=COLORES["fondo_widget"], fg=COLORES["texto"]).grid(row=2, column=0, padx=5, pady=5, sticky="w")
    
    a_unidad = ttk.Combobox(frame_controles, values=["Celsius", "Fahrenheit", "Kelvin"], 
                           state="readonly", width=13)
    a_unidad.grid(row=2, column=1, padx=5, pady=5)
    a_unidad.current(1)
    
    # Botón de conversión
    boton_convertir = tk.Button(frame_controles, text="Convertir", 
                               font=("Arial", 11, "bold"), bg=COLORES["primario"], 
                               fg="white", cursor="hand2", width=15)
    boton_convertir.grid(row=3, column=0, columnspan=2, pady=15)
    aplicar_estilo_boton(boton_convertir, COLORES["primario"], COLORES["hover"])
    
    # Función para realizar la conversión
    def realizar_conversion():
        valor = entrada_valor.get()
        de_uni = de_unidad.get()
        a_uni = a_unidad.get()
        
        resultado = convertir_temperatura(valor, de_uni, a_uni)
        
        if resultado is not None:
            # Mostrar resultado
            for widget in frame_contenido.winfo_children():
                if isinstance(widget, tk.Frame) and widget != frame_controles:
                    widget.destroy()
            
            frame_resultado = tk.Frame(frame_contenido, bg=COLORES["fondo_widget"])
            frame_resultado.pack(pady=10)
            
            resultado_texto = f"{valor} {de_uni} = {resultado} {a_uni}"
            
            # Información adicional educativa
            info_extra = ""
            if de_uni == "Celsius" and a_uni == "Fahrenheit":
                info_extra = "Fórmula: °F = (°C × 9/5) + 32"
            elif de_uni == "Fahrenheit" and a_uni == "Celsius":
                info_extra = "Fórmula: °C = (°F - 32) × 5/9"
            elif "Kelvin" in [de_uni, a_uni]:
                info_extra = "Cero absoluto: 0 K = -273.15 °C = -459.67 °F"
            
            tk.Label(frame_resultado, text=resultado_texto, 
                    font=("Arial", 14, "bold"), bg=COLORES["fondo_widget"], 
                    fg=COLORES["exito"]).pack(pady=5)
            
            if info_extra:
                tk.Label(frame_resultado, text=info_extra, 
                        font=("Arial", 10, "italic"), bg=COLORES["fondo_widget"], 
                        fg=COLORES["texto_claro"]).pack(pady=5)
        else:
            messagebox.showerror("Error", "Por favor ingresa un valor numérico válido")
    
    boton_convertir.config(command=realizar_conversion)
    
    # Ejemplo educativo
    frame_ejemplo = tk.Frame(frame_contenido, bg=COLORES["fondo_widget"])
    frame_ejemplo.pack(pady=(20, 10))
    
    tk.Label(frame_ejemplo, text="Ejemplos comunes:", 
             font=("Arial", 11, "bold"), bg=COLORES["fondo_widget"], 
             fg=COLORES["texto"]).pack()
    
    ejemplos = [
        "0 °C = 32 °F (Punto de congelación del agua)",
        "100 °C = 212 °F (Punto de ebullición del agua)",
        "37 °C = 98.6 °F (Temperatura corporal normal)",
        "-40 °C = -40 °F (Misma temperatura en ambas escalas)"
    ]
    
    for ejemplo in ejemplos:
        tk.Label(frame_ejemplo, text=ejemplo, font=("Arial", 9), 
                bg=COLORES["fondo_widget"], fg=COLORES["texto_claro"]).pack(anchor="w", padx=20)

def mostrar_conversion_longitud():
    """Muestra la interfaz para conversión de longitud"""
    global tipo_conversion_actual
    tipo_conversion_actual = "longitud"
    limpiar_area_conversion()
    
    # Título explicativo
    titulo = tk.Label(frame_contenido, text="Conversor de Longitud", 
                      font=("Arial", 16, "bold"), bg=COLORES["fondo_widget"], fg=COLORES["primario"])
    titulo.pack(pady=(10, 5))
    
    explicacion = tk.Label(frame_contenido, 
                           text="Convierte entre metros, kilómetros, millas y pies.\nEl metro (m) es la unidad base del Sistema Internacional.\n1 kilómetro = 1000 metros.\n1 milla ≈ 1609 metros.\n1 pie ≈ 0.3048 metros.",
                           font=("Arial", 10), bg=COLORES["fondo_widget"], fg=COLORES["texto_claro"],
                           justify="center")
    explicacion.pack(pady=(0, 15))
    
    # Frame para controles de entrada
    frame_controles = tk.Frame(frame_contenido, bg=COLORES["fondo_widget"])
    frame_controles.pack(pady=10)
    
    # Etiqueta y campo de entrada
    tk.Label(frame_controles, text="Valor a convertir:", 
             font=("Arial", 11), bg=COLORES["fondo_widget"], fg=COLORES["texto"]).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    
    entrada_valor = tk.Entry(frame_controles, font=("Arial", 11), width=15, 
                            relief="solid", bd=1, highlightbackground=COLORES["borde"])
    entrada_valor.grid(row=0, column=1, padx=5, pady=5)
    entrada_valor.insert(0, "0")
    
    # Unidades de origen
    tk.Label(frame_controles, text="De unidad:", 
             font=("Arial", 11), bg=COLORES["fondo_widget"], fg=COLORES["texto"]).grid(row=1, column=0, padx=5, pady=5, sticky="w")
    
    de_unidad = ttk.Combobox(frame_controles, values=["Metros", "Kilómetros", "Millas", "Pies"], 
                            state="readonly", width=13)
    de_unidad.grid(row=1, column=1, padx=5, pady=5)
    de_unidad.current(0)
    
    # Unidades de destino
    tk.Label(frame_controles, text="A unidad:", 
             font=("Arial", 11), bg=COLORES["fondo_widget"], fg=COLORES["texto"]).grid(row=2, column=0, padx=5, pady=5, sticky="w")
    
    a_unidad = ttk.Combobox(frame_controles, values=["Metros", "Kilómetros", "Millas", "Pies"], 
                           state="readonly", width=13)
    a_unidad.grid(row=2, column=1, padx=5, pady=5)
    a_unidad.current(1)
    
    # Botón de conversión
    boton_convertir = tk.Button(frame_controles, text="Convertir", 
                               font=("Arial", 11, "bold"), bg=COLORES["primario"], 
                               fg="white", cursor="hand2", width=15)
    boton_convertir.grid(row=3, column=0, columnspan=2, pady=15)
    aplicar_estilo_boton(boton_convertir, COLORES["primario"], COLORES["hover"])
    
    # Función para realizar la conversión
    def realizar_conversion():
        valor = entrada_valor.get()
        de_uni = de_unidad.get()
        a_uni = a_unidad.get()
        
        resultado = convertir_longitud(valor, de_uni, a_uni)
        
        if resultado is not None:
            # Mostrar resultado
            for widget in frame_contenido.winfo_children():
                if isinstance(widget, tk.Frame) and widget != frame_controles:
                    widget.destroy()
            
            frame_resultado = tk.Frame(frame_contenido, bg=COLORES["fondo_widget"])
            frame_resultado.pack(pady=10)
            
            resultado_texto = f"{valor} {de_uni} = {resultado} {a_uni}"
            
            # Información adicional educativa
            info_extra = ""
            if de_uni == "Kilómetros" and a_uni == "Millas":
                info_extra = "1 km ≈ 0.621 millas"
            elif de_uni == "Metros" and a_uni == "Pies":
                info_extra = "1 m ≈ 3.281 pies"
            
            tk.Label(frame_resultado, text=resultado_texto, 
                    font=("Arial", 14, "bold"), bg=COLORES["fondo_widget"], 
                    fg=COLORES["exito"]).pack(pady=5)
            
            if info_extra:
                tk.Label(frame_resultado, text=info_extra, 
                        font=("Arial", 10, "italic"), bg=COLORES["fondo_widget"], 
                        fg=COLORES["texto_claro"]).pack(pady=5)
        else:
            messagebox.showerror("Error", "Por favor ingresa un valor numérico válido")
    
    boton_convertir.config(command=realizar_conversion)
    
    # Ejemplo educativo
    frame_ejemplo = tk.Frame(frame_contenido, bg=COLORES["fondo_widget"])
    frame_ejemplo.pack(pady=(20, 10))
    
    tk.Label(frame_ejemplo, text="Ejemplos comunes:", 
             font=("Arial", 11, "bold"), bg=COLORES["fondo_widget"], 
             fg=COLORES["texto"]).pack()
    
    ejemplos = [
        "1 km = 0.621 millas",
        "1 milla = 1.609 km",
        "1 m = 3.281 pies",
        "Maratón: 42.195 km = 26.219 millas"
    ]
    
    for ejemplo in ejemplos:
        tk.Label(frame_ejemplo, text=ejemplo, font=("Arial", 9), 
                bg=COLORES["fondo_widget"], fg=COLORES["texto_claro"]).pack(anchor="w", padx=20)

def mostrar_conversion_moneda():
    """Muestra la interfaz para conversión de moneda"""
    global tipo_conversion_actual
    tipo_conversion_actual = "moneda"
    limpiar_area_conversion()
    
    # Título explicativo
    titulo = tk.Label(frame_contenido, text="Conversor de Moneda", 
                      font=("Arial", 16, "bold"), bg=COLORES["fondo_widget"], fg=COLORES["primario"])
    titulo.pack(pady=(10, 5))
    
    explicacion = tk.Label(frame_contenido, 
                           text="Convierte entre diferentes monedas usando tasas de cambio de ejemplo.\nEstas tasas son para fines educativos y pueden no reflejar\nlas tasas actuales del mercado.",
                           font=("Arial", 10), bg=COLORES["fondo_widget"], fg=COLORES["texto_claro"],
                           justify="center")
    explicacion.pack(pady=(0, 15))
    
    # Frame para controles de entrada
    frame_controles = tk.Frame(frame_contenido, bg=COLORES["fondo_widget"])
    frame_controles.pack(pady=10)
    
    # Etiqueta y campo de entrada
    tk.Label(frame_controles, text="Valor a convertir:", 
             font=("Arial", 11), bg=COLORES["fondo_widget"], fg=COLORES["texto"]).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    
    entrada_valor = tk.Entry(frame_controles, font=("Arial", 11), width=15, 
                            relief="solid", bd=1, highlightbackground=COLORES["borde"])
    entrada_valor.grid(row=0, column=1, padx=5, pady=5)
    entrada_valor.insert(0, "1")
    
    # Monedas de origen
    tk.Label(frame_controles, text="De moneda:", 
             font=("Arial", 11), bg=COLORES["fondo_widget"], fg=COLORES["texto"]).grid(row=1, column=0, padx=5, pady=5, sticky="w")
    
    monedas = ["USD", "EUR", "GBP", "JPY", "COP", "MXN"]
    de_moneda = ttk.Combobox(frame_controles, values=monedas, 
                            state="readonly", width=13)
    de_moneda.grid(row=1, column=1, padx=5, pady=5)
    de_moneda.current(0)
    
    # Monedas de destino
    tk.Label(frame_controles, text="A moneda:", 
             font=("Arial", 11), bg=COLORES["fondo_widget"], fg=COLORES["texto"]).grid(row=2, column=0, padx=5, pady=5, sticky="w")
    
    a_moneda = ttk.Combobox(frame_controles, values=monedas, 
                           state="readonly", width=13)
    a_moneda.grid(row=2, column=1, padx=5, pady=5)
    a_moneda.current(1)
    
    # Botón de conversión
    boton_convertir = tk.Button(frame_controles, text="Convertir", 
                               font=("Arial", 11, "bold"), bg=COLORES["primario"], 
                               fg="white", cursor="hand2", width=15)
    boton_convertir.grid(row=3, column=0, columnspan=2, pady=15)
    aplicar_estilo_boton(boton_convertir, COLORES["primario"], COLORES["hover"])
    
    # Función para realizar la conversión
    def realizar_conversion():
        valor = entrada_valor.get()
        de_mon = de_moneda.get()
        a_mon = a_moneda.get()
        
        resultado = convertir_moneda(valor, de_mon, a_mon)
        
        if resultado is not None:
            # Mostrar resultado
            for widget in frame_contenido.winfo_children():
                if isinstance(widget, tk.Frame) and widget != frame_controles:
                    widget.destroy()
            
            frame_resultado = tk.Frame(frame_contenido, bg=COLORES["fondo_widget"])
            frame_resultado.pack(pady=10)
            
            resultado_texto = f"{valor} {de_mon} = {resultado} {a_mon}"
            
            # Mostrar tasa de cambio
            if de_mon != a_mon:
                if de_mon in TASAS_CAMBIO and a_mon in TASAS_CAMBIO[de_mon]:
                    tasa = TASAS_CAMBIO[de_mon][a_mon]
                    info_tasa = f"Tasa: 1 {de_mon} = {tasa} {a_mon}"
                else:
                    info_tasa = f"Tasa calculada mediante conversión intermedia"
                
                tk.Label(frame_resultado, text=info_tasa, 
                        font=("Arial", 10, "italic"), bg=COLORES["fondo_widget"], 
                        fg=COLORES["texto_claro"]).pack(pady=5)
            
            tk.Label(frame_resultado, text=resultado_texto, 
                    font=("Arial", 14, "bold"), bg=COLORES["fondo_widget"], 
                    fg=COLORES["exito"]).pack(pady=5)
        else:
            messagebox.showerror("Error", "Por favor ingresa un valor numérico válido")
    
    boton_convertir.config(command=realizar_conversion)
    
    # Información sobre tasas de cambio
    frame_info = tk.Frame(frame_contenido, bg=COLORES["fondo_widget"])
    frame_info.pack(pady=(20, 10))
    
    tk.Label(frame_info, text="Tasas de cambio de ejemplo (1 USD):", 
             font=("Arial", 11, "bold"), bg=COLORES["fondo_widget"], 
             fg=COLORES["texto"]).pack()
    
    tasas_usd = TASAS_CAMBIO["USD"]
    for moneda, tasa in tasas_usd.items():
        tk.Label(frame_info, text=f"1 USD = {tasa} {moneda}", font=("Arial", 9), 
                bg=COLORES["fondo_widget"], fg=COLORES["texto_claro"]).pack(anchor="w", padx=20)

def mostrar_conversion_peso():
    """Muestra la interfaz para conversión de peso"""
    global tipo_conversion_actual
    tipo_conversion_actual = "peso"
    limpiar_area_conversion()
    
    # Título explicativo
    titulo = tk.Label(frame_contenido, text="Conversor de Peso", 
                      font=("Arial", 16, "bold"), bg=COLORES["fondo_widget"], fg=COLORES["primario"])
    titulo.pack(pady=(10, 5))
    
    explicacion = tk.Label(frame_contenido, 
                           text="Convierte entre kilogramos, gramos, libras y onzas.\nEl kilogramo (kg) es la unidad base de masa en el SI.\n1 kg = 1000 gramos.\n1 libra ≈ 0.4536 kg.\n1 onza ≈ 0.02835 kg.",
                           font=("Arial", 10), bg=COLORES["fondo_widget"], fg=COLORES["texto_claro"],
                           justify="center")
    explicacion.pack(pady=(0, 15))
    
    # Frame para controles de entrada
    frame_controles = tk.Frame(frame_contenido, bg=COLORES["fondo_widget"])
    frame_controles.pack(pady=10)
    
    # Etiqueta y campo de entrada
    tk.Label(frame_controles, text="Valor a convertir:", 
             font=("Arial", 11), bg=COLORES["fondo_widget"], fg=COLORES["texto"]).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    
    entrada_valor = tk.Entry(frame_controles, font=("Arial", 11), width=15, 
                            relief="solid", bd=1, highlightbackground=COLORES["borde"])
    entrada_valor.grid(row=0, column=1, padx=5, pady=5)
    entrada_valor.insert(0, "0")
    
    # Unidades de origen
    tk.Label(frame_controles, text="De unidad:", 
             font=("Arial", 11), bg=COLORES["fondo_widget"], fg=COLORES["texto"]).grid(row=1, column=0, padx=5, pady=5, sticky="w")
    
    de_unidad = ttk.Combobox(frame_controles, values=["Kilogramos", "Gramos", "Libras", "Onzas"], 
                            state="readonly", width=13)
    de_unidad.grid(row=1, column=1, padx=5, pady=5)
    de_unidad.current(0)
    
    # Unidades de destino
    tk.Label(frame_controles, text="A unidad:", 
             font=("Arial", 11), bg=COLORES["fondo_widget"], fg=COLORES["texto"]).grid(row=2, column=0, padx=5, pady=5, sticky="w")
    
    a_unidad = ttk.Combobox(frame_controles, values=["Kilogramos", "Gramos", "Libras", "Onzas"], 
                           state="readonly", width=13)
    a_unidad.grid(row=2, column=1, padx=5, pady=5)
    a_unidad.current(1)
    
    # Botón de conversión
    boton_convertir = tk.Button(frame_controles, text="Convertir", 
                               font=("Arial", 11, "bold"), bg=COLORES["primario"], 
                               fg="white", cursor="hand2", width=15)
    boton_convertir.grid(row=3, column=0, columnspan=2, pady=15)
    aplicar_estilo_boton(boton_convertir, COLORES["primario"], COLORES["hover"])
    
    # Función para realizar la conversión
    def realizar_conversion():
        valor = entrada_valor.get()
        de_uni = de_unidad.get()
        a_uni = a_unidad.get()
        
        resultado = convertir_peso(valor, de_uni, a_uni)
        
        if resultado is not None:
            # Mostrar resultado
            for widget in frame_contenido.winfo_children():
                if isinstance(widget, tk.Frame) and widget != frame_controles:
                    widget.destroy()
            
            frame_resultado = tk.Frame(frame_contenido, bg=COLORES["fondo_widget"])
            frame_resultado.pack(pady=10)
            
            resultado_texto = f"{valor} {de_uni} = {resultado} {a_uni}"
            
            # Información adicional educativa
            info_extra = ""
            if de_uni == "Kilogramos" and a_uni == "Libras":
                info_extra = "1 kg ≈ 2.205 libras"
            elif de_uni == "Libras" and a_uni == "Kilogramos":
                info_extra = "1 libra ≈ 0.454 kg"
            
            tk.Label(frame_resultado, text=resultado_texto, 
                    font=("Arial", 14, "bold"), bg=COLORES["fondo_widget"], 
                    fg=COLORES["exito"]).pack(pady=5)
            
            if info_extra:
                tk.Label(frame_resultado, text=info_extra, 
                        font=("Arial", 10, "italic"), bg=COLORES["fondo_widget"], 
                        fg=COLORES["texto_claro"]).pack(pady=5)
        else:
            messagebox.showerror("Error", "Por favor ingresa un valor numérico válido")
    
    boton_convertir.config(command=realizar_conversion)
    
    # Ejemplo educativo
    frame_ejemplo = tk.Frame(frame_contenido, bg=COLORES["fondo_widget"])
    frame_ejemplo.pack(pady=(20, 10))
    
    tk.Label(frame_ejemplo, text="Ejemplos comunes:", 
             font=("Arial", 11, "bold"), bg=COLORES["fondo_widget"], 
             fg=COLORES["texto"]).pack()
    
    ejemplos = [
        "1 kg = 2.205 libras",
        "1 libra = 16 onzas",
        "1 kg = 1000 gramos",
        "Persona promedio: 70 kg = 154.3 libras"
    ]
    
    for ejemplo in ejemplos:
        tk.Label(frame_ejemplo, text=ejemplo, font=("Arial", 9), 
                bg=COLORES["fondo_widget"], fg=COLORES["texto_claro"]).pack(anchor="w", padx=20)

def mostrar_instrucciones():
    """Muestra las instrucciones de uso de la aplicación"""
    messagebox.showinfo("Instrucciones",
                       "CONVERSOR EDUCATIVO DE UNIDADES Y MONEDAS\n\n"
                       "Esta aplicación te permite practicar conversiones entre diferentes unidades:\n\n"
                       "1. TEMPERATURA: Convierte entre Celsius, Fahrenheit y Kelvin\n"
                       "2. LONGITUD: Convierte entre metros, kilómetros, millas y pies\n"
                       "3. MONEDA: Convierte entre diferentes monedas (tasas de ejemplo)\n"
                       "4. PESO: Convierte entre kilogramos, gramos, libras y onzas\n\n"
                       "INSTRUCCIONES:\n"
                       "- Selecciona el tipo de conversión en el menú lateral\n"
                       "- Ingresa el valor a convertir\n"
                       "- Selecciona las unidades de origen y destino\n"
                       "- Haz clic en 'Convertir' para ver el resultado\n\n"
                       "¡Aprende practicando!")

def salir_aplicacion():
    """Cierra la aplicación"""
    if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?"):
        ventana.destroy()

# ============================================
# CONFIGURACIÓN DE LA VENTANA PRINCIPAL
# ============================================

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Conversor Educativo de Unidades y Monedas")
ventana.geometry("900x700")
ventana.configure(bg=COLORES["fondo"])

# Centrar ventana en pantalla
ventana.update_idletasks()
ancho_ventana = ventana.winfo_width()
alto_ventana = ventana.winfo_height()
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)
ventana.geometry(f"{900}x{700}+{x}+{y}")

# ============================================
# INTERFAZ GRÁFICA
# ============================================

# Frame principal
frame_principal = tk.Frame(ventana, bg=COLORES["fondo"])
frame_principal.pack(fill="both", expand=True, padx=20, pady=20)

# Encabezado
encabezado = tk.Frame(frame_principal, bg=COLORES["primario"], height=80)
encabezado.pack(fill="x", pady=(0, 20))
encabezado.pack_propagate(False)

tk.Label(encabezado, text="CONVERSOR EDUCATIVO", 
         font=("Arial", 24, "bold"), bg=COLORES["primario"], fg="white").pack(expand=True)

tk.Label(encabezado, text="Para estudiantes de bachillerato", 
         font=("Arial", 12), bg=COLORES["primario"], fg="#E0E0FF").pack(expand=True)

# Contenedor principal (sidebar + área de contenido)
contenedor = tk.Frame(frame_principal, bg=COLORES["fondo"])
contenedor.pack(fill="both", expand=True)

# ============================================
# SIDEBAR (MENÚ LATERAL)
# ============================================

sidebar = tk.Frame(contenedor, bg=COLORES["secundario"], width=200, 
                  relief="solid", bd=1, highlightbackground=COLORES["borde"])
sidebar.pack(side="left", fill="y", padx=(0, 10))
sidebar.pack_propagate(False)

# Título del sidebar
tk.Label(sidebar, text="MENÚ DE CONVERSIÓN", 
         font=("Arial", 14, "bold"), bg=COLORES["secundario"], 
         fg="white", pady=15).pack(fill="x")

# Botones del sidebar
opciones = [
    ("🌡️ TEMPERATURA", mostrar_conversion_temperatura),
    ("📏 LONGITUD", mostrar_conversion_longitud),
    ("💰 MONEDA", mostrar_conversion_moneda),
    ("⚖️ PESO", mostrar_conversion_peso),
    ("❓ INSTRUCCIONES", mostrar_instrucciones),
    ("🚪 SALIR", salir_aplicacion)
]

for texto, comando in opciones:
    boton = tk.Button(sidebar, text=texto, font=("Arial", 11, "bold"),
                     bg=COLORES["acento"], fg="white", cursor="hand2",
                     anchor="w", padx=15, pady=12, relief="flat",
                     command=comando)
    boton.pack(fill="x", padx=10, pady=5)
    aplicar_estilo_boton(boton, COLORES["acento"], COLORES["hover"])

# ============================================
# ÁREA DE CONTENIDO PRINCIPAL
# ============================================

frame_derecha = tk.Frame(contenedor, bg=COLORES["fondo"])
frame_derecha.pack(side="right", fill="both", expand=True)

# Frame para contenido de conversión
frame_conversion = tk.Frame(frame_derecha, bg=COLORES["fondo_widget"], 
                           relief="solid", bd=1, highlightbackground=COLORES["borde"])
frame_conversion.pack(fill="both", expand=True)

# Mensaje de bienvenida inicial
frame_bienvenida = tk.Frame(frame_conversion, bg=COLORES["fondo_widget"])
frame_bienvenida.pack(fill="both", expand=True)

tk.Label(frame_bienvenida, text="¡Bienvenido al Conversor Educativo!", 
         font=("Arial", 20, "bold"), bg=COLORES["fondo_widget"], 
         fg=COLORES["primario"]).pack(pady=(80, 20))

tk.Label(frame_bienvenida, 
         text="Selecciona un tipo de conversión en el menú lateral para comenzar.\n\n"
              "Esta herramienta te ayudará a comprender y practicar conversiones\n"
              "entre diferentes unidades de medida y monedas.\n\n"
              "Ideal para estudiantes de bachillerato que deseen fortalecer\n"
              "sus habilidades en matemáticas y ciencias.",
         font=("Arial", 12), bg=COLORES["fondo_widget"], 
         fg=COLORES["texto"], justify="center").pack(pady=10)

# Pie de página
footer = tk.Frame(frame_principal, bg=COLORES["texto_claro"], height=40)
footer.pack(fill="x", pady=(20, 0))
footer.pack_propagate(False)

tk.Label(footer, text="© 2026 Conversor Educativo - Para fines educativos", 
         font=("Arial", 9), bg=COLORES["texto_claro"], fg="white").pack(expand=True)

# ============================================
# INICIAR APLICACIÓN
# ============================================

ventana.mainloop()