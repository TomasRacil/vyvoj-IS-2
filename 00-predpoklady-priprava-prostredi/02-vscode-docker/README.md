# **VS Code a Docker: Moderní vývojové prostředí**

V této sekci si nastavíme profesionální vývojové prostředí. Opustíme zastaralý způsob instalace všech knihoven přímo do vašeho operačního systému a přejdeme na moderní přístup pomocí kontejnerizace.

## **Proč to děláme?**

Vzpomeňte si na situaci, kdy učitel řekl: *"Mně to funguje,"* ale vám kód házel chyby, protože jste měli jinou verzi Pythonu nebo knihovny.

* **VS Code (Visual Studio Code):** Není to jen textový editor, je to mocné IDE (Integrated Development Environment), které je standardem v průmyslu.  
* **Docker:** Umožňuje nám zabalit celý počítač (operační systém, knihovny, nastavení) do malé "krabičky" zvané kontejner.  
* **Propojení:** VS Code umí běžet na vašem fyzickém počítači, ale editovat a spouštět kód uvnitř Docker kontejneru. Díky tomu budeme mít všichni ve třídě **naprosto identické prostředí**.

## **Obsah této sekce**

Tuto sekci jsme rozdělili do tří praktických kroků. Postupujte popořadě:

### [**01. Instalace nástrojů**](./01-instalace)

* Instalace Visual Studio Code.  
* Instalace Docker Desktop (nebo Engine).  
* Příprava rozšíření.

### [**02. Seznámení s VS Code**](./02-zaklady-vscode)

* Jak se v editoru neztratit.  
* Klávesové zkratky, které vám zachrání život (nebo alespoň čas).  
* Práce s terminálem a příkazovou paletou.

### [**03. Propojení (Dev Containers)**](./03-dev-containers)

* To nejdůležitější: Jak otevřít projekt v kontejneru.  
* Instalace rozšíření "Dev Containers".  
* Ověření, že vše funguje.

**Tip:** Nepřeskakujte instalaci rozšíření ve VS Code. Bez nich je to jen "hloupý" poznámkový blok. S nimi je to nástroj, který za vás napíše polovinu kódu.