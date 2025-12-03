# **Příklad 03: Propojení VS Code a Dockeru (Dev Containers)**

 Místo toho, abychom instalovali Python, C++ nebo Javu přímo do Windows/Macu, řekneme VS Code: *"Vytvoř mi Docker kontejner, kde je všechno nainstalované, a připoj se k němu."*

## **Koncept: Dev Container**

Rozšíření **Dev Containers** (které jsme instalovali v kroku 01) umožňuje VS Code používat Docker kontejner jako plnohodnotné vývojové prostředí.

* Váš kód leží na vašem disku.  
* VS Code běží na vašem počítači.  
* **Ale:** Všechny příkazy (kompilace, spouštění skriptů, terminál) se vykonávají **uvnitř** Linuxového kontejneru.

## **Postup: Otevření projektu v kontejneru**

Zkusíme si vytvořit jednoduché prostředí pro Python (i když ho nemáte v PC nainstalovaný, bude to fungovat!).

1. **Vytvořte novou složku** kdekoli na disku (např. `moje-docker-zkouska`) a otevřete ji ve VS Code (`File` -> `Open Folder`).  
2. **Otevřete Command Palette** (`Ctrl+Shift+P` / `Cmd+Shift+P`).  
3. Začněte psát: `Dev Containers: Add Dev Container Configuration Files...` a vyberte tuto možnost.  
4. VS Code se vás zeptá na definici prostředí:  
   * Vyberte: **Show All Definitions...**  
   * Najděte a vyberte: **Python 3** (nebo jakýkoli jiný jazyk, který chcete zkusit).  
   * Verze: Vyberte `default` nebo `3.10`.  
   * Další doplňky (Features): Zatím nic nezaškrtávejte a dejte **OK**.  
5. Všimněte si, že se ve vašem projektu vytvořila složka `.devcontainer` se souborem `devcontainer.json`. Tento soubor říká Dockeru, jak má prostředí vypadat.  
6. **Reopen in Container:**  
   * VS Code by měl detekovat novou konfiguraci a vpravo dole zobrazit tlačítko "Reopen in Container". Klikněte na něj.  
   * *Pokud se to nezobrazí:* Otevřete Command Palette a napište `Dev Containers: Reopen in Container`.

## **Co se děje teď?**

Při prvním spuštění to bude chvíli trvat (stahuje se Linux image, instaluje se Python). Sledujte stav v pravém dolním rohu.

Jakmile se okno načte, podívejte se do **levého dolního rohu** VS Code. Měli byste tam vidět zelený indikátor s textem:

**Dev Container: Python 3**

## **Ověření**

Nyní jste "uvnitř" Linuxu, i když používáte Windows/Mac.

1. Otevřete ve VS Code terminál (Ctrl + `).  
2. Zadejte příkaz pro zjištění verze OS:  

   ```shell
   cat /etc/os-release
   ```

   Uvidíte, že jste pravděpodobně v systému **Debian** nebo **Ubuntu**, ne ve vašem hostitelském systému!  
3. Zkuste verzi Pythonu:
  
   ```shell
   python --version
   ```

   Měla by odpovídat tomu, co jste vybrali v konfiguraci.

## **Shrnutí**

Právě jste vytvořili izolované vývojové prostředí.

* Pokud byste tuto složku poslali spolužákovi, VS Code mu nabídne "Reopen in Container" a on bude mít **na bit přesně stejné prostředí** jako vy.  
* Pokud kontejner rozbijete, stačí ho smazat a nechat VS Code vytvořit znovu (Rebuild). Váš počítač zůstane čistý.