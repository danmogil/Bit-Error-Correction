from socket import socket, AF_INET, SOCK_STREAM 
from random import random
from HammingCode import HammingCode

BIT_ERROR_RATE =  0.05

def transmit(filepath: str, HOST: str, PORT: int):
  sock = socket(AF_INET, SOCK_STREAM)
  sock.bind((HOST, PORT))
  sock.listen(1)
  print('Waiting for connection...')
  while True:
    connection, address = sock.accept()
    print(f'New connection: {address}\nTransmitting Data...')
    with open(filepath) as f:
      code = HammingCode(f.read())
      transmission = code.encode()
      corrupted = simulateErrors(transmission)
      connection.send(corrupted.encode())
    print('Success')
    connection.close()
    break
  sock.close()

def simulateErrors(code: str):
  ls = list(code)
  numErrors = 0
  for i, bit in enumerate(ls):
    if random() <= BIT_ERROR_RATE:
      ls[i] = HammingCode.flipBit(bit)
      numErrors += 1
  print(f'Generated {numErrors} errors')
  return ''.join(ls)