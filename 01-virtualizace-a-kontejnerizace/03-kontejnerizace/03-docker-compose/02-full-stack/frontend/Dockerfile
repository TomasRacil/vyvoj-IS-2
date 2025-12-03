# Použijeme node image pro vývoj
FROM node:14-alpine

WORKDIR /app

# Nejdříve kopírujeme definice závislostí (caching vrstev)
COPY package.json .

# Instalace závislostí
RUN npm install

# Kopírování zbytku aplikace
COPY . .

# Start aplikace
CMD ["npm", "start"]