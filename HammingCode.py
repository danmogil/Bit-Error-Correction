class HammingCode:
  chunks: list[bytes]

  def __init__(self, bin: bytes):
    self.__split(bin)

  def encode(self) -> bytes:
    pass

  def decode(self) -> bytes:
    pass
      
  def __split(self, bin: bytes) -> None:
    sizes = [1, 4, 11, 26, 57, 120, 247]
    while len(bin) > 0:
      while len(bin) // sizes[-1] == 0: 
        sizes.pop(-1)
      self.chunks.append(bin[:sizes[-1]])
      bin = bin[sizes[-1]:]