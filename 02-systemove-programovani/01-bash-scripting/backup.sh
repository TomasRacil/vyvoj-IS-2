#!/bin/bash

# Uložíme si první argument do proměnné  
SOURCE_DIR=$1  
# Cesta, kam budeme zálohovat (používáme /tmp pro testování)  
BACKUP_DIR="/tmp/backups"  
# Aktuální datum a čas (např. 20231012_140000)  
TIMESTAMP=$(date +%Y%m%d_%H%M%S)  
# Název výsledného souboru  
BACKUP_NAME="backup_$TIMESTAMP.tar.gz"

# 1. Validace vstupu: Zkontolujeme, zda uživatel zadal cestu (-z znamená "je prázdný")  
if [ -z "$SOURCE_DIR" ]; then  
    echo "Chyba: Použití: $0 <cesta_k_zaloze>"  
    # Ukončíme skript s chybovým kódem 1  
    exit 1  
fi

# Vytvoříme složku pro zálohy, pokud neexistuje (-p nevypíše chybu, když už existuje)  
mkdir -p "$BACKUP_DIR"

# 2. Vytvoření zálohy pomocí tar  
# c = create, z = gzip komprese, f = file (výstup do souboru)  
echo "Vytvářím zálohu $BACKUP_NAME..."  
tar -czf "$BACKUP_DIR/$BACKUP_NAME" "$SOURCE_DIR" 2>/dev/null

# Zkontrolujeme návratový kód taru ($?)  
if [ $? -eq 0 ]; then  
    echo "Záloha úspěšná."  
else  
    echo "Chyba při tarování!"  
    exit 2  
fi

# 3. Rotace (Ponechat jen 5 nejnovějších)  
echo "Čistím staré zálohy..."  
cd "$BACKUP_DIR"

# ls -t: Seřadí soubory podle času (nejnovější nahoře)  
# tail -n +6: Vypíše vše od 6. řádku dál (tedy přeskočí 5 nejnovějších)  
# xargs -r rm --: Pro každý řádek zavolá příkaz rm (smaže ho)  
ls -t *.tar.gz 2>/dev/null | tail -n +6 | xargs -r rm --

echo "Hotovo."  