n, k = input().split()

for i in range(int(k)):
    if n[:-1] == 0:
        n = int(n) / 10 
    else:
        n = int(n) - 1

print(n)    
