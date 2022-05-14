from socket import AF_INET, SOCK_STREAM
from HammingCode import HammingCode
from TCPSocket import TCPSocket

class Receiver(TCPSocket):

  def __init__(self, TCP_IP: str, TCP_PORT: int):
    self._socket.connect((TCP_IP, TCP_PORT))

  def read() -> str:
    
    code = HammingCode()
    return code.decode()
    
  def writeToFile(self, filepath: str):
    bin = self.read()
    with open(filepath, 'w') as f:
      f.write(bin)