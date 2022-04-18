class BinaryCode:
  codewords: list[str] = []
  __fileName: str
  
  def __init__(self, fileName: str):
    with open(fileName) as f: 
      self.codewords = f.read().split() #allow variable length codewords?
      self.__fileName = fileName
  
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
    with open(f'CORRECTED_{self.__fileName}', 'w') as f:
      f.write(self.codewords)

  def __getHammingDistance() -> int:
    pass

  def __getMinDistance() -> int:
    pass

