import socket
import json


global MAIN_SOCKET, X_VALUE, Y_VALUE


def init_udp_server(*args, **kwargs):
    global MAIN_SOCKET, X_VALUE, Y_VALUE
    X_VALUE = kwargs.get('X_VALUE', 0)
    Y_VALUE = kwargs.get('Y_VALUE', 0)
    SOCKET_IP = kwargs.get('IP_SOCKET', '0.0.0.0')
    SOCKET_PORT = kwargs.get('SOCKET_PORT', 5000)
    SOCKET_PARALEL = kwargs.get('SOCKET_PARALEL', 1)
    MAIN_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    MAIN_SOCKET.bind((SOCKET_IP, SOCKET_PORT))
    MAIN_SOCKET.listen(SOCKET_PARALEL)
    print("Serwer echo działa na porcie 5000")


def update_state_machine(raw_data):
    global X_VALUE, Y_VALUE
    try:
        data = json.loads(raw_data.decode('utf-8'))
    except Exception as e:
        print("Błąd podczas parsowania danych:", e)
        return None

    X_VALUE = data.get('x', X_VALUE)
    Y_VALUE = data.get('y', Y_VALUE)


def spin_udp_server():
    global MAIN_SOCKET
    try:
        while True:
            print("Oczekiwanie na połączenie...")
            client_socket, client_address = MAIN_SOCKET.accept()
            print("Połączono z:", client_address)

            # Odbieranie danych i odsyłanie ich z powrotem (echo)
            while True:
                raw_data = client_socket.recv(1024)
                if not raw_data:
                    print("Rozłączenie z:", client_address)
                    break

                print("Otrzymano:", raw_data.decode('utf-8'))
                update_state_machine(raw_data)
                client_socket.send(raw_data)

            client_socket.close()
    except Exception as e:
        print("Wystąpił błąd:", e)
    finally:
        MAIN_SOCKET.close()
