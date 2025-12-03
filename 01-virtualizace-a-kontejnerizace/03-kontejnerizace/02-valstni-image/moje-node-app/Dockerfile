# 1. BASE IMAGE
# Používáme Node.js ve verzi 14 postavený na Alpine Linuxu.
# Alpine je extrémně malá distribuce Linuxu (cca 5 MB), ideální pro kontejnery.
FROM node:14-alpine

# 2. WORKDIR
# Vytvoříme složku pro aplikaci uvnitř kontejneru.
# Standardně se v Linuxu dávají aplikace do /usr/src/...
WORKDIR /usr/src/app

# 3. COPY (Kód)
# Kopírujeme soubor app.js do pracovního adresáře.
COPY app.js .

# 4. EXPOSE (Informace o portu)
# Tento příkaz je spíše dokumentační. Říká ostatním vývojářům (a Dockeru),
# že aplikace uvnitř naslouchá na portu 3000.
# Samotné zpřístupnění ven musíte ale udělat při 'docker run -p'.
EXPOSE 3000

# 5. CMD (Start)
# Spustíme aplikaci pomocí node.
CMD [ "node", "app.js" ]