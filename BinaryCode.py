import os

class BinaryCode:
  codewords: list[str] = []
  __fileName: str
  __length: int
  
  def __init__(self, path: str):
    with open(path) as f: 
      self.codewords = f.read().split()
      self.__fileName = os.path.basename(path)
      self.__length = len(self.codewords[0])
  
  def numDetectableErrors() -> int:
    pass

  def numCorrectableErrors() -> int:
    pass

  def detectErrors():
    pass

  def correctErrors():
    pass

  def writeCorrected(self):
    self.correctErrors()
    with open(f'./output/CORRECTED_{self.__fileName}', 'w') as f:
      f.write(self.codewords)

  def getHammingDistance(self, i, j) -> int:
    distance = 0
    for i, val in enumerate(self.codewords[i]): 
      if val != self.codewords[j][i]:
        distance += 1
    return distance 

  def getMinDistance(self) -> int:
    min = self.__length
    for i in range(len(self.codewords) - 1):
      for j in range(i + 1, len(self.codewords)):
        if self.codewords[i] == self.codewords[j]:
          continue
        hammingDistance = self.getHammingDistance(i, j)
        if hammingDistance < min:
          min = hammingDistance
    return min