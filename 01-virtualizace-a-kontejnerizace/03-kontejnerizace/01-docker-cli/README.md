# **01. Docker CLI: Základy a Sítě**

Command line utility dockeru (CLI) je váš hlavní nástroj pro komunikaci s Docker Enginem. V této lekci se naučíme spouštět kontejnery, spravovat je a propojovat.

## **1. Životní cyklus kontejneru**

### **Hello World**

Nejprve ověříme, že vše funguje.

```shell
docker run hello-world
```

Tento příkaz stáhl image z Docker Hubu, vytvořil kontejner, spustil ho (vypsal text) a ukončil se.

### **Interaktivní režim (Alpine Linux)**

Chceme se dostat "dovnitř" kontejneru. Použijeme alpine – extrémně malou distribuci Linuxu (cca 5 MB).

```shell
docker run --name muj-alpine -it alpine:latest /bin/sh
```

* `-i` (interactive): Udržuje STDIN otevřený.  
* `-t` (tty): Přidělí virtuální terminál.  
* `--name`: Pojmenuje kontejner (jinak dostane náhodné jméno).

Nyní jste uvnitř. Zkuste `ls`, `whoami` nebo `cat /etc/os-release`. Pro ukončení napište `exit`.

## **2. Běh na pozadí a Porty (PostgreSQL)**

Databáze a webové servery chceme spouštět na pozadí (**Detached mode**).

```shell
docker run --name mojedb -e POSTGRES_PASSWORD=tajneheslo -d postgres
```

* `-e`: Nastavení environment proměnné (konfigurace kontejneru).  
* `-d`: Detached mode (běží na pozadí).

Zkontrolujte, že běží:

```shell
docker ps
```

## **3. Networking: Propojení dvou kontejnerů**

Toto je klíčový úkol. Chceme propojit databázi (**PostgreSQL**) s grafickým správcem (**pgAdmin**), aniž bychom museli cokoli instalovat do Windows/macOS.

### **Krok A: Vytvoření sítě**

Kontejnery se navzájem nevidí, pokud nejsou ve stejné síti.

```shell
docker network create my-net
```

### **Krok B: Spuštění databáze v síti**

Nyní musíme dostat naši databázi do sítě `my-net`. Máme dvě možnosti:

**Varianta 1: Smazat a vytvořit znovu (Doporučeno)**
Abychom měli pořádek v názvech (a fungoval nám přesně návod v Kroku D), starou databázi smažeme a vytvoříme novou s názvem `db-server`.

```shell
docker rm -f mojedb

docker run --name db-server   
  --network my-net   
  -e POSTGRES_USER=student   
  -e POSTGRES_PASSWORD=heslo   
  -d postgres
```

**Varianta 2: Připojit stávající kontejner** Pokud byste měli v kontejneru mojedb důležitá data a nechtěli ho mazat, můžete ho připojit do sítě za chodu:

```shell
docker network connect my-net mojedb
```
*(Pozor: Pokud zvolíte tuto možnost, váš kontejner se stále jmenuje `mojedb`. V Kroku D tedy musíte jako Host name zadat mojedb místo `db-server`.)*

### **Krok C: Spuštění pgAdmin v síti**

pgAdmin je webové rozhraní pro správu DB. Musíme mu vystavit port ven, abychom ho viděli v prohlížeči.

```shell
docker run --name db-admin   
  --network my-net   
  -p 8080:80   
  -e PGADMIN_DEFAULT_EMAIL=admin@skola.cz   
  -e PGADMIN_DEFAULT_PASSWORD=admin   
  -d dpage/pgadmin4
```

* `-p 8080:80`: To, co je uvnitř kontejneru na portu 80, bude na mém PC na portu 8080.

### **Krok D: Připojení**

