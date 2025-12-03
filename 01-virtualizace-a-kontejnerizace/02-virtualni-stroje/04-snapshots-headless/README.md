# **04. Snapshoty a Headless režim**

V této poslední části se naučíme server spravovat tak, jak se to dělá v praxi – efektivně a bez zbytečné grafiky.

## **Snapshoty (Snímky stavu)**

Představte si, že jdete editovat kritický konfigurační soubor. Pokud uděláte chybu, server nenaběhne. Ve světě fyzických serverů máte problém. Ve virtuálním světě máme **Snapshoty**.

### **Úkol: Vytvoření "Záchranného bodu"**

1. Před jakoukoli riskantní akcí (nebo teď hned) si udělejte snapshot.  
2. Můžete to udělat ve VirtualBox GUI (Machine -> Take Snapshot).  
3. Nebo přes příkazovou řádku (na hostitelském PC!):  
   Musíte být ve složce, kde je nainstalovaný VirtualBox, nebo ji mít v PATH. 

   ```shell
   # Seznam běžících VM  
   VBoxManage list runningvms

   # Vytvoření snapshotu  
   VBoxManage snapshot "Ubuntu-Server" take "Funkcni-SSH-Config" --description "Stav po nastaveni klicu a site"
   ```

Teď můžete server klidně rozbít (např. `sudo rm -rf --no-preserve-root /`). Pro obnovu stačí vypnout VM a vrátit se ke snapshotu.

## **Headless Mode**

Když spravujete server přes SSH, nepotřebujete, aby vám na liště svítilo okno VirtualBoxu s černou konzolí. Zbytečně to žere grafický výkon a paměť.

### **Jak spustit server na pozadí**

1. Vypněte server (pokud běží).  
2. Ve VirtualBoxu klikněte na šipku vedle tlačítka **Start** a vyberte **Headless Start**.  
3. Okno se neotevře, ale ikonka VM se zazelená (Running).

Nyní se připojte přes svůj terminál (`ssh -p 2222 ...`).

### **Ovládání přes terminál**

Pokud chcete server vypnout a nefunguje SSH (nebo ho chcete "vyrvat ze zásuvky"), použijte příkazy na hostitelském PC:

```shell
# Graceful shutdown (jako stisknutí tlačítka vypnout)  
VBoxManage controlvm "Ubuntu-Server" acpipowerbutton

# Hard shutdown (vytržení ze zásuvky)  
VBoxManage controlvm "Ubuntu-Server" poweroff
```

## **Úkoly**

---

### 1. Úkol: Princip Snapshotů
Njelepší způsob jak pochopit sílu snapshotů je server nenávratně poškodit. V reálném světě by to znamenalo přeinstalaci, ve virtuálním světě je to otázka 5 sekund.

  * **Zadání:**
    1.  Vytvořte si snapshot s názvem "Funkcni-System" (pokud ho ještě nemáte).
    2.  Připojte se na server a spusťte příkaz, který smaže všechny spustitelné programy v systému (příkazy jako `ls`, `cp`, `mv` přestanou existovat):
        ```bash
        sudo rm -rf /bin/*
        ```
        *(Případně zkuste smazat kritické konfigurace: `sudo rm -rf /etc`)*
    3.  **Ověření:** Zkuste napsat `ls` nebo `vi`. Systém by měl hlásit `command not found`. Server je mrtvý.
    4.  Vypněte VM (pokud nejde `poweroff`, vypněte okno VirtualBoxu "tvrdě").
    5.  Obnovte snapshot "Funkcni-System" a nastartujte.
    6.  **Výsledek:** Server naběhne, jako by se nic nestalo.

---

