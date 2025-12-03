# **Příklad 02: Ověření funkčnosti (Testovací stroj)**

Nyní ověříme, zda váš počítač vůbec dovolí VirtualBoxu pracovat. Častým problémem je vypnutá virtualizace v BIOSu nebo konflikt s Windows Hyper-V.

## **Testovací postup**

Nebudeme zatím instalovat žádný systém, jen zkusíme vytvořit "prázdnou schránku".

1. Spusťte **VirtualBox**.  
2. Klikněte na velkou modrou ikonu **New** (Nový).  
3. Vyplňte údaje pro test:  
   * **Name:** Test-VM  
   * **Folder:** Nechte výchozí.  
   * **ISO Image:** Nechte prázdné (Not Selected).  
   * **Type:** Linux  
   * **Version:** Ubuntu (64-bit)  
4. Klikněte na **Next**.  
5. **Hardware:**  
   * Zkuste nastavit RAM alespoň na 4096 MB (pokud máte dost paměti).  
   * Processors: Zkuste nastavit 2 CPU.  
   * *Pokud vám posuvníky nedovolí nastavit více než 1 CPU nebo hlásí chybu, máte problém (viz níže).*  
6. Klikněte na **Next** -> **Next** -> **Finish**.

V levém sloupci by se měl objevit Test-VM se stavem "Powered Off".

## **Zkouška spuštění**

1. Vyberte `Test-VM` a klikněte na zelenou šipku **Start**.  
2. Mělo by se otevřít černé okno s logem VirtualBoxu a textem "No bootable medium found" (nebo podobná hláška).\*  
3. **PAK JE TO V POŘÁDKU** Znamená to, že virtualizace funguje, jen jsme tam nedali žádný systém.

## **Řešení problémů (Troubleshooting)**

Pokud se okno neotevře a vyskočí chyba, zkontrolujte následující:

### **Chyba: "VT-x is disabled in the BIOS for all CPU modes"**

Tohle je nejčastější problém. Váš procesor umí virtualizaci, ale je vypnutá v základní desce.

* **Řešení:** Restartujte počítač -> vstupte do BIOSu (klávesa F2, F10, Del nebo Enter při startu) -> hledejte položku **Intel Virtualization Technology** (nebo AMD-V / SVM) -> přepněte na **Enabled** -> Uložte a restartujte.

### **Chyba: "Verr_NEM_Vm_Create_Engine" nebo pomalý běh na Windows**

VirtualBox se "pere" s Windows funkcí Hyper-V nebo WSL2.

* **Řešení:** Většinou stačí zkontrolovat, že máte nejnovější verzi VirtualBoxu (verze 6+ už umí koexistovat s Hyper-V).

### **Chyba na macOS: "Kernel driver not installed (rc=-1908)"**

MacOS zablokoval ovladače VirtualBoxu.

* **Řešení:** Jděte do *System Settings* -> *Privacy & Security*. Měli byste tam vidět tlačítko "Allow" pro software od Oracle America. Povolte ho a restartujte Mac.

    Hotovo?  
    Pokud jste úspěšně viděli černé okno s chybou "No bootable medium", máte splněno. Tento testovací stroj můžete smazat (Pravým tlačítkem na `Test-VM` -> Remove -> Delete all files).