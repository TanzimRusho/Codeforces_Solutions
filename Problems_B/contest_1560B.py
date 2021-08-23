t = int(input())

for i in range(t):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    
    d = -1
    
    dif = abs(a-b)
    
    limit = 2*dif
    
    
    if limit < max(a,b) or c > limit:
        print(d)
        continue
    
    elif c + dif <= limit:
        d = c+dif
        
    elif c-dif > 0:
        d = c-dif
        
    print(d)
