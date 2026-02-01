import tkinter as tk
from tkinter import ttk, messagebox
import re

# ============================================
# CONFIGURACIÓN DE COLORES Y ESTILOS
# ============================================
COLORES = {
    "fondo_principal": "#1e3d59",  # Azul oscuro
    "fondo_secundario": "#2c5282",  # Azul medio
    "fondo_terciario": "#4a90e2",   # Azul claro
    "texto_principal": "#ffffff",   # Blanco
    "texto_secundario": "#f0f0f0",  # Blanco grisáceo
    "acento": "#ff6b6b",            # Rojo coral
    "acento_suave": "#ff8e8e",      # Rojo coral claro
    "verde": "#4CAF50",             # Verde
    "verde_hover": "#45a049",       # Verde oscuro para hover
    "naranja": "#ff9800",           # Naranja
    "naranja_hover": "#e68a00",     # Naranja oscuro para hover
    "borde": "#0d1b2a",             # Azul muy oscuro
}

# ============================================
# FUNCIONES PARA CÁLCULO DEL DÍGITO VERIFICADOR
# ============================================

def validar_formato_cedula(cedula):
    """
    Valida si la cédula tiene un formato correcto (10 dígitos).
    Retorna True si es válida, False en caso contrario.
    """
    # Verificar que sean exactamente 10 dígitos numéricos
    if not cedula.isdigit() or len(cedula) != 10:
        return False
    
    # Verificar que la provincia sea válida (01-24 o 30 para extranjeros)
    provincia = int(cedula[0:2])
    if provincia < 1 or (provincia > 24 and provincia != 30):
        return False
    
    return True

def calcular_digito_verificador(cedula_9_digitos):
    """
    Calcula el dígito verificador para los primeros 9 dígitos de una cédula.
    Algoritmo según el Registro Civil del Ecuador.
    """
    # Coeficientes para el cálculo
    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    
    # Verificar que la entrada tenga 9 dígitos
    if len(cedula_9_digitos) != 9 or not cedula_9_digitos.isdigit():
        return None
    
    suma_total = 0
    
    # Proceso de cálculo paso a paso
    pasos = []  # Para almacenar los pasos intermedios
    
    for i in range(9):
        digito = int(cedula_9_digitos[i])
        coeficiente = coeficientes[i]
        producto = digito * coeficiente
        
        # Si el producto es mayor a 9, restar 9
        if producto > 9:
            producto -= 9
        
        pasos.append({
            "posicion": i + 1,
            "digito": digito,
            "coeficiente": coeficiente,
            "producto": producto
        })
        
        suma_total += producto
    
    # Obtener el residuo de la división entre 10
    residuo = suma_total % 10
    
    # Calcular el dígito verificador
    if residuo == 0:
        digito_verificador = 0
    else:
        digito_verificador = 10 - residuo
    
    return {
        "digito_verificador": digito_verificador,
        "suma_total": suma_total,
        "residuo": residuo,
        "pasos": pasos
    }

# ============================================
# FUNCIONES PARA LA INTERFAZ GRÁFICA
# ============================================

def crear_boton(parent, texto, comando, color_normal, color_hover):
    """
    Crea un botón con efecto hover personalizado.
    """
    boton = tk.Button(
        parent,
        text=texto,
        font=("Arial", 12, "bold"),
        bg=color_normal,
        fg=COLORES["texto_principal"],
        activebackground=color_hover,
        activeforeground=COLORES["texto_principal"],
        relief="raised",
        borderwidth=2,
        padx=20,
        pady=10,
        cursor="hand2",
        command=comando
    )
    
    # Configurar eventos para efecto hover
    def on_enter(event):
        boton.config(bg=color_hover)
    
    def on_leave(event):
        boton.config(bg=color_normal)
    
    boton.bind("<Enter>", on_enter)
    boton.bind("<Leave>", on_leave)
    
    return boton

