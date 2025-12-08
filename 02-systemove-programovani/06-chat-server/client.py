import socket
import threading

HOST = '127.0.0.1' # Pokud testujete z jiného PC, zadejte IP serveru
PORT = 12345

def listen(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data: break
            print(f"\r{data.decode().strip()}\n> ", end="")
        except:
            break

def start():
    name = input("Jméno: ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("Server neběží!")
        return

    threading.Thread(target=listen, args=(s,), daemon=True).start()
    
    print(f"Připojeno k chatu. Pište zprávy ('exit' pro konec).")
    while True:
        msg = input("> ")
        if msg == 'exit': break
        s.send(f"{name}: {msg}".encode())
    s.close()

if __name__ == "__main__":
    start()