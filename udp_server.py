import socket
import json
from init_config import STATE
global MAIN_SOCKET


def init_udp_server(STATE):
    global MAIN_SOCKET
    socker_ip = "0.0.0.0" #STATE['SOCKET_IP'].value
    socket_port = STATE['SOCKET_PORT'].value
    socket_paralel = STATE['SOCKET_PARALEL'].value
    MAIN_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    MAIN_SOCKET.bind((socker_ip, socket_port))
    MAIN_SOCKET.listen(socket_paralel)
    print("Serwer nasłuchuje na porcie:", socket_port)


def update_state_machine(raw_data):
    from ui_flow import sliderX_changed, sliderY_changed
    global STATE
    try:
        data = json.loads(raw_data.decode('utf-8'))
        STATE['X_POINT'].value = data.get(STATE['X_POINT'].name, STATE['X_POINT'].value)
        STATE['Y_POINT'].value = data.get(STATE['Y_POINT'].name, STATE['Y_POINT'].value)

        sliderX_changed(STATE['X_POINT'].value)
        sliderY_changed(STATE['Y_POINT'].value)
        return "OK"
    except Exception as e:
        msg = "Błąd podczas parsowania danych: %s" % e
        print(msg)
        return msg


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
                msg = update_state_machine(raw_data)
                client_socket.send(raw_data+msg.encode('utf-8'))

            client_socket.close()
    except Exception as e:
        print("Wystąpił błąd:", e)
    finally:
        MAIN_SOCKET.close()
