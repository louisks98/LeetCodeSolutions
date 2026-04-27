using NUnit.Framework;

namespace CSharpQuestion;

public class LeetCode334
{
    // I didn't solve this myself.
    static bool IncreasingTriplet(int[] nums) 
    {
        var first = int.MaxValue;
        var second = int.MaxValue;

        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] <= first)
                first = nums[i];
            else if (nums[i] <= second)
                second = nums[i];
            else
                return true;
        }
        
        return false;
    }

    public static void RunChallenge()
    {
        int[] input1 = [1, 2, 3, 4, 5];
        Assert.IsTrue(IncreasingTriplet(input1));
        
        int[] input2 = [5,4,3,2,1];
        Assert.IsFalse(IncreasingTriplet(input2));

        int[] input3 = [0, 0, 0, 2, 0, 3];
        Assert.IsTrue(IncreasingTriplet(input3));

        int[] input4 = [2, 1, 5, 0, 4, 6];
        Assert.IsTrue(IncreasingTriplet(input4));
        
        int[] input5 = [20,100,10,12,5,13];
        Assert.IsTrue(IncreasingTriplet(input5));
        
        int[] input6 = [1,1,1,1,1,1];
        Assert.IsFalse(IncreasingTriplet(input6));
        
        int[] input7 = [5,1,6];
        Assert.IsFalse(IncreasingTriplet(input7));
        
        int[] input8 = [5,1,6,8];
        Assert.IsTrue(IncreasingTriplet(input8));
        
        int[] input9 = [5,1,6,4];
        Assert.IsFalse(IncreasingTriplet(input9));
    }
}