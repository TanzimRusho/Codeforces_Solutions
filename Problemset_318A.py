import math

n, k = input().split()
n, k = int(n), int(k)

if k <= math.ceil(n/2):
    res = 2*k-1

elif n%2==0 and k > math.ceil(n/2):
    res = (k-n//2)*2
    
elif n%2==1 and k > math.ceil(n/2):
    res = (k-n//2-1)*2 
    
print(res)
