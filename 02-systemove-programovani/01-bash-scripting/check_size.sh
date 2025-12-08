#!/bin/bash

SOUBOR="data.txt"

# Úkol 3:
# 1. Změňte SOUBOR tak, aby se bral z prvního argumentu ($1).
# 2. Přidejte kontrolu, zda soubor existuje (-f).
# 3. Zjistěte velikost (wc -c).
# 4. Pokud > 1000 bytů, vypište VELKÝ, jinak MALÝ.

# --- ZDE UPRAVTE KÓD ---

if [ -f "$SOUBOR" ]; then
    echo "Soubor $SOUBOR existuje."
    # Zde chybí logika pro velikost...
else
    echo "Chyba: Soubor neexistuje."
fi