# **01. Bash Scripting v praxi**

I když je Python velice silný nástroj, pro rychlé operace se soubory a pipes je Bash stále vhodnější. Správce systému musí umět napsat jednorázový script přímo v terminálu.

## **1. Bash vs. PowerShell (Windows)**

Než začneme: Bash je nativní pro Linux/macOS. Na Windows jej můžete používat přes **Git Bash** nebo **WSL**.

| Koncept | Bash (Linux) | PowerShell (Windows) |
| :---- | :---- | :---- |
| Proměnná | `NAME="Petr"` | `$Name = "Petr"` |
| Výpis | `echo $NAME` | `Write-Host $Name` |
| Podmínka | `if [ -f "file" ]; ...` | `if (Test-Path "file") { ... }` |
| Smyčka | `for i in {1..5}; ...` | `for (($i = 1); $i -lt 5; $i++){...}` |

## **2. Teorie: Základy Bashe**

Bash (Bourne Again SHell) je interpret příkazů. Skript je jen soubor s příkazy, které byste jinak psali ručně.

### **Proměnné**

V Bashi se proměnné přiřazují bez mezer kolem `=`.  
K jejich hodnotě přistupujeme pomocí `$`.

```bash
JMENO="Student"  
echo "Ahoj $JMENO"
```

### **Speciální proměnné**

* `$0` - Název skriptu.  
* `$1`, `$2`... - Argumenty předané skriptu (první, druhý...).  
* `$?` - Návratový kód posledního příkazu (0 = OK, cokoliv jiného = Chyba).  
* `$#` - Počet argumentů.

### **Podmínky (if)**

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

### **Cykly (Loops)**

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

### **Roury (Pipes) a Přesměrování**

To, co dělá Linux silným, je spojování programů.

* `|` (Pipe): Výstup jednoho programu pošle jako vstup druhému.  
  * `ls -l | grep ".txt"` (Zobraz jen textové soubory).  
* `>` (Redirect): Uloží výstup do souboru (přepíše ho).  
  * `echo "Log" > soubor.txt`  
* `>>` (Append): Přidá na konec souboru.  
* `2>` (Error Redirect): Přesměruje chybová hlášení.  
  * `find / -name "tajne" 2>/dev/null` (Zahoď chyby "Permission denied").

### **Užitečné příkazy pro skriptování**

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
  
## **3. Jak spustit skript?**

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


## **4. Praktické úkoly**

V této složce naleznete předpřipravené soubory ([`hello.sh`](./hello.sh), [`check_size.sh`](./check_size.sh), [`backup.sh`](./backup.sh), [`rename_logs.sh`](./rename_logs.sh)).

### **Úkol 1: Hello User**

1. Spusťte skript [`hello.sh`](./hello.sh).  
2. Upravte ho tak, aby:  
   * Přijal **jméno** jako první argument (`$1`).  
   * Pokud argument chybí (`-z "$1"`), vypíše: "Chyba: Zadej jméno" a skončí s chybou (`exit 1`).  
   * Pokud je jméno zadáno, vypíše: `"Ahoj [Jméno], dnes je [Aktuální Datum]"` (použijte příkaz date).

### **Úkol 2: Hromadné přejmenování**

1. Vytvořte si pomocné soubory: `touch test1.log test2.log test3.log`.  
2. Otevřete [`rename_logs.sh`](./rename_logs.sh).  
3. Doplňte do něj `for` cyklus, který projde všechny `.log` soubory.  
4. Každý soubor přejmenujte tak, že mu přidáte příponu `.bak`.  
5. Vypište `"Zálohuji: [původní] -> [nový]"`.

### **Úkol 3: Sledování velikosti**

1. Otevřete [`check_size.sh`](./check_size.sh).  
2. Skript by měl přijmout název souboru jako argument.  
3. Zjistěte, zda soubor existuje (`-f`). Pokud ne, vypište chybu.  
4. Pokud existuje, zjistěte jeho velikost (`wc -c < soubor`).  
5. Pokud je větší než 1000 bytů, vypište `"VELKÝ SOUBOR"`, jinak `"MALÝ SOUBOR"`.

### **Úkol 4: Rotující Zálohování**

Toto je reálný scénář. Upravte [`backup.sh`](./backup.sh) tak, aby:

1. Přijal cestu ke složce jako argument.  
2. Vytvořil `.tar.gz` archiv s časovým razítkem do složky `/tmp/backups` (nebo do lokální `backup` složky).  
3. **Logika rotace:** Zajistěte, aby ve složce záloh zůstalo maximálně **5 nejnovějších** souborů. Starší automaticky smažte.  
   * *Tip:* Použijte `ls -t | tail ... | xargs rm` nebo podobnou logiku.