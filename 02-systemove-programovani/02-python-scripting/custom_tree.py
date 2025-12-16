import os
import sys
import shutil

def draw_tree(start_path):
    """
    Vizualizuje strukturu adresářů a souborů ve formě stromu (jako příkaz tree).
    """
    if not os.path.exists(start_path):
        print(f"Chyba: Složka '{start_path}' neexistuje.")
        return

    print(f"Adresářový strom pro: {start_path}")
    print("." + os.sep) # Vypíše kořen jako "."

    # --- ÚKOL 4: ZDE DOPLŇTE KÓD ---
    
    # 1. Použijte os.walk(start_path) pro průchod stromem.
    #    for root, dirs, files in os.walk(start_path): ...
    
    # 2. Uvnitř cyklu musíte zjistit, jak hluboko jste zanoření, abyste udělali správné odsazení.
    #    
    #    Trik: Jak zjistit hloubku (level)?
    #    Použijte os.path.relpath(root, start_path). 
    #    Pokud je relativní cesta "A/B", hloubka je počet oddělovačů + 1.
    #    (Pozor na kořenový adresář, kde relpath je ".").
    
    # 3. Vytvořte odsazení (string). Např. 4 mezery * level.
    #    indent = '    ' * level
    
    # 4. Vypište aktuální složku (použijte os.path.basename(root)).
    #    Poznámka: Kořenový adresář už jsme vypsali nahoře, ten můžete přeskočit
    #    (pokud root != start_path).

    # 5. Projděte seznam 'files' a vypište soubory se správným odsazením (level + 1).

    for root, dirs, files in os.walk(start_path):
        # Výpočet relativní cesty od startu (např. "Slozka/PodSlozka")
        rel_path = os.path.relpath(root, start_path)
        
        # Pokud jsme v kořenu, rel_path je ".", nastavíme level na 0, jinak počítáme hloubku
        if rel_path == ".":
            level = 0
        else:
            # Hloubka se rovná počtu separátorů v cestě + 1
            # Např "A/B" má 1 separátor, ale je to level 2 (pod kořenem)
            level = rel_path.count(os.sep) + 1
            
            # Výpis aktuální složky
            indent = '|   ' * (level - 1) + '|-- '
            print(f"{indent}{os.path.basename(root)}/")

        # Výpis souborů v aktuální složce
        sub_indent = '|   ' * level + '|-- '
        for f in files:
            print(f"{sub_indent}{f}")


if __name__ == "__main__":
    # Testovací data
    TARGET_DIR = "dummy_data_tree"
    
    # Úklid před testem (smazání staré verze, pokud existuje)
    if os.path.exists(TARGET_DIR): shutil.rmtree(TARGET_DIR)
    
    # Vytvoření složité struktury pro testování
    print(f"[SETUP] Vytvářím testovací data v '{TARGET_DIR}'...")
    
    os.makedirs(os.path.join(TARGET_DIR, "Projekt_A", "Data"))
    os.makedirs(os.path.join(TARGET_DIR, "Projekt_A", "Logs"))
    os.makedirs(os.path.join(TARGET_DIR, "Projekt_B", "SRC"))
    os.makedirs(os.path.join(TARGET_DIR, "Obrazky"))
    
    # Vytvoříme soubory na různých úrovních
    with open(os.path.join(TARGET_DIR, "root_file.txt"), "w") as f: f.write("x")
    with open(os.path.join(TARGET_DIR, "Projekt_A", "readme.md"), "w") as f: f.write("x")
    with open(os.path.join(TARGET_DIR, "Projekt_A", "Data", "data.csv"), "w") as f: f.write("x")
    with open(os.path.join(TARGET_DIR, "Projekt_B", "script.py"), "w") as f: f.write("x")

    print("\n--- Výsledek příkazu tree ---")
    
    # Spuštění vašeho skriptu
    draw_tree(TARGET_DIR)
    
    print("\n-----------------------------")
    # Úklid po sobě (volitelné)
    # shutil.rmtree(TARGET_DIR)