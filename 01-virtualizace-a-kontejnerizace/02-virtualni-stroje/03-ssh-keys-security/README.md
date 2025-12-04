# **03. SSH Keys a Bezpečnost**

Zadávat heslo heslo při každém připojení je otravné. Zadávat složité heslo X7!mB9@qL je ještě otravnější. A mít na serveru povolené přihlašování heslem je bezpečnostní riziko (Brute-force útoky).

Řešením jsou **SSH klíče**.

## **Teorie: Asymetrická kryptografie**

Běžná hesla fungují na principu **symetrické kryptografie** (obě strany znají stejné tajemství). SSH klíče využívají **asymetrickou kryptografii**, která je založena na matematicky svázaném páru dvou odlišných klíčů:

1. **Veřejný klíč (Public Key):**  
   * Tento klíč můžete volně šířit. Dáváte ho serverům, kam se chcete připojovat.  
   * Slouží k **šifrování** zpráv pro vás nebo k **ověřování** vašich digitálních podpisů.  
   * Z veřejného klíče **nelze** spočítat klíč privátní.  
2. **Privátní klíč (Private Key):**  
   * Tento klíč musíte pečlivě chránit a nikdy ho nesmíte nikomu poslat.  
   * Slouží k **dešifrování** zpráv určených vám nebo k **digitálnímu podepisování**.

### **Jak probíhá přihlášení (SSH Handshake)?**

Proces ověření totožnosti probíhá tak, že server ověřuje, zda vlastníte privátní klíč, aniž byste ho museli posílat sítí.

1. **Klient:** "Ahoj, chci se přihlásit jako student a používám tento veřejný klíč."  
2. **Server:** Podívá se do souboru authorized_keys. Pokud tam klíč najde, vygeneruje náhodný řetězec (tzv. **Challenge**) a pošle ho klientovi.  
3. **Klient:** Vezme tento řetězec a **digitálně ho podepíše** svým **Privátním klíčem**. Výsledek pošle zpět serveru.  
4. **Server:** Vezme váš **Veřejný klíč** a ověří, zda podpis odpovídá původnímu řetězci. Pokud ano, znamená to, že musíte vlastnit privátní klíč, a server vás pustí dovnitř.

## **1. Generování páru klíčů (Hostitel)**

Tento krok děláte na svém **počítači (Windows/Mac)**, ne na serveru!

Otevřete terminál (PowerShell/Bash) a zadejte:

```shell
ssh-keygen -t ed25519 -C "vas-email@student.cz"
```

* `-t ed25519`: Moderní, bezpečný a rychlý algoritmus (lepší než staré RSA).  
* `-C`: Komentář pro identifikaci klíče (abyste poznali, komu patří).

Systém se zeptá, kam klíč uložit (nechte default Enter) a na Passphrase (pro výuku nechte prázdné Enter, v praxi zadejte heslo k odemčení klíče, což je další vrstva ochrany).

Vzniknou dva soubory (obvykle v `~/.ssh/`):

* `id_ed25519` (Váš **privátní** klíč. NIKDY nikomu neposílat!).  
* `id_ed25519.pub` (Váš **veřejný** klíč. Ten nahrajeme na server).

## **2. Nahrání veřejného klíče na server**

Musíme dostat obsah `id_ed25519.pub` do souboru `~/.ssh/authorized_keys` na serveru. Tím serveru říkáme: *"Tento veřejný klíč patří uživateli Student, pouštěj každého, kdo prokáže vlastnictví odpovídajícího privátního klíče."*

### **Varianta A: Automaticky (Linux/Mac/nový Windows)**

Pokud máte příkaz `ssh-copy-id` (nebo Windows s OpenSSH):

```shell
ssh-copy-id -p 2222 student@127.0.0.1
```

*Zadáte naposledy heslo a klíč se přenese.*

### **Varianta B: Ručně (Univerzální)**

1. Zobrazte si veřejný klíč na svém PC: `cat ~/.ssh/id_ed25519.pub` (nebo `type ...` na Windows).  
2. Zkopírujte ten řetězec (začíná `ssh-ed25519 ...`).  
3. Přihlašte se na server klasicky heslem.  
4. Na serveru: 
   ```bash
   mkdir -p ~/.ssh  
   echo "ZDE_VLOZTE_TEN_KOD_Z_KLICE" >> ~/.ssh/authorized_keys  
   chmod 600 ~/.ssh/authorized_keys  
   chmod 700 ~/.ssh
   ```

## **3. Test připojení**

Odhlaste se (`exit`) a zkuste se připojit znovu:

```shell
ssh -p 2222 student@127.0.0.1
```

Pokud vás to pustilo **bez hesla**, funguje to!

## **4. Hardening (Vypnutí hesel)**

Teď, když máme klíče, zakážeme hesla úplně. Tím zamezíme útokům hádačů hesel (botů, kteří zkouší admin/1234).

