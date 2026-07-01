# Datos interesantes 
# ¿Qué hace estás líneas de códigos?
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

Le dicen a Pytest: "Oye, sube una carpeta más arriba (a la raíz del proyecto) para buscar las importaciones". Así podrá leer tu archivo main.py perfectamente.

