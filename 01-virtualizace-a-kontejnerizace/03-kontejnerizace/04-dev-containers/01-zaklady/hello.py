import sys
import os

print("------------------------------------------------")
print(" Ahoj. Tento kód běží uvnitř Dev Containeru.")
print("------------------------------------------------")

print(f"Verze Pythonu: {sys.version}")
print(f"Operační systém: {os.uname().sysname} {os.uname().release}")

print("\nPokud toto čtete, vaše vývojové prostředí funguje správně.")