using NUnit.Framework;

namespace CSharpQuestion;

public class LeetCode238
{
    static int[] ProductExceptSelf(int[] nums)
    {
        int[] result = new int[nums.Length];
        int[] prefix = new int[nums.Length];
        prefix[0] = 1;
        for (int i = 1; i < nums.Length; i++)
            prefix[i] = prefix[i-1] * nums[i-1];

        int[] suffix = new int[nums.Length];
        suffix[nums.Length- 1] = 1;
        for (int i = nums.Length - 2; i >= 0; i--)
            suffix[i] = suffix[i+1] * nums[i+1];


        for (int i = 0; i < result.Length; i++)
            result[i] = prefix[i] * suffix[i];
        
        return result;
    }

    public static void RunChallenge()
    {
        int[] input1 = [1, 2, 3, 4];
        int[] expected1 = [24,12,8,6];
        var result1 = ProductExceptSelf(input1);
        Assert.AreEqual(expected1, result1);
        Console.WriteLine(string.Join(",", result1));
        
        int[] input2 = [-1, 1, 0, -3, 3];
        int [] expected2 = [0,0,9,0,0];
        var result2 = ProductExceptSelf(input2);
        Assert.AreEqual(expected2, result2);
        Console.WriteLine(string.Join(",", result2));
        
        int[] input3 = [0,1];
        int [] expected3 = [1,0];
        var result3 = ProductExceptSelf(input3);
        Assert.AreEqual(expected3, result3);
        Console.WriteLine(string.Join(",", result3));
    }
}