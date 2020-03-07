import socket

def server_program():
    # get the host name
    server_IP = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((server_IP,port))

    # how many clients can we listen ar max
    server_socket.listen(5)
    conn , address = server_socket.accept()
    print(" Connected to the client: " + str(address))
    print(str(conn.recv(1024).decode()))
    conn.send("Send the history".decode())
    file = open("logfile.txt" , "a")
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        file.write(data)
        file.write("\n")

        #data = input(" your input :->")
        #conn.send(data.encode())
    print("*"*100 + "\n\n the history data is fetched")
    conn.close()
    file.close()

if __name__ == '__main__':
    server_program()
