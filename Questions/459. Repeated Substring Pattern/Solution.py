import unittest

class SubstringPatternFinder:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 0:
            False

        sub = ""
        for c in s:
            sub += c

            if len(sub) > (len(s) / 2):
                return False

            i = s.count(sub)

            if i == 1 and len(sub) <= len(s):
                continue

            if (len(s) / len(sub)) % i != 0:
                continue 

            if len(s) == (len(sub) * i):
                return True
            
        return False
    

class SubstringPatternTest(unittest.TestCase):
    def test_case1(self):
        finder = SubstringPatternFinder()
        input = "abab"
        self.assertTrue(finder.repeatedSubstringPattern(input))

    def test_case2(self):
        finder = SubstringPatternFinder()
        input = "aba"
        self.assertFalse(finder.repeatedSubstringPattern(input))

    def test_case3(self):
        finder = SubstringPatternFinder()
        input = "abcabcabcabc"
        self.assertTrue(finder.repeatedSubstringPattern(input))

    def test_case4(self):
        finder = SubstringPatternFinder()
        input = "abcabdabeabf"
        self.assertFalse(finder.repeatedSubstringPattern(input))

    def test_case5(self):
        finder = SubstringPatternFinder()
        input = "abcdefabc"
        self.assertFalse(finder.repeatedSubstringPattern(input))

    def test_case6(self):
        finder = SubstringPatternFinder()
        input = "aaaaaaaaaa"
        self.assertTrue(finder.repeatedSubstringPattern(input))

    def test_case7(self):
        finder = SubstringPatternFinder()
        input = "aaa"
        self.assertTrue(finder.repeatedSubstringPattern(input))

    def test_case8(self):
        finder = SubstringPatternFinder()
        input = ""
        self.assertFalse(finder.repeatedSubstringPattern(input))


if __name__ == '__main__':
     unittest.main()