---
name: nueva-leccion
description: Crea una lección nueva en aprende_loops.py siguiendo la estructura y las reglas del proyecto. Úsala cuando el usuario pida añadir una lección, un tema o un ejercicio nuevo al programa.
---

# Crear una lección nueva

Sigue estos pasos en orden. Si el usuario no dijo qué tema enseñar, pregúntale antes de empezar.

## 1. Escribe la función de la lección

Ponla en `aprende_loops.py`, en la sección `# Lecciones`, antes de `mini_quiz()`. Usa siempre esta estructura:

```python
def nombre_de_la_leccion():
    titulo("🎯 Título con emoji")
    print("Explicación corta, para niños, de qué vamos a aprender.\n")
    valor = pedir_numero("¿Pregunta para el niño?", 1, 10)   # opcional
    mostrar_codigo(f"""
...el código de ejemplo...
""")
    ...exactamente el mismo código, ejecutándose de verdad, con pausa()...
    print("\n🎉 Mensaje final que explica qué pasó y por qué.")
    continuar()
```

Reglas:
- **El código mostrado y el ejecutado deben ser idénticos**: los mismos `print`, el mismo texto y los mismos emojis, sin sangría extra. La única diferencia permitida es `pausa()`.
- Si el código mostrado es un f-string y contiene llaves `{}` propias, escríbelas dobles: `{{variable}}`.
- Para pedir números usa siempre `pedir_numero(mensaje, minimo, maximo)`, con un máximo razonable para que la salida quepa en pantalla.
- Usa código simple: nada de comprensiones de listas, `lambda` ni formatos avanzados en lo que se muestra.

## 2. Registra la lección en el menú

En el diccionario `LECCIONES`, añádela justo antes del Mini-quiz y vuelve a numerar el quiz para que siga siendo la última opción. Usa el mismo emoji y título que en `titulo(...)`.

## 3. Revisa el texto

- Todo en español, en tono cercano para niños y con emojis.
- Artículos con el género correcto ("la rana", "el perro").
- Singular y plural según la cantidad ("1 vuelta", "2 vueltas").

## 4. Pruébala sin teclear

Ejecuta la lección directamente, pasándole las respuestas por stdin. Desactiva las pausas para que sea rápido:

```
printf '3\n\n' | python -c "import aprende_loops as a; a.pausa = lambda s=0: None; a.nombre_de_la_leccion()"
```

Comprueba en la salida que lo que se imprime coincide con el código mostrado. Prueba también el valor mínimo y el máximo que acepta `pedir_numero`.

## 5. Informa al usuario

Muestra un fragmento de la salida de la prueba y di en qué número del menú quedó la lección. No hagas commit hasta que el usuario lo pida.
