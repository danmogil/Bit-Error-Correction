from socket import AF_INET, SOCK_STREAM
from random import random
from HammingCode import HammingCode
from TCPSocket import TCPSocket

class Transmitter(TCPSocket):
  BIT_ERROR_RATE = .005

  def __init__(self, TCP_IP: str, TCP_PORT: int):
    self._socket.bind((TCP_IP, TCP_PORT))
    
  def open(self):
    self._socket.listen(1)
    while True:
      address = self._socket.accept()[1]
      print(f'New connection: {address}')
      req = input("Transmit? ( 'y' to continue ) ")
      if req == 'y': self.__transmit(input('Filepath: '))
      else: self.close()
  
  def __transmit(self, filepath: str):
    with open(filepath) as f:
      code = HammingCode(f.read())
      transmission = code.encode()
      corrupted = self.__simulateErrors(transmission)
      self._socket.send(corrupted)
      self.close()
  
  def __simulateErrors(self, code):
    for i in range(len(code)):
      if random() <= self.BIT_ERROR_RATE:
        code[i] = HammingCode.flipBit(code[i])
    return code