import subprocess

# 1. Modificar el archivo README.md desde Python
with open("README.md", "w", encoding="utf-8") as archivo:
    archivo.write("# Modificado desde Python\n")
    archivo.write("Este es un cambio real para que git lo detecte\n")
print("Archivo modificado correctamente")

# 2. Ejecutar el comando git desde Python
print("Iniciando automatización git...")

# 3. Ejecutamos 'git add .'
subprocess.run(["git", "add", "."])
print("- Archivo preparado (git add .)")

# 4. Ejecutamos 'git commit -m "Actualización desde Python"'
subprocess.run(["git", "commit", "-m", "Actualización desde Python"])
print("- Cambios confirmados (git commit)")

# 5. Ejecutamos 'git push'
subprocess.run(["git", "push"])
print("- Cambios subidos al repositorio (git push)")