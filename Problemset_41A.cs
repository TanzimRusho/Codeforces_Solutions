using System;

class Translation {
    static string Reverse(string text)
    {
        char[] chars = text.ToCharArray(); 
        char[] result = new char[text.Length];
        
        for(int i=0, j=text.Length-1; i < text.Length; ++i, --j)
        {
            result[i] = chars[j];
        }
        
        return new string(result);
    }
    
    
    static void Main()
    {
        string text1 = Console.ReadLine();
        string text2 = Console.ReadLine();
        
        if (text2 == Reverse(text1))
            Console.WriteLine("YES");
        else
            Console.WriteLine("NO");
    }        
}
