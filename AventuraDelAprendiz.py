"""
AVENTURA DEL APRENDIZ
Un juego educativo de consola para estudiantes de bachillerato.
El jugador toma decisiones que afectan su camino de aprendizaje en programación.

 ============================================================================
 SECCIÓN 1: INTRODUCCIÓN Y CONFIGURACIÓN INICIAL
 ============================================================================
"""
# Variables del juego - representan el progreso del jugador
nombre_estudiante = ""
puntos_conocimiento = 0
nivel_programacion = 1
decision_correcta_1 = False
decision_correcta_2 = False
decision_correcta_3 = False

# Mensaje de bienvenida
print("=" * 50)
print("        AVENTURA DEL APRENDIZ")
print("=" * 50)
print("\n¡Bienvenido/a a tu viaje de aprendizaje en programación!")
print("En este juego, tomarás decisiones que afectarán tu progreso.")
print("Cada elección correcta te dará puntos de conocimiento.")
print("\n" + "-" * 50)

# El jugador ingresa su nombre
nombre_estudiante = input("¿Cuál es tu nombre? ")
print(f"\n¡Perfecto, {nombre_estudiante}! Comencemos la aventura.")

# ============================================================================
# SECCIÓN 2: PRIMER DESAFÍO - FUNDAMENTOS DE PROGRAMACIÓN
# ============================================================================

print("\n" + "=" * 50)
print("DESAFÍO 1: EL CONCEPTO FUNDAMENTAL")
print("=" * 50)
print("\nTe encuentras en tu primera clase de programación.")
print("El profesor explica sobre variables y constantes.")
print("\nTe pregunta: ¿Qué almacena una variable en programación?")

# Opciones para el primer desafío
print("\nOpciones:")
print("1. Una dirección de memoria fija que no puede cambiar")
print("2. Un espacio en memoria que almacena datos que pueden cambiar")
print("3. Un comando que ejecuta una acción específica")
print("4. Un tipo de bucle infinito")

# El jugador toma su primera decisión
opcion_1 = input("\nElige una opción (1-4): ")

# Evaluamos la primera decisión usando match
match opcion_1:
    case "2":
        print("\n¡CORRECTO! Una variable es un espacio en memoria que")
        print("almacena datos que pueden cambiar durante la ejecución.")
        print("Ganas 10 puntos de conocimiento y subes al nivel 2.")
        puntos_conocimiento = 10
        nivel_programacion = 2
        decision_correcta_1 = True
    case "1":
        print("\nIncorrecto. Estás describiendo una constante, no una variable.")
        print("Las variables sí pueden cambiar su valor durante la ejecución.")
    case "3":
        print("\nIncorrecto. Estás describiendo una función o método.")
        print("Una variable almacena datos, no ejecuta acciones.")
    case "4":
        print("\nIncorrecto. Un bucle infinito es una estructura de control,")
        print("no tiene relación directa con el concepto de variable.")
    case _:
        print("\nOpción no válida. Recuerda: en programación, la precisión")
        print("es importante. Debes elegir entre las opciones 1-4.")

# ============================================================================
# SECCIÓN 3: SEGUNDO DESAFÍO - ESTRUCTURAS DE CONTROL
# ============================================================================

print("\n" + "=" * 50)
print("DESAFÍO 2: TOMANDO DECISIONES")
print("=" * 50)
print(f"\n{nivel_programacion}. Ahora estudias estructuras condicionales.")
print("El profesor presenta un problema:")
print("\n'Un programa necesita verificar si un número es positivo,'")
print("'negativo o cero. ¿Qué estructura usarías?'")

# Opciones para el segundo desafío
print("\nOpciones:")
print("1. Un bucle for que itere desde 0 hasta el número")
print("2. Una declaración if-elif-else para cada caso")
print("3. Una función recursiva que se llame a sí misma")
print("4. Una lista que contenga todos los posibles resultados")

# El jugador toma su segunda decisión
opcion_2 = input("\nElige una opción (1-4): ")

# Evaluamos la segunda decisión usando match
match opcion_2:
    case "2":
        print("\n¡EXCELENTE! Las estructuras if-elif-else son ideales")
        print("para tomar decisiones basadas en condiciones.")
        print("Ganas 15 puntos de conocimiento.")
        puntos_conocimiento = puntos_conocimiento + 15
        
        # Actualizamos el nivel si es apropiado
        if puntos_conocimiento >= 20:
            nivel_programacion = 3
            print("¡Felicidades! Has alcanzado el nivel 3 de programación.")
        else:
            print("Tu nivel de programación se mantiene en el nivel", nivel_programacion)
        
        decision_correcta_2 = True
    case "1":
        print("\nIncorrecto. Un bucle for es para repetición, no para")
        print("evaluar condiciones una sola vez.")
    case "3":
        print("\nIncorrecto. La recursión es compleja para este caso simple")
        print("y no es la solución más eficiente.")
    case "4":
        print("\nIncorrecto. Una lista podría almacenar resultados,")
        print("pero no decide qué caso aplicar.")
    case _:
        print("\nOpción no válida. En programación, elegir la herramienta")
        print("correcta para cada problema es fundamental.")

