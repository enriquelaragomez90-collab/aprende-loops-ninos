"""
🐍 ¡Aprende Bucles con Python! 🐍
Un programa para niños que enseña qué son los bucles (loops).

Cómo usarlo:  python aprende_loops.py
"""

import random
import sys
import time

# Para que los emojis se vean bien en Windows
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


# ---------------------------------------------------------------
# Ayudantes
# ---------------------------------------------------------------

def pausa(segundos=0.4):
    time.sleep(segundos)


def titulo(texto):
    print()
    print("=" * 50)
    print(f"  {texto}")
    print("=" * 50)


def mostrar_codigo(codigo):
    print("\n👀 Este es el código que vamos a usar:\n")
    for linea in codigo.strip("\n").split("\n"):
        print("    " + linea)
    print("\n✨ Y esto es lo que pasa:\n")
    pausa(0.8)


def pedir_numero(mensaje, minimo, maximo):
    """Pide un número y no se rinde hasta que el niño escriba uno válido."""
    while True:
        respuesta = input(f"{mensaje} ({minimo}-{maximo}): ").strip()
        if respuesta.lstrip("-").isdigit():
            numero = int(respuesta)
            if minimo <= numero <= maximo:
                return numero
            print(f"🙈 ¡Ups! Tiene que ser entre {minimo} y {maximo}. ¡Intenta otra vez!")
        else:
            print("🙈 ¡Eso no es un número! Escribe solo números, por favor.")


def continuar():
    input("\n👉 Presiona ENTER para volver al menú...")


# ---------------------------------------------------------------
# Lecciones
# ---------------------------------------------------------------

def que_es_un_bucle():
    titulo("🤔 ¿Qué es un bucle?")
    print("""
Imagina que tu maestra te dice: "¡Salta 5 veces!" 🦘

Tú no necesitas que te lo diga 5 veces, ¿verdad?
Solo escuchas UNA instrucción y la REPITES.

¡Eso es un BUCLE! 🔁
Un bucle le dice a la computadora: "repite esto varias veces".

En Python hay dos bucles muy famosos:
  🔹 for   -> "repite esto un número de veces"
  🔹 while -> "repite esto MIENTRAS algo sea verdad"
""")
    input("👉 Presiona ENTER para ver a la computadora saltar...")
    mostrar_codigo("""
for salto in range(1, 6):
    print("¡Salto número", salto, "!")
""")
    for salto in range(1, 6):
        print("   🦘 ¡Salto número", salto, "!")
        pausa()
    print("\n🎉 ¡La computadora saltó 5 veces con solo 2 líneas de código!")
    continuar()


def for_con_numeros():
    titulo("🔢 Bucle FOR: contar números")
    print("range(1, N+1) significa: 'los números del 1 hasta N'.\n")
    n = pedir_numero("¿Hasta qué número quieres contar?", 1, 30)
    mostrar_codigo(f"""
for numero in range(1, {n} + 1):
    print(numero)
""")
    for numero in range(1, n + 1):
        print("  ", numero)
        pausa(0.2)
    print(f"\n🎉 ¡El bucle se repitió {n} veces! Cada vuelta, 'numero' cambió de valor.")
    continuar()


def for_con_listas():
    titulo("🐶 Bucle FOR: recorrer una lista")
    animales = ["🐶 perro", "🐱 gato", "🐸 rana", "🦁 león", "🐧 pingüino"]
    print("Una LISTA es como una mochila con muchas cosas adentro.")
    print("El bucle 'for' saca las cosas UNA POR UNA. 🎒\n")
    mostrar_codigo("""
animales = ["perro", "gato", "rana", "león", "pingüino"]
for animal in animales:
    print("Me gusta el", animal)
""")
    for animal in animales:
        print("   Me gusta el", animal)
        pausa()
    print(f"\n🎉 La lista tenía {len(animales)} animales, ¡y el bucle dio {len(animales)} vueltas!")

    print("\n¡Ahora tú! Escribe 3 de tus comidas favoritas:")
    comidas = []
    for i in range(1, 4):
        comida = input(f"  Comida {i}: ").strip() or "sorpresa 🎁"
        comidas.append(comida)
    print()
    for comida in comidas:
        print(f"   😋 ¡Ñam ñam, {comida}!")
        pausa()
    continuar()


def dibujar_con_bucles():
    titulo("⭐ Dibujar con bucles")
    altura = pedir_numero("¿Qué tan alto quieres tu triángulo?", 1, 15)
    mostrar_codigo(f"""
for fila in range(1, {altura} + 1):
    print("⭐" * fila)
""")
    for fila in range(1, altura + 1):
        print("   " + "⭐" * fila)
        pausa(0.15)
    print("\n¡Ahora un árbol de Navidad! 🎄\n")
    for fila in range(1, altura + 1):
        espacios = " " * (altura - fila)
        print("   " + espacios + "*" * (2 * fila - 1))
        pausa(0.15)
    print("   " + " " * (altura - 1) + "|")
    print("\n🎉 Cada fila es una vuelta del bucle, ¡y en cada vuelta ponemos más estrellas!")
    continuar()


def tablas_de_multiplicar():
    titulo("✖️ Tablas de multiplicar")
    n = pedir_numero("¿Qué tabla quieres ver?", 1, 12)
    mostrar_codigo(f"""
for i in range(1, 11):
    print({n}, "x", i, "=", {n} * i)
""")
    for i in range(1, 11):
        print(f"   {n} x {i:>2} = {n * i}")
        pausa(0.2)
    print("\n🎉 ¡Sin el bucle tendrías que escribir 10 líneas! Con el bucle, solo 2.")
    continuar()


