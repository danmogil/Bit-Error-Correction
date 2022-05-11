from socket import socket, AF_INET, SOCK_STREAM
from random import random
from HammingCode import HammingCode

class Transmitter:
  __socket = socket
  BIT_ERROR_RATE = .005

  def __init__(self, TCP_IP: str, TCP_PORT: int):
    self.__socket = socket(AF_INET, SOCK_STREAM)
    self.__socket.bind((TCP_IP, TCP_PORT))
    self.__socket.listen(1)
  
  def transmit(self, filepath: str):
    with open(filepath) as f:
      code = HammingCode(f.read())
      transmission: str = code.encode()
      corrupted = self.__simulateErrors(transmission)
      #send
  
  def __simulateErrors(self, code):
    for i in range(len(code)):
      if random() <= self.BIT_ERROR_RATE:
        code[i] = HammingCode.flipBit(code[i])
    return code