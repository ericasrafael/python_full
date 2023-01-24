import socket
HOST = 'localhost'
PORT = 8002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT)) # conectando host e porta ao socket

s.listen(5)  # 5 clients

while True:
    newSock, _ = s.accept()
    m = newSock.recv(1024).decode() # decodificando bytes para string
    print(m)
    newSock.send(b'ok')



