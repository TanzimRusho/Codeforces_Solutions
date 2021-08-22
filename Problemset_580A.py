#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	
	scanf("%d", &n);
	
	int array[n];
	    
	int count = 1;
	int max_ = 1;
	
	for(int i=0; i < n; ++i)
	{
	    scanf("%d", &array[i]);
	    
	    if (i > 0)
	    {
    	    if (array[i] >= array[i-1])
    	    {
    	        ++count;
    	        max_ = max(count, max_);
    	    }   
    	    else
    	        count = 1;
	    }       
	}
	
	printf("%d\n", max_);
	
	return 0;
}
