# **05 - Analýza logů a Regulární výrazy**

Logy jsou základním zdrojem pravdy o tom, co se děje na serveru. V této lekci se naučíme dvě techniky:

1. **Post-mortem analýza:** Zpracování starých logů ze souboru (např. statistiky návštěvnosti).  
2. **Real-time monitoring:** Sledování živého toku dat a okamžitá reakce na chyby (alerting).

## **1. Regulární výrazy (Regex)**

Tato lekce předpokládá, že máte základní povědomí o tom, jak regulární výrazy fungují. Podrobné vysvětlení syntaxe a principů naleznete v [tomto repozitáři](https://github.com/TomasRacil/informatika-2/tree/master/05-pokrocily-python/11-regularni-vyrazy).

Zde budeme regexy využívat prakticky pomocí Python modulu re k extrakci dat (IP adresy, status kódy) z textových řetězců.

## **2. Zdroje dat: Soubor vs. Stream**

### **Statický soubor (File)**

Klasický přístup. Otevřeme soubor [`server.log`](./server.log), přečteme ho řádek po řádku, spočítáme data a zavřeme ho.

* **Použití:** Měsíční reporty, hledání příčiny včerejšího výpadku.

### **Dynamický stream (Pipe)**

Unixová filosofie: *"Všechno je soubor"*. Můžeme vzít výstup jednoho programu (např. `journalctl -f`, který vypisuje logy živě) a **přesměrovat (pipe `|`)** ho do našeho Python skriptu.

* **Příkaz:** `journalctl -f | python3 02_realtime_monitor.py`  
* **Python kód:** Nečte soubor `open()`, ale čte `sys.stdin` (standardní vstup).  
* **Použití:** Okamžité upozornění na Slack/Email, když se v logu objeví "CRITICAL".

## **3. Praktické ukázky**

V této složce naleznete:

* [`server.log`](./server.log): Statický soubor se vzorovými daty (přístupy a chyby).  
* [`01_log_stats.py`](01_log_stats.py): Skript pro statickou analýzu (počítání IP adres).  
* [`02_realtime_monitor.py`](./02_realtime_monitor.py): Skript pro čtení ze standardního vstupu (propojení s journalctl).

## **4. Cvičení (Úkoly)**

### **Úkol 1: Statická analýza (Statistiky)**

1. Spusťte `python3 01_log_stats.py`.  
2. Skript analyzuje soubor [`server.log`](./server.log) a vypíše nejčastější IP adresy.  
3. **Zadání:** Upravte skript tak, aby kromě IP adres počítal i **status kódy** (např. kolikrát nastala chyba 404). Regex skupina pro status je již připravena.

### **Úkol 2: Real-time monitoring (Bash Pipe)**

*Tento úkol vyžaduje Linux/WSL a příkaz journalctl.*

1. Prohlédněte si kód [`02_realtime_monitor.py`](./02_realtime_monitor.py). Všimněte si, že používá `sys.stdin`.  
2. Spusťte monitoring v terminálu:
   ```bash
   # Sledujeme systémové logy a filtrujeme je naším skriptem  
   journalctl -f | python3 02_realtime_monitor.py
   ```

3. Otevřete **druhý terminál** a vygenerujte logovací zprávu:
   ```bash
   logger "Toto je testovaci zprava"  
   logger "Pozor critical error v databazi"
   ```

4. V prvním okně byste měli vidět, že skript zprávu zachytil. Pokud zpráva obsahuje "error" nebo "fail", skript ji zvýrazní (vykřičníky, velká písmena).

### **Úkol 3: Hledání SSH útoků**

Pokud máte na stroji běžící SSH server (nebo WSL), zkuste monitorovat pokusy o přihlášení.

1. Spusťte monitor: `journalctl -u ssh -f | python3 02_realtime_monitor.py` (nebo `-u sshd`).  
2. Zkuste se přihlásit přes SSH s špatným heslem (`ssh localhost`).  
3. Váš Python skript by měl v reálném čase vypisovat řádky o selhání autentizace (`"Failed password..."`).