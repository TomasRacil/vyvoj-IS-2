import re
from collections import Counter

# Soubor s historickými daty
LOG_FILE = 'server.log'

# Regex pro Common Log Format (Apache/Nginx)
# 127.0.0.1 - - [10/Oct/2023...] "GET /index.html..." 200 2326
REGEX_PATTERN = r'^(\S+)\s+-\s+-\s+\[(.*?)\]\s+"(\S+)\s+(\S+)\s+.*?"\s+(\d{3})\s+.*'


def analyze_file():
    print(f"--- Analyzuji soubor: {LOG_FILE} ---")
    
    ip_counter = Counter()
    status_counter = Counter()
    
    try:
        with open(LOG_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if not line: continue

                match = re.match(REGEX_PATTERN, line)
                if match:
                    ip = match.group(1)      # IP adresa
                    status = match.group(5)  # Status kód (200, 404...)

                    ip_counter[ip] += 1
                    status_counter[status] += 1

        print("\n[TOP 5 Návštěvníků]")
        for ip, count in ip_counter.most_common(5):
            print(f"  {ip}: {count}x")

        print("\n[Status Kódy]")
        # Zde doplňte výpis statistik status kódů (Úkol 1)
        # ...

    except FileNotFoundError:
        print(f"Chyba: Soubor {LOG_FILE} neexistuje.")

if __name__ == "__main__":
    analyze_file()