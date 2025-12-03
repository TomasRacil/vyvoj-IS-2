#!/bin/bash

# Vytvoření testovacích dat
touch test1.log test2.log test3.log

echo "--- Začínám zálohování ---"

for soubor in *.log; do
    # mv [co] [kam]
    mv "$soubor" "$soubor.bak"
    echo "Zálohuji: $soubor -> $soubor.bak"
done

echo "--- Hotovo ---"
