# **03. Docker Compose: Orchestrace**

Doposud jsme spouštěli kontejnery ručně pomocí `docker run`. To je fajn pro jeden kontejner, ale co když jich potřebujeme pět? A co když musí startovat ve správném pořadí?

**Docker Compose** je nástroj pro definování a spouštění více kontejnerových aplikací. Celou konfiguraci zapíšeme do jednoho souboru `docker-compose.yml`.

## **Teorie: Infrastruktura jako Kód (IaC)**

Místo psaní dlouhých příkazů do terminálu (které si nikdo nepamatuje) popíšeme "cílový stav" systému.

* **Services (Služby):** Jednotlivé kontejnery (např. `databaze`, `backend`).  
* **Networks (Sítě):** Jak se kontejnery vidí.  
* **Volumes (Svazky):** Kam se ukládají data (aby přežila smazání kontejneru).

## **Základní příkazy**

Všechny příkazy se spouští ve složce, kde leží `docker-compose.yml`.

| Příkaz | Popis |
| :---- | :---- |
| `docker compose up` | Spustí všechny služby (vypisuje logy do terminálu). |
| `docker compose up -d` | Spustí služby na pozadí (Detached). |
| `docker compose down` | Zastaví a **smaže** kontejnery i sítě. |
| `docker compose stop` | Jen zastaví kontejnery (nemže). |
| `docker compose logs -f` | Sleduje výpis logů (jako `tail -f`). |
| `docker compose build` | Sestaví obrazy (pokud používáte `build:` místo `image:`). |

## **Praktický úkol 1: Databáze a Administrace**

V adresáři `01-db-admin` naleznete jednoduchý příklad, jak propojit databázi **PostgreSQL** s grafickým rozhraním **pgAdmin**.

1. Přejděte do adresáře: `cd 01-db-admin`  
2. Prohlédněte si soubor `docker-compose.yml`.  
3. Spusťte stack: `docker compose up -d` 
4. Otevřete prohlížeč na `http://localhost:8080` - *může chvíli trvat než naběhne pgAdmin* (Email: `admin@admin.com`, Heslo: `root`).  
5. Zkuste se připojit k serveru (Hostname: `database`, Databáze: `skola_db`, Uživatel: `student`, Heslo: `heslo`, ).

## **Praktický úkol 2: Full-Stack Aplikace**

V adresáři `02-full-stack` je simulace reálného vývoje. Máme tam:

* **Frontend:** React aplikace (formulář pro přidání úkolu).
* **Backend:** Python Flask API  (přijímá data a ukládá je do DB). 
* **Databáze:** PostgreSQL  (uchovává úkoly i po restartu).

Vše se musí sestavit a propojit.

1. Přejděte do adresáře: `cd ../02-full-stack` 
2. Spusťte sestavení a start: 
   ```shell
   docker compose up -d --build
   ```
   * *Přepínač `--build` je důležitý, protože musíme sestavit naše vlastní Dockerfiles.*  
3. Ověřte Frontend na `http://localhost:3000`
4. Zkuste přidat úkol (např. "Naučit se Docker").
5. **Test persistence:**
    * Vypněte kontejnery: `docker compose stop`
    * Znovu je zapněte: `docker compose up -d`
    * Obnovte stránku. Úkol tam stále bude. To je díky `volumes`.


## **Úkoly**

---

### 1. Úkol: Porty a Konfigurace
V souboru `docker-compose.yml` (ve složce `01-db-admin`) je definováno, že pgAdmin běží na portu 8080. Co když je tento port obsazený?
* **Zadání:**
    1.  Upravte `docker-compose.yml` tak, aby byl **pgAdmin** dostupný na portu **5050**.
    2.  Změňte heslo databáze (`POSTGRES_PASSWORD`) na `super_tajne`.
    3.  Aplikujte změny příkazem `docker compose up -d`.
    4.  **Ověření:** Připojte se na `http://localhost:5050` a zkuste se přihlásit k databázi. (Pozor: Staré heslo už nebude fungovat, musíte v pgAdminu upravit definici serveru nebo vytvořit novou).

---

### 2. Úkol: Volumes vs. Persistence
Mnoho začátečníků je zmatených z toho, kdy data mizí a kdy zůstávají.
* **Zadání:**
    1.  Ve složce `02-full-stack` spusťte aplikaci a přidejte přes webové rozhraní úkol "Koupit mléko".
    2.  Vypněte aplikaci příkazem `docker compose down`. (Tím se smažou kontejnery i sítě).
    3.  Spusťte ji znovu (`up -d`). Úkol tam stále je (díky volume).
    4.  **Cíl:** Zjistěte a proveďte příkaz, který vypne aplikaci A ZÁROVEŇ smaže i volume s daty, takže začnete s čistou databází.
    * *Nápověda:* Je to přepínač `-v` nebo `--volumes` u příkazu down.

---

### 3. Úkol: Přidání služby
Full-stack aplikace (ve složce `02-full-stack`) má Backend a Frontend. Profesionální aplikace často potřebují i mezipaměť (Cache).
* **Zadání:**
    1.  Otevřete `docker-compose.yml`.
    2.  Přidejte novou službu s názvem `cache`.
    3.  Použijte image `redis:alpine`.
    4.  Služba nemusí mapovat žádné porty ven, ale musí být ve stejné síti (`app-network`) jako backend.
    5.  **Ověření:** Spusťte stack a pomocí `docker compose ps` zkontrolujte, že Redis běží.

---

### 4. Úkol: Healthchecks
*Tento problém řeší každý DevOps inženýr. Aplikace padají, protože databáze startuje pomaleji než backend.*

V souboru `docker-compose.yml` máme `depends_on: - db`. To ale Dockeru říká jen: *"Počkej, až kontejner s databází nastartuje."* Neříká to: *"Počkej, až bude databáze připravena přijímat spojení."* (Postgresu trvá start několik sekund, zatímco Python naběhne hned a spadne na chybě připojení).

V kódu `app.py` to řešíme smyčkou `while` (retry logic), ale to je "programátorské" řešení. Existuje "systémové" řešení přímo v Dockeru.

* **Úkol:**
    1.  Odstraňte z `app.py` tu ošklivou `while` smyčku (funkci `init_db` a retry logiku), nechte jen jeden pokus o připojení. Když to teď spustíte, backend pravděpodobně spadne (Race Condition).
    2.  **Opravte to v `docker-compose.yml`:**
        * Přidejte do služby `db` sekci `healthcheck`. (Musí testovat, zda DB žije, např. příkazem `pg_isready -U dev_user`).
        * Upravte `depends_on` u služby `backend` do "dlouhé formy", kde nastavíte podmínku `condition: service_healthy`.
    3.  **Výsledek:** Když dáte `docker compose up`, uvidíte, že backend čeká (status `Created`), dokud databáze neoznámí, že je `healthy`, a teprve pak se spustí.