# **03. Kontejnerizace s Dockerem**

Tato sekce se věnuje jedné z nejdůležitějších technologii ve vývoji moderního backendu. Docker změnil způsob, jakým svět vyvíjí a provozuje software. Umožňuje nám zabalit aplikaci se vším, co potřebuje, a spustit ji kdekoli.

## **Teorie: Proč nestačily virtuální stroje?**

Před nástupem Dockeru (2013) řešili vývojáři velký problém: Jak zajistit, aby aplikace fungovala všude stejně?

* **Vývojář:** "U mě na notebooku (Windows + Python 3.9) to funguje."  
* **Server:** "Tady na produkci (Linux + Python 3.6) to hází chybu."

### **Řešení 1: Virtuální stroje (Těžká váha)**

Technicky vzato, tento problém už řešila virtualizace. Mohli jsme každou aplikaci zabalit do vlastního Virtuálního stroje (VM). Tím bychom zajistili dokonalou izolaci.  
Proč se to neujalo? Protože je to extrémně neefektivní.

* Představte si, že chcete spustit 3 malé webové aplikace (každá má 50 MB).  
* Ve světě VM musíte spustit **3 kompletní operační systémy**.  
* Každý OS si vezme 1 GB RAM a kus CPU jen na to, aby "existoval".  
* **Výsledek:** Plýtváte 90 % výkonu serveru na běh operačních systémů, ne na běh aplikací.

### **Řešení 2: Kontejnery (Lehká váha)**

Docker přišel s revoluční myšlenkou: **Co kdybychom izolovali aplikace, ale sdíleli ten těžký operační systém pod nimi?**

Docker vezme aplikaci a zabalí ji do **Image**.

* **Efektivita:** Kontejner neobsahuje celé jádro OS, jen vaši aplikaci a knihovny.  
* **Hustota:** Na serveru, kde běželo 5 virtuálek, můžete spustit 50 kontejnerů.  
* **Rychlost:** Startují v milisekundách (nemusí bootovat OS).

![VM](https://www.backblaze.com/blog/wp-content/uploads/2018/06/whats-the-diff-container-vs-vm.jpg)

## **Technické pozadí: Jak to funguje pod kapotou?**

Zatímco virtuální stroje (VM) virtualizují **hardware** (mají vlastní virtuální CPU, RAM a celé jádro OS), kontejnery virtualizují pouze **operační systém**.

Kontejnery využívají dvě klíčové funkce Linuxového jádra:

1. **Namespaces (Jmenné prostory):** Zajišťují **izolaci pohledu**.  
   * Proces v kontejneru si myslí, že je v systému sám (PID 1). Nevidí ostatní procesy na hostiteli.  
   * Má vlastní "virtuální" síťovou kartu, vlastní souborový systém (`/`), vlastní uživatele.  
2. **Control Groups (cgroups):** Zajišťují **izolaci zdrojů**.  
   * Omezují, kolik RAM a CPU může kontejner spotřebovat.  
   * Zabraňují tomu, aby jedna chyba v aplikaci "sežrala" celou paměť serveru a shodila ostatní kontejnery.

Díky tomu kontejnery poskytují **izolaci srovnatelnou s VM, ale s režií běžného procesu**.

## **Obsah modulu**

* [**01. Docker CLI (Příkazová řádka)**](./01-docker-cli)
    * Základy ovládání Dockeru.  
    * Spouštění hotových kontejnerů (Nginx, Postgres).  
    * Práce se sítěmi (Connecting containers).
* [**02. Dockerfile (Tvorba Images)**](./02-vlastni-image)
    * Jak vytvořit vlastní obraz.  
    * Vrstvení (Layers) a optimalizace.  
    * Praktická ukázka: Python Flask a Node.js aplikace.

* [**03. Docker Compose (Orchestrace)**](./03-docker-compose)
    * Spouštění více kontejnerů najednou jedním příkazem.  
    * Definice infrastruktury jako kód (`docker-compose.yml`).  
    * Projekt: Propojení Frontend (React) + Backend (Python) + Databáze.

* [**04. Dev Containers (Vývoj v kontejneru)**](./04-dev-containers)
    * Jak využít Docker nejen pro *běh* aplikace, ale i pro *vývoj*.  
    * Nastavení VS Code pro izolované vývojové prostředí.

## **Příprava**

Ujistěte se, že máte spuštěný Docker Desktop (nebo Docker Engine na Linuxu).  
Ověřte příkazem: 
```shell 
docker version  
```