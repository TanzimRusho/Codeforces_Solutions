from collections import deque

n, m =  map(int, input().split())

array = [int(x) for x in input().split()]

sorted_array = sorted(array)

#print(sorted_array)

length = len(array)

min_list = deque()

for i in range(length):
    try:
        min_ = sorted_array[i+n-1] - sorted_array[i] 
        #print(sorted_array[i], sorted_array[i+n-1])

        min_list.append(min_)
        
    except IndexError:
        break 
    
print(min(min_list))
