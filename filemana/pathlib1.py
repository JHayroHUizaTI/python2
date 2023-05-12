
from pathlib import Path

import os

#Ver directorio actual
print("1. Dir actual ", Path.cwd())

#Crear un directorio
path1 = Path("/home/whoami/Documents/project_vscode/python/projects")

print("2. Crear directorio nuevo: ", path1.mkdir())

