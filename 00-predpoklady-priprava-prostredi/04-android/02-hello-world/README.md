# **Příklad 02: Hello World (Ověření funkčnosti)**

Teď ověříme, zda dokážeme spustit aplikaci na virtuálním telefonu.

## **1. Vytvoření projektu**

1. Na úvodní obrazovce Android Studia klikněte na **New Project**.  
2. V záložce **Phone and Tablet** vyberte šablonu **Empty Views Activity** (pozor, nepleťte si s "Empty Activity" (bez slova Views), která používá Jetpack Compose - pro začátek je Views Activity jednodušší na pochopení struktury, ale pokud ji nevidíte, zvolte "Empty Activity").
3. **Nastavení projektu:**  
   * **Name:** `My First App` 
   * **Language:** **Kotlin**  
   * **Minimum SDK:** Nechte výchozí (např. API 24).  
4. Klikněte na **Finish**.

## **2. Čekání na Gradle (Sync)**

Jakmile se otevře okno editoru, **NIC NEDĚLEJTE**.  
Podívejte se do pravého dolního rohu. Uvidíte tam běžet procesy ("Gradle Build Running", "Scanning files"...).

* Android Studio si musí stáhnout knihovny pro sestavení projektu.  
* **První spuštění může trvat klidně 5–10 minut.**  
* Dokud se vlevo nahoře v panelu "Project" neobjeví zelené složky `app`, projekt není připraven.

## **3. Příprava Emulátoru**

Vpravo nahoře byste měli vidět roletku se zařízením (např. "Pixel 3a API 34").

1. Pokud tam vidíte "No Devices", klikněte na roletku a zvolte **Device Manager**.  
2. Klikněte na **Create Device**.  
3. Vyberte nějaký telefon (např. **Pixel 6**) a dejte Next.  
4. Vyberte System Image (zvolte ten, který má u sebe tlačítko Download, nebo ten doporučený).  
5. Dokončete průvodce.

## **4. Spuštění**

1. Máte vybrané zařízení v horní liště.  
2. Klikněte na zelený trojúhelník (**Run 'app'**).  
3. Počkejte. Otevře se nové okno s virtuálním telefonem.  
   * Telefon se musí zapnout (naběhnout Android).  
   * Poté se na něm nainstaluje vaše aplikace.  
4. Pokud vidíte na displeji telefonu nápis **"Hello World!"** (nebo "Hello Android!"), je to v pořádku.

Máte plně funkční prostředí pro vývoj mobilních aplikací.

## **Řešení problémů**

* **Emulátor je pomalý:** První start je vždy pomalý. Pokud je to ale nepoužitelné, zkontrolujte, zda máte v počítači dost volné RAM.  
* **Chyba "VT-x disabled":** Musíte povolit virtualizaci v BIOSu (viz sekce [03-virtualizace](../../03-virtualizace)).  
* **Chyba "Hyper-V":** Na Windows musí být pro Android Emulátor buď Hyper-V zapnuté (novější verze), nebo vypnuté (starší verze). Android Studio se to obvykle snaží opravit samo.