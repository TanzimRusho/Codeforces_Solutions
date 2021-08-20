n = int(input())

count = 1
max_ = 0

array = list(map(int, input().split()))

for i in range(1, n):
    if array[i]  >= array[i-1]:
        count += 1 
        if count > max_:
            max_ = count 
    else:
        count = 1 
        
print(max_)
