#include <iostream>
using namespace std;

int main()
{
    char colors[51];
    int n, i;
    
    cin >> n;
    
    int count = 0;
    
    for(i=0; i<n; ++i)
    {
        cin >> colors[i];       
        
        if (colors[i] == colors[i-1])
            ++count;
    }
    
    cout << count << endl;
    
}
    
    
    
