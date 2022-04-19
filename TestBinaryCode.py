import unittest

from BinaryCode import BinaryCode 

class TestBinaryCode(unittest.TestCase):

  def setUp(self):
    self.code = BinaryCode('./input/test_bin.txt')

  def test_getHammingDistance(self):
    self.assertEqual(self.code.getHammingDistance(0, 1), 3)
    self.assertEqual(self.code.getHammingDistance(0, 2), 3)
    self.assertEqual(self.code.getHammingDistance(0, 3), 5)

  def test_getMinDistance(self):
    self.assertEqual(self.code.getMinDistance(), 2)

if __name__ == '__main__':
    unittest.main()