1. Na serveru editujte konfiguraci SSH daemona: 
   ```bash 
   sudo nano /etc/ssh/sshd_config
   ```

2. Najděte (Ctrl+W) řádek `PasswordAuthentication` a změňte ho na:  
   `PasswordAuthentication no`

3. **Důležité:** V novějších systémech (např. Ubuntu 22.04+) může být na konci souboru řádek `Include /etc/ssh/sshd_config.d/*.conf`. Ten způsobí, že se načtou další konfigurační soubory, které mohou naše nastavení přepsat. Pro jistotu tento řádek zakomentujte přidáním `#` na začátek:
   `#Include /etc/ssh/sshd_config.d/*.conf`

4. Uložte (`Ctrl+O`, `Enter`) a ukončete (`Ctrl+X`).  
5. Restartujte službu:
   ```bash
   sudo systemctl restart ssh
   ```

*Pozor: Nyní se na server dostane jen ten, kdo má privátní klíč! Pokud ho ztratíte, jste ze serveru navždy zamčeni.*

## **Úkoly**

---

### 1. Úkol: Oprávnění

V návodu jste zadávali příkazy `chmod 600` a `chmod 700`. Co se ale stane, když to neuděláte? SSH server je paranoidní a odmítne použít klíče, které jsou "příliš viditelné" pro ostatní uživatele.

  * **Zadání:**
    1.  Přihlašte se na server a změňte práva složky `.ssh` na "všichni mohou všechno": `chmod 777 ~/.ssh`.
    2.  Odhlaste se (`exit`) a zkuste se znovu připojit klíčem.
    3.  **Výsledek:** Měl by po vás chtít heslo (nebo spojení odmítnout), protože server klíč ignoruje z důvodu špatných práv (tzv. `StrictModes`).
    4.  **Oprava:** Přihlašte se heslem (pokud jste je ještě nezakázali) nebo přes okno VirtualBoxu a vraťte práva zpět: `chmod 700 ~/.ssh`.

---

### 2. Úkol: Ověření zákazu

Vypnout hesla v konfiguraci je jedna věc, ale jak si ověříte, že to opravdu funguje?

  * **Zadání:** Pokuste se přinutit SSH klienta, aby nepoužil klíč, ale vyžádal si heslo.
  * **Příkaz:** `ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no -p 2222 student@127.0.0.1`
  * **Cíl:** Pokud jste správně nastavili `PasswordAuthentication no`, server vás musí okamžitě odmítnout hláškou `Permission denied (publickey)`. Nesmí vám dát šanci heslo ani napsat.

---

### 3. Úkol: SSH Config

Psát pokaždé `ssh -p 2222 student@127.0.0.1` je otravné. Profesionálové používají konfigurační soubor.

  * **Zadání:** Vytvořte na svém **hostitelském počítači** (ve Windows/Mac) soubor `~/.ssh/config` (ve složce, kde máte klíče).
  * **Obsah:**
    ```text
    Host myserver
    HostName 127.0.0.1
    Port 2222
    User student
    IdentityFile ~/.ssh/id_ed25519
    ```
  * **Test:** Nyní se musíte zvládnout připojit pouhým napsáním: `ssh myserver`.

---

### 4. Úkol: 2FA / Google Authenticator

*Tento úkol vyžaduje instalaci balíčků a hledání na internetu.*

Zabezpečení SSH klíčem je silné, ale co když vám někdo ukradne notebook s privátním klíčem? Pak se na server dostane. Zvyšte bezpečnost na maximum pomocí **Dvoufázového ověřování (MFA)**.

  * **Zadání:** Nastavte server tak, aby pro přihlášení vyžadoval **dvě věci současně**:
    1.  Váš SSH klíč (Něco, co máte v PC).
    2.  Jednorázový kód (OTP) z aplikace v mobilu (Něco, co máte u sebe).
  * **Postup (Nápověda):**
      * Nainstalujte na serveru `libpam-google-authenticator`.
      * Spusťte `google-authenticator` a naskenujte QR kód do mobilu.
      * Upravte `/etc/pam.d/sshd` (přidejte `auth required pam_google_authenticator.so`) a `/etc/ssh/sshd_config` (hledejte `KbdInteractiveAuthentication`, `AuthenticationMethods`, `ChallengeResponseAuthentication`, `PubkeyAuthentication`, `UsePAM`).
  * **Cíl:** Po zadání příkazu `ssh myserver` se vás server zeptá na `Verification code:`. Bez mobilu se nepřipojíte.
  * **Tip: Problémy se synchronizací času**
    * Jednorázové kódy (TOTP) jsou závislé na přesném čase. Pokud se čas serveru a vašeho telefonu liší o více než minutu, kódy nebudou fungovat.
    * Pokud máte problémy, synchronizujte čas na serveru:
      ```bash
      sudo apt update
      sudo apt install ntpdate
      sudo ntpdate pool.ntp.org
      ```