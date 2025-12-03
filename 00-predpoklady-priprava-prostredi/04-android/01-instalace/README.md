# **Příklad 01: Instalace Android Studia**

Android Studio obsahuje vše potřebné: editor kódu (IntelliJ IDEA), překladače (Gradle) a emulátor telefonu.

## **1. Stažení**

1. Jděte na oficiální web: [developer.android.com/studio](https://developer.android.com/studio).  
2. Klikněte na velké tlačítko **Download Android Studio**.  
3. Musíte souhlasit s licenčními podmínkami ("I have read and agree...").  
4. Stáhněte instalátor pro váš systém.

## **2. Instalace (Průvodce)**

Spusťte instalátor a proklikejte se jím. Důležité momenty:

* **Choose Components:** Ujistěte se, že je zaškrtnuto **Android Virtual Device** (často bývá ve výchozím nastavení).  
* **Install Location:** Neměňte, pokud nemusíte. Cesty s mezerami nebo diakritikou mohou v budoucnu dělat problémy (např. `C:\Users\Lukáš\...` může být problém, lepší je `C:\Android`).

## **3. První spuštění (Setup Wizard)**

Po instalaci spusťte Android Studio. Otevře se další průvodce nastavením ("Setup Wizard"), který teprve začne stahovat to nejdůležitější – Android SDK (Software Development Kit).

1. **Import Settings:** Pokud se ptá, zvolte "Do not import settings".  
2. **Welcome obrazovka:** Klikněte na Next.  
3. **Install Type:** Zvolte **Standard**.  
4. **Select UI Theme:** Vyberte si Dracula (tmavý) nebo Light (světlý).  
5. **Verify Settings (DŮLEŽITÉ):**  
   * Podívejte se do seznamu. Musíte tam vidět **Android SDK** a **Performance (Intel HAXM / AEHD)**.  
   * Vpravo uvidíte celkovou velikost stahování (bude to několik GB).  
6. **License Agreement:**  
   * Musíte kliknout vlevo na každou položku (např. `android-sdk-license`) a vpravo zakliknout **Accept**. Teprve až odsouhlasíte všechny, pustí vás dál.  
7. **Finish:** Nyní se začnou stahovat a instalovat komponenty. **To může trvat 10–30 minut.**

## **4. Ověření**

Až se vše dokončí a uvidíte uvítací obrazovku "Welcome to Android Studio" s tlačítkem **New Project**, máte nainstalováno.

    Problémy na Windows?
    Pokud vám instalátor na konci nahlásí chybu týkající se HAXM nebo Hypervisor, znamená to, že máte vypnutou virtualizaci v BIOSu (stejný problém jako u VirtualBoxu).