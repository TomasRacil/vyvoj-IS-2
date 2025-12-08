import os
import time
import shutil
import datetime

# Nastavení cest
LOG_DIR = "logs"
ARCHIVE_DIR = os.path.join(LOG_DIR, "archive")

def setup_dummy_logs():
    """
    PŘIPRAVENÁ FUNKCE - NEMĚNIT.
    Vytvoří testovací prostředí: složku logs/ a soubory s různým stářím.
    """
    if os.path.exists(LOG_DIR):
        shutil.rmtree(LOG_DIR) # Smaže staré pro čistý start
    os.makedirs(ARCHIVE_DIR)

    now = time.time()
    day = 86400 # Sekund v dni

    # Seznam souborů: (název, stáří_ve_dnech)
    files = [
        ("today.log", 0),
        ("recent.log", 3),
        ("old.log", 10),       # Měl by se přesunout do archivu
        ("very_old.log", 20),  # Měl by se přesunout do archivu
    ]
    
    # Soubory, které už v archivu jsou
    archive_files = [
        ("archived_ok.log", 10),
        ("archived_delete.log", 35) # Měl by se smazat (starší než 30 dní)
    ]

    print("[SETUP] Generuji testovací data...")
    
    # Vytvoření logů
    for name, age_days in files:
        path = os.path.join(LOG_DIR, name)
        with open(path, "w") as f: f.write(f"Log data created {age_days} days ago.")
        # Změna času modifikace souboru "do minulosti"
        file_time = now - (age_days * day)
        os.utime(path, (file_time, file_time))

    # Vytvoření archivních logů
    for name, age_days in archive_files:
        path = os.path.join(ARCHIVE_DIR, name)
        with open(path, "w") as f: f.write("Archived data...")
        file_time = now - (age_days * day)
        os.utime(path, (file_time, file_time))

def rotate_logs():
    print("--- Spouštím rotaci logů ---")
    now = time.time()
    
    # --- ÚKOL 2: ZDE DOPLŇTE KÓD ---

    # Krok 1: Archivace starých logů z LOG_DIR
    # Projděte soubory v LOG_DIR (os.listdir).
    # Ignorujte složku 'archive'.
    # Pokud je soubor starší než 7 dní:
    #   - Přesuňte ho do ARCHIVE_DIR (shutil.move).
    #   - (Volitelné) Přejmenujte ho (přidejte datum).
    
    # ... Váš kód ...

    # Krok 2: Mazání velmi starých logů z ARCHIVE_DIR
    # Projděte soubory v ARCHIVE_DIR.
    # Pokud je soubor starší než 30 dní:
    #   - Smažte ho (os.remove).
    #   - Vypište informaci o smazání.

    # Tip: Stáří souboru ve dnech zjistíte takto:
    # mtime = os.path.getmtime(cesta_k_souboru)
    # stari_dny = (now - mtime) / 86400
    
    pass

if __name__ == "__main__":
    setup_dummy_logs()
    rotate_logs()
    
    print("\n--- Kontrola výsledku ---")
    print(f"Obsah {LOG_DIR}: {os.listdir(LOG_DIR)}")
    print(f"Obsah {ARCHIVE_DIR}: {os.listdir(ARCHIVE_DIR)}")