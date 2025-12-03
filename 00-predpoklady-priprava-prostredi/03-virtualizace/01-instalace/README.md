# **Příklad 01: Instalace VirtualBoxu**

Oracle VM VirtualBox je open-source nástroj, který je zdarma a funguje na všech hlavních platformách.

## **1. Stažení instalátoru**

1. Přejděte na oficiální stránky [virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads).  
2. V sekci **VirtualBox 7.x.x platform packages** klikněte na odkaz pro váš systém:  
   * **Windows hosts** (pro Windows 10/11)  
   * **macOS / Intel hosts** (pro Macy s Intelem)  
   * **Developer preview for macOS / Arm64 (M1/M2/M3)** – *viz poznámka níže*.  
   * **Linux distributions** (pro Linux)

## **2. Stažení Extension Packu (Důležité!)**

Na stejné stránce o kousek níže najděte sekci **VirtualBox 7.x.x Oracle VM VirtualBox Extension Pack**.

1. Klikněte na **All supported platforms**.  
2. Stáhne se soubor s příponou .vbox-extpack. Budeme ho potřebovat po instalaci.

## **3. Instalace**

### **Pro Windows**

1. Spusťte stažený `.exe` soubor.  
2. Proklikejte instalátor (Next, Next...).  
3. Během instalace se může **krátce přerušit internetové připojení** (instalují se síťové ovladače). Nelekejte se.  
4. Po dokončení spusťte VirtualBox.

### **Pro macOS (Intel)**

1. Otevřete `.dmg` soubor.  
2. Dvakrát klikněte na ikonu `VirtualBox.pkg` a postupujte podle instrukcí.  
3. Pravděpodobně budete muset v **System Settings -> Privacy & Security** povolit rozšíření od Oracle.

### **Pro macOS (Apple Silicon - M1, M2, M3...)**

*Pozor: VirtualBox na čipech Apple Silicon je stále ve vývoji (Beta) a může být pomalý nebo nestabilní, protože musí emulovat instrukce x86.*

1. Stáhněte verzi pro **Arm64 / M1 / M2**.  
2. Nainstalujte standardně.  
3. Pokud by vám VirtualBox nefungoval spolehlivě, budeme to řešit individuálně (alternativou je placený Parallels nebo free UTM).

### **Pro Linux**

Použijte repozitář vaší distribuce nebo stáhněte `.deb`/`.rpm` balíček.

# Příklad pro Ubuntu/Debian

```shell
sudo apt update  
sudo apt install virtualbox virtualbox-ext-pack
```

## **4. Instalace Extension Packu**

Aby vám ve virtuálkách fungovalo USB 3.0, šifrování disku a další funkce:

1. Otevřete nainstalovaný VirtualBox.  
2. V menu klikněte na **File** -> **Tools** -> **Extension Pack Manager** (nebo jen dvakrát klikněte na stažený `.vbox-extpack` soubor).  
3. Klikněte na **Install** (nebo Upgrade).  
4. Musíte sjet posuvníkem licenčních podmínek až úplně dolů, jinak se tlačítko "I Agree" neaktivuje.  
5. Potvrďte instalaci.