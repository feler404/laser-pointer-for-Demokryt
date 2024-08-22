import _thread
import socket
from machine import Pin

# Global flag to control the listening loop
listening = True


# Function to run on the second core
def socket_listener(port):
    global listening
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)
    print("Socket listener started on core and port {port}")

    while listening:
        try:
            print("Waiting for connection...")
            client_socket, client_address = server_socket.accept()
            print("Connected to: {client_address}")

            while True:
                data = client_socket.recv(1024)
                if not data:
                    print("Disconnected from: {client_address}")
                    break
                print("Received: {data.decode('utf-8')}")
                # Process the received data here
                # For example, you could send it to a queue for processing on the main core

            client_socket.close()
        except Exception as e:
            print("Error in socket listener: {e}")

    server_socket.close()
    print("Socket listener stopped")


def start_socket_listener(port):
    _thread.start_new_thread(socket_listener, (port,))


def stop_socket_listener():
    global listening
    listening = False


def main():
    # Start the socket listener on the second core
    print(111)
    #start_socket_listener(12345)
    print(222)

    # Your main loop on the first core
    # try:
    #     while True:
    #         # Your main program logic here
    #         pass
    # except KeyboardInterrupt:
    #     print("Main program interrupted")
    # finally:
    #     stop_socket_listener()
    #     print("Main program ended")


if __name__ == "__main__":
    main()
