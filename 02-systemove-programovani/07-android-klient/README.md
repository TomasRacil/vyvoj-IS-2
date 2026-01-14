# **Návod: Propojení Androidu se serverem na PC (přes Windows Hotspot)**

Aby se váš telefon mohl připojit k serveru běžícímu na vašem PC (ať už v Linuxu, WSL nebo přímo ve Windows), musí být obě zařízení ve stejné síti a porty musí být správně nasměrovány.

## **Krok 1: Příprava sítě (Windows Hotspot)**

Nejprve musíme vytvořit společnou síť a zjistit IP adresu vašeho PC, na kterou se bude telefon připojovat.

1. Na Windows zapněte **Mobile Hotspot**.  
2. Připojte telefon k této Wi-Fi síti.  
3. Na PC otevřete terminál (PowerShell/CMD) a napište `ipconfig`.  
4. Hledejte adaptér, který se jmenuje např. "Local Area Connection* 10" nebo "Microsoft Wi-Fi Direct Virtual Adapter".  
5. Zapište si jeho **IPv4 Address**. (Např. `192.168.137.1`).

## **Krok 2: Konfigurace podle toho, kde server běží**

Vyberte si sekci podle vašeho prostředí:

### **A) Server běží ve VirtualBoxu (NAT)**
Musíme vytvořit "tunel" z Windows do virtuálního stroje.

1. V nastavení VM: **Network** -> **Advanced** -> **Port Forwarding**.
2. Přidejte pravidlo:
   - **Protocol:** TCP
   - **Host Port:** `12345`
   - **Guest Port:** `12345` (nebo port, na kterém běží váš skript).
3. Ostatní pole nechte prázdná.

### **B) Server běží ve WSL2**
WSL2 běží v izolované síti, takže musíme použít `portproxy`, aby Windows přeposílaly data do WSL.

1. **Zjistěte IP adresu WSL:** V terminálu WSL napište `ip addr show eth0` a najděte `inet` (např. `172.20.115.252`).
2. **Nastavte Proxy (v PowerShellu jako Admin):**
   ```powershell
   netsh interface portproxy add v4tov4 listenport=12345 listenaddress=0.0.0.0 connectport=12345 connectaddress=<IP_VASEHO_WSL>
   ```
   *(Pozor: IP adresa WSL se po restartu PC mění, příkaz je pak nutné zopakovat s novou IP).*

### **C) Server běží přímo ve Windows (Host)**
Zde je nastavení nejjednodušší, protože server běží přímo na rozhraní Hotspotu.

1. **Důležité:** V Python skriptu (nebo jiné aplikaci) se ujistěte, že server naslouchá na adrese `0.0.0.0` (všechna rozhraní), nikoliv jen na `127.0.0.1` (pouze pro tento počítač).
   ```python
   # Správně:
   server.bind(('0.0.0.0', 12345))
   ```

## **Krok 3: Povolení ve Windows Firewall**

Windows Firewall standardně blokuje příchozí spojení z jiných zařízení (vašeho telefonu). Musíme mu říct, že port 12345 je bezpečný.

1. Otevřete **PowerShell jako Administrátor**.  
2. Spusťte tento příkaz:
   ```powershell
   New-NetFirewallRule -DisplayName "Python Chat Server" -Direction Inbound -LocalPort 12345 -Protocol TCP -Action Allow
   ```

## **Krok 4: Test spojení**

1. **Na PC:** Spusťte váš server (ujistěte se, že běží na portu 12345).  
2. **Na Telefonu:** Otevřete TCP klienta (např. aplikaci "TCP Telnet Terminal").  
3. **Připojení:**  
   * **IP:** Zadejte IP adresu Windows z Kroku 1 (např. 192.168.137.1).  
   * **Port:** `12345`.  
4. Pokud se aplikace připojí (nehlásí Timeout/Connection Refused) a server vypíše "Nové připojení", máte hotovo!

---

### **💡 Tip pro řešení potíží:**
* **Ping:** Zkuste z telefonu pingnout IP adresu PC (pokud máte terminálovou aplikaci). Pokud ping neprochází, je problém v Hotspotu nebo Firewallu.
* **Netstat:** Na Windows můžete příkazem `netstat -an | findstr 12345` ověřit, zda váš počítač na daném portu skutečně naslouchá.
* **Reset WSL Proxy:** Pokud chcete smazat nastavení portproxy pro WSL, použijte:
  ```powershell
  netsh interface portproxy reset
  ```