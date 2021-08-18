from collections import deque

t = int(input())

A = deque()

for i in range(1, 1667):
    if i % 3 != 0 and i % 10 != 3:
        A.append(i)
        
for i in range(t):
    n = int(input())

    print(A[n-1])
