import socket
import threading
import random
import ssl
HEADER = 64
PORT = 5080
SERVER = "192.168.29.113"
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!disconnect"
HOST_NAME = socket.gethostname()
print(HOST_NAME)

#ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
#ssl_context.load_cert_chain(certfile="server_cert.pem", keyfile="server_key.pem")

with open("words.txt", "r") as file:
    words = file.read().splitlines()
    word_to_guess = random.choice(words).upper()

def handle_client(conn,addr):
    print("new connection")
    print(f"[New connection] {addr} [connected]")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(msg)
            i = 0
            res = list()
            while i < 5:
                if msg[i] == word_to_guess[i]:
                    res.append("V")
                else:
                    if msg[i] in word_to_guess:
                        res.append("O")
                    else:
                        res.append("X")
                i += 1
            response = ''.join(res)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            conn.send(response.encode(FORMAT))
    conn.close()


def start():
    server.listen()
    print("Server is listening on " + SERVER)
    print(word_to_guess)
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target= handle_client,args= (conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("starting")
start()