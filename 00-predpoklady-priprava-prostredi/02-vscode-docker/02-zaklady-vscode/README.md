# **Příklad 02: Seznámení s VS Code**

Než začneme programovat, musíme se naučit ovládat náš nástroj. VS Code má spoustu tlačítek, ale my si ukážeme jen to nejdůležitější.

## **Rozhraní editoru**

Otevřete VS Code. Vlevo uvidíte úzký pruh s ikonami (Activity Bar):

1. **Explorer (Ctrl+Shift+E):** Průzkumník souborů. Zde vidíte složky a soubory projektu.  
2. **Search (Ctrl+Shift+F):** Hledání (a nahrazování) textu v celém projektu.  
3. **Source Control (Ctrl+Shift+G):** Integrace Gitu. Zde budete psát commit messages a odesílat změny (viz sekce Git).  
4. **Run and Debug (Ctrl+Shift+D):** Nástroje pro hledání chyb v kódu.  
5. **Extensions (Ctrl+Shift+X):** Obchod s doplňky (Python, C++, témata vzhledu...).

## **Command Palette (Příkazová paleta)**

Toto je nejdůležitější zkratka v celém editoru. Zapamatujte si ji:

* **Windows/Linux:** `Ctrl + Shift + P`
* **macOS:** `Cmd + Shift + P`

Otevře se řádek nahoře uprostřed. Zde můžete ovládat úplně všechno. Zkuste do ní napsat:

* `Theme` -> pro změnu barvy editoru.  
* `Reload Window` -> pro restart editoru (když se něco zasekne).  
* `Settings` -> pro otevření nastavení.

## **Integrovaný Terminál**

Nemusíte přepínat okna mezi příkazovou řádkou a editorem. VS Code má terminál v sobě.

* **Zkratka:** Ctrl + ` (klávesa pod Esc, často s vlnovkou nebo středníkem).  
* Nebo v menu: `Terminal` -> `New Terminal`.

Zkuste v něm napsat příkaz `ls` (nebo `dir` na Windows), abyste viděli soubory ve složce.

## **Užitečné zkratky pro rychlou práci**

| Akce | Windows / Linux | macOS |
| :---- | :---- | :---- |
| Otevřít paletu příkazů | `Ctrl + Shift + P` | `Cmd + Shift + P` |
| Rychle otevřít soubor | `Ctrl + P` | `Cmd + P` |
| Zakomentovat řádek | `Ctrl + /` | `Cmd + /` |
| Zformátovat kód (uklidit) | `Shift + Alt + F` | `Shift + Option + F` |
| Více kurzorů (psát na více řádků) | `Alt + Click` | `Option + Click` |

## **Úkol**

1. Vytvořte ve VS Code nový soubor `test.txt`.  
2. Napište do něj několik řádků textu.  
3. Zkuste použít zkratku pro více kurzorů a na každý řádek připsat slovo "Ahoj" najednou.  
4. Otevřete integrovaný terminál a vypište obsah souboru (`cat test.txt` nebo `type test.txt`).