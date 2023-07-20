import socket
import threading




def handle_client(client_socket):
    while True:
        # receiving data from the client
        data = client_socket.recv(1024)
        if not data:
            break

        print(f"Received from client: {data.decode('utf-8')}")

        client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8000))
    server.listen(5)

    print('Server is listening for connections...')

    while True:
        client_socket, address = server.accept()
        print(f'connect to {address}')

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

        if __name__ == '__main__':
            start_server()
