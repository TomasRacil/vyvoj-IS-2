# **02. Dockerfile: Stavíme vlastní aplikace**

Doposud jsme používali hotové obrazy od cizích lidí (např. `postgres` nebo `nginx`). Nyní se naučíme zabalit vlastní aplikaci tak, aby šla spustit kdekoli. K tomu slouží soubor s názvem `Dockerfile`.

## **Teorie: Vrstvení obrazů (Layers)**

Docker image není jeden velký soubor, ale skládá se z vrstev (jako cibule). Každý příkaz v Dockerfile vytvoří novou vrstvu.

1. **Base Image:** Např. `python:3.9` (obsahuje OS a Python).  
2. **Dependencies:** Vrstva s nainstalovanými knihovnami (`pip install`).  
3. **App Code:** Vrstva s vaším kódem.

Proč je to důležité?  
Když změníte jen jeden řádek ve svém kódu, Docker nemusí stahovat znovu Python ani instalovat knihovny. Přebuduje jen tu poslední, nejtenčí vrstvu. To šetří čas i místo na disku.

## **Praktický úkol 1: Python Flask Aplikace**

V adresáři `muj-flask` máte připravenou jednoduchou webovou aplikaci. Otevřete si soubor `muj-flask/Dockerfile` a přečtěte si komentáře, abyste pochopili, co se děje.

### **Postup sestavení a spuštění**

1. Otevřete terminál a přejděte do složky s aplikací: 
   ```shell 
   cd muj-flask
   ```

2. **Build (Sestavení):** Vytvoříme image z našeho `Dockerfile`. 
   ```shell
   docker build -t moje-flask-app:v1 .
   ```

   * `-t`: Tag (název) obrazu.  
   * `.`: Tečka na konci je důležitá! Říká: "Hledej Dockerfile v aktuální složce".  
3. **Run (Spuštění):** Spustíme kontejner z našeho nového image.
   ```shell  
   docker run -p 5000:5000 moje-flask-app:v1
   ```

4. Ověření: Otevřete v prohlížeči
`http://localhost:5000`.

## **Praktický úkol 2: Node.js Aplikace**

V adresáři moje-node-app je ukázka v jiném jazyce (JavaScript), aby bylo vidět, že princip Dockerfile je univerzální.

### **Postup**

1. Přejděte do složky: 
   ```shell 
   cd ../moje-node-app
   ```

2. **Build:** 
   ```shell 
   docker build -t moje-node-app:v1 .
   ```

3. **Run:**  
   ```shell
   docker run -p 3000:3000 moje-node-app:v1
   ```

4. Ověření: Otevřete v prohlížeči `http://localhost:3000`.

## **3. Sdílení se světem (Docker Hub)**

Stejně jako dáváme zdrojový kód na GitHub, dáváme sestavené obrazy do tzv. **Container Registry**. Nejznámějším a výchozím registrem je **Docker Hub**.

### **Co je to Docker Hub?**

Je to veřejná knihovna obrazů. Když napíšete `FROM python`, Docker se podívá právě sem. Vy zde můžete mít vlastní repozitáře (veřejné zdarma, soukromé většinou placené).

### **Pravidla pojmenování**

Aby Docker věděl, komu image patří, musíte dodržet jmennou konvenci:  
`uzivatel/nazev-image:verze`

* **uzivatel:** Vaše jméno na Docker Hubu.  
* **nazev-image:** Jméno aplikace.  
* **verze (tag):** Např. v1, latest, 1.0.2.

### **Postup nahrání (Push)**

