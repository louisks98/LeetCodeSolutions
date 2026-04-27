using System.Text;

namespace CSharpQuestion;

public class LeetCode443
{
    static int Compress(char[] chars)
    {
        var sb = new StringBuilder();
        var current = chars[0];
        int counter = 1;
        for (int i = 1; i < chars.Length; i++)
        {
            var c = chars[i];
            if(current == c)
                counter++;
            else
            {
                if(counter == 1)
                    sb.Append(current);
                else
                    sb.Append($"{current}{counter}");
                
                counter = 1;
                current = c;
            }
        }
        
        if(counter == 1)
            sb.Append(current);
        else
            sb.Append($"{current}{counter}");

        for (int i = 0; i < sb.Length; i++)
            chars[i] = sb[i];
        
        return sb.ToString().Length;
    }
}