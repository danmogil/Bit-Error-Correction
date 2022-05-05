from functools import reduce

class HammingCode:
  __chunks: list[str]

  def __init__(self, bin: str):
    self.__split(bin)

  @staticmethod
  def flipBit(bit: str) -> str:
    return '1' if bit == '0' else '0'

  def encode(self) -> str:
    pass

  def decode(self) -> str:
    corrected = []
    for chunk in self.__chunks:
      error = reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bin(chunk)) if bit])
      if error: 
        if chunk.count('1') % 2 == 0: self.__log(chunk)
        else: chunk[error] = HammingCode.flipBit(chunk[error])
      corrected.append(chunk)
    return ''.join(corrected)
      
  def __split(self, bin: str) -> None:
    size = [1, 4, 11, 26, 57, 120, 247]
    while len(bin) > 0:
      while len(bin) // size[-1] == 0: 
        size.pop(-1)
      self.__chunks.append(bin[:size[-1]])
      bin = bin[size[-1]:]

  def __log(self, chunk: str):
    with open('./log.txt', 'a') as f:
      f.write(f'Cannot correct byte-chunk, more than 1 error detected:\n{chunk}')
    print('Log written')