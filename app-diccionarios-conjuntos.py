"""
JUEGO EDUCATIVO: DICCIONARIOS Y CONJUNTOS EN PYTHON
Autor: Experto en Desarrollo de Software Educativo
Destinatarios: Estudiantes de Bachillerato
Objetivo: Facilitar la comprensión de diccionarios y conjuntos mediante ejemplos interactivos
"""

import tkinter as tk
from tkinter import ttk, messagebox

# ============================================
# CONFIGURACIÓN INICIAL Y PALETA DE COLORES
# ============================================

# Paleta de colores moderna y atractiva
COLORES = {
    "fondo_principal": "#2C3E50",        # Azul oscuro elegante
    "fondo_secundario": "#34495E",       # Azul grisáceo
    "acento": "#3498DB",                  # Azul brillante
    "acento_hover": "#2980B9",            # Azul más oscuro para hover
    "exito": "#2ECC71",                   # Verde para operaciones exitosas
    "texto": "#ECF0F1",                   # Blanco grisáceo para texto
    "texto_oscuro": "#2C3E50",            # Azul oscuro para texto sobre fondo claro
    "borde": "#BDC3C7",                   # Gris claro para bordes
}

# ============================================
# FUNCIONES PARA EFECTOS VISUALES
# ============================================

def crear_boton_con_hover(parent, texto, comando, bg_color=COLORES["acento"], 
                         fg_color=COLORES["texto"], width=25):
    """
    Crea un botón con efecto hover personalizado
    
    Args:
        parent: Widget padre donde se colocará el botón
        texto: Texto que aparecerá en el botón
        comando: Función a ejecutar al hacer clic
        bg_color: Color de fondo normal
        fg_color: Color del texto
        width: Ancho del botón en caracteres
    """
    boton = tk.Button(
        parent,
        text=texto,
        command=comando,
        bg=bg_color,
        fg=fg_color,
        font=("Arial", 10, "bold"),
        width=width,
        relief="raised",
        bd=2,
        cursor="hand2"
    )
    
    # Configurar efecto hover
    def on_enter(event):
        boton.config(bg=COLORES["acento_hover"])
    
    def on_leave(event):
        boton.config(bg=bg_color)
    
    boton.bind("<Enter>", on_enter)
    boton.bind("<Leave>", on_leave)
    
    return boton

def limpiar_frame(frame):
    """Elimina todos los widgets de un frame"""
    for widget in frame.winfo_children():
        widget.destroy()

# ============================================
# FUNCIONES PARA DICCIONARIOS
# ============================================

def mostrar_diccionario_info():
    """Muestra información básica sobre diccionarios"""
    limpiar_frame(frame_contenido)
    
    tk.Label(
        frame_contenido,
        text="📚 ¿QUÉ ES UN DICCIONARIO?",
        font=("Arial", 16, "bold"),
        bg=COLORES["fondo_secundario"],
        fg=COLORES["texto"]
    ).pack(pady=10)
    
    explicacion = """
Un diccionario en Python es como un diccionario real:
- Cada palabra (clave) tiene su definición (valor)
- Las claves son ÚNICAS (no se repiten)
- Se accede a los valores usando las claves
- Los datos se almacenan en pares clave-valor

Ejemplo: 
estudiante = {
    "nombre": "Ana",
    "edad": 17,
    "curso": "1º Bachillerato",
    "materias": ["Matemáticas", "Física"]
}
"""
    
    tk.Label(
        frame_contenido,
        text=explicacion,
        font=("Arial", 11),
        bg=COLORES["fondo_secundario"],
        fg=COLORES["texto"],
        justify="left",
        wraplength=550
    ).pack(pady=10, padx=20)