def mostrar_pasos_calculo(resultado, cedula_9_digitos):
    """
    Muestra los pasos detallados del cálculo del dígito verificador.
    """
    # Crear ventana emergente para mostrar los pasos
    ventana_pasos = tk.Toplevel(ventana_principal)
    ventana_pasos.title("Pasos Detallados del Cálculo")
    ventana_pasos.geometry("700x500")
    ventana_pasos.configure(bg=COLORES["fondo_principal"])
    ventana_pasos.resizable(False, False)
    
    # Centrar la ventana
    ventana_pasos.transient(ventana_principal)
    ventana_pasos.grab_set()
    
    # Título
    titulo_frame = tk.Frame(ventana_pasos, bg=COLORES["fondo_secundario"])
    titulo_frame.pack(fill="x", padx=10, pady=10)
    
    titulo = tk.Label(
        titulo_frame,
        text=f"Cálculo Detallado para: {cedula_9_digitos}",
        font=("Arial", 14, "bold"),
        bg=COLORES["fondo_secundario"],
        fg=COLORES["texto_principal"],
        pady=10
    )
    titulo.pack()
    
    # Crear un canvas con scrollbar para contener los pasos
    frame_contenedor = tk.Frame(ventana_pasos, bg=COLORES["fondo_principal"])
    frame_contenedor.pack(fill="both", expand=True, padx=10, pady=5)
    
    canvas = tk.Canvas(frame_contenedor, bg=COLORES["fondo_principal"], highlightthickness=0)
    scrollbar = tk.Scrollbar(frame_contenedor, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg=COLORES["fondo_principal"])
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Mostrar los pasos del cálculo
    for i, paso in enumerate(resultado["pasos"]):
        paso_frame = tk.Frame(
            scrollable_frame,
            bg=COLORES["fondo_secundario"] if i % 2 == 0 else COLORES["fondo_terciario"],
            relief="ridge",
            borderwidth=1
        )
        paso_frame.pack(fill="x", padx=5, pady=2)
        
        texto_paso = f"Paso {i+1}: Dígito {paso['digito']} × Coeficiente {paso['coeficiente']} = {paso['digito'] * paso['coeficiente']}"
        
        if paso['digito'] * paso['coeficiente'] > 9:
            texto_paso += f" → {paso['digito'] * paso['coeficiente']} > 9, restamos 9 = {paso['producto']}"
        else:
            texto_paso += f" = {paso['producto']}"
        
        label_paso = tk.Label(
            paso_frame,
            text=texto_paso,
            font=("Arial", 11),
            bg=paso_frame.cget("bg"),
            fg=COLORES["texto_principal"],
            justify="left",
            anchor="w",
            padx=10,
            pady=5
        )
        label_paso.pack(fill="x")
    
    # Mostrar la suma total
    suma_frame = tk.Frame(
        scrollable_frame,
        bg=COLORES["fondo_secundario"],
        relief="raised",
        borderwidth=2
    )
    suma_frame.pack(fill="x", padx=5, pady=10)
    
    label_suma = tk.Label(
        suma_frame,
        text=f"Suma total: {resultado['suma_total']}",
        font=("Arial", 12, "bold"),
        bg=COLORES["fondo_secundario"],
        fg=COLORES["verde"],
        pady=8
    )
    label_suma.pack()
    
    # Mostrar el residuo y el dígito verificador
    resultado_frame = tk.Frame(
        scrollable_frame,
        bg=COLORES["fondo_terciario"],
        relief="raised",
        borderwidth=2
    )
    resultado_frame.pack(fill="x", padx=5, pady=5)
    
    texto_residuo = f"Residuo: {resultado['suma_total']} % 10 = {resultado['residuo']}"
    label_residuo = tk.Label(
        resultado_frame,
        text=texto_residuo,
        font=("Arial", 11),
        bg=COLORES["fondo_terciario"],
        fg=COLORES["texto_principal"],
        pady=5
    )
    label_residuo.pack()
    
    if resultado['residuo'] == 0:
        texto_dv = f"Dígito Verificador: 0 (porque el residuo es 0)"
    else:
        texto_dv = f"Dígito Verificador: 10 - {resultado['residuo']} = {resultado['digito_verificador']}"
    
    label_dv = tk.Label(
        resultado_frame,
        text=texto_dv,
        font=("Arial", 12, "bold"),
        bg=COLORES["fondo_terciario"],
        fg=COLORES["acento"],
        pady=5
    )
    label_dv.pack()
    
    # Botón para cerrar
    boton_cerrar = crear_boton(
        scrollable_frame,
        "Cerrar",
        ventana_pasos.destroy,
        COLORES["naranja"],
        COLORES["naranja_hover"]
    )
    boton_cerrar.pack(pady=20)

