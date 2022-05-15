from socket import socket, AF_INET, SOCK_STREAM 
from HammingCode import HammingCode

def receive(HOST: str, PORT: int):
  sock = socket(AF_INET, SOCK_STREAM)
  sock.connect((HOST, PORT))
  print('Reading data...')
  recv = sock.recv(1024).decode()
  data = HammingCode(recv).decode()
  with open(input("Output path: "), 'w') as f:
    f.write(data)
  print('Success')
  sock.close()