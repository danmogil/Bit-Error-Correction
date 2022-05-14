from unittest import TestCase, main
from HammingCode import HammingCode

class TestHammingCode(TestCase):

  def testEncode(self):
    self.assertEqual(HammingCode('1').encode(), '111')
    self.assertEqual(HammingCode('1011').encode(), '1011010')
    self.assertEqual(HammingCode('10011111001').encode(), '100111110011111')
    self.assertEqual(HammingCode('1011101').encode(), '1011010111000111')

  def testDecode(self):
    self.assertEqual(HammingCode('111').decode(), '1')
    self.assertEqual(HammingCode('1001010').decode(), '1011')
    self.assertEqual(HammingCode('100111110011111').decode(), '10011111001')

if __name__ == '__main__':
  main()