def calcular_y_mostrar():
    """
    Calcula el dígito verificador y muestra el resultado.
    """
    # Obtener la cédula del campo de entrada
    cedula_completa = entrada_cedula.get().strip()
    
    # Validar que se haya ingresado algo
    if not cedula_completa:
        messagebox.showwarning("Campo vacío", "Por favor ingresa una cédula para calcular.")
        entrada_cedula.focus_set()
        return
    
    # Validar el formato de la cédula
    if not validar_formato_cedula(cedula_completa):
        messagebox.showerror(
            "Cédula inválida", 
            "La cédula ingresada no tiene un formato válido.\n\n"
            "Debe tener 10 dígitos numéricos.\n"
            "Los dos primeros dígitos deben representar una provincia válida (01-24 o 30)."
        )
        entrada_cedula.select_range(0, tk.END)
        entrada_cedula.focus_set()
        return
    
    # Extraer los primeros 9 dígitos
    primeros_9_digitos = cedula_completa[:9]
    
    # Calcular el dígito verificador
    resultado = calcular_digito_verificador(primeros_9_digitos)
    
    if resultado is None:
        messagebox.showerror("Error", "Error al calcular el dígito verificador.")
        return
    
    # Mostrar el resultado en la interfaz
    digito_calculado = resultado["digito_verificador"]
    digito_real = cedula_completa[9]  # Último dígito de la cédula ingresada
    
    # Actualizar etiquetas de resultado
    etiqueta_resultado.config(
        text=f"Dígito calculado: {digito_calculado}",
        fg=COLORES["verde"]
    )
    
    etiqueta_cedula_completa.config(
        text=f"Cédula completa: {primeros_9_digitos}-{digito_calculado}",
        fg=COLORES["acento"]
    )
    
    # Verificar si el dígito calculado coincide con el ingresado
    if str(digito_calculado) == digito_real:
        etiqueta_validacion.config(
            text="✓ El dígito verificador es CORRECTO",
            fg=COLORES["verde"]
        )
    else:
        etiqueta_validacion.config(
            text=f"✗ El dígito verificador es INCORRECTO (ingresado: {digito_real})",
            fg=COLORES["acento"]
        )
    
    # Habilitar el botón para ver los pasos detallados
    boton_ver_pasos.config(state="normal", command=lambda: mostrar_pasos_calculo(resultado, primeros_9_digitos))
    
    # Mostrar información sobre la provincia
    mostrar_info_provincia(cedula_completa[:2])

def mostrar_info_provincia(codigo_provincia):
    """
    Muestra información sobre la provincia según los dos primeros dígitos de la cédula.
    """
    # Diccionario de provincias del Ecuador
    provincias = {
        "01": "Azuay",
        "02": "Bolívar",
        "03": "Cañar",
        "04": "Carchi",
        "05": "Cotopaxi",
        "06": "Chimborazo",
        "07": "El Oro",
        "08": "Esmeraldas",
        "09": "Guayas",
        "10": "Imbabura",
        "11": "Loja",
        "12": "Los Ríos",
        "13": "Manabí",
        "14": "Morona Santiago",
        "15": "Napo",
        "16": "Pastaza",
        "17": "Pichincha",
        "18": "Tungurahua",
        "19": "Zamora Chinchipe",
        "20": "Galápagos",
        "21": "Sucumbíos",
        "22": "Orellana",
        "23": "Santo Domingo de los Tsáchilas",
        "24": "Santa Elena",
        "30": "Extranjero"
    }
    
    nombre_provincia = provincias.get(codigo_provincia, "Desconocida")
    
    etiqueta_provincia.config(
        text=f"Provincia: {nombre_provincia} (Código: {codigo_provincia})",
        fg=COLORES["naranja"]
    )

def limpiar_campos():
    """
    Limpia todos los campos y resultados de la interfaz.
    """
    entrada_cedula.delete(0, tk.END)
    etiqueta_resultado.config(text="Dígito calculado: -")
    etiqueta_cedula_completa.config(text="Cédula completa: ----------")
    etiqueta_validacion.config(text="Ingresa una cédula y presiona Calcular")
    etiqueta_provincia.config(text="Provincia: -")
    boton_ver_pasos.config(state="disabled")
    entrada_cedula.focus_set()

def insertar_ejemplo():
    """
    Inserta un ejemplo de cédula válida en el campo de entrada.
    """
    # Ejemplo de cédula válida (la usaremos sin el último dígito para que el estudiante calcule)
    ejemplo = "1713176123"  # Esta cédula tiene dígito verificador 3
    entrada_cedula.delete(0, tk.END)
    entrada_cedula.insert(0, ejemplo)
    entrada_cedula.focus_set()

