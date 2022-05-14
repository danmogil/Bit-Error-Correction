from socket import AF_INET, SOCK_STREAM, socket

class TCPSocket:
  _socket: socket

  def __init__(self):
    self._socket = socket(AF_INET, SOCK_STREAM)

  def close(self):
    self._socket.close()