1. Otevřete prohlížeč na `http://localhost:8080`.  
2. Přihlašte se (email: `admin@skola.cz`, heslo: `admin`).  
3. Klikněte na **Add New Server**.  
   * **Host name/address:** `db-server` (V Docker síti se kontejnery vidí pod svými názvy. Pokud jste použili Variantu 2, zadejte `mojedb`)  
   * **Username:** `student`  
   * **Password:** `heslo`  
4. Pokud se připojíte, výborně. Propojili jste dva izolované systémy.

## **Úklid**

Po dokončení práce po sobě ukliďte:

```shell
docker rm -f db-server db-admin  
docker network rm my-net
```

## **Úkoly**

---

### 1. Úkol: Úklid
Začátečníci často spouští kontejnery a zapomínají na ně. Ty pak běží na pozadí nebo zabírají místo na disku.
* **Zadání:**
    1.  Spusťte experimentálně 3 kontejnery `hello-world`.
    2.  Spusťte příkaz, který vypíše **všechny** kontejnery (nejen ty běžící, ale i ty vypnuté/ukončené).
    3.  **Cíl:** Smažte všechny tyto zastavené kontejnery.
    4.  *Tip:* Můžete to dělat po jednom pomocí ID, nebo najít na internetu příkaz ("docker prune"), který smaže všechny zastavené najednou.

---

### 2. Úkol: Port Mapping
V materiálech jsme mapovali port 8080 na pgAdmin. Zkusme si to s jinou službou.
* **Zadání:**
    1.  Stáhněte a spusťte webový server **Nginx** (`nginx:alpine`) na pozadí (`-d`).
    2.  Nastavte port forwarding tak, aby byl server dostupný na vašem počítači na portu **9999** (uvnitř kontejneru běží Nginx standardně na portu 80).
    3.  **Ověření:** Otevřete prohlížeč na `http://localhost:9999`. Měli byste vidět "Welcome to nginx!".
  
---

### 3. Úkol: Docker Exec
Často potřebujete nahlédnout do kontejneru, který už běží (např. databáze), aniž byste ho vypínali. K tomu slouží příkaz `exec`.
* **Zadání:**
    1.  Mějte spuštěný Nginx z předchozího úkolu.
    2.  Použijte příkaz `docker exec` s přepínači `-it`, abyste se dostali do příkazové řádky (`/bin/sh`) tohoto **běžícího** kontejneru.
    3.  Uvnitř vytvořte soubor: `echo "Byl jsem tu" > /usr/share/nginx/html/tajne.html`.
    4.  Odejděte z kontejneru (`exit`).
    5.  **Ověření:** V prohlížeči na PC zadejte `http://localhost:9999/tajne.html`. Pokud se soubor zobrazí, úspěšně jste modifikovali běžící systém.

---

### 4. Úkol: DNS & Networks
*Tento problém nachytá 90 % začátečníků. Odpověď musíte najít v dokumentaci nebo na fórech.*

V lekci jsme si ukázali, že když vytvoříte vlastní síť (`docker network create`), kontejnery se vidí podle jména. Co se ale stane, když síť nevytvoříte?

* **Zadání:**
    1.  Spusťte dva kontejnery Alpine **bez definování sítě** (takže spadnou do výchozí "bridge" sítě):
        * `docker run -dit --name alpine1 alpine`
        * `docker run -dit --name alpine2 alpine`
    2.  Vstupte do `alpine1` a zkuste pingnout ten druhý: `ping alpine2`.
    3.  **Problém:** Uvidíte `bad address 'alpine2'`. Ping na jméno nefunguje!
    4.  **Úkol:**
        * Zjistěte (pomocí příkazu `docker inspect` z terminálu vašeho PC), jakou **IP adresu** má `alpine2`.
        * Zkuste z `alpine1` pingnout přímo tuto IP adresu. (To by mělo fungovat).
    5.  **Otázka k vyřešení:** Proč v defaultní síti nefungují jména (DNS), zatímco ve vlastní síti ano? Co musíte udělat, abyste mohli používat jména, aniž byste museli ručně hledat IP adresy?