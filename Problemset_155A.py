n = int(input())

array = list(map(int, input().split()))

maxm = 0
minm = 10000

count = 0

for i in range(1, n):
    if array[i] > maxm:
        maxm = array[i]
        count += 1
    elif array[i] < minm:
        minm = array[i]
        count += 1

print(count)    