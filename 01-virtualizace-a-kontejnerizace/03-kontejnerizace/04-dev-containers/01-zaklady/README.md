# **Příklad 01: Triviální Dev Container**

Cílem tohoto příkladu je otevřít Python soubor v prostředí, které má Python nainstalovaný, i když ho vy na svém počítači nemáte (nebo máte jinou verzi).

## **Struktura**

```
/01-zaklady  
├── .devcontainer/  
│   └── devcontainer.json  <-- Konfigurace prostředí  
└── hello.py               <-- Náš kód
```

## **Postup spuštění**

1. Ve VS Code zvolte **File -> Open Folder...** a vyberte složku `01-zaklady`.  
2. VS Code detekuje složku `.devcontainer` a vpravo dole se zeptá: *"Reopen in Container?"*  
3. Klikněte na **Reopen in Container**.  
   * *Pokud se nezeptal:* Stiskněte `F1` a napište `Dev Containers: Reopen in Container`.

## **Co se stane?**

* VS Code stáhne image `mcr.microsoft.com/devcontainers/python:3.11`.  
* Nastartuje kontejner.  
* Nainstaluje do něj rozšíření pro Python (jak je definováno v JSONu).  
* Otevře terminál uvnitř kontejneru.

## **Ověření**

Až se okno načte (vlevo dole bude zelený pruh), otevřete terminál (```Ctrl + ` ```) a zkuste:

```shell
python --version  
# Mělo by vypsat Python 3.11.x
```

Poté spusťte skript:

```shell
python hello.py 
``` 