def cuenta_regresiva():
    titulo("🚀 Bucle WHILE: ¡cuenta regresiva!")
    print("'while' significa 'mientras'.")
    print("El bucle se repite MIENTRAS la condición sea verdad.\n")
    inicio = pedir_numero("¿Desde qué número empezamos?", 1, 20)
    mostrar_codigo(f"""
cuenta = {inicio}
while cuenta > 0:
    print(cuenta)
    cuenta = cuenta - 1
print("¡Despegue!")
""")
    cuenta = inicio
    while cuenta > 0:
        print(f"   {cuenta}...")
        cuenta = cuenta - 1
        pausa(0.6)
    print("   🚀🔥 ¡DESPEGUE! 🔥🚀")
    print("\n💡 Cuando 'cuenta' llegó a 0, la condición 'cuenta > 0' fue FALSA y el bucle paró.")
    print("⚠️  Si olvidamos 'cuenta = cuenta - 1', ¡el bucle nunca pararía! Eso se llama bucle infinito.")
    continuar()


def adivina_el_numero():
    titulo("🎲 Juego: ¡Adivina el número!")
    secreto = random.randint(1, 50)
    print("Pensé un número entre 1 y 50. ¿Puedes adivinarlo? 🤫")
    print("(Este juego usa un bucle 'while': se repite MIENTRAS no adivines)\n")
    intentos = 0
    adivinado = False
    while not adivinado:
        intento = pedir_numero("Tu número", 1, 50)
        intentos += 1
        if intento < secreto:
            print("   ⬆️  ¡Más alto!")
        elif intento > secreto:
            print("   ⬇️  ¡Más bajo!")
        else:
            adivinado = True
    print(f"\n🎉🎉 ¡SÍ! Era el {secreto}. Lo lograste en {intentos} intentos.")
    print(f"💡 El bucle 'while' dio {intentos} vueltas, una por cada intento.")
    continuar()


def mini_quiz():
    titulo("🧠 Mini-quiz de bucles")
    preguntas = [
        ("¿Qué hace un bucle?",
         ["a) Borra el programa", "b) Repite instrucciones", "c) Apaga la compu"], "b"),
        ("¿Cuántas veces se repite:  for i in range(3): ?",
         ["a) 3 veces", "b) 1 vez", "c) 10 veces"], "a"),
        ("¿Qué bucle se repite MIENTRAS algo sea verdad?",
         ["a) for", "b) print", "c) while"], "c"),
    ]
    puntos = 0
    for numero, (pregunta, opciones, correcta) in enumerate(preguntas, start=1):
        print(f"\nPregunta {numero}: {pregunta}")
        for opcion in opciones:
            print("   " + opcion)
        respuesta = ""
        while respuesta not in ("a", "b", "c"):
            respuesta = input("Tu respuesta (a, b o c): ").strip().lower()
        if respuesta == correcta:
            print("   ✅ ¡Correcto!")
            puntos += 1
        else:
            print(f"   ❌ Casi... la respuesta era '{correcta}'.")
    print(f"\n🏆 Sacaste {puntos} de {len(preguntas)}.")
    if puntos == len(preguntas):
        print("🌟 ¡Eres un MAESTRO de los bucles! 🌟")
    else:
        print("💪 ¡Muy bien! Repasa las lecciones y vuelve a intentarlo.")
    print("💡 Por cierto... ¡este quiz usó un bucle 'for' para hacer las preguntas!")
    continuar()


# ---------------------------------------------------------------
# Menú principal
# ---------------------------------------------------------------

LECCIONES = {
    "1": ("🤔 ¿Qué es un bucle?", que_es_un_bucle),
    "2": ("🔢 Bucle FOR: contar números", for_con_numeros),
    "3": ("🐶 Bucle FOR: recorrer una lista", for_con_listas),
    "4": ("⭐ Dibujar con bucles", dibujar_con_bucles),
    "5": ("✖️  Tablas de multiplicar", tablas_de_multiplicar),
    "6": ("🚀 Bucle WHILE: cuenta regresiva", cuenta_regresiva),
    "7": ("🎲 Juego: adivina el número", adivina_el_numero),
    "8": ("🧠 Mini-quiz", mini_quiz),
}


def main():
    titulo("🐍 ¡Bienvenido a APRENDE BUCLES con Python! 🐍")
    nombre = input("\n¿Cómo te llamas? ").strip() or "amigo"
    print(f"\n¡Hola, {nombre}! 👋 Vamos a aprender juntos sobre los bucles.")

    # ¡Este menú también es un bucle while!
    jugando = True
    while jugando:
        titulo(f"📚 Menú de lecciones de {nombre}")
        for clave, (nombre_leccion, _) in LECCIONES.items():
            print(f"  {clave}. {nombre_leccion}")
        print("  0. 👋 Salir")
        print("\n  (Psst... ¡este menú también es un bucle 'while'! 🔁)")
        opcion = input("\n¿Qué quieres aprender? ").strip()

        if opcion == "0":
            jugando = False
        elif opcion in LECCIONES:
            LECCIONES[opcion][1]()
        else:
            print("🙈 Esa opción no existe. Elige un número del menú.")
            pausa(1)

    print(f"\n👋 ¡Adiós, {nombre}! Sigue practicando. ¡Eres genial! 🌈")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\n👋 ¡Hasta luego!")
