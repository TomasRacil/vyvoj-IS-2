import time
import signal
import sys
import os
import datetime

# --- Konfigurace ---
LOG_FILE = None # Pokud None, loguje do stdout (což Systemd zachytí)

def log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_msg = f"[{timestamp}] [PID {os.getpid()}] {message}"
    print(full_msg)
    sys.stdout.flush() # Důležité! Aby se log objevil v journalctl hned

def signal_handler(sig, frame):
    sig_name = signal.Signals(sig).name
    log(f"Zachycen signál {sig_name}. Ukončuji službu...")
    # Simulace úklidu
    time.sleep(1)
    log("Služba korektně ukončena.")
    sys.exit(0)

if __name__ == "__main__":
    # Registrace signálů pro graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    log("Služba startuje...")
    log(f"Pracovní adresář: {os.getcwd()}")
    
    # Simulace načítání konfigurace
    time.sleep(1)
    log("Konfigurace načtena.")

    # Hlavní smyčka služby
    counter = 0
    while True:
        counter += 1
        log(f"Služba běží... cyklus {counter}")
        
        # Simulace nějaké práce
        time.sleep(5)
        
        # Simulace občasné chyby (pro testování restartu)
        # if counter == 10:
        #     log("Kritická chyba! Pád aplikace.")
        #     sys.exit(1)