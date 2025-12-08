# **03 - Procesy a signály**

V této sekci se podíváme na to, co je to proces, jak vzniká, jak zaniká a jak jej můžeme ovládat pomocí signálů. Pochopení těchto konceptů je nezbytné pro správu serverů, psaní služeb na pozadí (daemon) a robustních skriptů.

## **1. Co je to proces?**

Proces je instance běžícího programu. Zatímco program je pasivní soubor na disku (binárka, skript), proces je aktivní entita v paměti, které operační systém přidělil zdroje (CPU čas, paměť, otevřené soubory).

### **Klíčové atributy procesu:**

* **PID (Process ID):** Jedinečné číselné ID procesu.  
* **PPID (Parent Process ID):** ID rodičovského procesu, který tento proces spustil.  
* **UID/GID:** Uživatel a skupina, pod kterými proces běží (určuje oprávnění).  
* **Stav:** V jaké fázi se proces nachází.

### **Stavy procesu (Process States)**

Když spustíte příkaz `ps aux` nebo `top`, uvidíte ve sloupci `STAT` nebo `S` kód stavu:

* **R (Running):** Proces běží nebo čeká ve frontě na CPU.  
* **S (Sleeping):** Proces čeká na událost (např. na vstup z klávesnice, data ze sítě, disk). Většina procesů je v tomto stavu.  
* **D (Uninterruptible Sleep):** Proces čeká na I/O operaci a **nelze** ho přerušit signálem (ani `SIGKILL`). Často značí problém s hardwarem (např. síťový disk).  
* **Z (Zombie):** Proces skončil, ale jeho rodič si ještě nepřečetl jeho návratový kód (pomocí `wait()`). Nezabírá paměť, jen záznam v tabulce procesů.  
* **T (Stopped):** Proces byl pozastaven (např. pomocí `Ctrl+Z` nebo signálem `SIGSTOP`).

## **2. Správa procesů: Linux vs. Windows**

Ačkoliv principy jsou stejné, příkazy se liší. Zde je srovnávací tabulka pro Bash a PowerShell.

| Akce | Linux (Bash) | Windows (PowerShell) | Poznámka |
| :---- | :---- | :---- | :---- |
| **Výpis procesů** | `ps aux` nebo `ps -ef` | `Get-Process` (alias `gps`, `ps`) | PowerShell vypisuje objekty, Bash text. |
| **Najít proces dle jména** | `pgrep -a python` | `Get-Process -Name python` |  |
| **Interaktivní sledování** | `top` nebo `htop` | Otevřít *Task Manager* nebo příkaz `top` (pokud je nainstalován) | Windows nemá nativní CLI `htop`, ale existují alternativy. |
| **Ukončení procesu (Soft)** | `kill <PID>`(SIGTERM) | `Stop-Process -Id <PID>` | Na Windows `Stop-Process` často funguje rovnou jako Force kill. |
| **Ukončení procesu (Hard)** | `kill -9 <PID>` (SIGKILL) | `Stop-Process -Id <PID> -Force` | Okamžité ukončení bez úklidu. |
| **Práce na pozadí** | `&` (na konci příkazu) | `Start-Process ... -NoNewWindow` | PowerShell má také joby: `Start-Job`. |

## **3. Signály (Linux) vs. Zprávy (Windows)**

Zde se obě platformy nejvíce rozcházejí.

### **Linux (POSIX)**

Linux používá **signály** pro komunikaci s procesy. Aplikace může signál zachytit a reagovat na něj (např. uložit data před ukončením).

| Signál | Číslo | Význam | Lze zachytit? |
| :---- | :---- | :---- | :---- |
| **SIGINT** | 2 | Přerušení z klávesnice (`Ctrl+C`). | ANO |
| **SIGTERM** | 15 | Žádost o ukončení (výchozí pro `kill`). | ANO |
| **SIGKILL** | 9 | Okamžité ukončení. Proces nemá šanci zareagovat. | **NE** |
| **SIGHUP** | 1 | "Zavěšení". Často používáno pro **reload konfigurace**. | ANO |

### **Windows**

Windows nepoužívá POSIX signály nativně. Používá systém zpráv a událostí (Console Events).

* **Ctrl+C:** Funguje podobně jako SIGINT (Python to umí zachytit na obou systémech).  
* **Kill:** Windows nemá přímý ekvivalent pro "jemný" SIGTERM zaslaný příkazem zvenčí. `Stop-Process` proces obvykle ukončí okamžitě (TerminateProcess API).  
* **SIGHUP:** Na Windows **neexistuje**. Aplikace na Windows obvykle nečtou konfiguraci na základě signálu.  
* **Fork (Zombie):** Windows nepoužívá `fork()` pro tvorbu procesů, takže koncept "Zombie" procesů zde v linuxovém smyslu neexistuje.

