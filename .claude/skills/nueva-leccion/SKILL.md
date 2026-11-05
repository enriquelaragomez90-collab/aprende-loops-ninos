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

En la lista `LECCIONES`, añade `("emoji Título", nombre_de_la_leccion)` justo antes del Mini-quiz, que siempre va al final. Usa el mismo emoji y título que en `titulo(...)`. Los números del menú se calculan solos según el orden de la lista, así que no hay que renumerar nada.

Si el concepto es nuevo, añade también una pregunta sobre él en `mini_quiz()`.

## 3. Revisa el texto

- Todo en español, en tono cercano para niños y con emojis.
- Artículos con el género correcto ("la rana", "el perro").
- Singular y plural según la cantidad ("1 vuelta", "2 vueltas").

## 4. Pruébala sin teclear

Ejecuta la lección directamente, pasándole las respuestas por stdin. Desactiva las pausas para que sea rápido. El comando depende de la terminal:

Con la herramienta Bash (Git Bash):
```
printf '3\n\n' | python -c "import aprende_loops as a; a.pausa = lambda s=0: None; a.nombre_de_la_leccion()"
```

Con la herramienta PowerShell (Windows PowerShell 5.1, donde `printf` no existe). PowerShell antepone un BOM invisible al texto de la tubería; sin `utf-8-sig`, la primera respuesta llega como `"﻿3"` y se rechaza:
```
"3`n`n" | python -c "import io, sys; sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8-sig'); import aprende_loops as a; a.pausa = lambda s=0: None; a.nombre_de_la_leccion()"
```

Comprueba en la salida que lo que se imprime coincide con el código mostrado. Prueba también el valor mínimo y el máximo que acepta `pedir_numero`.

## 5. Informa al usuario

Muestra un fragmento de la salida de la prueba y di en qué número del menú quedó la lección. No hagas commit hasta que el usuario lo pida.
