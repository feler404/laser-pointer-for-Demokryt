import socket
import json

# Ustawienia serwera
server_ip = '192.168.1.101'  # Zastąp adresem IP mikrokontrolera
server_port = 5000

# Tworzenie gniazda TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# Wysłanie wiadomości do serwera echo
message = {"X_POINT": 90, "Y_POINT": 100}
message = json.dumps(message)
client_socket.send(message.encode('utf-8'))

# Otrzymanie odpowiedzi z serwera (echo)
data = client_socket.recv(1024)
print("Otrzymano z serwera:", data.decode('utf-8'))

client_socket.close()