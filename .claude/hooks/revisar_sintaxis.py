"""
Hook de Claude Code: revisa la sintaxis de un archivo .py justo después
de que Claude lo edita o lo escribe.

Claude Code le pasa a este script, por la entrada estándar (stdin), un JSON
con la información de lo que acaba de pasar, por ejemplo:
    {"tool_name": "Edit", "tool_input": {"file_path": "C:/.../aprende_loops.py", ...}}

Códigos de salida:
    0 -> todo bien, Claude sigue normal
    2 -> hay un error; lo que imprimimos en stderr se le muestra a Claude
"""

import json
import py_compile
import sys

sys.stderr.reconfigure(encoding="utf-8")

datos = json.loads(sys.stdin.buffer.read().decode("utf-8"))
ruta = datos.get("tool_input", {}).get("file_path", "")

# Solo revisamos archivos de Python
if not ruta.endswith(".py"):
    sys.exit(0)

try:
    py_compile.compile(ruta, doraise=True)
except py_compile.PyCompileError as error:
    print(f"❌ Error de sintaxis en {ruta}:\n{error.msg}", file=sys.stderr)
    sys.exit(2)
