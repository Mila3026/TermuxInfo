import os
import platform

print("=== INFORMACIÓN DEL SISTEMA ===")

print("\nSistema Operativo:")
print(platform.system())

print("\nVersión:")
print(platform.version())

print("\nUsuario:")
os.system("whoami")

print("\nDirectorio actual:")
os.system("pwd")

print("\nArchivos disponibles:")
os.system("ls")
