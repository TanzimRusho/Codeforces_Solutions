t = int(input())

for i in range(t):
    a, b = input().split()
    a, b = int(a), int(b)
    
    if a % b == 0:
        print(0)
    else:
        print(b - a%b)
