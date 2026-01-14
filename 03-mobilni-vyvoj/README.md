# **Blok 2: Mobilní Vývoj (Android)**

Vítejte v bloku, kde se naučíme tvořit aplikace, které nosíte denně v kapse. Mobilní vývoj je o přímé interakci – váš kód reaguje na dotyky, gesta a polohu zařízení.

Využijeme jazyk **Kotlin**, který je moderním standardem pro Android vývoj (a nahradil starší Javu).

## **Historické okénko: Jak jsme se sem dostali?**

Než začneme psát kód, pojďme se podívat, jak se mobilní svět vyvíjel.

### **Před rokem 2007: Doba temna (tlačítková)**

* **Symbian (Nokia):** Král trhu. Skvělý na volání, ale instalace aplikací byla složitá a vývoj v C++ byl noční můrou.  
* **Windows Mobile (Microsoft):** Snažil se nacpat Windows 95 do malého displeje se stylusem. Nepoužitelné pro prsty.  
* **BlackBerry:** E-mailový stroj pro manažery.

### **2007: Revoluce (iPhone)**

Apple představil iPhone. Žádná klávesnice, kapacitní dotykový displej, plynulé animace. Změnil pravidla hry.

### **2008: Odpověď Googlu (Android)**

Google koupil malý startup **Android Inc.** (původně dělali OS pro foťáky) a vydal **Android 1.0** na telefonu T-Mobile G1.

* **Myšlenka:** Otevřený systém (Open Source), který může použít jakýkoliv výrobce (Samsung, HTC, Sony).  
* **Cíl:** Dostat služby Googlu (Search, Maps, Gmail) do každé kapsy.

## **Co je to Android?**

Android **není** jen jedna aplikace. Je to celý softwarový "stack" (vrstvy).

### **1. Linux Kernel (Spodek)**

Pro ty co to náhodou neví, tak andorid běží na Linuxu.

* Android využívá upravené jádro Linuxu pro správu hardwaru (displej, kamera, paměť, procesor).  
* Díky tomu nemusí Google psát ovladače pro každý čip – to řeší výrobci HW.

### **2. Hardware Abstraction Layer (HAL)**

Most mezi Linuxem a Androidem.

* Když zavoláte v kódu `camera.takePicture()`, HAL to přeloží pro konkrétní čočku od Sony nebo Samsungu.

### **3. Android Runtime (ART)**

Tady běží vaše aplikace.

* Aplikace píšeme v Kotlinu/Javě, ale procesor telefonu tomu nerozumí.  
* **Dříve (Dalvik):** Kód se překládal za běhu (JIT - Just In Time). Bylo to pomalé.  
* **Dnes (ART):** Kód se před-kompiluje při instalaci aplikace (AOT - Ahead Of Time). Je to mnohem rychlejší a šetrnější k baterii.

### **4. Java API Framework**

Sada knihoven, které používáme my vývojáři.

* Třídy jako `Activity`, `Button`, `NotificationManager`.

### **5. System Apps**

Aplikace, které vidí uživatel (Launcher, Telefon, Kontakty, a **Vaše Aplikace**).

## **Ekosystém: AOSP vs. GMS**

Často se plete "Android" a "Google Android".

1. **AOSP (Android Open Source Project):**  
   * Čistý Android. Zdrojový kód je volně dostupný.  
   * Může ho vzít kdokoliv (Amazon pro tablety Fire, výrobci ledniček, Huawei).  
   * **Neobsahuje:** Google Mapy, YouTube, Obchod Play.  
2. **GMS (Google Mobile Services):**  
   * To, co dělá Android Androidem.  
   * Balík proprietárních aplikací od Googlu (Play Store, Gmail, Maps API, Push notifikace).  
   * Výrobci musí Googlu platit (nebo plnit podmínky), aby to mohli mít v telefonu.  
   * *Příklad:* Huawei přišel o licenci na GMS, takže má telefony s Androidem (AOSP), ale bez Obchodu Play.

## **Cíle bloku**

1. Pochopit architekturu Android aplikace (`Activity`, `Fragment`, `Intent`).  
2. Naučit se tvořit uživatelské rozhraní pomocí **XML Layouts**.  
3. Zvládnout životní cyklus aplikace (co se stane, když otočím telefon?).  
4. Vytvořit funkční aplikaci, která reaguje na uživatele a ukládá data.

