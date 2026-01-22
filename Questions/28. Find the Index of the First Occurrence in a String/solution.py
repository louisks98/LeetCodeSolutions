import unittest

class SubStringFinder:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle, 0, len(haystack))
    

class SubstringFinderTest(unittest.TestCase):
    def test_case1(self):
        finder = SubStringFinder()
        haystack = "sadbutsad"
        needle = "sad"
        expected = 0

        self.assertEqual(expected, finder.strStr(haystack, needle))

    def test_case2(self):
        finder = SubStringFinder()
        haystack = "leetcode"
        needle = "leeto"
        expected = -1

        self.assertEqual(expected, finder.strStr(haystack, needle))

    def test_case3(self):
        finder = SubStringFinder()
        haystack = "gaaabaaaaaaaaaaa"
        needle = "aaaaa"
        expected = 5

        self.assertEqual(expected, finder.strStr(haystack, needle))

    def test_case4(self):
        finder = SubStringFinder()
        haystack = "0010101010001110110000110"
        needle = "1110"
        expected = 12

        self.assertEqual(expected, finder.strStr(haystack, needle))

    def test_case5(self):
        finder = SubStringFinder()
        haystack = "a"
        needle = "a"
        expected = 0

        self.assertEqual(expected, finder.strStr(haystack, needle))

    def test_case6(self):
        finder = SubStringFinder()
        haystack = "aa"
        needle = "a"
        expected = 0

        self.assertEqual(expected, finder.strStr(haystack, needle))


    def test_case7(self):
        finder = SubStringFinder()
        haystack = "a"
        needle = "aaaaaaaa"
        expected = -1

        self.assertEqual(expected, finder.strStr(haystack, needle))

    def test_case8(self):
        finder = SubStringFinder()
        haystack = "0"
        needle = "aaaaaaaa"
        expected = -1

        self.assertEqual(expected, finder.strStr(haystack, needle))

    def test_case8(self):
        finder = SubStringFinder()
        haystack = "abc"
        needle = "c"
        expected = 2

        self.assertEqual(expected, finder.strStr(haystack, needle))


if __name__ == '__main__':
     unittest.main()