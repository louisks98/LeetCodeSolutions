import unittest

class AnagramFinder:
    def isAnagram(self, s: str, t: str) -> bool:    
        if len(s) != len(t):
            return False
        
        if(len(s) == 0):
            return False

        sorted_s = "".join(sorted(s.lower()))
        sorted_t = "".join(sorted(t.lower()))

        for ct, cs in zip(sorted_t, sorted_s):
            if ct != cs:
                return False
            
        return True
    


class TestAnagram(unittest.TestCase):
    def test_case1(self):
        finder = AnagramFinder()
        input1 = "anagram"
        input2 = "nagaram"
        self.assertTrue(finder.isAnagram(input1, input2))

    def test_case2(self):
        finder = AnagramFinder()
        input1 = "rat"
        input2 = "car"
        self.assertFalse(finder.isAnagram(input1, input2))

    def test_case3(self):
        finder = AnagramFinder()
        input1 = ""
        input2 = "car"
        self.assertFalse(finder.isAnagram(input1, input2))

    def test_case4(self):
        finder = AnagramFinder()
        input1 = ""
        input2 = ""
        self.assertFalse(finder.isAnagram(input1, input2))

    def test_case5(self):
        finder = AnagramFinder()
        input1 = "12345"
        input2 = "72413"
        self.assertFalse(finder.isAnagram(input1, input2))

    def test_case5(self):
        finder = AnagramFinder()
        input1 = "12345"
        input2 = "25143"
        self.assertTrue(finder.isAnagram(input1, input2))

    def test_case6(self):
        finder = AnagramFinder()
        input1 = "Hello World"
        input2 = " WlelloHrdo"
        self.assertTrue(finder.isAnagram(input1, input2))

    def test_case7(self):
        finder = AnagramFinder()
        input1 = "Hello"
        input2 = "lloeh"
        self.assertTrue(finder.isAnagram(input1, input2))


if __name__ == '__main__':
     unittest.main()