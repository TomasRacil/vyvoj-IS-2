# **01. Bash Scripting v praxi**

I když je Python velice silný nástroj, pro rychlé operace se soubory a pipes je Bash stále vhodnější. Správce systému musí umět napsat jednorázový script přímo v terminálu.

## **Teorie: Základy Bashe**

Bash (Bourne Again SHell) je interpret příkazů. Skript je jen soubor s příkazy, které byste jinak psali ručně.

### **1. Proměnné**

V Bashi se proměnné přiřazují bez mezer kolem `=`.  
K jejich hodnotě přistupujeme pomocí `$`.

```bash
JMENO="Student"  
echo "Ahoj $JMENO"
```

### **2. Speciální proměnné**

* `$0` - Název skriptu.  
* `$1`, `$2`... - Argumenty předané skriptu (první, druhý...).  
* `$?` - Návratový kód posledního příkazu (0 = OK, cokoliv jiného = Chyba).  
* `$#` - Počet argumentů.

### **3. Podmínky (if)**

Používáme `if [ podminka ]; then ... fi`. Mezery uvnitř `[ ]` jsou povinné!

```bash
if [ -f "/etc/passwd" ]; then  
    echo "Soubor existuje"  
elif [ -d "/etc" ]; then  
    echo "Je to složka"  
else  
    echo "Nic"  
fi
```

**Užitečné přepínače pro podmínky:**

* **Soubory a složky:**  
  * `-f "cesta"`: True, pokud soubor existuje a je to soubor.  
  * `-d "cesta"`: True, pokud složka existuje.  
  * `-e "cesta"`: True, pokud "něco" (soubor nebo složka) existuje.  
* **Řetězce:**  
  * `-z "$VAR"`: True, pokud je proměnná prázdná (délka nula).  
  * `-n "$VAR"`: True, pokud proměnná NENÍ prázdná.  
  * `"$A" == "$B"`: Porovnání shody textu.  
  * `"$A" != "$B"`: Nerovná se.  
* **Čísla (POZOR: nepoužívejte >, <, ale písmena):**  
  * `-eq`: Rovná se (EQual).  
  * `-ne`: Nerovná se (Not Equal).  
  * `-gt`: Větší než (Greater Than) - např. [ `5 -gt 2` ].  
  * `-lt`: Menší než (Less Than).  
  * `-ge`: Větší nebo rovno (Greater or Equal).  
  * `-le`: Menší nebo rovno (Less or Equal).

### **4. Cykly (Loops)**

Pro automatizaci opakovaných úloh jsou cykly klíčové.

For cyklus: Prochází seznam položek (soubory, čísla, řetězce).  
# Projde všechny .log soubory v aktuálním adresáři

```bash
for soubor in *.log; do  
    echo "Zpracovávám: $soubor"  
    mv "$soubor" "$soubor.old"  
done
```

While cyklus: Běží, dokud je podmínka pravdivá.  

```bash
# Čte soubor řádek po řádku  
count=1  
while read radek; do  
    echo "Řádek $count: $radek"  
    ((count++))  
done < seznam.txt
```

### **5. Roury (Pipes) a Přesměrování**

To, co dělá Linux silným, je spojování programů.

* `|` (Pipe): Výstup jednoho programu pošle jako vstup druhému.  
  * `ls -l | grep ".txt"` (Zobraz jen textové soubory).  
* `>` (Redirect): Uloží výstup do souboru (přepíše ho).  
  * `echo "Log" > soubor.txt`  
* `>>` (Append): Přidá na konec souboru.  
* `2>` (Error Redirect): Přesměruje chybová hlášení.  
  * `find / -name "tajne" 2>/dev/null` (Zahoď chyby "Permission denied").

### **6. Užitečné příkazy pro skriptování**

V úlohách budete potřebovat tyto základní Linuxové nástroje:

* **`touch soubor`**: Vytvoří prázdný soubor (nebo aktualizuje čas změny, pokud už existuje).  
* **`mv co kam`**: Přesune nebo přejmenuje soubor (Move).  
  * *Příklad:* `mv data.txt data.bak` (přejmenování).  
* **`cp co kam`**: Zkopíruje soubor (Copy).  
* **`rm soubor`**: Smaže soubor (Remove).  
* **`date`**: Vypíše aktuální datum.  
* `wc` (Word Count): Počítá řádky, slova nebo znaky.  
  * `wc -c`: Počet znaků (bytes).  
  * `wc -l`: Počet řádků.  
  * *Příklad:* `wc -c < soubor.txt` (zjistí velikost souboru).



