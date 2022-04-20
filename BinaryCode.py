from os import path

class BinaryCode:
  codewords: list[str] = []
  __fileName: str
  __length: int
  
  def __init__(self, file_path: str):
    with open(file_path) as f: 
      self.codewords = f.read().split()
      self.__fileName = path.basename(file_path)
      self.__length = len(self.codewords[0])
  
  def numDetectableErrors(self) -> int:
    minDistance = self.getMinDistance() - 1
    return minDistance if minDistance > -1 else 0

  def numCorrectableErrors(self) -> int:
    return self.numDetectableErrors() // 2

# assume triple repetition encoding
  def detectErrors(self):
    errors = []
    for codeword in self.codewords:
      step = self.__length / 3
      repetitions = {codeword[i:i+step] for i in range(0, self.__length, step)}
      if len(repetitions) > 1:
        errors.append(codeword)
    return errors 

  def correctErrors():
     
    pass

  def writeCorrected(self):
    self.correctErrors()
    with open(f'./output/CORRECTED_{self.__fileName}', 'w') as f:
      f.write(self.codewords)

  def getHammingDistance(self, i, j) -> int:
    self.__assertDistanceConditions()
    distance = 0
    for i, val in enumerate(self.codewords[i]): 
      if val != self.codewords[j][i]:
        distance += 1
    return distance 

  def getMinDistance(self) -> int:
    self.__assertDistanceConditions()
    min = self.__length
    for i in range(len(self.codewords) - 1):
      for j in range(i + 1, len(self.codewords)):
        if self.codewords[i] == self.codewords[j]:
          continue
        hammingDistance = self.getHammingDistance(i, j)
        if hammingDistance < min:
          min = hammingDistance
    return min

  def __assertDistanceConditions(self):
    try:
      assert len(self.codewords) > 1, "Error: |C| < 2"
      assert all(len(codeword) == self.__length for codeword in self.codewords), "Error: variable codeword length"
    except AssertionError as error:
      print(error)
      exit()