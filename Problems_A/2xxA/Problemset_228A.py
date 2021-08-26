from collections import deque

colors = list(input().split())

temp = deque()

count = 0

for color in colors:
    if color not in temp:
        temp.append(color)
        count += 1 
        
    else:
        continue
    
print(4-count)
