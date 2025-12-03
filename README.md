# **Vývoj a Správa Informačních Systémů 2 (VSIS-2)**

Tento blok se skládá ze tří hlavních částí. Začneme přípravou prostředí, postavíme si vlastní virtuální infrastrukturu, naučíme se ji skriptovat a nakonec k ní připojíme mobilního klienta.

## **Harmonogram a Témata**

Výuka je rozdělena do logických bloků s následující hodinovou dotací:

| Datum | Čas | Blok | Téma | Zaměření |
| :---- | :---- | :---- | :---- | :---- |
| **03.12.** | 11:40 | **Úvod** | **00. Příprava prostředí** | Instalace nástrojů: Git, VS Code, Docker, VirtualBox, Android Studio |
| **03.12.** | 14:30 | **Virtualizace** | **01. Teorie & VM** | Emulace vs Virtualizace, Hypervisory, Vagrant (IaC) |
| **04.12.** | 08:00 | **Virtualizace** | **02. Docker Basics** | Kontejnery vs VM, Docker CLI, Spuštění DB |
| **08.12.** | 08:00 | **Virtualizace** | **03. Images & Build** | Tvorba vlastních obrazů, Dockerfile, Vrstvy |
| **08.12.** | 09:50 | **Virtualizace** | **04. Orchestrace** | Docker Compose, Networking, Persistence dat |
| **15.12.** | 09:50 | **SysProg** | **05. Python & OS** | Práce se souborovým systémem, náhrada Bash skriptů |
| **16.12.** | 09:50 | **SysProg** | **06. Procesy** | Správa procesů, Signály (SIGINT/KILL), Subprocess |
| **16.12.** | 11:40 | **SysProg** | **07. Služby** | Tvorba systémových služeb (Systemd Daemons) |
| **17.12.** | 11:40 | **SysProg** | **08. Logy & Sítě** | Logování, Regex analýza, Sockets basics |
| **17.12.** | 14:30 | **Mobilní** | **09. Teorie Androidu** | Architektura OS Android (HAL, ART), Životní cyklus Activity, Gradle |
| **18.12.** | 11:40 | **Mobilní** | **10. UI & HTTP** | Tvorba UI (XML Layouts) a HTTP komunikace (Retrofit) |
| **14.01.** | 08:00 | **Mobilní** | **11. Data & Offline** | Persistence dat, Lokální databáze, Caching |
| **15.01.** | 11:40 | **Mobilní** | **12. Integrace** | Propojení s backendem, Finální ladění |
| **16.01.** | 09:50 | **Závěr** | **13. Rezerva** | Závěrečný test |

## **Podmínky splnění předmětu**

Tento blok je koncipován jako kombinace praktických cvičení a studentských prezentací.

**Poznámka k hodnocení:** Výsledky studentů (body z testu a hodnocení kvality prezentací) budou předány kolegovi, který je zohlední v celkovém závěrečném hodnocení předmětu Vývoj a správa IS.

Pro úspěšné absolvování této části je nutné splnit následující body:

### **1. Prezentace (2x za semestr)**

Každý student musí v průběhu semestru **dvakrát** aktivně vystoupit s prezentací na odborné téma související s probíranou látkou.

* **Formát:** Teoretický úvod + **praktická ukázka** (live coding nebo demo).  
* **Délka:** cca 15–20 minut.  
* **Témata:** Budou upřesněna na cvičeních (např. "Jak funguje Kubernetes", "Alternativy k Systemd", "Jetpack Compose v Androidu").

### **2. Závěrečný test**

Na konci semestru proběhne písemný test, který ověří znalosti ze všech probíraných bloků.

## **Požadavky na software**

Protože se učíme od začátku, **první hodinu věnujeme instalaci**. Kompletní seznam potřebných nástrojů a návody k instalaci naleznete v sekci:

[**00. Příprava prostředí**](./00-priprava-prostredi)

Pokud chcete být napřed a ušetřit čas na cvičení, doporučujeme si tuto sekci projít a nainstalovat nástroje předem.

## **Struktura repozitáře**

* [00-priprava-prostredi/](./00-priprava-prostredi) - Instalace a nastavení prostředí.  
* [01-virtualizace-a-kontejnerizace/](./01-virtualizace-a-kontejnerizace) - Od VirtualBoxu po Docker Compose.  
* [02-systemove-programovani/](./02-systemove-programovani) - Python a Bash pro správu serverů.  
* [03-mobilni-klient/](./03-mobilni-klient) - Android aplikace komunikující s naším serverem.