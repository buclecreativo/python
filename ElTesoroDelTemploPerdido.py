"""
 AVENTURA MATEMÁTICA: EL TESORO DEL TEMPLO PERDIDO
 Juego educativo para estudiantes de bachillerato
 Autor: Experto en Desarrollo de Software Educativo

 ------------------------------------------------------------
 BIENVENIDA E INSTRUCCIONES
 ------------------------------------------------------------
"""
print("=" * 50)
print("AVENTURA MATEMÁTICA: EL TESORO DEL TEMPLO PERDIDO")
print("=" * 50)
print()
print("¡Bienvenido, aventurero!")
print("Has llegado al antiguo templo matemático donde se esconde un tesoro legendario.")
print("Para encontrarlo, deberás resolver acertijos matemáticos en cada sala.")
print("Cada respuesta correcta te llevará más cerca del tesoro.")
print()

# ------------------------------------------------------------
# VARIABLES DEL JUEGO
# ------------------------------------------------------------

# Puntos de vida del jugador (empieza con 3)
vida_jugador = 3

# Control de progreso (0: inicio, 1: primera sala, 2: segunda sala, 3: tesoro)
progreso = 0

# Variable para almacenar respuestas del jugador
respuesta_jugador = ""

# ------------------------------------------------------------
# SALA DE ENTRADA - PRIMER DESAFÍO
# ------------------------------------------------------------

print("_" * 50)
print("SALA DE ENTRADA: LA PUERTA NUMÉRICA")
print("_" * 50)
print()
print("Ante ti hay una puerta de piedra con una inscripción:")
print("'Para entrar, resuelve: 15 + 7 × 2'")
print("Recuerda: primero multiplicaciones, luego sumas.")
print()

# Pedir respuesta al jugador
respuesta_jugador = input("Tu respuesta: ")

# Verificar respuesta
if respuesta_jugador == "29":
    print("¡Correcto! 15 + 7 × 2 = 15 + 14 = 29")
    print("La puerta se abre lentamente...")
    progreso = 1  # Avanzar a la siguiente sala
else:
    print("Incorrecto. La respuesta correcta es 29.")
    print("15 + 7 × 2 = 15 + 14 = 29")
    vida_jugador = vida_jugador - 1  # Perder un punto de vida
    print(f"Pierdes un punto de vida. Te quedan {vida_jugador} puntos.")
    progreso = 1  # Aún puede continuar, pero con menos vida

print()
print("Avanzas a la siguiente sala.")
print()

# ------------------------------------------------------------
# SEGUNDA SALA - SEGUNDO DESAFÍO
# ------------------------------------------------------------

if progreso == 1:
    print("_" * 50)
    print("SALA DEL PUENTE: EL ACERTIJO GEOMÉTRICO")
    print("_" * 50)
    print()
    print("Un profundo foso bloquea tu camino.")
    print("Solo hay un puente que se activa con la respuesta correcta.")
    print()
    print("Enunciado: Un triángulo tiene lados de 3cm, 4cm y 5cm.")
    print("¿Es un triángulo rectángulo? (responde 'si' o 'no')")
    print("Pista: Recuerda el teorema de Pitágoras: a² + b² = c²")
    print()
    
    # Pedir respuesta al jugador
    respuesta_jugador = input("Tu respuesta: ")
    
    # Verificar respuesta
    if respuesta_jugador.lower() == "si":
        print("¡Correcto! 3² + 4² = 9 + 16 = 25 = 5²")
        print("El puente se activa y puedes cruzarlo.")
        progreso = 2  # Avanzar a la siguiente sala
    else:
        print("Incorrecto. 3² + 4² = 9 + 16 = 25, que es igual a 5².")
        print("Por lo tanto, SÍ es un triángulo rectángulo.")
        vida_jugador = vida_jugador - 1  # Perder un punto de vida
        print(f"Pierdes un punto de vida. Te quedan {vida_jugador} puntos.")
        
        # Verificar si el jugador todavía tiene vida
        if vida_jugador <= 0:
            progreso = -1  # Juego terminado (derrota)
        else:
            progreso = 2  # Aún puede continuar
    
    print()
    print("Continuas tu aventura.")
    print()

