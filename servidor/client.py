import socket
HOST = 'localhost'
PORT = 8002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

# s.send(b'Enviado!')
s.send(input('Digite aqui: ').encode())  # codifica para binário

confirm = s.recv(1024)

if confirm == b"ok":
    print("message received!")
