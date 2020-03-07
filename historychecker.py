import sqlite3
import socket

def historysaver():

    con = sqlite3.connect('/home/pinakee/.config/google-chrome/Default/History')
    c = con.cursor()
    c.execute("select url, title, visit_count, last_visit_time from urls")
    history  = c.fetchall()

    file = open("historysaver.txt", 'a')


    for h in history:
        file.write(h[0])
        #file.write("\n")

    server_IP = socket.gethostname()
    port = 5000
    client_socket = socket.socket()
    client_socket.connect((server_IP,port))

    client_socket.send("Hey server...".encode())
    print(str(client_socket.recv(1024).decode()))

    filename='historysaver.txt'
    f = open(filename,'rb')
    print(" sending ....")
    client_socket.send("Sending the history ...".encode())
    print(" Sent..")

    l = f.read(1024)
    while (l):
       client_socket.send(l)
       print('Sent ' , l)
       l = f.read(1024)
    f.close()

    print('Done sending')
    client_socket.send('Thank you for connecting'.encode())
    client_socket.close()

    file.close()

historysaver()
