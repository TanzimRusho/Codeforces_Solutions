using System;

class AlmostLuckyNumber {
    static void Main()
    {
        string num = Console.ReadLine();
        
        int count = 0;
        
        int length = num.Length;
        
        for (int i=0; i<length; ++i)
        {                        
            if (num[i] == '4' || num[i]== '7')
                ++count;
        }
        if (count == 4 || count == 7)
            Console.WriteLine("YES");
        else
            Console.WriteLine("NO");
    }        
}