def crear_diccionario_interactivo():
    """Interfaz para crear y manipular diccionarios"""
    limpiar_frame(frame_contenido)
    
    # Variables para almacenar el diccionario
    diccionario = {}
    
    # Frame para entrada de datos
    frame_entrada = tk.Frame(frame_contenido, bg=COLORES["fondo_secundario"])
    frame_entrada.pack(pady=10)
    
    tk.Label(
        frame_entrada,
        text="CREA TU DICCIONARIO",
        font=("Arial", 14, "bold"),
        bg=COLORES["fondo_secundario"],
        fg=COLORES["texto"]
    ).grid(row=0, column=0, columnspan=3, pady=10)
    
    # Campos para clave y valor
    tk.Label(frame_entrada, text="Clave:", bg=COLORES["fondo_secundario"], 
             fg=COLORES["texto"]).grid(row=1, column=0, padx=5)
    entry_clave = tk.Entry(frame_entrada, width=20, font=("Arial", 10))
    entry_clave.grid(row=1, column=1, padx=5)
    
    tk.Label(frame_entrada, text="Valor:", bg=COLORES["fondo_secundario"], 
             fg=COLORES["texto"]).grid(row=1, column=2, padx=5)
    entry_valor = tk.Entry(frame_entrada, width=20, font=("Arial", 10))
    entry_valor.grid(row=1, column=3, padx=5)
    
    # Área para mostrar el diccionario
    text_area = tk.Text(
        frame_contenido,
        height=8,
        width=60,
        font=("Consolas", 10),
        bg="#ECF0F1",
        fg=COLORES["texto_oscuro"]
    )
    text_area.pack(pady=10, padx=20)
    text_area.insert("1.0", "Tu diccionario aparecerá aquí...")
    text_area.config(state="disabled")
    
    def agregar_par():
        """Agrega un par clave-valor al diccionario"""
        clave = entry_clave.get().strip()
        valor = entry_valor.get().strip()
        
        if not clave:
            messagebox.showwarning("Advertencia", "La clave no puede estar vacía")
            return
        
        if not valor:
            messagebox.showwarning("Advertencia", "El valor no puede estar vacío")
            return
        
        diccionario[clave] = valor
        entry_clave.delete(0, tk.END)
        entry_valor.delete(0, tk.END)
        actualizar_diccionario()
    
    def eliminar_par():
        """Elimina un par clave-valor del diccionario"""
        clave = entry_clave.get().strip()
        
        if not clave:
            messagebox.showwarning("Advertencia", "Ingresa una clave para eliminar")
            return
        
        if clave in diccionario:
            del diccionario[clave]
            messagebox.showinfo("Éxito", f"Clave '{clave}' eliminada")
            entry_clave.delete(0, tk.END)
        else:
            messagebox.showerror("Error", f"La clave '{clave}' no existe")
        
        actualizar_diccionario()
    
    def buscar_clave():
        """Busca una clave en el diccionario"""
        clave = entry_clave.get().strip()
        
        if not clave:
            messagebox.showwarning("Advertencia", "Ingresa una clave para buscar")
            return
        
        if clave in diccionario:
            messagebox.showinfo("Resultado", f"Clave: {clave}\nValor: {diccionario[clave]}")
        else:
            messagebox.showinfo("Resultado", f"La clave '{clave}' no existe")
    
    def actualizar_diccionario():
        """Actualiza la visualización del diccionario"""
        text_area.config(state="normal")
        text_area.delete("1.0", tk.END)
        
        if diccionario:
            for clave, valor in diccionario.items():
                text_area.insert(tk.END, f'"{clave}": "{valor}"\n')
        else:
            text_area.insert("1.0", "El diccionario está vacío")
        
        text_area.config(state="disabled")
    
    # Botones de acción
    frame_botones = tk.Frame(frame_contenido, bg=COLORES["fondo_secundario"])
    frame_botones.pack(pady=10)
    
    crear_boton_con_hover(frame_botones, "➕ Agregar", agregar_par, 
                         bg_color=COLORES["exito"], width=15).pack(side="left", padx=5)
    crear_boton_con_hover(frame_botones, "🔍 Buscar", buscar_clave, 
                         width=15).pack(side="left", padx=5)
    crear_boton_con_hover(frame_botones, "🗑️ Eliminar", eliminar_par, 
                         bg_color="#E74C3C", width=15).pack(side="left", padx=5)

