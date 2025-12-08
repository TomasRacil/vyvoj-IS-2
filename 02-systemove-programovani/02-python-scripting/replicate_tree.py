import os
import sys
import shutil

def replicate_structure(src, dst):
    """
    Zkopíruje adresářovou strukturu ze 'src' do 'dst', ale BEZ souborů.
    """
    if not os.path.exists(src):
        print(f"Chyba: Zdrojová složka '{src}' neexistuje.")
        return

    print(f"Replikuji strukturu: {src} -> {dst}")

    # --- ÚKOL 4: ZDE DOPLŇTE KÓD ---
    
    # 1. Použijte os.walk(src) pro průchod zdrojovým stromem.
    #    for dirpath, dirnames, filenames in os.walk(src): ...
    
    # 2. Pro každý nalezený adresář (dirpath) musíte vytvořit ekvivalent v cíli.
    #    
    #    Trik: Jak zjistit cestu v cíli?
    #    Musíte vzít 'dirpath' (např. "source/A/B") a nahradit začátek "source" za "target".
    #    
    #    Elegantní způsob:
    #    relative_path = os.path.relpath(dirpath, src)  # "A/B"
    #    target_path = os.path.join(dst, relative_path) # "target/A/B"
    
    # 3. Vytvořte složku (os.makedirs s parametrem exist_ok=True).
    
    pass

if __name__ == "__main__":
    # Testovací data
    SRC = "source_tree_dummy"
    DST = "target_tree_dummy"
    
    # Úklid před testem
    if os.path.exists(SRC): shutil.rmtree(SRC)
    if os.path.exists(DST): shutil.rmtree(DST)
    
    # Vytvoření složité struktury
    print("[SETUP] Vytvářím zdrojovou strukturu...")
    os.makedirs(os.path.join(SRC, "Projekt_A", "Data"))
    os.makedirs(os.path.join(SRC, "Projekt_A", "Logs"))
    os.makedirs(os.path.join(SRC, "Projekt_B", "SRC"))
    # Vytvoříme i nějaké soubory (ty se NEmají zkopírovat)
    with open(os.path.join(SRC, "Projekt_A", "readme.txt"), "w") as f: f.write("text")

    # Spuštění replikace
    replicate_structure(SRC, DST)
    
    print("\n--- Výsledek (Cílová složka) ---")
    # Výpis výsledku pro kontrolu
    for root, dirs, files in os.walk(DST):
        print(f"Složka: {root}")
        if files:
            print(f"  CHYBA! Zkopírovaly se i soubory: {files}")