import socket
import threading
import signal
import sys
import os

# Odkaz na teorii soketů: [DOPLNIT_ODKAZ]
# Odkaz na teorii threadingu: [DOPLNIT_ODKAZ]

HOST = '0.0.0.0'
PORT = 12345
clients = []
server_socket = None

def log(msg):
    """Pomocná funkce pro logování, aby to vypadalo hezky v systemd"""
    # Systemd automaticky přidává časovou značku, takže stačí čistý text
    print(f"[SERVER PID {os.getpid()}] {msg}", flush=True)

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                client.close()
                if client in clients:
                    clients.remove(client)

def handle_client(client_socket, address):
    log(f"Nové připojení: {address}")
    try:
        client_socket.send("Vítejte v chatu!\n".encode('utf-8'))
        while True:
            message = client_socket.recv(1024)
            if not message:
                break
            # Logujeme aktivitu (v reálu bychom logovali obsah zpráv jen pro audit)
            log(f"Zpráva od {address}: {len(message)} bajtů")
            broadcast(message, client_socket)
    except Exception as e:
        log(f"Chyba u klienta {address}: {e}")
    finally:
        client_socket.close()
        if client_socket in clients:
            clients.remove(client_socket)
        log(f"Odpojení: {address}")

def signal_handler(sig, frame):
    """Obsluha signálů pro korektní ukončení služby (Systemd stop)"""
    log("Zachycen signál ukončení (SIGINT/SIGTERM).")
    log("Provádím Graceful Shutdown...")
    
    # Uzavřít všechny klientské sokety
    for client in clients:
        client.close()
    
    # Uzavřít hlavní soket
    if server_socket:
        server_socket.close()
    
    log("Server ukončen. Nashledanou.")
    sys.exit(0)

def start_server():
    global server_socket
    
    # Registrace signálů (propojení s lekcí 03)
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        log(f"Server startuje na {HOST}:{PORT}")
        
        while True:
            try:
                client_sock, addr = server_socket.accept()
                clients.append(client_sock)
                thread = threading.Thread(target=handle_client, args=(client_sock, addr))
                thread.daemon = True # Vlákno se ukončí, když skončí hlavní program
                thread.start()
            except OSError:
                break # Soket byl zavřen při shutdownu

    except Exception as e:
        log(f"Kritická chyba serveru: {e}")
    finally:
        if server_socket:
            server_socket.close()

if __name__ == "__main__":
    start_server()