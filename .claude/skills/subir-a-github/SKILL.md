---
name: subir-a-github
description: Revisa los cambios pendientes, hace el commit con un mensaje en español y lo sube a GitHub (push).
disable-model-invocation: true
---

# Subir los cambios a GitHub

El usuario está aprendiendo, así que explica cada paso en una frase sencilla. Si algo falla, detente y explica qué pasó; no lo fuerces.

## 1. Mira qué cambió

```
git status --short
git diff --stat
```

- Si no hay cambios, díselo al usuario y termina.
- Lee el diff (`git diff`) para entender qué cambió y poder escribir un buen mensaje.
- No incluyas archivos que no deban subirse: `__pycache__/`, `.claude/settings.local.json`, archivos temporales, contraseñas o claves. Si ves alguno sin ignorar, pregunta antes de seguir.

## 2. Comprueba que el programa no esté roto

```
python -c "import ast; ast.parse(open('aprende_loops.py', encoding='utf-8').read()); print('sintaxis OK')"
```

Si falla, no hagas commit: explica el error y ofrece arreglarlo.

## 3. Escribe el mensaje del commit

- En español. La primera línea es un resumen corto en imperativo ("Añade…", "Corrige…"), de unos 70 caracteres como máximo.
- Después, una línea en blanco y una lista de los cambios importantes.
- Al final, las líneas de atribución que indique Claude Code, si las hay.

Escribe el mensaje en un archivo dentro de la carpeta temporal (scratchpad) y usa `git commit -F <archivo>`. Con `-m` y comillas, PowerShell 5.1 rompe el mensaje.

## 4. Haz el commit

Añade los archivos por nombre, no con `git add -A` ni `git add .`:

```
git add <archivo1> <archivo2> ...
git commit -F <archivo-del-mensaje>
```

## 5. Sube a GitHub

```
git push
```

Si el push se rechaza porque GitHub tiene cambios que aquí no están, no uses `--force`. Explícalo y propón `git pull --rebase` antes de reintentar.

## 6. Informa al usuario

Di qué archivos se subieron, el código corto del commit (por ejemplo `a96a9c0`) y el enlace al repositorio en GitHub.
