#!/bin/bash

# Uložíme 1. argument do proměnné
JMENO=$1

# Kontrola, zda je proměnná prázdná (-z)
if [ -z "$JMENO" ]; then
    echo "Chyba: Zadej jméno!"
    exit 1
fi

DATUM=$(date)
echo "Ahoj $JMENO, dnes je $DATUM"