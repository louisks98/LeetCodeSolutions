import unittest

class SignProduct:
    @staticmethod
    def array_sign(nums: list[int]) -> int:
        if 0 in nums:
            return 0

        signs = [i for i, n in enumerate(nums) if n < 0]
        if len(signs) % 2 == 0:
            return 1
        else:
            return -1
        

class SignProductTest(unittest.TestCase):
    def test_case1(self):
        input = [-1,-2,-3,-4,3,2,1]
        expected = 1
        self.assertEqual(expected, SignProduct.array_sign(input))

    def test_case2(self):
        input = [1,5,0,2,-3]
        expected = 0
        self.assertEqual(expected, SignProduct.array_sign(input))

    def test_case3(self):
        input = [-1,1,-1,1,-1]
        expected = -1
        self.assertEqual(expected, SignProduct.array_sign(input))

    def test_case4(self):
        input = [0]
        expected = 0
        self.assertEqual(expected, SignProduct.array_sign(input))

    def test_case5(self):
        input = [-3,-3,-3]
        expected = -1
        self.assertEqual(expected, SignProduct.array_sign(input))

    def test_case6(self):
        input = [-4,-4,-4,-4]
        expected = 1
        self.assertEqual(expected, SignProduct.array_sign(input))

    def test_case7(self):
        input = [2,2]
        expected = 1
        self.assertEqual(expected, SignProduct.array_sign(input))

    

if __name__ == '__main__':
    unittest.main()