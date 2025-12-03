import os
import shutil
import time
from datetime import datetime
from pathlib import Path

# Konfigurace
LOG_DIR = Path("logs")
ARCHIVE_DIR = LOG_DIR / "archive"
DAYS_ARCHIVE = 7
DAYS_DELETE = 30

def get_file_age_days(filepath):
    stat = filepath.stat()
    age_seconds = time.time() - stat.st_mtime
    return age_seconds / (24 * 3600)

def main():
    if not LOG_DIR.exists():
        print(f"Složka {LOG_DIR} neexistuje. Vytvořte ji.")
        return

    # Zajistíme existenci archivu
    ARCHIVE_DIR.mkdir(exist_ok=True)

    print(f"--- Rotace logů v {LOG_DIR} ---")

    # 1. Procházíme hlavní složku (hledáme kandidáty na archivaci)
    for log_file in LOG_DIR.glob("*.log"):
        age = get_file_age_days(log_file)
        
        if age > DAYS_ARCHIVE:
            # Zformátujeme datum modifikace pro název
            mtime = datetime.fromtimestamp(log_file.stat().st_mtime)
            date_str = mtime.strftime("%Y-%m-%d")
            
            # Nový název: puvodni_DATUM.log
            new_name = f"{log_file.stem}_{date_str}{log_file.suffix}"
            target_path = ARCHIVE_DIR / new_name
            
            print(f"[ARCHIV] {log_file.name} ({age:.1f} dní) -> {new_name}")
            shutil.move(str(log_file), str(target_path))

    # 2. Procházíme archiv (hledáme kandidáty na smazání)
    for archive_file in ARCHIVE_DIR.glob("*.log"):
        age = get_file_age_days(archive_file)
        
        if age > DAYS_DELETE:
            print(f"[SMAZAT] {archive_file.name} ({age:.1f} dní)")
            os.remove(archive_file)

    print("--- Hotovo ---")

if __name__ == "__main__":
    main()