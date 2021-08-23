import math

t = int(input())

for i in range(t):
    number = int(input())
    
    seven = int(math.ceil(math.sqrt(number)))
    
    mid = seven * seven - (seven-1)
    
    if number == mid:
        print(seven, seven)
        
    elif number < mid:
        print((seven - (mid-number)), seven)
    
    else:
        print(seven, (seven-(number-mid)))
    
