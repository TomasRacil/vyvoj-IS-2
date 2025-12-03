# **Blok 1: Virtualizace a Kontejnerizace**

V tomto bloku se podíváme na základ moderní infrastruktury. Zatímco v předchozích ročnících jste psali kód, který běžel přímo na vašem procesoru a operačním systému, v profesionální praxi se aplikace spouštějí v izolovaných prostředích.

## **Cíle bloku**

1. Pochopit rozdíl mezi **Emulací**, **Virtualizací** a **Kontejnerizací**.  
2. Nainstalovat a zprovoznit **Linux Server** ve virtuálním stroji.  
3. Ovládnout **Docker CLI** pro správu kontejnerů.  
4. Naučit se psát **Dockerfiles** a používat **Docker Compose**.

## **Srovnání technologií**

Představte si, že chcete bydlet (spustit aplikaci).

| Koncept | Technický popis | Příklad |
| :---- |  :---- | :---- |
| **Běžný běh (Native)** | Aplikace běží přímo na hostitelském operačním systému a hardwaru. Má přístup ke všem systémovým prostředkům. Poskytuje maximální výkon, ale nulovou izolaci od systému. | `python main.py` spuštěný v terminálu vašeho PC. |
| **Emulace** | Software softwarově simuluje cizí hardware (jinou architekturu procesoru). Musí překládat každou instrukci CPU, což je výpočetně velmi náročné a pomalé. | Spouštění Android aplikací (ARM) na PC s Intelem (x86). Hraní GameBoy her na PC. |
| **Virtualizace (VM)** | Hypervisor rozděluje fyzický hardware na virtuální stroje. Každé VM má **vlastní jádro operačního systému (Kernel)**, virtuální disk a přidělenou paměť. Je to bezpečná a silná izolace, ale náročná na zdroje (každé VM zabírá GB paměti). | VirtualBox, VMware, Hyper-V, cloudové instance (AWS EC2). |
| **Kontejnerizace** | Kontejnery **sdílejí jádro hostitelského operačního systému**, ale mají izolovaný uživatelský prostor (procesy, souborový systém, síť). Startují v řádu milisekund a mají minimální režii. | **Docker**, Podman, Kubernetes. |

## **Obsah**

* [**01. Emulace (Teorie)**](./01-emulace)  
* [**02. Virtuální stroje (Praxe - Linux Server)**](./02-virtualni-stroje)  
* [**03. Kontejnerizace (Docker)**](./03-kontejnerizace)