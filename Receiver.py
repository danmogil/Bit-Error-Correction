from socket import socket, AF_INET, SOCK_STREAM

class Receiver:
  __socket = socket

  def __init__(self,TCP_IP: str, TCP_PORT: int):
    self.__socket(AF_INET, SOCK_STREAM)
    self.__socket.connect((TCP_IP, TCP_PORT))

  def writeToFile(self, filepath: str):
    with open(filepath, 'wb') as f:
      pass