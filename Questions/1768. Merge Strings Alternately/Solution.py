import unittest

class AltStringMerger:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result: str = ""
        len1: int = len(word1)
        len2: int = len(word2)
        substring: str = ""

        if(len1 > len2):
            substring = word1[len2:]
        
        if(len2 > len1):
            substring = word2[len1:]

        for i in range(min(len1, len2)):
            result += word1[i] + word2[i]

        result += substring

        return result
    

class MergeStringTest(unittest.TestCase):

    def test_case1(self):
        merger = AltStringMerger()
        test1 = ["abc", "pqr"]
        expected = "apbqcr"
        self.assertEqual(expected, merger.mergeAlternately(test1[0], test1[1]))

    def test_case2(self):
        merger = AltStringMerger()
        test2 = ["ab", "pqrs"]
        expected = "apbqrs"
        self.assertEqual(expected, merger.mergeAlternately(test2[0], test2[1]))

    def test_case3(self):
        merger = AltStringMerger()
        test3 = ["abcd", "pq"]
        expected = "apbqcd"
        self.assertEqual(expected, merger.mergeAlternately(test3[0], test3[1]))


if __name__ == '__main__':
    unittest.main()