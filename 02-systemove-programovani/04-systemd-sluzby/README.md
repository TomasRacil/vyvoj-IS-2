# **04 - Systemd a Systémové služby**

Když vyvíjíte backendovou aplikaci (v Pythonu, Node.js, Javě), nestačí ji jen spustit v terminálu. Potřebujete, aby běžela na pozadí, **automaticky se spustila po startu serveru** a **restartovala se**, pokud spadne.

V Linuxu se o toto stará **init systém** (nejčastěji **Systemd**). Ve Windows jsou to **Windows Services**.

## **1. Co je to Systemd?**

Systemd je správce systému a služeb pro Linux. Je to první proces, který se spustí po startu jádra (má **PID 1**). Jeho úkolem je inicializovat uživatelský prostor a spravovat ostatní procesy.

### **Klíčové komponenty:**

* **systemctl:** Hlavní příkaz pro ovládání služeb (start, stop, restart).  
* **journalctl:** Příkaz pro čtení logů (vše, co služba vypíše na stdout/stderr, zachytí Systemd).  
* **Unit files (.service):** Konfigurační soubory definující, jak se má služba chovat.

## **2. Správa služeb: Linux vs. Windows**

| Akce | Linux (Systemd) | Windows (PowerShell) |
| :---- | :---- | :---- |
| **Výpis služeb** | `systemctl list-units --type=service` | `Get-Service` |
| **Stav služby** | `systemctl status <name>` | `Get-Service -Name <name>` |
| **Start služby** | `sudo systemctl start <name>` | `Start-Service -Name <name>` |
| **Stop služby** | `sudo systemctl stop <name>` | `Stop-Service -Name <name>` |
| **Restart služby** | `sudo systemctl restart <name>` | `Restart-Service -Name <name>` |
| **Povolení po startu** | `sudo systemctl enable <name>` | `Set-Service -Name <name> -StartupType Automatic` |
| **Zakázání po startu** | `sudo systemctl disable <name>` | `Set-Service -Name <name> -StartupType Disabled` |

## **3. Struktura Systemd Unit souboru**

Aby Systemd věděl, jak vaši aplikaci spustit, vytvoříte soubor s koncovkou `.service` (obvykle v `/etc/systemd/system/`).

Příklad `moje-aplikace.service`:

```text
[Unit]  
Description=Moje skvělá Python služba  
After=network.target  # Spustit až po nahození sítě

[Service]  
Type=simple  
User=mujuzivatel  
WorkingDirectory=/opt/moje-aplikace  
ExecStart=/usr/bin/python3 /opt/moje-aplikace/main.py  
Restart=on-failure    # Restartovat, pokud proces spadne (exit code != 0)  
RestartSec=5          # Počkat 5s před restartem  
Environment=PORT=8080 # Nastavení proměnných prostředí

[Install]  
WantedBy=multi-user.target # Úroveň běhu (běžný serverový režim)
```

## **4. Windows Services (Specifika)**

Na Windows je spuštění běžného Python skriptu jako služby složitější než na Linuxu. Windows Service očekává speciální API pro komunikaci se správcem služeb.

Máte dvě možnosti:

1. **NSSM (Non-Sucking Service Manager):** Velmi populární nástroj třetí strany, který "obalí" jakýkoliv `.exe` nebo skript (Python, Bat) a udělá z něj Windows Službu.  
2. **Knihovna `pywin32`:** Úprava Python kódu tak, aby implementoval Windows Service API.

*V rámci cvičení se zaměříme primárně na Linux/Systemd, který je průmyslovým standardem pro běh serverových aplikací.*

## **5. Praktické ukázky**

V této složce naleznete:

* [`dummy_service.py`](./dummy_service.py): Jednoduchý Python skript simulující dlouhodobě běžící službu.  
* [`dummy_service.service`](./dummy_service.service): Vzorový konfigurační soubor pro Systemd.

## **6. Cvičení (Úkoly)**

### **Úkol 1: Příprava skriptu**

1. Prohlédněte si `dummy_service.py`. Všimněte si, že implementuje obsluhu signálů (z minulé lekce) a vypisuje logy se značkami času.  
2. Zkuste si ho spustit ručně v terminálu: `python3 dummy_service.py`.  
3. Ukončete ho `Ctrl+C`.

### **Úkol 2: Instalace Systemd služby (Linux/WSL)**

*Pokud jste na Windows bez WSL, tento úkol pouze prostudujte.*

1. Upravte soubor `dummy_service.service`:  
   * Změňte `User=` na své uživatelské jméno (zjistíte příkazem `whoami`).  
   * Změňte cesty v `WorkingDirectory` a `ExecStart` tak, aby odpovídaly tomu, kde máte soubor `dummy_service.py` uložený (použijte absolutní cesty, např. `/home/student/vyvoj-IS-2/...`).  
2. Zkopírujte (nebo nalinkujte) soubor do systémové složky:
   ```bash  
   sudo cp dummy_service.service /etc/systemd/system/
   ```

3. Řekněte Systemd, aby načetl novou konfiguraci:
   ```bash
   sudo systemctl daemon-reload
   ```

### **Úkol 3: Ovládání služby**

1. Spusťte službu:
   ```bash
   sudo systemctl start dummy_service
   ```

2. Ověřte, že běží:
   ```shell
   sudo systemctl status dummy_service
   ```

   *Měli byste vidět zelené "active (running)" a posledních pár řádků logu.*

### **Úkol 4: Logování a Restart**

1. Sledujte logy služby v reálném čase:
   ```bash
   journalctl -u dummy_service -f
   ```

2. V druhém okně službu "zabijte" (simulace pádu):
   ```bash
   sudo kill -9 <PID_služby>
   ```

   *(PID najdete v `status` nebo `pgrep`)*  
3. Sledujte v `journalctl`, co se stane. Systemd by měl zaregistrovat pád a po 5 sekundách službu **automaticky restartovat** (díky `Restart=on-failure`).

### **Úkol 5: Úklid**

Po dokončení cvičení službu zastavte a odstraňte, aby vám neběžela na pozadí navždy.

1. `sudo systemctl stop dummy_service`
2. `sudo systemctl disable dummy_service`  
3. `sudo rm /etc/systemd/system/dummy_service.service`
4. `sudo systemctl daemon-reload`