def mostrar_info_algoritmo():
    """
    Muestra información sobre el algoritmo de cálculo del dígito verificador.
    """
    info = """
    ALGORITMO PARA CALCULAR EL DÍGITO VERIFICADOR

    1. Tomar los primeros 9 dígitos de la cédula.
    2. Multiplicar cada dígito por un coeficiente:
       - Posición impar (1, 3, 5, 7, 9): coeficiente 2
       - Posición par (2, 4, 6, 8): coeficiente 1
    3. Si el resultado de la multiplicación es mayor a 9, restar 9.
    4. Sumar todos los resultados obtenidos.
    5. Calcular el residuo de la división entre 10.
    6. El dígito verificador es:
       - 0 si el residuo es 0
       - 10 - residuo si el residuo es diferente de 0

    Ejemplo rápido:
    Cédula: 171317612-?
    Coeficientes: 2,1,2,1,2,1,2,1,2
    Cálculo:
      1×2=2, 7×1=7, 1×2=2, 3×1=3, 1×2=2, 7×1=7, 6×2=12→3, 1×1=1, 2×2=4
    Suma: 2+7+2+3+2+7+3+1+4 = 31
    Residuo: 31 % 10 = 1
    Dígito verificador: 10 - 1 = 9
    """
    
    messagebox.showinfo("Algoritmo de Cálculo", info)

# ============================================
# CONFIGURACIÓN DE LA VENTANA PRINCIPAL
# ============================================

# Crear ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Cálculo del Dígito Verificador - Cédula Ecuatoriana")
ventana_principal.configure(bg=COLORES["fondo_principal"])

# Centrar la ventana en la pantalla
ancho_ventana = 800
alto_ventana = 900
ancho_pantalla = ventana_principal.winfo_screenwidth()
alto_pantalla = ventana_principal.winfo_screenheight()
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)
ventana_principal.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
ventana_principal.resizable(False, False)

# ============================================
# INTERFAZ GRÁFICA - COMPONENTES
# ============================================

# Marco principal para organizar los elementos
marco_principal = tk.Frame(ventana_principal, bg=COLORES["fondo_principal"], padx=20, pady=20)
marco_principal.pack(fill="both", expand=True)

# Título de la aplicación
titulo = tk.Label(
    marco_principal,
    text="CÁLCULO DEL DÍGITO VERIFICADOR",
    font=("Arial", 24, "bold"),
    bg=COLORES["fondo_principal"],
    fg=COLORES["texto_principal"],
    pady=20
)
titulo.pack()

subtitulo = tk.Label(
    marco_principal,
    text="Cédula Ecuatoriana - Aplicación Educativa",
    font=("Arial", 14),
    bg=COLORES["fondo_principal"],
    fg=COLORES["texto_secundario"],
    pady=5
)
subtitulo.pack()

# Línea separadora
separador = ttk.Separator(marco_principal, orient="horizontal")
separador.pack(fill="x", pady=20)

# Marco para la explicación
marco_explicacion = tk.Frame(
    marco_principal,
    bg=COLORES["fondo_secundario"],
    relief="ridge",
    borderwidth=2,
    padx=15,
    pady=15
)
marco_explicacion.pack(fill="x", pady=10)

explicacion = tk.Label(
    marco_explicacion,
    text="El dígito verificador es el último número de la cédula ecuatoriana (posición 10).\n"
         "Sirve para validar que la cédula sea auténtica y esté correctamente construida.\n"
         "Ingresa una cédula de 10 dígitos para calcular y verificar su dígito verificador.",
    font=("Arial", 11),
    bg=COLORES["fondo_secundario"],
    fg=COLORES["texto_principal"],
    justify="center",
    wraplength=700 #controlar el ajuste automático del texto
)
explicacion.pack()

# Marco para entrada de datos
marco_entrada = tk.Frame(marco_principal, bg=COLORES["fondo_principal"], pady=20)
marco_entrada.pack()

etiqueta_instruccion = tk.Label(
    marco_entrada,
    text="Ingresa una cédula ecuatoriana (10 dígitos):",
    font=("Arial", 12, "bold"),
    bg=COLORES["fondo_principal"],
    fg=COLORES["texto_principal"]
)
etiqueta_instruccion.grid(row=0, column=0, columnspan=2, pady=10)

# Campo de entrada para la cédula
entrada_cedula = tk.Entry(
    marco_entrada,
    font=("Arial", 16),
    width=20,
    justify="center",
    relief="solid",
    borderwidth=2
)
entrada_cedula.grid(row=1, column=0, columnspan=2, pady=10, ipady=8)
entrada_cedula.focus_set()

