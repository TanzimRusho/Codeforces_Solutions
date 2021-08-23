t = int(input())

for i in range(t):
    n = int(input())
    sm = n//3
    bg = sm + 1
    
    if n % 3 == 0:
        print(sm, sm)
    
    elif n%3 != 0 and 2*bg + sm == n :
        print(sm, bg)
    elif n%3 != 0 and 2*sm + bg == n:
        print(bg, sm)