## **4. Praktické ukázky**

V této složce naleznete hotové skripty, které slouží jako **inspirace** pro řešení úkolů níže:

* [`01_trap_signals.sh`](./01_trap_signals.sh): Bash skript ukazující, jak zachytit signál a smazat po sobě soubory.  
* [`02_python_handler.py`](./02_python_handler.py): Python skript demonstrující "Graceful Shutdown" (ukončení s úklidem).  
* [`03_zombie_maker.py`](./03_zombie_maker.py): Skript, který záměrně vytvoří chybový stav (Zombie proces) pro studijní účely.

## **5. Cvičení (Úkoly)**

V těchto úkolech nebudete jen spouštět hotové skripty, ale **napíšete si vlastní jednoduchou službu (démona)** a naučíte se ji spravovat.

### **Úkol 1: Tvorba vlastního démona (Python)**

*Funguje na Linux i Windows.*

1. Vytvořte nový soubor `muj_demon.py`.  
2. Naprogramujte v něm nekonečnou smyčku (`while True`), která:  
   * Každé 2 sekundy vypíše aktuální čas a text `"Služba běží..."` (použijte `time.sleep(2)`).  
3. Implementujte obsluhu signálu **SIGINT** (`Ctrl+C`):  
   * Když uživatel stiskne `Ctrl+C`, program **nesmí spadnout** na výjimku `KeyboardInterrupt`.  
   * Místo pádu program zachytí signál, vypíše `"Uklízím data a končím..."`, počká 1 sekundu (simulace ukládání) a teprve poté skončí (`sys.exit(0)`).  
4. **Ověření:** Spusťte program a zkuste ho ukončit pomocí `Ctrl+C`. Měli byste vidět vaši úklidovou hlášku.

### **Úkol 2: Správa démona na pozadí (Terminál)**

*Rozdíly v OS.*

1. Spusťte váš `muj_demon.py` na pozadí.  
   * *Linux:* `python3 muj_demon.py &`  
   * *Windows:* Spusťte ho v novém okně nebo použijte `Start-Process python -ArgumentList "muj_demon.py"`.  
2. Najděte **PID** vašeho běžícího procesu (pomocí `ps`, `pgrep` nebo `Get-Process`).  
3. Pošlete procesu signál pro ukončení.  
   * *Linux:* `kill <PID>` (pošle SIGTERM).  
   * *Windows:* `Stop-Process -Id <PID>`.  
   * **Otázka:** Stihl proces vypsat "Uklízím data...", nebo skončil okamžitě? (Na Linuxu by měl reagovat, na Windows to záleží na implementaci pythonu, často skončí hned).  
4. Zkuste to znovu, ale tentokrát ukončete proces **násilně** (`kill -9` / `-Force`). Hláška o úklidu by se neměla objevit nikdy.

### **Úkol 3: Oprava Zombie procesu (Linux/WSL)**

*Tento úkol vyžaduje Linux/WSL. Na Windows tento mechanismus nefunguje.*

1. Prostudujte a spusťte referenční skript `03_zombie_maker.py`.  
2. Ověřte v druhém terminálu, že vznikl proces ve stavu `Z` (Zombie/Defunct).  
3. **Váš úkol:** Upravte skript 03_zombie_maker.py tak, abyste chybu opravili.  
   * *Nápověda:* Rodičovský proces je zodpovědný za své potomky. Musí zavolat funkci `os.wait()` (nebo `waitpid`), aby si přečetl návratový kód potomka a tím ho "pohřbil".  
4. Ověřte, že po vaší úpravě proces po skončení z výpisu `ps` ihned zmizí.

### **Úkol 4: Reload konfigurace za běhu (Pokročilé - Linux/WSL)**

*Simulace chování serverů jako Nginx. Na Windows tento signál není dostupný.*

1. Vytvořte vedle skriptu soubor `config.txt` a napište do něj číslo (např. `5`). To bude interval čekání.  
2. Upravte váš `muj_demon.py` tak, aby:  
   * Při startu načetl toto číslo ze souboru a použil ho v `time.sleep()`.  
   * Zaregistroval handler pro signál **SIGHUP**.  
   * Když obdrží SIGHUP, **znovu načte** soubor `config.txt` a vypíše `"Konfigurace obnovena: nový interval X"`.  
3. **Experiment:**  
   * Spusťte skript (interval 5s).  
   * Změňte v `config.txt` číslo na `1`.  
   * Pošlete procesu signál: `kill -HUP <PID>`.  
   * Sledujte, zda se skript zrychlil, aniž byste ho museli restartovat.