# ============================================================================
# SECCIÓN 4: TERCER DESAFÍO - LÓGICA BOOLEANA
# ============================================================================

print("\n" + "=" * 50)
print("DESAFÍO 3: LÓGICA BOOLEANA")
print("=" * 50)
print(f"\nNivel actual: {nivel_programacion}")
print("Puntos de conocimiento: {puntos_conocimiento}")
print("\nEl profesor presenta un ejercicio de lógica booleana:")
print("\n'Si A = True y B = False, ¿cuál es el resultado de A and B?'")

# Opciones para el tercer desafío
print("\nOpciones:")
print("1. True")
print("2. False")
print("3. Error de sintaxis")
print("4. None")

# El jugador toma su tercera decisión
opcion_3 = input("\nElige una opción (1-4): ")

# Evaluamos la tercera decisión usando match
match opcion_3:
    case "2":
        print("\n¡PERFECTO! El operador 'and' solo devuelve True si")
        print("AMBOS operandos son True. Como B es False,")
        print("el resultado es False.")
        print("Ganas 20 puntos de conocimiento.")
        puntos_conocimiento = puntos_conocimiento + 20
        
        # Determinamos el nivel final basado en los puntos
        if puntos_conocimiento >= 40:
            nivel_programacion = 5
        elif puntos_conocimiento >= 30:
            nivel_programacion = 4
        elif puntos_conocimiento >= 20:
            nivel_programacion = 3
        elif puntos_conocimiento >= 10:
            nivel_programacion = 2
        else:
            nivel_programacion = 1
            
        decision_correcta_3 = True
    case "1":
        print("\nIncorrecto. Revisa la tabla de verdad del operador 'and':")
        print("True and True = True")
        print("True and False = False")
        print("False and True = False")
        print("False and False = False")
    case "3":
        print("\nIncorrecto. La expresión es sintácticamente válida.")
        print("Python puede evaluar 'True and False' sin errores.")
    case "4":
        print("\nIncorrecto. None es un valor especial en Python,")
        print("no el resultado de una operación booleana con valores conocidos.")
    case _:
        print("\nOpción no válida. Recuerda que en lógica booleana")
        print("solo hay dos valores posibles: True y False.")

# ============================================================================
# SECCIÓN 5: RESULTADOS FINALES Y RETROALIMENTACIÓN
# ============================================================================

print("\n" + "=" * 50)
print("        RESUMEN DE TU AVENTURA")
print("=" * 50)

# Mostramos estadísticas finales
print(f"\n¡Felicidades, {nombre_estudiante}!")
print("\nHas completado tu aventura de aprendizaje.")
print("\n" + "-" * 30)
print("ESTADÍSTICAS FINALES:")
print("-" * 30)
print(f"Puntos de conocimiento: {puntos_conocimiento}/45")
print(f"Nivel de programación alcanzado: {nivel_programacion}/5")
print(f"Decisiones correctas: {decision_correcta_1 + decision_correcta_2 + decision_correcta_3}/3")

# Determinamos el mensaje final basado en el rendimiento
print("\n" + "-" * 30)
print("EVALUACIÓN FINAL:")
print("-" * 30)

match nivel_programacion:
    case 5:
        print("¡ERES UN GENIO DE LA PROGRAMACIÓN!")
        print("Dominas los conceptos fundamentales.")
        print("Sigue así y serás un excelente programador/a.")
    case 4:
        print("¡EXCELENTE TRABAJO!")
        print("Tienes un sólido entendimiento de los conceptos básicos.")
        print("Con un poco más de práctica, alcanzarás la maestría.")
    case 3:
        print("¡BUEN TRABAJO!")
        print("Entiendes los conceptos principales.")
        print("Sigue practicando para fortalecer tu conocimiento.")
    case 2:
        print("¡VAS POR BUEN CAMINO!")
        print("Has comprendido algunos conceptos importantes.")
        print("Revisa los temas donde tuviste dificultades.")
    case _:
        print("¡PRIMEROS PASOS!")
        print("La programación requiere práctica constante.")
        print("No te rindas, revisa los conceptos y vuelve a intentarlo.")

# Mensaje final educativo
print("\n" + "=" * 50)
print("       CONSEJOS PARA SEGUIR APRENDIENDO")
print("=" * 50)
print("\n1. La programación se aprende practicando, no solo estudiando.")
print("2. Comete errores: son oportunidades para aprender.")
print("3. Divide problemas grandes en pequeños pasos manejables.")
print("4. La paciencia y persistencia son tus mejores aliadas.")
print("\n¡Gracias por jugar Aventura del Aprendiz!")
print("Esperamos que hayas disfrutado y aprendido.")