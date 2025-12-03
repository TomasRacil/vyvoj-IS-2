# **Příklad 01: Instalace nástrojů**

Abychom mohli začít, musíme dostat do vašeho počítače dva hlavní kusy softwaru. Nebojte se, je to jednorázová akce.

## **1. Instalace VS Code**

Visual Studio Code je lehký, ale výkonný editor zdrojového kódu.

1. Přejděte na [code.visualstudio.com](https://code.visualstudio.com/).  
2. Stáhněte verzi pro váš OS (Windows/macOS/Linux).  
3. Nainstalujte standardním způsobem ("Next, Next, Finish").  
   * *Tip pro Windows:* Při instalaci zaškrtněte políčka **"Add 'Open with Code' action..."**. Hodí se to, když chcete rychle otevřít složku kliknutím pravým tlačítkem.

## **2. Instalace Dockeru**

Docker nám umožní spouštět Linuxové prostředí i na Windows nebo Macu.

### **Pro Windows**

1. Stáhněte a nainstalujte **Docker Desktop** z [docker.com](https://www.docker.com/products/docker-desktop/).  
2. **Důležité:** Během instalace (nebo po ní) budete pravděpodobně vyzváni k instalaci **WSL 2** (Windows Subsystem for Linux). Toto **potvrďte a proveďte**. Docker na Windows potřebuje WSL 2 pro rychlý chod.  
3. Po instalaci restartujte počítač.  
4. Spusťte Docker Desktop a počkejte, až se vlevo dole objeví zelený pruh nebo ikona velryby přestane blikat.

### **Pro macOS**

1. Stáhněte a nainstalujte **Docker Desktop** (verzi pro Intel nebo Apple Silicon podle vašeho procesoru).  
2. Spusťte aplikaci a udělte jí potřebná oprávnění.

### **Pro Linux**

1. Postupujte podle návodu pro vaši distribuci (např. Ubuntu) na [docs.docker.com](https://docs.docker.com/engine/install/).  
2. Nezapomeňte přidat svého uživatele do skupiny docker: `sudo usermod -aG docker $USER` (abyste nemuseli psát sudo před každým příkazem dockeru).

## **3. Instalace rozšíření do VS Code**

Samotný VS Code neumí s Dockerem mluvit napřímo. Potřebujeme "tlumočníka".

1. Otevřete VS Code.  
2. Vlevo na liště klikněte na ikonu kostiček (Extensions) nebo stiskněte `Ctrl+Shift+X` (Mac: `Cmd+Shift+X`).  
3. Do vyhledávání napište: `Dev Containers`.  
4. Nainstalujte rozšíření od Microsoftu (bývá často součástí balíčku "Remote Development").

## **4. Ověření funkčnosti**

Otevřete terminál (ve Windows PowerShell nebo CMD, na Mac/Linux Terminál) a zadejte tyto příkazy. Pokud vypíší verzi, máte vyhráno.

```shell
code --version  
# Mělo by vypsat např.: 1.85.1...
```

```shell
docker --version  
# Mělo by vypsat např.: Docker version 24.0.5...
```

**Problémy?** Pokud `docker` hlásí chybu, ujistěte se, že aplikace Docker Desktop běží na pozadí!