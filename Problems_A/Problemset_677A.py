n, h = input().split()
n, h = int(n), int(h)

min_width = 0

heights = [int(h) for h in input().split()]

for height in heights:
    if height > h:
        min_width += 2
    else:
        min_width += 1

print(min_width)    
    
