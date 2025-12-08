# **Návod: Propojení Androidu a Virtuálky (Windows Hotspot)**

Aby se váš telefon mohl připojit k serveru, který běží uvnitř virtuálního stroje (VirtualBox/VMware) na vašem počítači, musíme vytvořit "tunel" pomocí **NAT Port Forwardingu**.

## **Krok 1: Zjištění IP adresy Windows (Hotspot)**

Toto je adresa, na kterou se bude váš telefon připojovat.

1. Na Windows zapněte **Mobile Hotspot**.  
2. Připojte telefon k této Wi-Fi síti.  
3. Na PC otevřete terminál (PowerShell/CMD) a napište `ipconfig`.  
4. Hledejte adaptér, který se jmenuje např. "Local Area Connection* 10" nebo "Microsoft Wi-Fi Direct Virtual Adapter".  
5. Zapište si jeho **IPv4 Address**. (Např. `192.168.137.1`).

## **Krok 2: Nastavení VirtualBoxu**

Musíme říct VirtualBoxu, aby vše, co přijde na port 12345 ve Windows, poslal do virtuálky.

1. Vypněte virtuálku (nebo ji nechte běžet, funguje to i za běhu).  
2. Otevřete **Settings (Nastavení)** vaší virtuálky -> **Network (Síť)**.  
3. Ujistěte se, že **Attached to (Připojeno k)** je nastaveno na **NAT**.  
4. Rozklikněte **Advanced (Pokročilé)** a klikněte na tlačítko **Port Forwarding**.  
5. Přidejte nové pravidlo (tlačítko `+`):  
   * **Name:** ChatServer  
   * **Protocol:** TCP  
   * **Host IP:** `0.0.0.0` (nebo nechte prázdné)  
   * **Host Port:** `12345` (Port ve Windows)  
   * **Guest IP:** (Nechte prázdné)  
   * **Guest Port:** `12345` (Port v Python skriptu uvnitř VM)  
6. Potvrďte OK.

## **Krok 3: Povolení ve Windows Firewall**

Windows Firewall ve výchozím stavu blokuje příchozí spojení z cizích zařízení (telefonu).

1. Otevřete **PowerShell jako Administrátor**.  
2. Spusťte tento příkaz (vytvoří pravidlo pro povolení portu):

`New-NetFirewallRule -DisplayName "Python Chat Server" -Direction Inbound -LocalPort 12345 -Protocol TCP -Action Allow`

*Alternativně můžete firewall pro profil "Private/Public" dočasně vypnout, ale to se z bezpečnostních důvodů nedoporučuje.*

## **Krok 4: Test spojení**

1. **Na PC (VM):** Spusťte Python server.  
2. **Na Telefonu:** Otevřete TCP klienta (např. aplikaci "TCP Telnet Terminal").  
3. **Připojení:**  
   * **IP:** Zadejte IP adresu Windows z Kroku 1 (např. 192.168.137.1).  
   * **Port:** 12345.  
4. Pokud se aplikace připojí (nehlásí Timeout/Connection Refused) a server vypíše "Nové připojení", máte hotovo!