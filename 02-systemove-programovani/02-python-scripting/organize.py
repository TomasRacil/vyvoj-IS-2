import shutil
import sys
from pathlib import Path

# Definice pravidel
RULES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".svg", ".bmp"},
    "Documents": {".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"},
    "Archives": {".zip", ".tar", ".gz", ".rar", ".7z"},
    "Scripts": {".py", ".sh", ".js", ".bat"}
}

def get_unique_path(path):
    """
    Pokud soubor existuje, přidá k němu číslo (např. file_1.txt).
    """
    if not path.exists():
        return path
        
    stem = path.stem
    suffix = path.suffix
    counter = 1
    
    while True:
        new_path = path.with_name(f"{stem}_{counter}{suffix}")
        if not new_path.exists():
            return new_path
        counter += 1

def organize_folder(target_dir):
    root = Path(target_dir)
    if not root.exists():
        print("Cesta neexistuje.")
        return

    # Vytvoření složek
    for folder_name in RULES.keys():
        (root / folder_name).mkdir(exist_ok=True)

    print(f"--- Organizuji: {root} ---")
    
    moved_count = 0
    
    for item in root.iterdir():
        if item.is_file():
            suffix = item.suffix.lower()
            
            # Hledáme, kam soubor patří
            dest_folder = None
            for folder, extensions in RULES.items():
                if suffix in extensions:
                    dest_folder = folder
                    break
            
            if dest_folder:
                target_path = root / dest_folder / item.name
                
                # Řešení kolizí
                final_path = get_unique_path(target_path)
                
                print(f"Přesouvám: {item.name} -> {dest_folder}/{final_path.name}")
                shutil.move(str(item), str(final_path))
                moved_count += 1

    print(f"--- Hotovo. Přesunuto {moved_count} souborů. ---")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    organize_folder(path)