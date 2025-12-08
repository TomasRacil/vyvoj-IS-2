# **02. Systémové programování**

Vítejte v druhém bloku. V minulé části jsme si postavili server. Teď se naučíme, jak ho efektivně ovládat, automatizovat a monitorovat.

Jako správci systému musíte ovládat dva jazyky:

1. **Bash:** Pro rychlé jednorázové úkoly a práci v terminálu.  
2. **Python:** Pro složitější automatizaci, logiku a robustní nástroje.

## **Cíle tohoto bloku**

1. **Bash Scripting:** Naučit se psát skripty pro správu souborů a procesů.  
2. **Python Automation:** Nahradit složité Bash konstrukce čitelným Python kódem.  
3. **Služby (Daemons):** Vytvořit aplikaci, která běží na pozadí (Systemd).  
4. **Logy a Sítě:** Analyzovat logy pomocí Regexu a vytvořit TCP server.

## **Obsah**

| Složka | Téma | Praktický úkol |
| :---- | :---- | :---- |
| [**01. Bash Scripting**](./01-bash-scripting) | Rychlá automatizace v Shellu | **Backup Script:** Automatická archivace a rotace záloh. |
| [**02. Python Automation**](./02-python-scripting) | Pokročilá práce s FS (shutil, pathlib) | **Smart Cleanup:** Inteligentní promazávání starých dat. |
| [**03. Procesy a Watchdogs**](./03-procesy-signaly) | Řízení procesů (subprocess, signal) | **Service Watchdog:** Skript, který hlídá a restartuje jiné aplikace. |
| [**04. Systemd Daemons**](./04-systemd-sluzby) | Tvorba systémových služeb | **MyService:** Registrace Python skriptu do Systemd. |
| [**05. Logy a Sítě**](./05-logy-site) | Regex analýza a Sockets | **Log Parser** & **Chat Server** (Backend pro Android). |
| [**06. Chat Server**](./06-chat-server) | Síťová komunikace (Sockets) | Chat Backend: Multithreaded TCP server. |
| [**07. Propojení s Androidem**](./07-android-klient) | Integrace a sítě (NAT, Firewall) | **End-to-End Test:** Spojení fyzického telefonu s virtuálním serverem. |

## **Prerekvizity**

Budete potřebovat běžící Linux (vaše VM z minula nebo Docker kontejner).

# Ověření
```bash
bash --version  
python3 --version
```