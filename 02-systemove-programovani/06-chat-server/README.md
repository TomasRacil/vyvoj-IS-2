# **06 - Chat Server: Nasazení a Monitoring**

Cílem této lekce je vzít hotovou backendovou aplikaci (Chat Server) a **nasadíme ji jako profesionální systémovou službu**. Nejsou tu rozebírány sokety a threading, pokud si to chcete připomenout můžete to udělat [zde](https://github.com/TomasRacil/informatika-2/tree/master/05-pokrocily-python).

## **Cíl lekce**

Spojit vše, co jsme se naučili:

1. Spustit Python server, který naslouchá na síti.  
2. Zaregistrovat jej do **Systemd**, aby běžel automaticky po startu a restartoval se při pádu.  
3. Sledovat jeho aktivitu pomocí **Journalctl** a našeho **Log Monitoru** z minulé lekce.

## **1. Architektura**

* **Chat Server (Python):** Běží na portu 12345. Loguje události (připojení, odpojení, chyby) na standardní výstup (`stdout`).  
* **Systemd:** Spravuje proces serveru. Přesměrovává `stdout` do systémového deníku.  
* **Klient:** Android aplikace nebo terminálový skript připojující se k serveru.  
* **Admin (Vy):** Sleduje logy a řídí službu.

## **2. Soubory v této složce**

* [`server.py`](./server.py): Hotový kód serveru. Obsahuje ošetření signálů (SIGTERM) pro korektní ukončení.  
* [`client.py`](./client.py): Testovací klient.  
* [`chat_server.service`](./chat_server.service): Konfigurační soubor pro Systemd.

## **3. Cvičení (Úkoly)**

### **Úkol 1: Ruční test serveru**

Než něco automatizujeme, musíme ověřit, že to funguje ručně.

1. Spusťte server: `python3 server.py`
2. V druhém okně spusťte klienta: `python3 client.py`  
3. Pošlete zprávu.  
4. Ukončete server pomocí `Ctrl+C` (SIGINT). Všimněte si, že server vypíše "Graceful shutdown..." – to je důležité pro Systemd.

### **Úkol 2: Instalace služby (Systemd)**

1. Upravte soubor [`chat_server.service`](./chat_server.service):  
   * Nastavte `User` na vašeho uživatele.  
   * Nastavte absolutní cesty v `WorkingDirectory` a `ExecStart` k souboru `server.py`.  
2. Nainstalujte a spusťte službu:  
   
   ```bash
   sudo cp chat_server.service /etc/systemd/system/  
   sudo systemctl daemon-reload  
   sudo systemctl start chat_server  
   sudo systemctl enable chat_server
   ```

3. Ověřte stav: `systemctl status chat_server`.

### **Úkol 3: Monitoring v reálném čase (Propojení bloků)**

Nyní využijeme skript z minulé lekce ([`05-logy-site/02_realtime_monitor.py`](../05-logy-site/02_realtime_monitor.py)) k automatickému sledování chatu.

1. Ujistěte se, že služba běží.  
2. Spusťte monitorovací "pipeline":  
   ```bash
   # Sledujeme logy naší služby a posíláme je do Python analyzátoru  
   journalctl -u chat_server -f | python3 ../05-logy-regex/02_realtime_monitor.py
   ```

3. V jiném terminálu se připojte klientem a pište zprávy.  
4. **Simulace incidentu:** Odpojte klienta násilně (zavřete terminál nebo `Ctrl+C`). Server zaloguje "Chyba" nebo "Odpojení". Váš monitor by to měl zachytit a zvýraznit.

### **Úkol 4: Restart při pádu**

1. Zjistěte PID serveru (`systemctl status chat_server`).  
2. Zabijte ho (`sudo kill -9 <PID>`).  
3. Sledujte v okně s monitorem, co se stane. Měli byste vidět přerušení a následně nové logy "Server startuje...", jak ho Systemd oživil.