from unittest import TestCase, main
from HammingCode import HammingCode

class TestHammingCode(TestCase):

  def testEncode(self):
    self.assertEqual(HammingCode('1').encode(), '111') # (3, 1)
    self.assertEqual(HammingCode('1011').encode(), '1011010') # (7, 4)
    self.assertEqual(HammingCode('10011111001').encode(), '100111110011111') # (15, 11)
    self.assertEqual(HammingCode('1011101').encode(), '1011010111000111') # auto-scaling

  # 1-error each
  def testDecode(self):
    self.assertEqual(HammingCode('101').decode(), '1')
    self.assertEqual(HammingCode('1001010').decode(), '1011')
    self.assertEqual(HammingCode('100011110011111').decode(), '10011111001')
    self.assertEqual(HammingCode('1011011111000111').decode(), '1011101')

if __name__ == '__main__':
  main()