## **Zdrojové kódy (Referenční repozitář)**

Pro tento blok jsme připravili speciální repozitář, který obsahuje kompletní funkční aplikaci rozdělenou do fází.

[**Odkaz na repozitář s kódem**](https://github.com/TomasRacil/MyFirstAndroidApp) 

### **Jak s repozitářem pracovat?**

Repozitář používá **větve (branches)** pro každou lekci. Pokud se v návodu ztratíte, můžete si stáhnout funkční kód pro danou fázi.

## **Obsah kurzu**

* **[01. Úvod do Android Studia](https://github.com/TomasRacil/MyFirstAndroidApp/tree/01-starter)**
* Struktura projektu, Gradle, Android Manifest.
* První spuštění na emulátoru vs. fyzickém zařízení.

* **[02. Tvorba UI (XML Layouts)](https://github.com/TomasRacil/MyFirstAndroidApp/tree/02-ui-layouts)**
* LinearLayout vs. ConstraintLayout.
* Práce s vizuálním editorem.
* Tvorba formuláře (`EditText`, `Button`, `TextView`).

* **[03. Logika a Interaktivita](https://github.com/TomasRacil/MyFirstAndroidApp/tree/03-logic-basic)**
* Propojení XML s Kotlin kódem (`findViewById` vs. `ViewBinding`).
* Obsluha kliknutí (Listeners).
* Zobrazování "Toast" zpráv.

* **[04. Navigace a Životní cyklus](https://github.com/TomasRacil/MyFirstAndroidApp/tree/04-lifecycle-intents)**
* Metody `onCreate`, `onPause`, `onResume`.
* Přechod mezi obrazovkami (Intent).
* Předávání dat mezi aktivitami.

* **[05. Architektura (ViewModel)](https://github.com/TomasRacil/MyFirstAndroidApp/tree/05-lifecycle-fix)**
* ViewModel a zachování dat při rotaci obrazovky.
* Oddělení logiky od UI komponent.

* **[06. Dynamické seznamy (RecyclerView)](https://github.com/TomasRacil/MyFirstAndroidApp/tree/06-chat-ui)**
* **Adapter Pattern**: Propojení dat s grafickým rozhraním.
* Vlastní design položky (chatovací bublina) v XML.
* Recyklace prvků a efektivní zobrazení velkého množství dat.

* **[07. Trvalé ukládání (SharedPreferences)](https://github.com/TomasRacil/MyFirstAndroidApp/tree/07-settings)**
* Ukládání konfiguračních dat (IP adresa, port).
* Práce s dvojicemi Klíč–Hodnota.
* Persistence: Data, která přežijí i restart aplikace.

* **[08. Síťová komunikace a Coroutines](https://github.com/TomasRacil/MyFirstAndroidApp/tree/08-networking-send)**
* **Kotlin Coroutines**: Proč nesmí síť běžet na hlavním vlákně (`Dispatchers.IO`).
* Odesílání dat přes TCP Sockets.
* Správa oprávnění (Internet Permission) v Manifestu.

* **[09. Příjem zpráv a LiveData](https://github.com/TomasRacil/MyFirstAndroidApp/tree/09-networking-read)**
* Čtení ze socketu v reálném čase (nekonečná smyčka).
* **LiveData**: Jak dát aktivitě vědět, že dorazila nová zpráva.
* Kompletní propojení: Síť -> ViewModel -> UI.

## **Emulátor vs. Fyzický telefon**

Vývoj pro Android je náročný na výkon počítače.

| Metoda | Výhody | Nevýhody |
| :---- | :---- | :---- |
| **Emulátor (AVD)** | Nemusíte mít Android telefon. Snadné testování různých velikostí displeje. | **Žere hodně RAM (min. 4GB jen pro sebe).** Na pomalých PC je nepoužitelný. |
| **Fyzický telefon** | Extrémně rychlé. Nezatěžuje váš PC. Reálný chování (dotyk, senzory). | Musíte mít Android zařízení a USB kabel. Nutnost zapnout "Developer Mode". |

**Doporučení:** Pokud máte Android telefon, noste si ho do hodin i s kabelem! Ušetříte si spoustu nervů s pomalým emulátorem.

## **Prerekvizity**

* Nainstalované **Android Studio** (viz [Příprava prostředí](../00-predpoklady-priprava-prostredi/04-android)).  
* Základní znalost objektově orientovaného programování (třídy, dědičnost).