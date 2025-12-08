import os
import sys

def analyze_directory(path):
    """
    Rekurzivně projde složku, spočítá velikosti a najde největší soubory.
    """
    # Kontrola existence cesty
    if not os.path.exists(path):
        print(f"Chyba: Cesta '{path}' neexistuje.")
        return

    print(f"--- Analyzuji: {os.path.abspath(path)} ---")
    
    total_size = 0
    all_files = [] # Sem ukládejte n-tice: (cesta_k_souboru, velikost)

    # --- ÚKOL 1: ZDE DOPLŇTE KÓD ---
    
    # 1. Použijte os.walk(path) pro průchod stromem adresářů.
    #    for root, dirs, files in os.walk(path): ...
    
    # 2. Uvnitř cyklu projděte seznam 'files'.
    #    - Sestavte plnou cestu: filepath = os.path.join(root, filename)
    #    - Zjistěte velikost: size = os.path.getsize(filepath)
    #    - Přičtěte k total_size.
    #    - Přidejte do seznamu all_files: all_files.append((filepath, size))
    
    # ... Váš kód ...

    # Výpis celkové velikosti (převeďte na MB)
    print(f"Celková velikost: {total_size / (1024*1024):.2f} MB")
    
    # --- ÚKOL 1 (Pokračování): TOP 5 ---
    
    # 3. Seřaďte seznam all_files podle velikosti (od největšího).
    #    Tip: all_files.sort(key=lambda x: x[1], reverse=True)
    
    print("\n[TOP 5 Největších souborů]")
    # 4. Vypište prvních 5 položek.
    #    Format: "Soubor: ... Velikost: ... MB"
    
    # ... Váš kód ...

if __name__ == "__main__":
    # Zpracování argumentů příkazové řádky
    # Použití: python du_analyzer.py <cesta>
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
    else:
        target_dir = "." # Pokud není argument, použij aktuální složku
        
    analyze_directory(target_dir)