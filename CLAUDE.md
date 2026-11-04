# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Proyecto

Programa interactivo de consola para niños que enseña bucles (`for` y `while`) en Python. Todo está en un solo archivo, `aprende_loops.py`. Solo usa la biblioteca estándar de Python 3, sin dependencias. No hay tests, linter ni build.

## Comandos

```
python aprende_loops.py
```

Para probar sin interacción, pasa la entrada por stdin o importa el módulo; `main()` solo se ejecuta bajo `__main__`. Ejemplo en PowerShell:

```
"--5`nabc`n7" | python -c "import aprende_loops as a; print(a.pedir_numero('n', 1, 10))"
```

## Arquitectura

- **Menú**: `main()` recorre en un bucle `while` el diccionario `LECCIONES`, que asocia cada tecla del menú a un `(título, función)`. Para añadir una lección se escribe la función y se registra en `LECCIONES`.
- **Estructura de cada lección**: `titulo(...)`, luego una explicación, después `mostrar_codigo("""...""")` con el código de ejemplo, luego la ejecución real de ese mismo código con `pausa()` entre pasos y, al final, `continuar()`.
- **Entrada del usuario**: los números se piden siempre con `pedir_numero(mensaje, minimo, maximo)`, que repite la pregunta hasta recibir un número válido y acepta solo dígitos ASCII. Las demás entradas validan en bucle y muestran un mensaje amable cuando la respuesta no es válida.
- Al inicio, stdout se reconfigura a UTF-8 con `errors="replace"` para que los emojis no rompan la consola de Windows.

## Convenciones

- **El código mostrado debe coincidir exactamente con lo que se ejecuta**: el mismo `print`, el mismo texto, los mismos emojis y sin sangría extra. Es el principio pedagógico central (“este es el código, esto es lo que pasa”). La única diferencia permitida es `pausa()`.
- Todo el texto para el usuario está en español, en un tono infantil y con emojis. Cuida la gramática: artículos con el género correcto y singular/plural según la cantidad (“1 intento”, “2 intentos”).
- Los ejemplos de código deben ser sencillos y legibles para niños: mejor `while condición` que banderas auxiliares, y nada de formatos avanzados en el código mostrado.
