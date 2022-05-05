from socket import socket, AF_INET, SOCK_STREAM
from random import random

from HammingCode import HammingCode

class Transmitter:
  __socket = socket

  def __init__(self, TCP_IP: str, TCP_PORT: int):
    self.__socket = socket(AF_INET, SOCK_STREAM)
    self.__socket.bind((TCP_IP, TCP_PORT))
    self.__socket.listen(1)
  
  def transmit(self, filepath: str):
    with open(filepath) as f:
      code = HammingCode(f.read())
      transmission: str = code.encode()
      corrupted = self.__simulateErrors(transmission)

  def __simulateErrors(self, data: str) -> str:
    bitErrorRate = .005
    for i in range(len(data)):
      if random() <= bitErrorRate:
        data[i] = HammingCode.flipBit(data[i])
    return data