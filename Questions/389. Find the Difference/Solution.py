import unittest

class DifferenceFinder:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) <= 0 and len(s) >= 1000:
            return ""
        if len(t) != len(s) + 1:
            return ""
        
        if len(s) == 0:
            return t

        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
    
        for ct, cs in zip(sorted_t, sorted_s):
            if ct != cs:
                return ct
            
        return sorted_t[-1]



class FindDiferenceTest(unittest.TestCase):
    def test_case1(self):
        finder = DifferenceFinder()
        input1 = "abcd"
        input2 = "abcde"
        expected = "e"
        self.assertEqual(expected, finder.findTheDifference(input1, input2))

    def test_case2(self):
        finder = DifferenceFinder()
        input1 = ""
        input2 = "y"
        expected = "y"
        self.assertEqual(expected, finder.findTheDifference(input1, input2))

    def test_case3(self):
        finder = DifferenceFinder()
        input1 = "asdfg"
        input2 = "dftgsa"
        expected = "t"
        self.assertEqual(expected, finder.findTheDifference(input1, input2))

    def test_case3(self):
        finder = DifferenceFinder()
        input1 = "a"
        input2 = "aa"
        expected = "a"
        self.assertEqual(expected, finder.findTheDifference(input1, input2))

    def test_case3(self):
        finder = DifferenceFinder()
        input1 = "poui"
        input2 = "piiou"
        expected = "i"
        self.assertEqual(expected, finder.findTheDifference(input1, input2))

    def test_case4(self):
        finder = DifferenceFinder()
        input1 = "pouii"
        input2 = "piiobu"
        expected = "b"
        self.assertEqual(expected, finder.findTheDifference(input1, input2))


if __name__ == '__main__':
     unittest.main()
        
