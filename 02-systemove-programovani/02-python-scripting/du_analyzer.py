import sys
from pathlib import Path

def analyze_directory(path):
    root_path = Path(path)
    
    if not root_path.exists():
        print(f"Chyba: Cesta {path} neexistuje.")
        return

    print(f"--- Analyzuji: {root_path.resolve()} ---")
    
    total_size = 0
    all_files = []

    # rglob('*') projde rekurzivně všechno
    for item in root_path.rglob('*'):
        if item.is_file():
            try:
                size = item.stat().st_size
                total_size += size
                all_files.append((item, size))
            except OSError as e:
                print(f"Nelze číst {item}: {e}")

    # Seřadíme soubory podle velikosti (od největšího)
    # lambda x: x[1] znamená "řaď podle druhého prvku n-tice", což je velikost
    all_files.sort(key=lambda x: x[1], reverse=True)

    print(f"\nCelková velikost: {total_size / (1024*1024):.2f} MB")
    print(f"Počet souborů: {len(all_files)}")
    
    print("\nTOP 5 Největších souborů:")
    print("-" * 40)
    for file_path, size in all_files[:5]:
        print(f"{size / (1024*1024):8.2f} MB | {file_path.name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        target = "." # Defaultně aktuální adresář
    else:
        target = sys.argv[1]
        
    analyze_directory(target)