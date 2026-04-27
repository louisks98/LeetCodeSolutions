import unittest

class ZeroesMover :
    def moveZeroes(self, nums: list[int]) -> None:
        end = len(nums)
        i = -1
        while i < end and i + 1 < end:
            i += 1
            if nums[i] != 0:
                continue
            
            nums.append(nums.pop(i))
            end -= 1
            i -= 1
        



class ZeroesTest(unittest.TestCase):
    def testCase1(self):
        input = [0,1,0,3,12]
        expected = [1,3,12,0,0]
        mover = ZeroesMover()
        mover.moveZeroes(input)
        self.assertEqual(expected, input)

    def testCase2(self):    
        input = [0]
        expected = [0]
        mover = ZeroesMover()
        mover.moveZeroes(input)
        self.assertEqual(expected, input)

    def testCase3(self):    
        input = [0,0,0,0]
        expected = [0,0,0,0]
        mover = ZeroesMover()
        mover.moveZeroes(input)
        self.assertEqual(expected, input)

    def testCase4(self):    
        input = [3,3,0,0]
        expected = [3,3,0,0]
        mover = ZeroesMover()
        mover.moveZeroes(input)
        self.assertEqual(expected, input)

    def testCase4(self):    
        input = [0,0,1]
        expected = [1,0,0]
        mover = ZeroesMover()
        mover.moveZeroes(input)
        self.assertEqual(expected, input)

    def testCase5(self):    
        input = [1]
        expected = [1]
        mover = ZeroesMover()
        mover.moveZeroes(input)
        self.assertEqual(expected, input)


if __name__ == '__main__':
     unittest.main()