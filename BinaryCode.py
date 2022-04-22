from os import path

'''
# Daniel Mogil and Jacob Creasy

* assume triple repetition encoding
'''

class BinaryCode:
  codewords: list[str] = []
  __fileName: str
  __length: int
  
  def __init__(self, file_path: str, delimiter = ' '):
    with open(file_path) as f: 
      self.codewords = f.read().strip().split(delimiter)
      self.__fileName = path.basename(file_path)
      self.__length = len(self.codewords[0])
  
  def numDetectableErrors(self) -> int:
    minDistance = self.getMinDistance() - 1
    return minDistance if minDistance > -1 else 0

  def numCorrectableErrors(self) -> int:
    return self.numDetectableErrors() // 2

  def detectErrors(self) -> list[tuple]:
    errors = []
    for i, codeword in enumerate(self.codewords):
      repetitions = set(self.__splitCodeword(codeword))
      if len(repetitions) > 1:
        errors.append((i, codeword))
    return errors

  def correctErrors(self) -> None:
    errors = self.detectErrors()
    for i, error in errors:
      repetitions = self.__splitCodeword(error)
      corrected = max(repetitions, key = repetitions.count) * 3
      self.codewords[i] = corrected

  def writeCorrected(self):
    self.correctErrors()
    with open(f'./output/CORRECTED_{self.__fileName}', 'w') as f:
      [f.write(codeword + " ") for codeword in self.codewords]

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

  def __splitCodeword(self, codeword) -> list[str]:
      step = int(self.__length / 3)
      repetitions = [codeword[i:i+step] for i in range(0, self.__length, step)]  
      return repetitions

  def __assertDistanceConditions(self):
    try:
      assert len(self.codewords) > 1, "Error: |C| < 2"
      assert all(len(codeword) == self.__length for codeword in self.codewords), "Error: variable codeword length"
    except AssertionError as error:
      print(error)
      exit()