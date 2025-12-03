#!/bin/bash

# Skript pro kontrolu prostředí - Informatika 4 (Linux/macOS)

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}--- KONTROLA PROSTŘEDÍ PRO INFORMATIKU 4 ---${NC}\n"

ALL_OK=true

# 1. Kontrola GIT
printf "[1/4] Kontrola Git... "
if command -v git &> /dev/null; then
    VER=$(git --version)
    echo -e "${GREEN}OK ($VER)${NC}"
else
    echo -e "${RED}CHYBA! Git nebyl nalezen.${NC}"
    ALL_OK=false
fi

# 2. Kontrola VS Code
printf "[2/4] Kontrola VS Code... "
if command -v code &> /dev/null; then
    VER=$(code --version | head -n 1)
    echo -e "${GREEN}OK ($VER)${NC}"
else
    echo -e "${YELLOW}VAROVÁNÍ (příkaz 'code' nenalezen, ale GUI může být nainstalováno)${NC}"
fi

# 3. Kontrola Dockeru
printf "[3/4] Kontrola Dockeru... "
if command -v docker &> /dev/null; then
    VER=$(docker --version)
    echo -e "${GREEN}OK ($VER)${NC}"
    
    printf "      Zkouším připojení k Docker Daemonovi... "
    if docker info &> /dev/null; then
        echo -e "${GREEN}OK (Daemon běží)${NC}"
    else
        echo -e "${RED}CHYBA! (Docker neběží nebo nemáte práva - zkuste sudo?)${NC}"
        ALL_OK=false
    fi
else
    echo -e "${RED}CHYBA! Docker nebyl nalezen.${NC}"
    ALL_OK=false
fi

# 4. Kontrola VirtualBox
printf "[4/4] Kontrola VirtualBox... "
if command -v VBoxManage &> /dev/null; then
    VER=$(VBoxManage --version)
    echo -e "${GREEN}OK ($VER)${NC}"
else
    echo -e "${YELLOW}INFO (VBoxManage nenalezen, zkontrolujte instalaci ručně)${NC}"
fi

echo ""
if [ "$ALL_OK" = true ]; then
    echo -e "${GREEN}VŠE VYPADÁ V POŘÁDKU! JSTE PŘIPRAVENI. ✅${NC}"
else
    echo -e "${RED}NĚKTERÉ NÁSTROJE CHYBÍ. ZKONTROLUJTE VÝPIS VÝŠE. ❌${NC}"
fi