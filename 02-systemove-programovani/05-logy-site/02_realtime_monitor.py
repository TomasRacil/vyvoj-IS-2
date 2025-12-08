import sys
import re
import time

# Tento skript neotvírá soubor. Čte data, která mu "tečou" na vstup (Pipe).
# Použití: journalctl -f | python3 02_realtime_monitor.py

def monitor_stream():
    print("--- Start Real-time Monitor (Ctrl+C pro ukončení) ---")
    print("Čekám na data ze standardního vstupu (stdin)...")

    # Regex pro hledání podezřelých slov (case insensitive)
    error_pattern = re.compile(r"(error|fail|critical|denied)", re.IGNORECASE)

    try:
        # sys.stdin se chová jako otevřený soubor, který nikdy nekončí (pokud stream běží)
        for line in sys.stdin:
            line = line.strip()
            
            # Pokud řádek obsahuje chybu, zvýrazníme ho
            if error_pattern.search(line):
                # Vypíšeme s vykřičníky pro upoutání pozornosti
                print(f"\n[!!! ALERT !!!] {line}")
                
                # Zde by se mohlo poslat upozornění na Slack/Email
                # send_slack_notification(line)
            else:
                # Běžné řádky vypíšeme jen tak (nebo je můžeme ignorovat)
                # print(f"[INFO] {line}")
                pass

    except KeyboardInterrupt:
        print("\nMonitor ukončen.")

if __name__ == "__main__":
    monitor_stream()