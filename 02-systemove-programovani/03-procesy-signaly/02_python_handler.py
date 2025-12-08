import signal
import time
import sys
import os

def signal_handler(sig, frame):
    """
    Tato funkce se zavolá, když proces obdrží specifikovaný signál.
    """
    sig_name = signal.Signals(sig).name
    print(f"\n[INFO] Zachycen signál: {sig_name} ({sig})")
    
    # Zde by proběhl úklid - uložení stavu, zavření DB spojení, smazání tmp souborů
    print("[INFO] Probíhá úklid (ukládání dat, zavírání souborů)...")
    time.sleep(1) # Simulace práce
    
    print("[INFO] Hotovo. Ukončuji proces. Nashledanou.")
    sys.exit(0)

if __name__ == "__main__":
    print(f"Startuji aplikaci. Moje PID je: {os.getpid()}")
    print("Zkuste mě ukončit pomocí Ctrl+C (SIGINT) nebo příkazem 'kill <PID>' (SIGTERM).")
    print("Pro násilné ukončení bez úklidu použijte 'kill -9 <PID>'.")

    # Registrace handlerů pro SIGINT (Ctrl+C) a SIGTERM (kill výchozí)
    # Pozor: SIGKILL (9) zachytit nelze!
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Nekonečná smyčka simulující práci
    counter = 0
    while True:
        print(f"Pracuji... ({counter})")
        counter += 1
        time.sleep(2)