import os
import shutil

# Složka, kterou budeme uklízet
BASE_DIR = "downloads_test"

# Pravidla pro třídění
EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Docs": [".pdf", ".txt", ".docx", ".xlsx"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Scripts": [".py", ".sh", ".bat"]
}

def setup_mess():
    """
    PŘIPRAVENÁ FUNKCE.
    Vytvoří složku downloads_test a naplní ji soubory.
    """
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)
    
    # Seznam souborů k vytvoření
    files = [
        "dovolena.jpg", "faktura.pdf", "data.zip", "skript.py", 
        "poznamky.txt", "pisnicka.mp3", # mp3 nemá kategorii -> zůstane
        "dovolena.jpg" # Simulace kolize (tento soubor vytvoříme až uvnitř složky Images)
    ]
    
    print("[SETUP] Vytvářím nepořádek...")
    for f in files:
        if f == "dovolena.jpg" and os.path.exists(os.path.join(BASE_DIR, f)):
            continue # Přeskočíme duplikát v rootu
        with open(os.path.join(BASE_DIR, f), "w") as file:
            file.write("Dummy content")
            
    # Simulace kolize: V cílové složce Images už jeden soubor "dovolena.jpg" bude
    os.makedirs(os.path.join(BASE_DIR, "Images"), exist_ok=True)
    with open(os.path.join(BASE_DIR, "Images", "dovolena.jpg"), "w") as f:
        f.write("Stará fotka, kterou nechceme přepsat!")

def organize():
    print(f"Uklízím složku: {os.path.abspath(BASE_DIR)}")
    
    # Získáme seznam souborů v kořenu složky
    all_files = [f for f in os.listdir(BASE_DIR) if os.path.isfile(os.path.join(BASE_DIR, f))]

    for filename in all_files:
        # Získání přípony (např. ".jpg")
        file_ext = os.path.splitext(filename)[1].lower()
        
        # --- ÚKOL 3: ZDE DOPLŇTE KÓD ---
        
        # 1. Zjistěte, do které složky soubor patří (podle EXTENSIONS).
        #    Pokud přípona není ve slovníku, soubor přeskočte.
        
        # 2. Vytvořte cílovou složku, pokud neexistuje (os.makedirs).
        
        # 3. Vyřešte kolizi názvů:
        #    Cílová cesta: destination = os.path.join(BASE_DIR, folder_name, filename)
        #    Dokud os.path.exists(destination):
        #       Upravte název (např. "soubor_1.txt") a zkuste to znovu.
        
        # 4. Přesuňte soubor (shutil.move).
        
        pass

if __name__ == "__main__":
    setup_mess()
    organize()
    print("\nHotovo. Podívejte se do složky 'downloads_test'.")