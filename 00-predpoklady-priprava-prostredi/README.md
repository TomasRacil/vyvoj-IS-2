# **Blok 00: Předpoklady a příprava prostředí**
 
V tomto bloku si připravíme pracovní prostředí pro tento výukový blok. Naším cílem je mít funkční prostředí, ve kterém můžeme psát kód, spouštět kontejnery a virtualizovat operační systémy.

## **Rychlý start (Minimum pro první hodinu)**

Pokud spěcháte, ujistěte se, že máte nainstalované nástroje označené jako **Priorita: Vysoká**. Android Studio můžete odložit na později.

| Nástroj | Verze (min.) | K čemu to bude? | Priorita | Detailní návod |
| :---- | :---- | :---- | :---- | :---- |
| [**Git**](./01-git) | 2.30+ | Odevzdávání úkolů a správa verzí. | 🔴 Vysoká | [Jít do složky 01-git](./01-git) |
| [**VS Code**](./02-vscode-docker) | Latest | Hlavní editor pro psaní kódu. | 🔴 Vysoká | [Jít do složky 02-vscode-docker](./02-vscode-docker) |
| [**Docker**](./02-vscode-docker) | 20.10+ | Spouštění izolovaných aplikací. | 🔴 Vysoká | [Jít do složky 02-vscode-docker](./02-vscode-docker) |
| [**VirtualBox**](./03-virtualizace) | 7.0+ | Běh celých operačních systémů (Linux). | 🔴 Vysoká | [Jít do složky 03-virtualizace](./03-virtualizace) |
| [**Android Studio**](./04-android) | Latest | Vývoj mobilních aplikací. | 🟢 Nízká\* | [Jít do složky 04-android](./04-android) |

*\*Poznámka: Instalaci Android Studia můžete odložit až na později, kdy začne blok Mobilní vývoj. Je to velký soubor (několik GB), proto doporučujeme stahovat doma na rychlém připojení.*

## **Ověřte si své prostředí (Skripty)**

Připravil jsem pro vás automatické skripty, které zkontrolují, zda máte vše potřebné nainstalované a nastavené.

### **Pro Windows (PowerShell)**

Stáhněte si skript `test_env_windows.ps1` a spusťte jej v PowerShellu (pravým tlačítkem -> *Run with PowerShell*). *Možná budete muset povolit spouštění skriptů příkazem:* Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

### **Pro macOS / Linux (Bash)**

Otevřete terminál ve složce se skriptem a spusťte:  
```bash
chmod +x test_env_unix.sh  
./test_env_unix.sh
```

Pokud uvidíte všude zelené "OK", jste připraveni na výuku.