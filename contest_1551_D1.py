t = int(input())

for i in range(t):
    n, m, k = input().split()
    n = int(n)
    m = int(m)
    k = int(k)
    
    if n%2==0 and m%2 == 0:
        if k <= (n*m)//2:
            print("YES")
        else:
            print("NO")
    elif n%2 == 0 and m % 2 != 0:  
        if k <= (n*m-2)//2:
            print("YES")
        else:
            print("NO")

    else:
        print("NO")