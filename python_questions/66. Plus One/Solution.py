import unittest

class PlusOne:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits) - 1
        while i >= 0:
                digit = digits[i]
                if digit < 9:
                    digits[i] += 1
                    break

                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                i -= 1

        return digits



class Tests(unittest.TestCase):
    def testCase1(self):
        plus = PlusOne()
        input = [1,2,3]
        expected = [1,2,4]
        self.assertEqual(expected, plus.plusOne(input))

    def testCase2(self):
        plus = PlusOne()
        input = [4,3,2,1]
        expected = [4,3,2,2]
        self.assertEqual(expected, plus.plusOne(input))

    def testCase3(self):
        plus = PlusOne()
        input = [9]
        expected = [1,0]
        self.assertEqual(expected, plus.plusOne(input))

    def testCase4(self):
        plus = PlusOne()
        input = [9,9,9]
        expected = [1,0,0,0]
        self.assertEqual(expected, plus.plusOne(input))

    def testCase5(self):
        plus = PlusOne()
        input = [4,9]
        expected = [5,0]
        self.assertEqual(expected, plus.plusOne(input))

    def testCase6(self):
        plus = PlusOne()
        input = [4,9,9]
        expected = [5,0,0]
        self.assertEqual(expected, plus.plusOne(input))
    
    def testCase7(self):
        plus = PlusOne()
        input = [0]
        expected = [1]
        self.assertEqual(expected, plus.plusOne(input))






if __name__ == '__main__':
     unittest.main()