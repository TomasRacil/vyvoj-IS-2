import os
import time
import sys

def create_zombie():
    pid = os.fork()

    if pid > 0:
        # RODIČOVSKÝ PROCES
        print(f"[Rodič] Jsem proces PID {os.getpid()}.")
        print(f"[Rodič] Vytvořil jsem potomka PID {pid}.")
        print("[Rodič] Nyní budu 30 sekund spát a SCHVÁLNĚ si nepřečtu návratový kód potomka.")
        print(f"[Info] Otevřete si nový terminál a spusťte: ps -p {pid} -o stat,ppid,pid,cmd")
        print("[Info] Měli byste vidět stav 'Z' nebo 'Z+' (Zombie/Defunct).")
        
        time.sleep(30)
        
        # Správně by rodič měl udělat toto, aby zombie zmizela:
        # os.wait() 
        print("\n[Rodič] Probouzim se a končím. Zombie proces by měl být nyní odstraněn systémem (init).")

    else:
        # POTOMEK
        print(f"  [Potomek] Jsem proces PID {os.getpid()}.")
        print("  [Potomek] Okamžitě končím!")
        # Potomek končí, ale stává se Zombie, dokud si rodič nepřečte exit code.
        sys.exit(0)

if __name__ == "__main__":
    create_zombie()