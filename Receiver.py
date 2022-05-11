from socket import socket, AF_INET, SOCK_STREAM
from HammingCode import HammingCode

class Receiver:
  __socket = socket

  def __init__(self, TCP_IP: str, TCP_PORT: int):
    self.__socket(AF_INET, SOCK_STREAM)
    self.__socket.connect((TCP_IP, TCP_PORT))

  def read() -> str:
    #receive
    code = HammingCode()
    return code.decode()
    
  def writeToFile(self, filepath: str):
    bin = self.read()
    with open(filepath, 'w') as f:
      f.write(bin)