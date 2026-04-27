using NUnit.Framework;

namespace CSharpQuestion;

public class LeetCode151
{
    static string ReverseWords(string s)
    {
        s = s.Trim();
        string[] words = s.Split(' ');
        string[] trimmedWords = words.Select(w => w.Trim()).Where(w => !string.IsNullOrEmpty(w)).ToArray();
        Array.Reverse(trimmedWords);
        return string.Join(" ", trimmedWords);
    }

    public static void RunChallenge()
    {
        string test1 = "the sky is blue";
        string expected1 = "blue is sky the";
        Assert.AreEqual(expected1, ReverseWords(test1));

        string test2 = "  hello world  ";
        string expected2 = "world hello";
        Assert.AreEqual(expected2, ReverseWords(test2));
        
        string test3 = "a good   example";
        string expected3 = "example good a";
        Assert.AreEqual(expected3, ReverseWords(test3));
        
        string test4 = "    ";
        string expected4 = "";
        Assert.AreEqual(expected4, ReverseWords(test4));
        
        string test5 = "q";
        string expected5 = "q";
        Assert.AreEqual(expected5, ReverseWords(test5));
    }
}