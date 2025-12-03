# **02: Python Scripting**

V této lekci se zaměříme na pokročilou správu souborového systému pomocí Pythonu. Základní práci se soubory (`open()`, `read()`) už znáte, ale v systémové správě potřebujeme manipulovat s celými stromy adresářů, přesouvat soubory podle metadat, analyzovat využití disku nebo bezpečně pracovat s cestami napříč operačními systémy (Windows vs. Linux).

## **Klíčové knihovny pro automatizaci**

Python nabízí několik standardních knihoven, které jsou pro správce systému denním chlebem.

### **1. Modul `os` (Operating System)**

Tento modul poskytuje nízkoúrovňové rozhraní pro interakci s operačním systémem. Je to "švýcarský nůž", který umí téměř vše, co umí terminál.

* **Manipulace se soubory:**  
  * `os.remove('file.txt')` - Smaže soubor.  
  * `os.rename('old.txt', 'new.txt')` - Přejmenuje soubor.  
  * `os.chmod('script.py', 0o755)` - Změní oprávnění (jako `chmod`).  
* **Adresáře:**  
  * `os.mkdir('nova_slozka')` - Vytvoří jednu složku.  
  * `os.makedirs('a/b/c')` - Vytvoří celou cestu (jako `mkdir -p`).  
  * `os.rmdir('slozka')` - Smaže *prázdnou* složku.  
  * `os.listdir('.')` - Vypíše obsah adresáře (vrátí seznam názvů).  
  * `os.walk('.')` - Rekurzivně projde celý strom adresářů.  
* **Prostředí a cesty:**  
  * `os.environ` - Slovník s proměnnými prostředí (např. `os.environ.get('HOME')`).  
  * `os.path.join('a', 'b')` - Spojí cesty správně podle OS (`/` nebo `\`).  
  * `os.path.exists('soubor')`, `os.path.isfile('soubor')`.

### **2. Modul `shutil` (Shell Utilities)**

Zatímco `os` řeší nízkoúrovňové operace (často mapované 1:1 na systémová volání), `shutil` nabízí vysokoúrovňové operace, které byste jinak museli složitě programovat.

* **Kopírování:**  
  * `shutil.copy('zdroj', 'cil')` - Kopíruje soubor (včetně obsahu).  
  * `shutil.copy2('zdroj', 'cil')` - Kopíruje soubor **i s metadaty** (čas vytvoření, modifikace).  
  * `shutil.copytree('src_dir', 'dst_dir')` - Zkopíruje celou složku rekurzivně (jako `cp -r`).  
* **Mazání:**  
  * `shutil.rmtree('slozka')` - Smaže složku i s obsahem (nebezpečné, jako `rm -rf`).  
* **Přesun:**  
  * `shutil.move('zdroj', 'cil')` - Přesune soubor nebo složku.  
* **Archivace:**  
  * `shutil.make_archive('nazev', 'zip', 'adresar')` - Vytvoří ZIP/TAR archiv.  
* **Disk Usage:**  
  * `shutil.disk_usage('/')` - Vrátí informace o volném místě na disku.

### **3. Modul `pathlib` (Moderní přístup)**

Od Pythonu 3.4 je k dispozici `pathlib`, který nahrazuje starší práci s cestami přes `os.path`. Místo textových řetězců používá objekty. Je to dnes preferovaný způsob.

* **Vytvoření cesty:** `p = Path('/var/log/syslog')`  
* **Navigace:** `p.parent`, `p.name`, `p.suffix` (přípona).  
* **Spojování:** `full_path = Path('/home') / 'user' / 'data'` (operátor `/`).  
* **Metody:**  
  * `p.exists()`, `p.is_dir()`.  
  * `p.read_text()` / `p.write_text()` - Rychlé čtení/zápis obsahu.  
  * `p.glob('*.log')` - Hledání souborů.

## **Praktické úkoly**

Připravili jsme tři úkoly, které simulují reálné scénáře údržby serveru.

### **Úkol 1: "Disk Usage Monitor"**

Správce potřebuje vědět, které složky zabírají nejvíce místa. Napište skript `du_analyzer.py`, který:

1. Přijme cestu k adresáři jako argument příkazové řádky (např. pomocí `sys.argv` nebo `argparse`).  
2. Rekurzivně projde všechny soubory v dané cestě (využijte `os.walk` nebo `pathlib.Path.rglob`).  
3. Sečte velikost všech souborů.  
4. Najde a vypíše **TOP 5 největších souborů** (název + velikost v MB).  
5. Vypíše celkovou velikost adresáře.

**Tip:** Velikost souboru zjistíte pomocí `os.path.getsize(cesta)` nebo `Path(cesta).stat().st_size`.

### **Úkol 2: "Smart Log Rotator"**

Server generuje logy, které musíme archivovat, aby nezaplnily disk. Logika je složitější než u běžného `logrotate`.

**Zadání:** Napište skript `rotate_logs.py`, který zpracuje složku `logs/`:

1. Vytvoří složku `logs/archive`, pokud neexistuje.  
2. Projde všechny soubory s příponou `.log`.  
3. Zkontroluje datum poslední modifikace (`st_mtime`).  
4. **Pravidla:**  
   * Logy starší než **7 dní** přesune do `archive/` a přejmenuje na `nazev_DATUM.log` (např. `app_2023-10-01.log`).  
   * Logy starší než **30 dní** (které už jsou v archivu) **smaže úplně**.  
   * Soubory mladší než 7 dní nechá na místě.

**Příprava dat (Bash):**

```bash
mkdir -p logs/archive  
touch logs/today.log  
touch -d "10 days ago" logs/old.log  
touch -d "40 days ago" logs/archive/ancient_2023-01-01.log
```

### **Úkol 3: "Organizace souborů podle typu"**

Uživatelé ukládají vše do jedné složky `Downloads`. Udělejte v tom pořádek.

**Zadání:** Napište skript `organize.py`, který:

1. Projde zadanou složku.  
2. Vytvoří podsložky `Images`, `Documents`, `Archives`, `Scripts`.  
3. Přesune soubory podle jejich přípony:  
   * `.jpg`, `.png`, `.gif` -> `Images`  
   * `.pdf`, `.docx`, `.txt` -> `Documents`  
   * `.zip`, `.tar`, `.gz` -> `Archives`  
   * `.py`, `.sh` -> `Scripts`  
4. Ostatní soubory nechá být.  
5. Ošetří kolize názvů (pokud soubor v cíli už existuje, nepřepíše ho, ale přidá k názvu číslo, např. `image_1.jpg`).

## **Bonusová úloha: Replikace stromu**

Napište skript, který zkopíruje celou adresářovou strukturu ze zdroje do cíle, ale bez souborů.  
Tedy vytvoří "kostru" adresářů.

* Využijte `os.walk` pro průchod zdrojem.  
* Využijte `os.makedirs` pro vytváření složek v cíli.  
* Cestu v cíli odvodíte nahrazením kořenové části cesty zdroje.