### 2. Úkol: Headless Mode
Headless režim není jen o tom, že nevidíte okno. Je to o tom, že server běží na pozadí nezávisle na grafickém rozhraní VirtualBoxu.
* **Zadání:**
    1.  Spusťte VM v **Headless režimu** (`Shift + Start`).
    2.  Jakmile naběhne (ikona ve VirtualBoxu zezelená), **zavřete celé okno aplikace VirtualBox**. (Nebojte se, VirtualBox se jen zeptá, zda nechat VM běžet na pozadí – potvrďte to).
    3.  Nyní máte v počítači aktivni server.
    4.  **Cíl:** Připojte se k němu přes terminál (`ssh myserver`) a vytvořte soubor `touch jsem_zde.txt`.
    5.  Až poté znovu otevřete aplikaci VirtualBox, připojte se k obrazovce serveru (tlačítko Show) a zkontrolujte, že soubor existuje.

---

### 3. Úkol: VBoxManage
Grafické rozhraní je fajn, ale správný admin umí ovládat virtualizaci z příkazové řádky. VirtualBox k tomu má nástroj `VBoxManage`.

**Příprava (Pro Windows uživatele):**
Příkaz `VBoxManage` standardně nefunguje v běžném příkazovém řádku, protože není v systémové cestě. Musíte jít za ním.
1.  Otevřete PowerShell.
2.  Zadejte příkaz: `cd "C:\Program Files\Oracle\VirtualBox"` (nebo tam, kde máte VirtualBox nainstalovaný).
3.  Ověřte funkčnost napsáním: `.\VBoxManage.exe --version` (Ta tečka a lomítko na začátku jsou důležité!).

* **Zadání:**
    1.  Vypište seznam všech virtuálních strojů: `.\VBoxManage.exe list vms`
    2.  Zjistěte detailní info o vašem serveru: `.\VBoxManage.exe showvminfo "nazev-vasi-vm"` (zkuste ve výpisu najít, kolik má přidělené RAM).
    3.  **Finále:** Vypněte server přes příkazovou řádku (tvrdé vypnutí): `.\VBoxManage.exe controlvm "nazev-vasi-vm" poweroff`.

---

### 4. Úkol: Linked Clones
*Tento úkol vyžaduje hledání v dokumentaci VirtualBoxu.*

Představte si, že potřebujete otestovat komunikaci mezi **dvěma** servery. Instalovat druhý server od nuly trvá 20 minut a sežere dalších 25 GB místa na disku. To nechceme.

VirtualBox umí vytvořit tzv. **Linked Clone (Propojený klon)**. Ten sdílí disk s původním strojem a ukládá si jen změny (takže zabere třeba jen 10 MB).

* **Zadání:**
    1.  Vytvořte snapshot vašeho vypnutého serveru.
    2.  Pomocí `VBoxManage clonevm` (nebo v GUI přes pravé tlačítko -> Clone) vytvořte **Propojený klon** s názvem `Server-B`.
    3.  **Důležité:** Musíte vygenerovat novou MAC adresu pro síťovou kartu (volba "Generate new MAC addresses"), jinak budou mít oba stroje v síti konflikt.
    4.  Spusťte oba stroje najednou (původní i klon).
    5.  **Problém:** Pokud necháte síť nastavenou na "NAT", oba stroje budou mít pravděpodobně stejnou IP (10.0.2.15) a neuvidí na sebe.
    6.  **Řešení (Challenge):**
        *   **Krok 1: Oprava ID klonu.** Na klonovaném serveru (`Server-B`) musíte vygenerovat nové unikátní ID. Připojte se k němu přes konzoli VirtualBoxu a spusťte:
            ```bash
            sudo rm /etc/machine-id
            sudo systemd-machine-id-setup
            sudo reboot
            ```
        *   **Krok 2: Společná síť.** Změňte nastavení sítě obou strojů na **Internal Network** (Vnitřní síť) nebo vytvořte **NAT Network**.
            * *Tip: Pokud zvolíte Internal Network, možná budete muset nastavit IP adresy ručně, protože tam neběží DHCP server.*
    7.  **Cíl:**
      * Zjistěte IP adresu Serveru A (`ip a`).
      * Zjistěte IP adresu Serveru B.
      * Z terminálu Serveru A úspěšně **pingněte** Server B:
      ```bash
      ping <IP-ADRESA-SERVERU-B>
      ```
      * Pokud vidíte odezvu (bytes from ...), vyhráli jste.