# ------------------------------------------------------------
# TERCERA SALA - TERCER DESAFÍO
# ------------------------------------------------------------

if progreso == 2:
    print("_" * 50)
    print("SALA FINAL: EL ENIGMA DEL TESORO")
    print("_" * 50)
    print()
    print("Has llegado a la cámara final. Ante ti hay tres cofres:")
    print("Cofre de Oro: 2x + 10 = 20")
    print("Cofre de Plata: 3y - 5 = 10")
    print("Cofre de Bronce: z/2 + 3 = 8")
    print()
    print("Solo uno contiene el tesoro verdadero.")
    print("Para saber cuál, resuelve las ecuaciones y encuentra:")
    print("¿Cuál es el valor de x + y + z?")
    print()
    
    # Pedir respuesta al jugador
    respuesta_jugador = input("Tu respuesta: ")
    
    # Verificar respuesta
    if respuesta_jugador == "30":
        print("¡Excelente! Resolvamos paso a paso:")
        print("Para el cofre de oro: 2x + 10 = 20 → 2x = 10 → x = 5")
        print("Para el cofre de plata: 3y - 5 = 10 → 3y = 15 → y = 5")
        print("Para el cofre de bronce: z/2 + 3 = 8 → z/2 = 5 → z = 10")
        print("x + y + z = 5 + 5 + 10 = 30")
        print()
        print("¡El cofre de bronce se abre revelando el TESORO!")
        progreso = 3  # Victoria
    else:
        print("Respuesta incorrecta. Veamos la solución:")
        print("Primera ecuación: 2x + 10 = 20 → 2x = 10 → x = 5")
        print("Segunda ecuación: 3y - 5 = 10 → 3y = 15 → y = 5")
        print("Tercera ecuación: z/2 + 3 = 8 → z/2 = 5 → z = 10")
        print("La suma es: 5 + 5 + 10 = 30")
        vida_jugador = vida_jugador - 1  # Perder un punto de vida
        print(f"Pierdes un punto de vida. Te quedan {vida_jugador} puntos.")
        
        # Verificar si el jugador todavía tiene vida
        if vida_jugador <= 0:
            progreso = -1  # Juego terminado (derrota)
        else:
            print("A pesar del error, el cofre de bronce se abre...")
            progreso = 3  # Aún puede ganar
    
    print()

# ------------------------------------------------------------
# FINAL DEL JUEGO - RESULTADOS
# ------------------------------------------------------------

print("=" * 50)
print("FIN DE LA AVENTURA")
print("=" * 50)
print()

if progreso == 3:
    # Victoria
    print("¡FELICIDADES, AVENTURERO!")
    print("Has encontrado el Tesoro del Templo Perdido.")
    print()
    
    if vida_jugador == 3:
        print("¡PERFECTO! Completaste la aventura sin perder puntos de vida.")
        print("Eres un verdadero maestro de las matemáticas.")
    elif vida_jugador == 2:
        print("Muy bien. Completaste la aventura con 2 puntos de vida.")
        print("Tienes buenos conocimientos matemáticos.")
    elif vida_jugador == 1:
        print("Completaste la aventura con 1 punto de vida.")
        print("Necesitas repasar algunos conceptos, pero lo lograste.")
    
    print()
    print("El tesoro contiene:")
    print("- Un antiguo libro de matemáticas")
    print("- Una calculadora de piedra preciosa")
    print("- El certificado de 'Aventurero Matemático'")
    
elif progreso == -1:
    # Derrota
    print("GAME OVER")
    print("Has perdido todos tus puntos de vida.")
    print()
    print("No te rindas. Vuelve a intentarlo repasando:")
    print("1. Orden de operaciones (PEMDAS)")
    print("2. Teorema de Pitágoras")
    print("3. Resolución de ecuaciones simples")
    print()
    print("¡La práctica hace al maestro!")

else:
    # Error inesperado
    print("El juego ha encontrado un estado inesperado.")
    print("Vuelve a ejecutarlo para una nueva aventura.")

print()
print("=" * 50)
print("Gracias por jugar a Aventura Matemática")
print("Desarrollado con fines educativos")
print("=" * 50)