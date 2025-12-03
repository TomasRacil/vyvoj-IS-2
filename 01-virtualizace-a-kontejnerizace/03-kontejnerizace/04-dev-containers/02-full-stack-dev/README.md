# **Příklad 02: Full-Stack Vývoj (Centralizovaná konfigurace)**

V tomto scénáři simulujeme profesionální **Monorepo**. Máme jeden repozitář, který obsahuje backend, frontend i databázi.

Abychom udrželi zdrojové kódy čisté, veškerá konfigurace pro VS Code a Docker je v centrální složce `.devcontainer` v kořenu projektu.

## **Struktura projektu**

Všimněte si, že složky backend a frontend obsahují **pouze** zdrojový kód.

```
/02-full-stack-dev  
├── docker-compose.yml          <-- HLAVNÍ DEFINICE INFRASTRUKTURY  
│  
├── .devcontainer/              <-- CENTRÁLNÍ KONFIGURACE (zde je ten rozdíl)  
│   ├── backend/  
│   │   └── devcontainer.json   <-- "Jsem backend vývojář, připoj mě k Pythonu"  
│   └── frontend/  
│       └── devcontainer.json   <-- "Jsem frontend vývojář, připoj mě k Node.js"  
│  
├── /backend                    <-- Čistý Python projekt (žádný balast)  
│   └── app.py  
│  
└── /frontend                   <-- Čistý Node.js projekt  
    └── package.json
```

## **Jak pracovat (Workflow)**

Postup je velmi podobný, ale při otevírání složky ve VS Code musíme být přesní.

### **Scénář A: Jsem Backend Vývojář**

1. Ve VS Code otevřete **kořenovou složku** `02-full-stack-dev`.  
2. Stiskněte `F1` a zvolte **Dev Containers: Reopen in Container...**  
3. VS Code se vás zeptá: *"Kterou definici chcete použít?"*  
4. Vyberte **Backend (Python)**.  
5. VS Code nastartuje celý stack (pomocí `docker-compose.yml` v kořenu), ale vás "přenese" do backend kontejneru.

### **Scénář B: Jsem Frontend Vývojář**

1. Ve VS Code otevřete **kořenovou složku** `02-full-stack-dev` (např. v novém okně).  
2. Zvolte **Dev Containers: Reopen in Container...**  
3. Vyberte **Frontend (Node.js)**.  
4. Jste v prostředí s Node.js.

## **Výhoda**

Zdrojový kód je oddělený od nástrojů (IDE). Pokud se rozhodnete přejít z VS Code na jiný editor, složky `backend` a `frontend` zůstávají čisté.