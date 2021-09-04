from collections import deque

text = input()

seen = deque()

count = 0

ignore_chars = [',', ' ', '{', '}']

for ch in text:
    if ch in ignore_chars:
        continue
    
    if ch not in seen:
        seen.append(ch)
        count += 1
        
    else:
        continue 
    
print(count)
        
