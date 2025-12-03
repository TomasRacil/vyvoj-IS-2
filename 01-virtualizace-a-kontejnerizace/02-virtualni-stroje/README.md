# **02. Virtuální stroje**

V předchozích ročnících jste možná spustili virtuální stroj, ale v tomto dokumentu si vysvětlíme, jak je technicky možné, že na jednom fyzickém procesoru běží pět různých operačních systémů najednou, aniž by se zhroutily.

Tato kapitola pokrývá architekturu, historii, klíčové hráče na trhu a problematiku licencování.

## **0. Historie: Kdo to vymyslel?**

Možná si myslíte, že virtualizaci není zas tak stará technologie, ale to je omyl. Virtualizace je starší než sám internet.

### **60. léta: IBM a Mainframy**

V 60. letech stál počítač miliony dolarů (např. **IBM System/360**). Firmy si nemohly dovolit koupit počítač pro každé oddělení.

* **Problém:** Jak zajistit, aby účetní program neshodil výpočet inženýrů, když oba běží na jednom obrovském stroji? A jak zajistit, aby drahý procesor nečinně nečekal?  
* **Řešení:** IBM vyvinulo **CP-40** a později **CP-67** – první systémy, které uměly vytvořit "virtuální stroje".  
* **Klíčové důvody zavedení (které platí dodnes):**  
  1. **Izolace procesů (Bezpečnost a Stabilita):** Každý virtuální stroj dostal svůj oddělený paměťový prostor. Pokud se jeden systém zhroutil, ostatní běžely dál bez přerušení.  
  2. **Využití zdrojů (Efektivita):** Mainframe byl příliš drahý na to, aby běžel jen na 20 %. Virtualizace umožnila "vyždímat" hardware na 100 % tím, že když jeden virtuální stroj čekal na data z pásky, procesor okamžitě přepnul na jiný stroj.  
* **Klíčový pojem:** **Time-sharing** (sdílení času). CPU přepínalo mezi úlohami tak rychle, že to vypadalo, že běží paralelně.

### **80. a 90. léta: Ústup ze slávy**

S nástupem levných osobních počítačů (PC) a serverů x86 (Intel) virtualizace téměř zmizela. Hardware byl tak levný, že se vyplatilo koupit pro každou aplikaci nový fyzický server ("Jeden server, jedna aplikace"). To vedlo k plýtvání (servery běžely vytížené na 5 %).

### **1998: Renesance (VMware)**

V roce 1998 přišla malá firma VMware s revolučním nápadem: "Vraťme virtualizaci zpět, ale na levné procesory Intel."
Vyřešili extrémně složitý problém virtualizace architektury x86 (viz níže "Binární translace") a změnili svět IT. Dnes je virtualizace standardem.

## **1. Architektura: Jak to funguje "pod kapotou"**

Abychom pochopili virtualizaci, musíme se podívat na architekturu procesorů x86 (Intel/AMD).

### **Ochranné kruhy (CPU Rings)**

Standardní procesor neumožňuje každému programu dělat cokoliv. Bezpečnost je řešena pomocí tzv. **Protection Rings** (Ochranné kruhy), číslovaných 0 až 3.

* **Ring 0 (Kernel Mode):** Nejnižší úroveň. Má přímý přístup k hardwaru (RAM, I/O porty, instrukce CPU). Zde běží **jádro operačního systému** (Windows Kernel, Linux Kernel).  
* **Ring 1 & 2:** Historicky vyhrazeno pro ovladače (dnes se moc nepoužívá).  
* **Ring 3 (User Mode):** Zde běží běžné aplikace (Word, Chrome, VS Code). Nemohou přímo sáhnout na hardware. Pokud chtějí zapsat na disk, musí "poprosit" Ring 0 (System Call).

### **Problém virtualizace**

Když spustíte virtuální stroj (Guest), instalujete do něj operační systém. Tento OS (např. Ubuntu) si myslí, že je pánem počítače a chce běžet v **Ring 0**. Jenže v Ring 0 už běží váš hostitelský systém (Windows). Dva králové na jednom trůnu sedět nemohou.

### **Řešení A: Binární translace (Historie)**

Před rokem 2005 musel hypervisor (např. starý VMware) složitě "podvádět". Když se Guest OS pokusil o instrukci určenou pro Ring 0, hypervisor ji za letu odchytil (Trap) a přeložil na bezpečnější variantu.

* **Nevýhoda:** Extrémně pomalé a náročné na vývoj.

### **Řešení B: Hardwarová akcelerace (VT-x / AMD-V)**

Dnešní procesory mají speciální instrukční sady (Intel VT-x, AMD-V). Ty zavádí nový režim, často nazývaný **Ring -1** (Root Mode).

* **Host (Hypervisor)** běží v **Root Mode (Ring -1)**.  
* **Guest (Virtuální OS)** běží v **Non-Root Mode (Ring 0)**.

Díky tomu si virtuální Windows myslí, že mají plný přístup k HW (jsou v Ring 0), ale ve skutečnosti je kontroluje Hypervisor sedící ještě o úroveň níže.

**Proto musíte v BIOSu zapínat "Intel Virtualization Technology". Bez toho se Ring -1 neaktivuje.**

## **2. Správa zdrojů: Magie sdílení**

