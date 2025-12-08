# **02: Python Scripting**

V této lekci se zaměříme na pokročilou správu souborového systému pomocí Pythonu. Základní práci se soubory (`open()`, `read()`) už znáte, ale v systémové správě potřebujeme manipulovat s celými stromy adresářů, přesouvat soubory podle metadat, analyzovat využití disku nebo bezpečně pracovat s cestami napříč operačními systémy (Windows vs. Linux).

## **1. Klíčové knihovny pro automatizaci**

Python nabízí několik standardních knihoven, které jsou pro správce systému denním chlebem.

### **Modul `os` (Operating System)**

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
  * `os.path.join('a', 'b')` - Spojí cesty správně podle OS (`/` nebo ``).  
  * `os.path.exists('soubor')`, `os.path.isfile('soubor')`.

### **Modul `shutil` (Shell Utilities)**

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

### **Modul `pathlib` (Moderní přístup)**

Od Pythonu 3.4 je k dispozici `pathlib`, který nahrazuje starší práci s cestami přes `os.path`. Místo textových řetězců používá objekty. Je to dnes preferovaný způsob.

* **Vytvoření cesty:** `p = Path('/var/log/syslog')`  
* **Navigace:** `p.parent`, `p.name`, `p.suffix` (přípona).  
* **Spojování:** `full_path = Path('/home') / 'user' / 'data'` (operátor `/`).  
* **Metody:**  
  * `p.exists()`, `p.is_dir()`.  
  * `p.read_text()` / `p.write_text()` - Rychlé čtení/zápis obsahu.  
  * `p.glob('*.log')` - Hledání souborů.

## **2. Praktické úkoly**

V této složce naleznete kostry skriptů ("skeletons"), které musíte dokončit.

### **Úkol 1: "Disk Usage Monitor" ([`du_analyzer.py`](./du_analyzer.py))**

Správce potřebuje vědět, co zabírá místo na disku.

1. Otevřete [`du_analyzer.py`](./du_analyzer.py).  
2. Doplňte funkci `analyze_directory`, aby rekurzivně prošla složku (použijte `os.walk`).  
3. Spočítejte celkovou velikost.  
4. Implementujte logiku pro nalezení **TOP 5 největších souborů**.  
5. Výstup musí být čitelný (velikost v MB).

### **Úkol 2: "Smart Log Rotator" ([`rotate_logs.py`](./rotate_logs.py))**

Simulace archivace starých logů. Skript obsahuje funkci `setup_dummy_logs`, která vytvoří testovací data s různým stářím.

1. Spusťte skript, aby se vygenerovala složka `logs/`.  
2. Implementujte funkci `rotate_logs`:  
   * Vytvořte složku `logs/archive`.  
   * Projděte `.log` soubory.  
   * Pokud je soubor starší než **7 dní**: Přesuňte ho do archivu a přejmenujte (přidejte datum).  
   * Pokud je soubor v archivu starší než **30 dní**: Smaže se.  
   * *Tip:* Čas modifikace zjistíte přes `os.path.getmtime()` a porovnáte s `time.time()`.

### **Úkol 3: "Organizace souborů" ([`organize.py`](./organize.py))**

Uklidíme složku s "nepořádkem".

1. Skript vygeneruje testovací soubory (`test.jpg`, `doc.pdf`...).  
2. Doplňte logiku třídění do podsložek (`Images`, `Docs`, `Archives`, `Scripts`).  
3. **Kritické:** Ošetřete **kolize názvů**. Pokud `image.jpg` už v cíli existuje, nový soubor se musí jmenovat `image_1.jpg`. Nepřepisujte data!

### **Úkol 4: Replikace přikazu tree ([`replicate_tree.py`](./replicate_tree.py))**

Napište skript, který zkopíruje strukturu adresářů (tree), ale **bez souborů**.

1. Vstup: Zdrojová složka a cílová složka.  
2. Použijte `os.walk` pro průchod zdrojem.  
3. V cíli vytvářejte odpovídající prázdné složky pomocí `os.makedirs`.  
4. Soubory ignorujte.