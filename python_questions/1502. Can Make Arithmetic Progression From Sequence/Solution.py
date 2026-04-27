import unittest

class ArithmeticProgression:
    @staticmethod
    def canMakeArithmeticProgression(arr: list[int]) -> bool:
        arr.sort()
        n = arr[1] - arr[0]
        j = 2
        for i in range(1, len(arr)):
            if j > len(arr) - 1:
             break
            x = arr[j] - arr[i]
            if x != n:
                return False
            
            j += 1
            
        return True
        # tried to find a solution other than looping the array 
        # s1 = sum(arr)
        # d = arr[1] - arr[0]
        # n = len(arr)
        # s2 = n / 2 * (2 * arr[0] + (n - 1) * d)

        # return s1 == s2
            


class ArithmeticProgressionTest(unittest.TestCase):
    def test_case1(self):
        input = [3,5,1]
        self.assertTrue(ArithmeticProgression.canMakeArithmeticProgression(input))

    def test_case2(self):
        input = [1,2,4]
        self.assertFalse(ArithmeticProgression.canMakeArithmeticProgression(input))

    def test_case3(self):
        input = [1,1,1]
        self.assertTrue(ArithmeticProgression.canMakeArithmeticProgression(input))

    def test_case4(self):
        input = [11,2,8,5]
        self.assertTrue(ArithmeticProgression.canMakeArithmeticProgression(input))

    def test_case5(self):
        input = [-2,10,2,6]
        self.assertTrue(ArithmeticProgression.canMakeArithmeticProgression(input))

    def test_case6(self):
        input = [1,10,10,10,19]
        self.assertFalse(ArithmeticProgression.canMakeArithmeticProgression(input))

    def test_case7(self):
        input = [1,2,3,2,5]
        self.assertFalse(ArithmeticProgression.canMakeArithmeticProgression(input))

    def test_case8(self):
        input = [1,2,2,5,5]
        self.assertFalse(ArithmeticProgression.canMakeArithmeticProgression(input))


if __name__ == '__main__':
    unittest.main()