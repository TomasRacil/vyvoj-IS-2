#!/bin/bash

# Úkol 4: Rotující zálohování
# 1. Skript přijme cestu ke složce jako argument.
# 2. Vytvoří tar.gz archiv v BACKUP_DIR.
# 3. Smaže staré zálohy, aby jich zůstalo jen 5.

BACKUP_DIR="./backups"
SOURCE_DIR=$1
DATUM=$(date +%Y%m%d_%H%M%S)

# Kontrola argumentu
if [ -z "$SOURCE_DIR" ]; then
    echo "Chyba: Musíte zadat složku k zálohování."
    echo "Použití: ./backup.sh <složka>"
    exit 1
fi

# Vytvoření složky pro zálohy
mkdir -p "$BACKUP_DIR"

# Název archivu
ARCHIV="$BACKUP_DIR/backup_$DATUM.tar.gz"

echo "Zálohuji $SOURCE_DIR do $ARCHIV..."

# Vytvoření archivu (potlačíme chyby 2>/dev/null)
tar -czf "$ARCHIV" "$SOURCE_DIR" 2>/dev/null

if [ $? -eq 0 ]; then
    echo "Záloha úspěšná."
else
    echo "Chyba při vytváření archivu!"
    exit 1
fi

# --- ZDE DOPLŇTE LOGIKU ROTACE ---
# Tip: Použijte ls -t (seřadit podle času) a tail
# ls -t "$BACKUP_DIR"/*.tar.gz | tail -n +6 ...

echo "Rotace záloh zatím není implementována."