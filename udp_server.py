import socket
import json
from init_config import STATE


class UDP_Server:
    def __init__(self, STATE, logger):
        self.logger = logger
        socker_ip = "0.0.0.0" #STATE['SOCKET_IP'].value
        socket_port = STATE['SOCKET_PORT'].value
        socket_paralel = STATE['SOCKET_PARALEL'].value
        self.MAIN_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.MAIN_SOCKET.bind((socker_ip, socket_port))
        self.MAIN_SOCKET.listen(socket_paralel)
        self.logger.info("Serwer nasłuchuje na porcie: %d" % socket_port)

    def update_state_machine(self, raw_data):
        from ui_flow import sliderX_changed, sliderY_changed
        global STATE
        try:
            data = json.loads(raw_data.decode('utf-8'))
            STATE['X_POINT'].set(data.get(STATE['X_POINT'].name, STATE['X_POINT'].value))
            STATE['Y_POINT'].set(data.get(STATE['Y_POINT'].name, STATE['Y_POINT'].value))

            sliderX_changed(STATE['X_POINT'].value)
            sliderY_changed(STATE['Y_POINT'].value)
            return {"status": 200}
        except Exception as e:
            details = "Błąd podczas parsowania danych: %s" % e
            self.logger.error(details)
            return {"status": 500, "details": details}

    def spin_udp_server(self):
        try:
            while True:
                self.logger.info("Oczekiwanie na połączenie...")
                client_socket, client_address = self.MAIN_SOCKET.accept()
                self.logger.info("Połączono z: %s" % str(client_address))

                while True:
                    raw_data = client_socket.recv(1024)
                    if not raw_data:
                        self.logger.info("Rozłączenie z: %s" % str(client_address))
                        break

                    self.logger.info("Otrzymano: %s" % raw_data.decode('utf-8'))
                    msg = self.update_state_machine(raw_data)
                    client_socket.send(json.dumps(msg).encode('utf-8'))

                client_socket.close()
        except Exception as e:
            self.logger.error("Wystąpił błąd: %s" % e)
        finally:
            self.MAIN_SOCKET.close()
