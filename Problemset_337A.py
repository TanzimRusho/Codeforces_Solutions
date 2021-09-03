from collections import deque

n, m =  map(int, input().split())

array = [int(x) for x in input().split()]

sorted_array = sorted(array)

length = len(array)

min_list = deque()

for i in range(0, length, n):
    try:
        min_ = sorted_array[i+n-1] - sorted_array[i] 
        min_list.append(min_)
        
    except IndexError:
        break 
    
print(min(min_list))
