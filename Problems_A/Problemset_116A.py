n = int(input())

sum_a = sum_b = 0
capacity = []

for i in range(n):
    a, b = input().split()
    a, b = int(a), int(b)
    
    sum_a += a 
    sum_b += b
    
    capacity.append(sum_b-sum_a)
    
print(max(capacity))
