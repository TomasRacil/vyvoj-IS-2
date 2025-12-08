import time

class SimpleEmulator:
    def __init__(self):
        # --- HARDWARE STAV ---
        self.register_a = 0
        self.register_b = 0
        self.pc = 0  # Program Counter (ukazatel, kde v paměti jsme)
        self.running = True

    def run(self, memory):
        
         # --- BOOTLOADER ---
        print("\n" * 2)
        print("   _____ _           _    ")
        print("  / ____| |         | |   ")
        print(" | (___ | |__   ___ | |_  ")
        print("  \___ \| '_ \ / _ \| __| ")
        print("  ____) | | | | (_) | |_  ")
        print(" |_____/|_| |_|\___/ \__| ")
        print("\n")
        time.sleep(1)
        print("BIOS v1.0 Initializing...")
        time.sleep(0.7)
        print(f"Načítám paměť ({len(memory)} bytes)... OK")
        time.sleep(0.7)
        print("Bootuji z ROM...")
        print("-" * 50)
        time.sleep(1)
        
        while self.running and self.pc < len(memory):
            # 1. FETCH: Načti instrukci z paměti
            opcode = memory[self.pc]
            self.pc += 1

            # 2. DECODE & EXECUTE: Rozhodni, co dělat podle čísla instrukce
            if opcode == 0x01:  # LOAD_A
                value = memory[self.pc] # Přečti další byte jako hodnotu
                print(f"[HW] LOAD_A: Načítám hodnotu {value} do Registru A")
                self.register_a = value
                self.pc += 1 # Posuneme se o parametr

            elif opcode == 0x02:  # LOAD_B
                value = memory[self.pc]
                print(f"[HW] LOAD_B: Načítám hodnotu {value} do Registru B")
                self.register_b = value
                self.pc += 1

            elif opcode == 0x03:  # ADD
                print(f"[HW] ADD: Sčítám A ({self.register_a}) + B ({self.register_b})")
                self.register_a = self.register_a + self.register_b

            elif opcode == 0x04:  # PRINT
                print(f" >>>> VÝSTUP DISPLEJE: {self.register_a} <<<<")
                # Simulace pomalosti I/O operace
                time.sleep(0.5) 

            elif opcode == 0x05:  # SUB
                print(f"[HW] SUB: Odčítám A ({self.register_a}) - B ({self.register_b})")
                self.register_a = self.register_a - self.register_b

            elif opcode == 0x06:  # SWAP
                print(f"[HW] SWAP: Prohazuji A ({self.register_a}) <-> B ({self.register_b})")
                self.register_a, self.register_b = self.register_b, self.register_a

            elif opcode == 0xFF:  # HALT
                print("[HW] HALT: Zastavuji CPU.")
                self.running = False

            else:
                print(f"[CHYBA] Neznámá instrukce: {opcode}")
                self.running = False
            
            # Simulace taktu procesoru (aby to student stíhal číst)
            time.sleep(0.2)

# --- SOFTWARE (ROM) ---
# Toto jsou "binární data", která by normálně byla v .exe souboru
# Program:
# 1. Do A dej 10
# 2. Do B dej 5
# 3. Prohoď je (A=5, B=10)
# 4. Sečti je (A = 5 + 10 = 15)
# 5. Odečti je (A = 15 - 10 = 5)
# 6. Vypiš A
program_rom = [
    0x01, 10,  # LOAD_A 10
    0x02, 5,   # LOAD_B 5
    0x06,      # SWAP (A=5, B=10)
    0x03,      # ADD  (A = 5 + 10 = 15)
    0x05,      # SUB  (A = 15 - 10 = 5)
    0x04,      # PRINT
    0xFF       # HALT
]

if __name__ == "__main__":
    cpu = SimpleEmulator()
    cpu.run(program_rom)