def operaciones_diccionario():
    """Demuestra operaciones comunes con diccionarios"""
    limpiar_frame(frame_contenido)
    
    tk.Label(
        frame_contenido,
        text="OPERACIONES COMUNES CON DICCIONARIOS",
        font=("Arial", 14, "bold"),
        bg=COLORES["fondo_secundario"],
        fg=COLORES["texto"]
    ).pack(pady=10)
    
    # Crear un diccionario de ejemplo
    diccionario_ejemplo = {
        "nombre": "Carlos",
        "edad": "16",
        "ciudad": "Madrid",
        "hobbie": "Programación"
    }
    
    def mostrar_operacion(operacion):
        """Muestra el resultado de diferentes operaciones"""
        resultado = ""
        
        if operacion == "keys":
            resultado = "claves = diccionario.keys()\n"
            resultado += f"Resultado: {list(diccionario_ejemplo.keys())}"
        
        elif operacion == "values":
            resultado = "valores = diccionario.values()\n"
            resultado += f"Resultado: {list(diccionario_ejemplo.values())}"
        
        elif operacion == "items":
            resultado = "elementos = diccionario.items()\n"
            resultado += f"Resultado: {list(diccionario_ejemplo.items())}"
        
        elif operacion == "get":
            resultado = "edad = diccionario.get('edad', 'No encontrado')\n"
            resultado += f"Resultado: {diccionario_ejemplo.get('edad', 'No encontrado')}"
        
        elif operacion == "update":
            diccionario_copia = diccionario_ejemplo.copy()
            nuevos_datos = {"curso": "1º Bachillerato", "nota": "A"}
            diccionario_copia.update(nuevos_datos)
            resultado = "diccionario.update(nuevos_datos)\n"
            resultado += f"Resultado: {diccionario_copia}"
        
        elif operacion == "clear":
            diccionario_copia = diccionario_ejemplo.copy()
            diccionario_copia.clear()
            resultado = "diccionario.clear()\n"
            resultado += f"Resultado: {diccionario_copia}"
        
        # Mostrar resultado
        ventana_resultado = tk.Toplevel(ventana_principal)
        ventana_resultado.title("Resultado de la Operación")
        ventana_resultado.geometry("500x200")
        ventana_resultado.configure(bg=COLORES["fondo_principal"])
        ventana_resultado.resizable(False, False)
        
        tk.Label(
            ventana_resultado,
            text="📋 RESULTADO",
            font=("Arial", 12, "bold"),
            bg=COLORES["fondo_principal"],
            fg=COLORES["texto"]
        ).pack(pady=10)
        
        tk.Label(
            ventana_resultado,
            text=resultado,
            font=("Consolas", 10),
            bg="#ECF0F1",
            fg=COLORES["texto_oscuro"],
            justify="left",
            wraplength=450
        ).pack(pady=10, padx=20)
    
    # Botones para cada operación
    operaciones = [
        (".keys() - Obtener claves", "keys"),
        (".values() - Obtener valores", "values"),
        (".items() - Obtener pares", "items"),
        (".get() - Obtener valor seguro", "get"),
        (".update() - Actualizar", "update"),
        (".clear() - Limpiar", "clear")
    ]
    
    frame_botones = tk.Frame(frame_contenido, bg=COLORES["fondo_secundario"])
    frame_botones.pack(pady=10)
    
    for i, (texto, op) in enumerate(operaciones):
        btn = crear_boton_con_hover(frame_botones, texto, 
                                   lambda o=op: mostrar_operacion(o), 
                                   width=30)
        btn.grid(row=i//2, column=i%2, padx=10, pady=5)

# ============================================
# FUNCIONES PARA CONJUNTOS
# ============================================

def mostrar_conjunto_info():
    """Muestra información básica sobre conjuntos"""
    limpiar_frame(frame_contenido)
    
    tk.Label(
        frame_contenido,
        text="🔢 ¿QUÉ ES UN CONJUNTO?",
        font=("Arial", 16, "bold"),
        bg=COLORES["fondo_secundario"],
        fg=COLORES["texto"]
    ).pack(pady=10)
    
    explicacion = """
Un conjunto en Python es como un conjunto matemático:
- Almacena elementos ÚNICOS (sin duplicados)
- Los elementos NO tienen orden específico
- Ideal para eliminar duplicados
- Soporta operaciones de conjuntos (unión, intersección, etc.)

Ejemplo: 
materias = {"Matemáticas", "Física", "Química", "Matemáticas"}
Resultado: {"Matemáticas", "Física", "Química"} 
(nota: "Matemáticas" solo aparece una vez)
"""
    
    tk.Label(
        frame_contenido,
        text=explicacion,
        font=("Arial", 11),
        bg=COLORES["fondo_secundario"],
        fg=COLORES["texto"],
        justify="left",
        wraplength=550
    ).pack(pady=10, padx=20)

def crear_conjunto_interactivo():
    """Interfaz para crear y manipular conjuntos"""
    limpiar_frame(frame_contenido)
    
    # Variable para almacenar el conjunto
    conjunto = set()
    
    # Frame para entrada de datos
    frame_entrada = tk.Frame(frame_contenido, bg=COLORES["fondo_secundario"])
    frame_entrada.pack(pady=10)
    
    tk.Label(
        frame_entrada,
        text="CREA TU CONJUNTO",
        font=("Arial", 14, "bold"),
        bg=COLORES["fondo_secundario"],
        fg=COLORES["texto"]
    ).grid(row=0, column=0, columnspan=2, pady=10)
    
    # Campo para elemento
    tk.Label(frame_entrada, text="Elemento:", bg=COLORES["fondo_secundario"], 
             fg=COLORES["texto"]).grid(row=1, column=0, padx=5)
    entry_elemento = tk.Entry(frame_entrada, width=30, font=("Arial", 10))
    entry_elemento.grid(row=1, column=1, padx=5)
    
    # Área para mostrar el conjunto
    text_area = tk.Text(
        frame_contenido,
        height=8,
        width=60,
        font=("Consolas", 10),
        bg="#ECF0F1",
        fg=COLORES["texto_oscuro"]
    )
    text_area.pack(pady=10, padx=20)
    text_area.insert("1.0", "Tu conjunto aparecerá aquí...")
    text_area.config(state="disabled")
    
    def agregar_elemento():
        """Agrega un elemento al conjunto"""
        elemento = entry_elemento.get().strip()
        
        if not elemento:
            messagebox.showwarning("Advertencia", "El elemento no puede estar vacío")
            return
        
        tamaño_anterior = len(conjunto)
        conjunto.add(elemento)
        entry_elemento.delete(0, tk.END)
        
        if len(conjunto) == tamaño_anterior:
            messagebox.showinfo("Info", f"El elemento '{elemento}' ya existe en el conjunto")
        
        actualizar_conjunto()
    
    def eliminar_elemento():
        """Elimina un elemento del conjunto"""
        elemento = entry_elemento.get().strip()
        
        if not elemento:
            messagebox.showwarning("Advertencia", "Ingresa un elemento para eliminar")
            return
        
        if elemento in conjunto:
            conjunto.remove(elemento)
            messagebox.showinfo("Éxito", f"Elemento '{elemento}' eliminado")
            entry_elemento.delete(0, tk.END)
        else:
            messagebox.showerror("Error", f"El elemento '{elemento}' no existe")
        
        actualizar_conjunto()
    
    def limpiar_conjunto():
        """Limpia todos los elementos del conjunto"""
        conjunto.clear()
        messagebox.showinfo("Info", "Conjunto limpiado")
        actualizar_conjunto()
    
    def actualizar_conjunto():
        """Actualiza la visualización del conjunto"""
        text_area.config(state="normal")
        text_area.delete("1.0", tk.END)
        
        if conjunto:
            elementos = list(conjunto)
            for i, elemento in enumerate(elementos, 1):
                text_area.insert(tk.END, f"{i}. {elemento}\n")
        else:
            text_area.insert("1.0", "El conjunto está vacío")
        
        text_area.config(state="disabled")
    
    # Botones de acción
    frame_botones = tk.Frame(frame_contenido, bg=COLORES["fondo_secundario"])
    frame_botones.pack(pady=10)
    
    crear_boton_con_hover(frame_botones, "➕ Agregar", agregar_elemento, 
                         bg_color=COLORES["exito"], width=15).pack(side="left", padx=5)
    crear_boton_con_hover(frame_botones, "🗑️ Eliminar", eliminar_elemento, 
                         bg_color="#E74C3C", width=15).pack(side="left", padx=5)
    crear_boton_con_hover(frame_botones, "🧹 Limpiar Todo", limpiar_conjunto, 
                         width=15).pack(side="left", padx=5)

def operaciones_conjuntos():
    """Demuestra operaciones comunes con conjuntos"""
    limpiar_frame(frame_contenido)
    
    tk.Label(
        frame_contenido,
        text="OPERACIONES DE CONJUNTOS",
        font=("Arial", 14, "bold"),
        bg=COLORES["fondo_secundario"],
        fg=COLORES["texto"]
    ).pack(pady=10)
    
    # Crear conjuntos de ejemplo
    conjunto_A = {"Matemáticas", "Física", "Química", "Historia"}
    conjunto_B = {"Matemáticas", "Lengua", "Historia", "Biología"}
    
    def mostrar_operacion_conjuntos(operacion):
        """Muestra el resultado de diferentes operaciones de conjuntos"""
        resultado = f"Conjunto A: {sorted(conjunto_A)}\n"
        resultado += f"Conjunto B: {sorted(conjunto_B)}\n\n"
        
        if operacion == "union":
            resultado += "A | B (UNIÓN): Elementos en A o en B\n"
            resultado += f"Resultado: {sorted(conjunto_A.union(conjunto_B))}"
        
        elif operacion == "interseccion":
            resultado += "A & B (INTERSECCIÓN): Elementos en A y en B\n"
            resultado += f"Resultado: {sorted(conjunto_A.intersection(conjunto_B))}"
        
        elif operacion == "diferencia":
            resultado += "A - B (DIFERENCIA): Elementos en A pero no en B\n"
            resultado += f"Resultado: {sorted(conjunto_A.difference(conjunto_B))}"
        
        elif operacion == "diferencia_simetrica":
            resultado += "A ^ B (DIFERENCIA SIMÉTRICA): Elementos en A o B pero no en ambos\n"
            resultado += f"Resultado: {sorted(conjunto_A.symmetric_difference(conjunto_B))}"
        
        elif operacion == "subconjunto":
            es_subconjunto = conjunto_A.issubset(conjunto_B)
            resultado += f"A ⊆ B (SUBCONJUNTO): ¿A es subconjunto de B?\n"
            resultado += f"Resultado: {'Sí' if es_subconjunto else 'No'}"
        
        # Mostrar resultado
        ventana_resultado = tk.Toplevel(ventana_principal)
        ventana_resultado.title("Resultado de la Operación")
        ventana_resultado.geometry("500x250")
        ventana_resultado.configure(bg=COLORES["fondo_principal"])
        ventana_resultado.resizable(False, False)
        
        tk.Label(
            ventana_resultado,
            text="📊 RESULTADO DE OPERACIÓN",
            font=("Arial", 12, "bold"),
            bg=COLORES["fondo_principal"],
            fg=COLORES["texto"]
        ).pack(pady=10)
        
        tk.Label(
            ventana_resultado,
            text=resultado,
            font=("Consolas", 10),
            bg="#ECF0F1",
            fg=COLORES["texto_oscuro"],
            justify="left",
            wraplength=450
        ).pack(pady=10, padx=20)
    
    # Botones para cada operación
    operaciones = [
        ("Unión (A | B)", "union"),
        ("Intersección (A & B)", "interseccion"),
        ("Diferencia (A - B)", "diferencia"),
        ("Diferencia Simétrica (A ^ B)", "diferencia_simetrica"),
        ("Subconjunto (A ⊆ B)", "subconjunto")
    ]
    
    frame_botones = tk.Frame(frame_contenido, bg=COLORES["fondo_secundario"])
    frame_botones.pack(pady=10)
    
    for i, (texto, op) in enumerate(operaciones):
        btn = crear_boton_con_hover(frame_botones, texto, 
                                   lambda o=op: mostrar_operacion_conjuntos(o), 
                                   width=25)
        btn.pack(pady=5)

# ============================================
# FUNCIONES PARA EJEMPLOS PRÁCTICOS
# ============================================

def ejemplo_aplicado():
    """Muestra ejemplos prácticos de uso de diccionarios y conjuntos"""
    limpiar_frame(frame_contenido)
    
    tk.Label(
        frame_contenido,
        text="🎯 EJEMPLOS PRÁCTICOS",
        font=("Arial", 16, "bold"),
        bg=COLORES["fondo_secundario"],
        fg=COLORES["texto"]
    ).pack(pady=10)
    
    # Crear notebook para pestañas
    notebook = ttk.Notebook(frame_contenido)
    notebook.pack(fill="both", expand=True, padx=20, pady=10)
    
    # Estilo para las pestañas
    style = ttk.Style()
    style.configure("TNotebook", background=COLORES["fondo_secundario"])
    style.configure("TNotebook.Tab", 
                   background=COLORES["acento"],
                   foreground=COLORES["texto"],
                   font=("Arial", 10, "bold"),
                   padding=[10, 5])
    style.map("TNotebook.Tab", 
             background=[("selected", COLORES["acento_hover"])])
    
    # Ejemplo 1: Agenda de contactos (diccionario)
    frame_agenda = tk.Frame(notebook, bg=COLORES["fondo_secundario"])
    notebook.add(frame_agenda, text="📒 Agenda de Contactos")
    
    explicacion1 = """
AGENDA DE CONTACTOS (Diccionario)

Cada contacto tiene:
- Nombre (clave)
- Teléfono (valor)

Operaciones útiles:
1. Agregar contacto: agenda[nombre] = telefono
2. Buscar: agenda.get(nombre, "No encontrado")
3. Listar todos: agenda.items()
4. Eliminar: del agenda[nombre]

Ejemplo práctico:
"""
    
    tk.Label(
        frame_agenda,
        text=explicacion1,
        font=("Arial", 11),
        bg=COLORES["fondo_secundario"],
        fg=COLORES["texto"],
        justify="left",
        wraplength=550
    ).pack(pady=10, padx=20)
    
    # Mostrar código de ejemplo
    codigo_agenda = """
# Crear agenda
agenda = {}

# Agregar contactos
agenda["Ana"] = "600123456"
agenda["Carlos"] = "600654321"
agenda["María"] = "600987654"

# Buscar un contacto
telefono_ana = agenda.get("Ana", "No encontrado")

# Mostrar todos los contactos
for nombre, telefono in agenda.items():
    print(f"{nombre}: {telefono}")
"""
    
    text_codigo1 = tk.Text(
        frame_agenda,
        height=12,
        width=60,
        font=("Consolas", 10),
        bg="#2C3E50",
        fg="white"
    )
    text_codigo1.pack(pady=10, padx=20)
    text_codigo1.insert("1.0", codigo_agenda)
    text_codigo1.config(state="disabled")
    
    # Ejemplo 2: Sistema de votación (conjunto)
    frame_votacion = tk.Frame(notebook, bg=COLORES["fondo_secundario"])
    notebook.add(frame_votacion, text="🗳️ Sistema de Votación")
    
    explicacion2 = """
SISTEMA DE VOTACIÓN (Conjunto)

Para evitar votos duplicados:
- Cada votante se identifica con un ID único
- Usamos un conjunto para almacenar IDs
- Los conjuntos automáticamente eliminan duplicados

Beneficios:
✓ No hay votos duplicados
✓ Verificación rápida de votante
✓ Fácil limpieza de datos
"""
    
    tk.Label(
        frame_votacion,
        text=explicacion2,
        font=("Arial", 11),
        bg=COLORES["fondo_secundario"],
        fg=COLORES["texto"],
        justify="left",
        wraplength=550
    ).pack(pady=10, padx=20)
    
    # Mostrar código de ejemplo
    codigo_votacion = """
# Conjunto para votantes registrados
votantes = set()

# Registrar votos
votantes.add("ID123")  # Voto de Juan
votantes.add("ID456")  # Voto de Ana
votantes.add("ID123")  # Intento de voto duplicado (ignorado)

# Verificar si alguien ya votó
if "ID123" in votantes:
    print("Este votante ya ejerció su derecho")
else:
    print("Puede votar")

# Total de votantes únicos
print(f"Total votantes: {len(votantes)}")
"""
    
    text_codigo2 = tk.Text(
        frame_votacion,
        height=12,
        width=60,
        font=("Consolas", 10),
        bg="#2C3E50",
        fg="white"
    )
    text_codigo2.pack(pady=10, padx=20)
    text_codigo2.insert("1.0", codigo_votacion)
    text_codigo2.config(state="disabled")
    
    # Ejemplo 3: Inventario (diccionario anidado)
    frame_inventario = tk.Frame(notebook, bg=COLORES["fondo_secundario"])
    notebook.add(frame_inventario, text="📦 Sistema de Inventario")
    
    explicacion3 = """
INVENTARIO (Diccionario Anidado)

Estructura compleja:
- Producto (clave principal)
- Detalles (valor como otro diccionario)

Ventajas:
✓ Organización jerárquica
✓ Acceso rápido a información específica
✓ Fácil expansión con nuevos campos
"""
    
    tk.Label(
        frame_inventario,
        text=explicacion3,
        font=("Arial", 11),
        bg=COLORES["fondo_secundario"],
        fg=COLORES["texto"],
        justify="left",
        wraplength=550
    ).pack(pady=10, padx=20)
    
    # Mostrar código de ejemplo
    codigo_inventario = """
# Inventario con diccionario anidado
inventario = {
    "laptop": {
        "precio": 899.99,
        "cantidad": 15,
        "categoria": "electrónica"
    },
    "libro": {
        "precio": 19.99,
        "cantidad": 50,
        "categoria": "papelería"
    }
}

# Acceder a información específica
precio_laptop = inventario["laptop"]["precio"]

# Agregar nuevo producto
inventario["tablet"] = {
    "precio": 299.99,
    "cantidad": 25,
    "categoria": "electrónica"
}

# Mostrar inventario completo
for producto, detalles in inventario.items():
    print(f"{producto}: {detalles}")
"""
    
    text_codigo3 = tk.Text(
        frame_inventario,
        height=12,
        width=60,
        font=("Consolas", 10),
        bg="#2C3E50",
        fg="white"
    )
    text_codigo3.pack(pady=10, padx=20)
    text_codigo3.insert("1.0", codigo_inventario)
    text_codigo3.config(state="disabled")

# ============================================
# FUNCIONES PARA QUIZ INTERACTIVO
# ============================================

def iniciar_quiz():
    """Inicia un quiz interactivo sobre diccionarios y conjuntos"""
    limpiar_frame(frame_contenido)
    
    # Preguntas y respuestas
    preguntas = [
        {
            "pregunta": "¿Cuál es la principal característica de las claves en un diccionario?",
            "opciones": ["Son numéricas", "Son únicas", "Son opcionales", "Son mutables"],
            "respuesta": 1,
            "explicacion": "Las claves en un diccionario deben ser ÚNICAS. No pueden haber dos claves iguales."
        },
        {
            "pregunta": "¿Qué operación usarías para eliminar duplicados de una lista?",
            "opciones": ["lista.unique()", "set(lista)", "lista.remove_duplicates()", "dict.fromkeys(lista)"],
            "respuesta": 1,
            "explicacion": "Convertir a conjunto: set(lista). Los conjuntos automáticamente eliminan duplicados."
        },
        {
            "pregunta": "¿Cómo accedes al valor asociado a la clave 'edad' en un diccionario?",
            "opciones": ["diccionario[0]", "diccionario.get('edad')", "diccionario.ages()", "diccionario('edad')"],
            "respuesta": 1,
            "explicacion": "diccionario.get('edad') es la forma segura. También puedes usar diccionario['edad']."
        },
        {
            "pregunta": "¿Qué retorna la operación A & B con conjuntos?",
            "opciones": ["Unión", "Diferencia", "Intersección", "Complemento"],
            "respuesta": 2,
            "explicacion": "A & B retorna la INTERSECCIÓN: elementos que están en AMBOS conjuntos."
        },
        {
            "pregunta": "¿Cuál es la diferencia principal entre lista y conjunto?",
            "opciones": ["El conjunto es más rápido", "El conjunto no permite duplicados", 
                        "La lista usa más memoria", "El conjunto tiene índice"],
            "respuesta": 1,
            "explicacion": "La diferencia principal es que los CONJUNTOS NO PERMITEN DUPLICADOS."
        }
    ]
    
    # Variables del quiz
    pregunta_actual = 0
    puntaje = 0
    respuestas_usuario = []
    
    def mostrar_pregunta():
        """Muestra la pregunta actual"""
        nonlocal pregunta_actual
        
        # Limpiar frame
        for widget in frame_contenido.winfo_children():
            widget.destroy()
        
        if pregunta_actual >= len(preguntas):
            mostrar_resultado()
            return
        
        pregunta = preguntas[pregunta_actual]
        
        # Mostrar número de pregunta
        tk.Label(
            frame_contenido,
            text=f"Pregunta {pregunta_actual + 1} de {len(preguntas)}",
            font=("Arial", 12, "bold"),
            bg=COLORES["fondo_secundario"],
            fg=COLORES["acento"]
        ).pack(pady=10)
        
        # Mostrar la pregunta
        tk.Label(
            frame_contenido,
            text=pregunta["pregunta"],
            font=("Arial", 13, "bold"),
            bg=COLORES["fondo_secundario"],
            fg=COLORES["texto"],
            wraplength=550,
            justify="center"
        ).pack(pady=20, padx=20)
        
        # Variable para selección
        seleccion = tk.IntVar(value=-1)
        
        # Crear frame para opciones
        frame_opciones = tk.Frame(frame_contenido, bg=COLORES["fondo_secundario"])
        frame_opciones.pack(pady=10)
        
        # Mostrar opciones de respuesta
        for i, opcion in enumerate(pregunta["opciones"]):
            rb = tk.Radiobutton(
                frame_opciones,
                text=opcion,
                variable=seleccion,
                value=i,
                font=("Arial", 11),
                bg=COLORES["fondo_secundario"],
                fg=COLORES["texto"],
                selectcolor=COLORES["acento"],
                activebackground=COLORES["fondo_secundario"],
                cursor="hand2"
            )
            rb.pack(anchor="w", pady=5)
        
        def siguiente_pregunta():
            """Avanza a la siguiente pregunta"""
            nonlocal pregunta_actual, puntaje
            
            if seleccion.get() == -1:
                messagebox.showwarning("Advertencia", "Por favor, selecciona una respuesta")
                return
            
            # Guardar respuesta
            respuestas_usuario.append(seleccion.get())
            
            # Verificar si es correcta
            if seleccion.get() == pregunta["respuesta"]:
                puntaje += 1
            
            pregunta_actual += 1
            mostrar_pregunta()
        
        # Botón para continuar
        btn_siguiente = crear_boton_con_hover(
            frame_contenido,
            "✅ Siguiente Pregunta",
            siguiente_pregunta,
            bg_color=COLORES["exito"],
            width=25
        )
        btn_siguiente.pack(pady=20)
    
    def mostrar_resultado():
        """Muestra los resultados del quiz"""
        # Limpiar frame
        for widget in frame_contenido.winfo_children():
            widget.destroy()
        
        # Calcular porcentaje
        porcentaje = (puntaje / len(preguntas)) * 100
        
        # Mostrar resultado
        tk.Label(
            frame_contenido,
            text="🎉 ¡QUIZ COMPLETADO! 🎉",
            font=("Arial", 18, "bold"),
            bg=COLORES["fondo_secundario"],
            fg=COLORES["exito"]
        ).pack(pady=20)
        
        tk.Label(
            frame_contenido,
            text=f"Puntuación: {puntaje}/{len(preguntas)} ({porcentaje:.1f}%)",
            font=("Arial", 16, "bold"),
            bg=COLORES["fondo_secundario"],
            fg=COLORES["texto"]
        ).pack(pady=10)
        
        # Mensaje según puntuación
        if porcentaje >= 80:
            mensaje = "¡Excelente! Dominas los conceptos de diccionarios y conjuntos."
        elif porcentaje >= 60:
            mensaje = "¡Buen trabajo! Tienes un buen entendimiento de los conceptos."
        else:
            mensaje = "¡Sigue practicando! Revisa los ejemplos y vuelve a intentarlo."
        
        tk.Label(
            frame_contenido,
            text=mensaje,
            font=("Arial", 12),
            bg=COLORES["fondo_secundario"],
            fg=COLORES["texto"],
            wraplength=500,
            justify="center"
        ).pack(pady=20, padx=20)
        
        # Botón para ver explicaciones
        def ver_explicaciones():
            ventana_explicaciones = tk.Toplevel(ventana_principal)
            ventana_explicaciones.title("Explicaciones del Quiz")
            ventana_explicaciones.geometry("600x400")
            ventana_explicaciones.configure(bg=COLORES["fondo_principal"])
            
            texto_explicaciones = tk.Text(
                ventana_explicaciones,
                font=("Arial", 11),
                bg="#ECF0F1",
                fg=COLORES["texto_oscuro"],
                wrap="word",
                padx=10,
                pady=10
            )
            texto_explicaciones.pack(fill="both", expand=True, padx=10, pady=10)
            
            for i, pregunta in enumerate(preguntas):
                texto_explicaciones.insert(tk.END, f"Pregunta {i+1}: {pregunta['pregunta']}\n")
                texto_explicaciones.insert(tk.END, f"Tu respuesta: {pregunta['opciones'][respuestas_usuario[i]]}\n")
                texto_explicaciones.insert(tk.END, f"Respuesta correcta: {pregunta['opciones'][pregunta['respuesta']]}\n")
                texto_explicaciones.insert(tk.END, f"Explicación: {pregunta['explicacion']}\n")
                texto_explicaciones.insert(tk.END, "-"*50 + "\n\n")
            
            texto_explicaciones.config(state="disabled")
        
        # Frame para botones
        frame_botones = tk.Frame(frame_contenido, bg=COLORES["fondo_secundario"])
        frame_botones.pack(pady=20)
        
        crear_boton_con_hover(
            frame_botones,
            "📖 Ver Explicaciones",
            ver_explicaciones,
            width=20
        ).pack(side="left", padx=10)
        
        crear_boton_con_hover(
            frame_botones,
            "🔄 Reiniciar Quiz",
            iniciar_quiz,
            bg_color=COLORES["exito"],
            width=20
        ).pack(side="left", padx=10)
        
        crear_boton_con_hover(
            frame_botones,
            "🏠 Volver al Menú",
            mostrar_bienvenida,
            bg_color=COLORES["acento_hover"],
            width=20
        ).pack(side="left", padx=10)
    
    mostrar_pregunta()

# ============================================
# FUNCIÓN PRINCIPAL Y CONFIGURACIÓN DE VENTANA
# ============================================

def mostrar_bienvenida():
    """Muestra la pantalla de bienvenida"""
    limpiar_frame(frame_contenido)
    
    # Título principal
    tk.Label(
        frame_contenido,
        text="🐍 APRENDE PYTHON: DICCIONARIOS Y CONJUNTOS",
        font=("Arial", 20, "bold"),
        bg=COLORES["fondo_secundario"],
        fg=COLORES["texto"]
    ).pack(pady=30)
    
    # Descripción
    descripcion = """
¡Bienvenido al Juego Educativo de Python!

Este programa te ayudará a entender dos estructuras de datos fundamentales:

📚 DICCIONARIOS: Almacenan datos en pares clave-valor
🔢 CONJUNTOS: Almacenan elementos únicos sin orden específico

Selecciona una opción del menú para comenzar tu aprendizaje interactivo.
"""
    
    tk.Label(
        frame_contenido,
        text=descripcion,
        font=("Arial", 12),
        bg=COLORES["fondo_secundario"],
        fg=COLORES["texto"],
        justify="center",
        wraplength=600
    ).pack(pady=20, padx=20)
    
    # Frame para menú principal
    frame_menu = tk.Frame(frame_contenido, bg=COLORES["fondo_secundario"])
    frame_menu.pack(pady=30)
    
    # Botones del menú principal (izquierda: Diccionarios, derecha: Conjuntos)
    botones_menu = [
        ("📘 Introducción a Diccionarios", mostrar_diccionario_info, COLORES["acento"]),
        ("🔧 Crear Diccionario Interactivo", crear_diccionario_interactivo, COLORES["acento"]),
        ("⚙️ Operaciones con Diccionarios", operaciones_diccionario, COLORES["acento"]),
        ("📗 Introducción a Conjuntos", mostrar_conjunto_info, "#9B59B6"),
        ("🔨 Crear Conjunto Interactivo", crear_conjunto_interactivo, "#9B59B6"),
        ("🛠️ Operaciones con Conjuntos", operaciones_conjuntos, "#9B59B6"),
        ("🎯 Ejemplos Prácticos", ejemplo_aplicado, COLORES["exito"]),
        ("🧠 Quiz Interactivo", iniciar_quiz, "#E67E22"),
    ]
    
    # Organizar botones en dos columnas
    for i, (texto, comando, color) in enumerate(botones_menu):
        if i < 4:  # Primera columna
            col = 0
            fila = i
        else:  # Segunda columna
            col = 1
            fila = i - 4
        
        btn = crear_boton_con_hover(
            frame_menu,
            texto,
            comando,
            bg_color=color,
            width=30
        )
        btn.grid(row=fila, column=col, padx=10, pady=5, sticky="ew")
    
    # Información del autor
    tk.Label(
        frame_contenido,
        text="Desarrollado para estudiantes de Bachillerato\n© 2024 - Juego Educativo Python",
        font=("Arial", 9, "italic"),
        bg=COLORES["fondo_secundario"],
        fg=COLORES["texto"],
        justify="center"
    ).pack(pady=20)

# ============================================
# CONFIGURACIÓN DE LA VENTANA PRINCIPAL
# ============================================

# Crear ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Juego Educativo: Diccionarios y Conjuntos en Python")
ventana_principal.configure(bg=COLORES["fondo_principal"])

# Centrar ventana en pantalla
ancho_ventana = 800
alto_ventana = 700
ancho_pantalla = ventana_principal.winfo_screenwidth()
alto_pantalla = ventana_principal.winfo_screenheight()
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2) - 50
ventana_principal.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
ventana_principal.resizable(False, False)

# Crear frame para la barra superior
frame_superior = tk.Frame(
    ventana_principal,
    bg=COLORES["fondo_secundario"],
    height=80
)
frame_superior.pack(fill="x")
frame_superior.pack_propagate(False)

# Título en barra superior
tk.Label(
    frame_superior,
    text="🎓 JUEGO EDUCATIVO DE PYTHON",
    font=("Arial", 18, "bold"),
    bg=COLORES["fondo_secundario"],
    fg=COLORES["texto"]
).pack(side="left", padx=30, pady=20)

# Botón de inicio en barra superior
btn_inicio = crear_boton_con_hover(
    frame_superior,
    "🏠 Inicio",
    mostrar_bienvenida,
    bg_color=COLORES["acento"],
    width=15
)
btn_inicio.pack(side="right", padx=30, pady=20)

# Crear frame para contenido principal
frame_contenido = tk.Frame(
    ventana_principal,
    bg=COLORES["fondo_secundario"]
)
frame_contenido.pack(fill="both", expand=True, padx=20, pady=20)

# Mostrar pantalla de bienvenida al iniciar
mostrar_bienvenida()

# Iniciar el bucle principal de la aplicación
ventana_principal.mainloop()