Hypervisor neizoluje jen CPU, ale i paměť a disky.

### **Virtualizace paměti (Shadow Page Tables)**

Existují tři vrstvy paměti:

1. **Guest Virtual Memory:** Adresy, které vidí aplikace uvnitř VM.  
2. **Guest Physical Memory:** Co si VM myslí, že je skutečná RAM.  
3. **Host Physical Memory:** Skutečné čipy RAM ve vašem notebooku.

Hypervisor musí neustále přepočítávat mapování mezi těmito vrstvami.

* **Memory Ballooning:** Pokročilá technika, kdy hypervisor nainstaluje do Guesta speciální ovladač (balónek). Když hostiteli dochází RAM, "nafoukne" balónek uvnitř VM. VM si myslí, že paměť spotřebovává nějaký program, a začne odkládat data na disk (swap), čímž uvolní fyzickou RAM pro jiné VM.

### **Virtualizace disku (Thin vs. Thick Provisioning)**

* **Thick Provisioning (Tlustý):** Vytvoříte 50 GB disk a on okamžitě zabere 50 GB na fyzickém disku. Je to nejrychlejší, ale plýtvá místem.  
* **Thin Provisioning (Tenký):** Vytvoříte 50 GB disk, ale na fyzickém disku zabere jen tolik, kolik je tam dat (např. 2 GB). Jak data přibývají, soubor roste. Je to úsporné, ale může to fragmentovat disk.

## **3. Typy Hypervisorů (Opakování pro kontext)**

| Typ | Název | Popis |
| :---- | :---- | :---- |
| **Typ 1** | **Bare-Metal** | Instaluje se přímo na "železo". Žádné Windows, žádný Linux pod ním. Hypervisor JE operační systém. (ESXi, Hyper-V Server, Proxmox). |
| **Typ 2** | **Hosted** | Běží jako aplikace v OS. (VirtualBox, VMware Workstation). |

## **4. Hráči na trhu a Licencování**

Toto je klíčová část pro vaši budoucí kariéru. Vědět, co použít v domácím labu a co v korporátu za miliony, je zásadní.

### **VMware (Broadcom)**

Dlouholetý král virtualizace. Jejich produkt **VMware vSphere (ESXi)** je standardem ve většině velkých firem (Fortune 500).

* **Aktuální situace (2023/2024):** Společnost Broadcom koupila VMware a radikálně změnila licencování. Zrušili trvalé licence (koupím jednou a mám) a zavedli drahé předplatné.  
* **Dopad:** Mnoho firem nyní hledá levnější alternativy (migrace na Hyper-V nebo Proxmox).  
* **Produkty:** ESXi (server), Workstation (desktop - nyní zdarma pro osobní použití!).

### **Microsoft Hyper-V**

Hypervisor integrovaný přímo do Windows.

* **Výhoda:** Pokud máte Windows Server, máte Hyper-V "zdarma". Běží na něm celý cloud Microsoft Azure.  
* **Použití:** Velmi silný v korporátním prostředí, které už jede na Microsoftu.

### **KVM (Kernel-based Virtual Machine)**

Open-source řešení, které je součástí Linuxového jádra. KVM dělá z Linuxu hypervisor Typu 1.

* **Kdo ho používá?** Google Cloud, AWS (částečně), Red Hat. Je to motor, na kterém běží většina internetu.  
* **Proxmox VE:** Velmi populární platforma pro nadšence a menší/střední firmy. Je to hezké grafické rozhraní nad KVM. Je zdarma (nebo s placenou podporou) a v poslední době masivně roste díky "útěku od VMware".

### **Oracle VirtualBox**

Nástroj, který budeme používat my. Je skvělý na výuku, protože je zdarma a multiplatformní.

* **Licenční past (Extension Pack):** Pozor! Samotný VirtualBox je GPL (zdarma). Ale **Extension Pack** (podpora USB 3.0, RDP, šifrování) je zdarma **pouze pro osobní a výukové účely**.  
* **Varování:** Pokud si Extension Pack nainstalujete ve firmě bez zaplacení licence, Oracle vás může zažalovat (a dělá to).

## **5. Kontejnerizace vs. Virtualizace (Stručně)**

Zatímco virtuální stroje emulují **hardware** (abychom mohli spustit celý OS), kontejnery (Docker) emulují pouze **operační systém** (abychom mohli spustit jednu aplikaci).

* VM = Vysoká izolace, velká režie (GB RAM).  
* Kontejner = Sdílené jádro, minimální režie (MB RAM).

V moderní infrastruktuře se tyto světy prolínají – často běží Docker kontejnery uvnitř virtuálních strojů v cloudu.

## **Obsah praktické části**

Nyní, když chápete teorii, vrhneme se na praxi. Přeměníme vaši instalaci VirtualBoxu na simulované datacentrum.

* [**01. Instalace Linux Serveru**](./01-instalace-serveru) - *Základní setup.*  
* [**02. Síťování a Port Forwarding**](./02-sitovani-port-forwarding) - *Jak se dostat dovnitř přes NAT.*  
* [**03. SSH a Bezpečnost**](./03-ssh-keys-security) - *Generování klíčů a hardening.*  
* [**04. Snapshoty a Headless režim**](./04-snapshots-headless) - *Profesionální správa.*