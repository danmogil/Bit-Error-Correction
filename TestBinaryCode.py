import unittest

from BinaryCode import BinaryCode 

class TestBinaryCode(unittest.TestCase):

  def setUp(self):
    self.codeA = BinaryCode('./input/test_bin1.txt')
    self.codeB = BinaryCode('./input/test_bin2.txt')

  def test_detectErrors(self):
    errorCodewordsA = [error[1] for error in self.codeA.detectErrors()]
    self.assertEqual(errorCodewordsA, ['000000000000100', '011100111101111'])
    
    errorCodewordsB = [error[1] for error in self.codeB.detectErrors()]
    self.assertEqual(errorCodewordsB, ['110111111', '001101011', '010010011'])

  def test_CorrectErrors(self):
    self.codeA.correctErrors()
    self.assertEqual(len(self.codeA.detectErrors()), 0)

    self.codeB.correctErrors()
    self.assertEqual(len(self.codeB.detectErrors()), 0)

  def test_numDetectableErrors(self):
    self.assertEqual(self.codeA.numDetectableErrors(), 3)
    self.assertEqual(self.codeB.numDetectableErrors(), 0)

  def test_numCorrectableErrors(self):
    self.assertEqual(self.codeA.numCorrectableErrors(), 1)
    self.assertEqual(self.codeB.numCorrectableErrors(), 0)
    
  def test_getHammingDistance(self):
    self.assertEqual(self.codeA.getHammingDistance(0, 1), 10)
    self.assertEqual(self.codeA.getHammingDistance(0, 2), 10)
    self.assertEqual(self.codeA.getHammingDistance(0, 3), 14)
    
    self.assertEqual(self.codeB.getHammingDistance(0, 1), 5)
    self.assertEqual(self.codeB.getHammingDistance(0, 2), 6)
    self.assertEqual(self.codeB.getHammingDistance(0, 3), 1)

  def test_getMinDistance(self):
    self.assertEqual(self.codeA.getMinDistance(), 4)
    self.assertEqual(self.codeB.getMinDistance(), 1)

if __name__ == '__main__':
    unittest.main()