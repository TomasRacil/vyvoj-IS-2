#!/bin/bash

SOUBOR=$1

if [ ! -f "$SOUBOR" ]; then
    echo "Chyba: Soubor neexistuje."
    exit 1
fi

# Získání velikosti (wc -c vrátí číslo)
VELIKOST=$(wc -c < "$SOUBOR")

echo "Velikost souboru je: $VELIKOST bytů"

# Porovnání čísel (-gt znamená Greater Than - větší než)
if [ $VELIKOST -gt 1000 ]; then
    echo "VELKÝ SOUBOR"
else
    echo "MALÝ SOUBOR"
fi