# Marco para botones principales
marco_botones = tk.Frame(marco_principal, bg=COLORES["fondo_principal"], pady=20)
marco_botones.pack()

# Botón para calcular
boton_calcular = crear_boton(
    marco_botones,
    "🔍 Calcular Dígito",
    calcular_y_mostrar,
    COLORES["verde"],
    COLORES["verde_hover"]
)
boton_calcular.grid(row=0, column=0, padx=10, pady=5)

# Botón para limpiar
boton_limpiar = crear_boton(
    marco_botones,
    "🗑️ Limpiar",
    limpiar_campos,
    COLORES["naranja"],
    COLORES["naranja_hover"]
)
boton_limpiar.grid(row=0, column=1, padx=10, pady=5)

# Botón para ejemplo
boton_ejemplo = crear_boton(
    marco_botones,
    "📋 Ejemplo",
    insertar_ejemplo,
    COLORES["fondo_terciario"],
    COLORES["acento_suave"]
)
boton_ejemplo.grid(row=0, column=2, padx=10, pady=5)

# Marco para mostrar resultados
marco_resultados = tk.Frame(
    marco_principal,
    bg=COLORES["fondo_secundario"],
    relief="groove",
    borderwidth=3,
    padx=20,
    pady=20
)
marco_resultados.pack(fill="x", pady=20)

# Etiquetas para mostrar resultados
etiqueta_resultado = tk.Label(
    marco_resultados,
    text="Dígito calculado: -",
    font=("Arial", 14, "bold"),
    bg=COLORES["fondo_secundario"],
    fg=COLORES["texto_principal"],
    pady=5
)
etiqueta_resultado.pack()

etiqueta_cedula_completa = tk.Label(
    marco_resultados,
    text="Cédula completa: ----------",
    font=("Arial", 12),
    bg=COLORES["fondo_secundario"],
    fg=COLORES["texto_principal"],
    pady=5
)
etiqueta_cedula_completa.pack()

etiqueta_validacion = tk.Label(
    marco_resultados,
    text="Ingresa una cédula y presiona Calcular",
    font=("Arial", 12),
    bg=COLORES["fondo_secundario"],
    fg=COLORES["texto_secundario"],
    pady=5
)
etiqueta_validacion.pack()

etiqueta_provincia = tk.Label(
    marco_resultados,
    text="Provincia: -",
    font=("Arial", 11, "italic"),
    bg=COLORES["fondo_secundario"],
    fg=COLORES["texto_principal"],
    pady=5
)
etiqueta_provincia.pack()

# Botón para ver pasos detallados (inicialmente deshabilitado)
boton_ver_pasos = crear_boton(
    marco_resultados,
    "📊 Ver Pasos Detallados",
    lambda: None,
    COLORES["fondo_terciario"],
    COLORES["acento_suave"]
)
boton_ver_pasos.pack(pady=15)
boton_ver_pasos.config(state="disabled")

# Marco para información adicional
marco_info = tk.Frame(marco_principal, bg=COLORES["fondo_principal"], pady=20)
marco_info.pack()

# Botón para información del algoritmo
boton_info_algoritmo = crear_boton(
    marco_info,
    "ℹ️ Ver Algoritmo de Cálculo",
    mostrar_info_algoritmo,
    COLORES["fondo_terciario"],
    COLORES["acento_suave"]
)
boton_info_algoritmo.pack()

# Información sobre las provincias
info_provincias = tk.Label(
    marco_info,
    text="Nota: Los dos primeros dígitos representan la provincia de emisión de la cédula.",
    font=("Arial", 10, "italic"),
    bg=COLORES["fondo_principal"],
    fg=COLORES["texto_secundario"],
    pady=10
)
info_provincias.pack()

# Pie de página
pie_pagina = tk.Label(
    marco_principal,
    text="Aplicación Educativa - Cálculo del Dígito Verificador de la Cédula Ecuatoriana\n"
         "Desarrollada para estudiantes de bachillerato - © 2023",
    font=("Arial", 9),
    bg=COLORES["fondo_principal"],
    fg=COLORES["texto_secundario"],
    pady=20
)
pie_pagina.pack()

# ============================================
# CONFIGURACIÓN DE EVENTOS ADICIONALES
# ============================================

# Permitir calcular presionando Enter en el campo de entrada
entrada_cedula.bind("<Return>", lambda event: calcular_y_mostrar())

# ============================================
# INICIALIZACIÓN DE LA APLICACIÓN
# ============================================

# Ejecutar la aplicación
ventana_principal.mainloop()