n = int(input())

count = 0

for i in range(n):
    p, q = input().split()
    p, q = int(p), int(q)
    
    if q-p >= 2:
        count += 1
        
print(count)
