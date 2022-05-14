from numpy import matmul, concatenate, vstack, identity, array_equal, count_nonzero, shape
from math import floor, log2
from itertools import count
from typing import Union

class HammingCode:
  __bin: str
  __chunks: list[tuple[list, int]]
  
  def __init__(self, bin: str):
    self.__bin = bin
    self.__chunks = []

  def encode(self) -> str:
    self.__split(self.__bin, True)
    code = ''
    for chunk in self.__chunks:
      received = chunk[0]
      encoded = matmul(received, self.__getGeneratorMatrix(chunk)) % 2
      code += ''.join(map(str, encoded))
    return code

  def decode(self) -> str:
    self.__split(self.__bin, False)
    decoded = ''
    for chunk in self.__chunks:
      received, numParity = chunk
      codeword = received[:len(received)-numParity]
      parityCheckMatrix = self.__getParityCheckMatrix(chunk)
      error = matmul(received, parityCheckMatrix.T) % 2
      if count_nonzero(error) > 1: 
        for col in range(shape(parityCheckMatrix)[1] - numParity):
          if array_equal(error, parityCheckMatrix[:,col]):
            codeword[col] = self.flipBit(codeword[col])
            break
      decoded += ''.join(map(str, codeword))
    return decoded

  def flipBit(self, bit: Union[str, int]) -> str:
    return '1' if str(bit) == '0' else '0'

  def __getGeneratorMatrix(self, chunk):
    received, numParity = chunk
    P, I = self.__getParityMatrix(numParity), identity(len(received), dtype=int)
    return concatenate((I, P.T), 1)
 
  def __getParityCheckMatrix(self, chunk):
    numParity = chunk[1]
    P, I = self.__getParityMatrix(numParity), identity(numParity, dtype=int)
    return concatenate((P, I), 1)

  def __getParityMatrix(self, numParity):
    P = []
    for bit in range(1, 2 ** numParity):
      if not float.is_integer(log2(bit)):
        P.append([int(i) for i in format(bit, f'0{numParity}b')])
    return vstack(P).T

  def __split(self, bin, isDataBitsOnly):
    codeLen = len(bin)
    if codeLen == 0: 
      return
    numParity = self.__getNumParity(codeLen, isDataBitsOnly)
    numTot = 2 ** numParity - 1
    size = numTot - numParity if isDataBitsOnly else numTot
    chunk = [int(bit) for bit in bin[:size]]
    self.__chunks.append((chunk, numParity))
    self.__split(bin[size:], isDataBitsOnly)

  def __getNumParity(self, len, isDataBitsOnly):
    if isDataBitsOnly:
      for p in count(start=2):
        if 2 ** p - p - 1 > len or p == 9:
          return p - 1
    return floor(log2(len + 1))
