import socket
import historychecker


def client_program():
    server_IP = socket.gethostname()
    port = 5000

    client_socket = socket.socket()

    client_socket.connect((server_IP,port))

    message = str(input(" Your input here: "))
    while message.lower() != "bye":
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(" Recieved from the server side :-> {}".format(data))
        message = input(" Send input to the server -->")



    client_socket.close()


if __name__ == "__main__":
    client_program()