1. **Registrace:** Vytvořte si účet na [hub.docker.com](https://hub.docker.com/).  
2. **Přihlášení v terminálu:**
   ```shell  
   docker login
   ```

   *Zadejte své uživatelské jméno a heslo (nebo Access Token).*
 
3. **Přejmenování (Tagging)**: Náš lokální image `moje-node-app:v1` musíme "přetaggovat", aby obsahoval vaše jméno.  
   *(Nahraďte `vas_login` vaším skutečným loginem na Docker Hubu.)*
   ```shell
   docker tag moje-node-app:v1 vas_login/moje-node-app:v1
   ```

4. **Odeslání (Push)**: Nyní image odešleme do cloudu.
   ```shell  
   docker push vas_login/moje-node-app:v1
   ```

5. **Ověření:** Nyní můžete jít na jiný počítač (nebo poprosit spolužáka) a spustit:
   ```shell 
   docker run -p 3000:3000 vas_login/moje-node-app:v1
   ```
   Docker si image stáhne z internetu a spustí ho. Funguje to kdekoli na světě.


## **Úkoly**

---

### 1. Úkol: Statický obsah

Nejjednodušší použití Dockeru je zabalení statické HTML stránky.

  * **Zadání:**
    1.  Vytvořte si na počítači složku `muj-web` a v ní soubor `index.html` s libovolným textem (např. "Toto je můj web v kontejneru").
    2.  Vytvořte `Dockerfile`, který:
          * Vychází z oficiálního obrazu `nginx:alpine`.
          * Pomocí instrukce `COPY` nahraje váš `index.html` do složky `/usr/share/nginx/html/` uvnitř kontejneru.
    3.  **Sestavení:** `docker build -t muj-web:v1 .`
    4.  **Spuštění:** `docker run -d -p 8888:80 muj-web:v1`
    5.  **Ověření:** Otevřete `http://localhost:8888`. Musíte vidět váš text, ne výchozí stránku Nginxu.

---

### 2. Úkol: ENV Variables

Hardcodovat konfiguraci (hesla, barvy, texty) přímo do kódu je špatná praxe. Docker image by měl být univerzální a konfigurovatelný zvenčí.

  * **Zadání:**
    1.  Upravte Python aplikaci (`app.py` v adresáři `muj-flask`) z materiálů.
    2.  Místo pevného textu "Ahoj!" ať aplikace vypisuje obsah proměnné prostředí `POZDRAV`. Pokud proměnná není nastavena, použije defaultní hodnotu.
          * *Nápověda:* Použijte `os.getenv("POZDRAV", "Výchozí ahoj")`.
    3.  Přebudujte image (`docker build -t muj-flask:env .`).
    4.  **Test:** Spusťte kontejner s přepínačem `-e`:
        `docker run -p 5000:5000 -e POZDRAV="Nazdar světe" muj-flask:env`
    5.  V prohlížeči by se měl změnit text, aniž byste měnili kód image.

---

### 3. Úkol: Slim vs. Full

Velikost image je důležitá. Menší image se rychleji stahuje a zabírá méně místa.

  * **Zadání:**
    1.  Podívejte se, jak velký je váš image `muj-flask:env` (příkaz `docker images`).
    2.  Upravte `Dockerfile`: Změňte `FROM python:3.9` (nebo slim) na plnou verzi `python:3.9` (pokud jste měli slim, dejte full, a naopak, abyste viděli rozdíl).
    3.  Sestavte jako `muj-flask:velky`.
    4.  **Porovnání:** O kolik MB se liší? (Často je to rozdíl i 800 MB vs 100 MB).

---

### 4. Úkol: Alpine

*Tento úkol není v materiálech. Musíte pochopit, jak funguje Linuxový balíčkovací systém uvnitř Alpine.*

V materiálech používáme pohodlný image `python:3.9-slim`, kde už je Python nainstalovaný. Co když ale potřebujete začít od píky?

  * **Zadání:**
    1.  Vytvořte Dockerfile pro vaši Flask aplikaci, ale jako základ použijte **čistý systém**:
        ```dockerfile
        FROM alpine:latest
        ```
    2.  Když zkusíte tento image sestavit a spustit, selže to (`python: not found`), protože Alpine v základu Python neobsahuje.
    3.  **Úkol:**
          * Přidejte do Dockerfile instrukci `RUN`, která pomocí balíčkovacího manažera `apk` nainstaluje `python3` a `py3-pip`.
          * *Pozor:* Alpine používá `apk`, ne `apt`!
          * Musíte také vytvořit virtuální prostředí (venv) nebo povolit instalaci balíčků globálně (v nejnovějších verzích Pythonu na Alpine je to nutné obejít přes `--break-system-packages` nebo konfiguraci).
    4.  **Cíl:** Funkční Flask aplikace běžící na image, který jste si sestavili sami.