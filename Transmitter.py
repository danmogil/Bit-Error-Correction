from socket import socket, AF_INET, SOCK_STREAM

from HammingCode import HammingCode

class Transmitter:
  __socket = socket

  def __init__(self, TCP_IP: str, TCP_PORT: int):
    self.__socket = socket(AF_INET, SOCK_STREAM)
    self.__socket.bind((TCP_IP, TCP_PORT))
    self.__socket.listen(1)
  
  def transmit(self, filepath: str):
    with open(filepath, 'rb') as f:
      code = HammingCode(f.read())
      transmission: bytes = code.encode()