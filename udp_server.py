import socket

global MAIN_SOCKET


def init_udp_server():
    global MAIN_SOCKET
    MAIN_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    MAIN_SOCKET.bind(('0.0.0.0', 5000))  # Wiązanie do wszystkich interfejsów, na porcie 12345
    MAIN_SOCKET.listen(5)  # Oczekiwanie na jedno połączenie naraz
    print("Serwer echo działa na porcie 5000")


def spin_udp_server():
    global MAIN_SOCKET
    try:
        while True:
            print("Oczekiwanie na połączenie...")
            client_socket, client_address = MAIN_SOCKET.accept()
            print("Połączono z:", client_address)

            # Odbieranie danych i odsyłanie ich z powrotem (echo)
            while True:
                data = client_socket.recv(1024)
                if not data:
                    print("Rozłączenie z:", client_address)
                    break
                print("Otrzymano:", data.decode('utf-8'))
                client_socket.send(data)  # Odsyłanie danych z powrotem do klienta

            client_socket.close()
    except Exception as e:
        print("Wystąpił błąd:", e)
    finally:
        server_socket.close()