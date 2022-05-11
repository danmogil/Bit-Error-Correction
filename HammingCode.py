from numpy import matmul, concatenate, vstack, identity
from math import floor, log2

class HammingCode:
  __bin: str
  __chunks: list[tuple(list, int)]
  
  def __init__(self, bin: str):
    self.__bin = bin

  def encode(self) -> str:
    self.__split(self.__bin, True)
    return self.__applyMatrix(self.__getGeneratorMatrix)

  def decode(self) -> str:
    self.__split(self.__bin)
    return self.__applyMatrix(self.__getParityCheckMatrix)

  def flipBit(self, bit: str) -> str:
    return '1' if bit == '0' else '0'

  def __applyMatrix(self, matrix: function) -> str:
    code = ''
    for chunk in self.__chunks:
      code += str(matmul(vstack(chunk), matrix(chunk)).item())
    return code

  def __getGeneratorMatrix(self, chunk):
    P, I = self.__getParityMatrix(chunk[0]), identity(len(chunk[0]) + chunk[1], dtype=int)
    return concatenate((I, P))
 
  def __getParityCheckMatrix(self, chunk):
    P, I = self.__getParityMatrix(chunk[0]), identity(chunk[1], dtype=int)
    return concatenate((P, I))

  def __getParityMatrix(self, chunk):
    P, dimensions = [], chunk[1]
    for bit in range(1, dimensions ** 2 + 1):
      if not float.is_integer(log2(bit)):
        P.append([int(i) for i in format(bit, f'0{dimensions}b')])
    return vstack(P).T

  def __split(self, bin, dataBitsOnly = False):
    codeLen = len(bin)
    if codeLen == 0: 
      return
    numParity = self.__greatestPowerOf2(codeLen)
    numTot = 2 ** numParity
    size = numTot - numParity if dataBitsOnly else numTot
    chunk = [int(bit) for bit in bin[:size]]
    self.__chunks.append((chunk, numParity))
    self.__split(bin[size:], dataBitsOnly)
      
  def __greatestPowerOf2(self, n):
    return floor(log2(n))