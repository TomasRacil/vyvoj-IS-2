# **04. Dev Containers: Vývoj přímo v Dockeru**

Zatím jsme Docker používali k **běhu** hotových aplikací. Ale co **vývoj**?

Představte si scénář:

* **Backend tým** potřebuje Python 3.9, PostgreSQL a specifické C++ knihovny.  
* **Frontend tým** potřebuje Node.js 18 (protože na 20 to padá) a jinou sadu nástrojů.

Pokud si toto všechno nainstalujete do svého Windows/Macu, vznikne "konfliktní peklo". Řešením jsou **Dev Containers**.

## **Jak to funguje?**

VS Code se rozdělí na dvě části:

1. **Klient (UI):** Běží na vašem fyzickém počítači. Vidíte okna, menu, barvy.  
2. **Server (Terminal, Debugger, Language Server):** Běží **uvnitř** Docker kontejneru.

Vy píšete kód ve Windows, ale kód se ukládá a spouští v Linuxu uvnitř kontejneru.

## **Obsah lekce**

Tato sekce jsme rozdělena na dvě části:

* [**01. Základy (Jeden skript)**](./01-zaklady)
    * Nejjednodušší možná ukázka.  
    * Otevřeme Python prostředí, aniž bychom měli Python nainstalovaný v PC.

* [**02. Pokročilý Full-Stack (Backend + Frontend)**](./02-full-stack-dev)
    * Simulace reálného scénáře full-stack developera.  
    * Budeme mít **dva různé kontejnery**:  
        1. **Backend:** Automaticky nastartuje Python i databázi PostgreSQL.  
        2. **Frontend:** Izolované prostředí pro Node.js.  
    * Ukážeme si, jak pracovat ve dvou oknech VS Code zároveň.

## **Prerekvizity**

Musíte mít nainstalované rozšíření **Dev Containers** ve VS Code.