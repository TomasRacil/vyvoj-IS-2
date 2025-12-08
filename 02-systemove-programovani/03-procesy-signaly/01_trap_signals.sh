#!/bin/bash

# Vytvoříme dočasný soubor, který budeme chtít po sobě uklidit
TEMP_FILE="/tmp/moje_data_$$.txt"
touch "$TEMP_FILE"

echo "Byl vytvořen dočasný soubor: $TEMP_FILE"
echo "PID skriptu: $$"

# Funkce pro úklid
cleanup() {
    echo ""
    echo "!!! Byl zachycen signál k ukončení !!!"
    echo "Mažu dočasný soubor $TEMP_FILE..."
    rm -f "$TEMP_FILE"
    echo "Úklid hotov. Končím."
    exit 0
}

# Příkaz trap "past"
# Říká: Pokud přijde signál SIGINT (Ctrl+C) nebo SIGTERM, spusť funkci 'cleanup'
trap cleanup SIGINT SIGTERM

echo "Skript běží. Zkuste zmáčknout Ctrl+C."
echo "Pokud proces zabijete přes 'kill -9', trap se nespustí a soubor v /tmp zůstane."

count=1
while true; do
    echo "Běžím... $count"
    sleep 2
    ((count++))
done