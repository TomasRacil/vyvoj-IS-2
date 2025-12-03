# **Virtualizace: Příprava prostředí**

V této sekci si připravíme nástroj pro **virtualizaci**. Na rozdíl od Dockeru, který sdílí jádro vašeho systému, nám virtualizace umožní spustit kompletní cizí operační systém (např. Linux Server) v izolovaném okně uvnitř vašeho Windows nebo macOS.

## **Proč instalujeme VirtualBox?**

Pro výuku sítí a serverů potřebujeme "pískoviště" (sandbox), kde můžeme bezpečně:

* Formátovat disky.  
* Měnit síťová nastavení.  
* Zkoušet viry nebo nebezpečné skripty.

Pokud byste to dělali na svém hlavním počítači, riskujete ztrátu dat. Ve virtuálním stroji (VM) se při chybě nic nestane – prostě ho smažete a vytvoříte znovu.

## **Obsah této sekce**

Tuto sekci jsme rozdělili do dvou kroků. Cílem je mít pouze připravený nástroj, samotný systém budeme instalovat později.

### [**01. Instalace VirtualBoxu**](./01-instalace)

* Stažení a instalace Oracle VM VirtualBox.  
* Instalace Extension Packu (důležité pro USB a hardware).  
* Specifika pro Apple Silicon (M1/M2/M3).

### [**02. Ověření funkčnosti**](./02-overeni)

* Kontrola, zda jde vytvořit virtuální stroj.  
* **Řešení problémů:** Co dělat, když počítač hlásí "VT-x is disabled" nebo konflikt s Hyper-V.

**Upozornění:** Virtualizace vyžaduje hardwarovou podporu procesoru. Pokud máte velmi starý notebook, může to být problém. V kroku 02 si ověříme, zda je vše v pořádku.