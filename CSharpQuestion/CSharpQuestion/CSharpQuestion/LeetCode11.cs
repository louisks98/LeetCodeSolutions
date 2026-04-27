using NUnit.Framework;

namespace CSharpQuestion;

public class LeetCode11
{
    static int MaxArea(int[] height) 
    {
        int head = 0;
        int tail = height.Length - 1;
        int area = 0;
        
        while (tail > head)
        {
            var tempArea = Math.Min(height[head], height[tail]) * (tail - head);
            area = Math.Max(area, tempArea);
            if (height[head] < height[tail])
                head++;
            else
                tail--;
        }
        
        return area;
    }

    public static void RunChallenge()
    {
        int[] input = [1, 8, 6, 2, 5, 4, 8, 3, 7];
        var expected = 49;
        Assert.AreEqual(expected, MaxArea(input));
        
        int[] input2 = [1, 1];
        var expected2 = 1;
        Assert.AreEqual(expected2, MaxArea(input2));
        
        int[] input3 = [0, 0];
        var expected3 = 0;
        Assert.AreEqual(expected3, MaxArea(input3));
        
        int[] input4 = [2,3,10,5,7,8,9];
        var expected4 = 36;
        Assert.AreEqual(expected4, MaxArea(input4));
        
        int[] input5 = [4,3,2,1,4];
        var expected5 = 16;
        Assert.AreEqual(expected5, MaxArea(input5));

        int[] input6 = [1, 2, 4, 3];
        var expected6 = 4;
        Assert.AreEqual(expected6, MaxArea(input6));
    }
}