n = int(input())

array = [int(x) for x in input().split()]

res = [0] * n 

for i in range(n):
    res[array[i]-1] = i+1

for i in range(n):
    print(res[i], end=" ")