## **Klíčové koncepty pro adminy**

* **Exit Codes (`$?`):** Každý příkaz vrací číslo. `0` = OK, cokoli jiného = Chyba. Skript by měl končit `exit 0` nebo `exit 1` při chybě.  
* **Command Substitution (`$(...)`):** Uložení výstupu příkazu do proměnné.  
  * `DATUM=$(date +%F)`

## **Praktické úkoly**

Pro procvičení si vyzkoušíme čtyři samostatné úkoly od jednoduchých po složité.

### **Jak spustit skript? Oprávnění v Linuxu**

Než se pustíte do úkolů, je klíčové pochopit, jak skript spustit. Nestačí ho jen napsat.

1.  **Shebang (`#!/bin/bash`)**
    Na úplně první řádek každého Bash skriptu patří tzv. "shebang". Říká systému, jakým interpretem má skript spustit.
    ```bash
    #!/bin/bash
    echo "Tento skript se spustí pomocí Bashe."
    ```

2.  **Oprávnění ke spuštění (`chmod`)**
    V Linuxu má každý soubor oprávnění pro tři kategorie uživatelů: **vlastníka** (user), **skupinu** (group) a **ostatní** (others). Oprávnění jsou pro **čtení** (`r`), **zápis** (`w`) a **spuštění** (`x`).

    Když vytvoříte nový soubor, standardně nemá oprávnění ke spuštění. Musíte mu ho explicitně přidat příkazem `chmod` (change mode).

    ```bash
    # Přidá (+) oprávnění ke spuštění (x) pro všechny uživatele
    chmod +x muj_skript.sh
    ```

3.  **Spuštění skriptu**
    Jakmile má skript oprávnění, můžete ho spustit. Pokud jste ve stejné složce jako skript, musíte použít prefix `./`, který říká "spusť soubor z tohoto adresáře".

    ```bash
    # Spustí skript, který je v aktuální složce
    ./muj_skript.sh
    ```
    Proč `./`? Z bezpečnostních důvodů není aktuální adresář standardně v systémové cestě (`$PATH`), takže musíte explicitně uvést, kde se soubor nachází.

### **Úkol 1: "Hello User" (Argumenty a Proměnné)**

Vytvořte skript `hello.sh`, který:

1. Přijme **jméno** jako první argument.  
2. Pokud argument chybí, vypíše: "Chyba: Zadej jméno" a skončí s chybou.  
3. Pokud je jméno zadáno, vypíše: "Ahoj [Jméno], dnes je [Aktuální Datum]".

**Tip:** Datum získáte příkazem date.

### **Úkol 2: "Hromadné přejmenování" (Cykly)**

Vytvořte skript `rename_logs.sh`, který:

1. Vytvoří testovací soubory `test1.log`, `test2.log`, `test3.log` (pro účely testování).  
2. Pomocí cyklu `for` projde všechny `.log` soubory v aktuálním adresáři.  
3. Každý soubor přejmenuje tak, že mu přidá příponu `.bak` (např. `test1.log.bak`).  
4. Vypíše "Zálohuji: [původní] -> [nový]".

**Tip:** Pro vytvoření prázdných souborů použijte příkaz `touch`.

### **Úkol 3: "Sledování velikosti" (Podmínky a Příkazy)**

Vytvořte skript `check_size.sh`, který:

1. Přijme název souboru jako argument.  
2. Zjistí, zda soubor existuje.  
3. Pokud neexistuje, vypíše chybu.  
4. Pokud existuje, zjistí jeho velikost.  
5. Pokud je soubor větší než 1000 bytů, vypíše "VELKÝ SOUBOR". Jinak vypíše "MALÝ SOUBOR".

**Tip:** Velikost souboru v bytech zjistíte příkazem `wc -c < soubor`.

### **Úkol 4 (Bonus): "Rotující Zálohování" (Komplexní úloha)**

Toto je reálný scénář, se kterým se setkáte v praxi. Vytvořte skript backup.sh, který zazálohuje složku, ale nenechá disk zaplnit starými zálohami.

**Zadání:**

1. Skript přijme cestu ke složce jako argument.  
2. Vytvoří .tar.gz archiv s časovým razítkem v názvu do složky /tmp/backups.  
3. **Logika rotace:** Ponechá pouze **5 nejnovějších záloh**, starší automaticky smaže.

**Tip pro rotaci:** Použijte kombinaci ls -t (seřadit podle času) a tail nebo find.