# 1. BASE IMAGE (Základní vrstva)
# Každý Dockerfile musí začínat příkazem FROM.
# Říkáme tím: "Vezmi oficiální obraz Pythonu ve verzi 3.9 (verze slim je ořezaná a menší)"
# Tento obraz už obsahuje nainstalovaný Linux (Debian) a Python.
FROM python:3.9-slim

# 2. WORKDIR (Pracovní adresář)
# Vytvoří uvnitř kontejneru složku /app a přepne se do ní.
# Všechny další příkazy (COPY, RUN, CMD) se budou provádět v této složce.
# Je to jako příkaz 'cd /app' a 'mkdir /app'.
WORKDIR /app

# 3. INSTALACE ZÁVISLOSTÍ (Dependencies)
# Spustíme příkaz uvnitř kontejneru.
# Zde instalujeme knihovnu Flask pomocí pip.
# V reálném projektu byste spíše kopírovali requirements.txt a instalovali z něj.
RUN pip install flask

# 4. COPY (Kopírování kódu)
# Příkaz má formát: COPY <co_na_mém_PC> <kam_do_kontejneru>
# Tečka znamená "aktuální adresář".
# Takže kopírujeme soubor app.py z našeho počítače do složky /app v kontejneru.
COPY app.py .

# 5. CMD (Příkaz po spuštění)
# Toto je příkaz, který se vykoná ve chvíli, kdy napíšete 'docker run'.
# Spustí náš Python skript.
CMD ["python", "app.py"]