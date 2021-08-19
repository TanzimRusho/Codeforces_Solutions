import math

n = int(input())

groups = [int(x) for x in input().split()]

count_mems = {1:0, 2:0, 3:0, 4:0}

for group in groups:
    count_mems[group] += 1 

count = count_mems[4]
del count_mems[4]  
          
while count_mems[1] != 0 and count_mems[3] != 0:
    count_mems[1] -= 1 
    count_mems[3] -= 1 
    count += 1 

num_pair_2 = count_mems[2] // 2

if count_mems[2] % 2 == 0:
    count += num_pair_2
    count_mems[2] = 0 
    
else:
    count += num_pair_2
    count_mems[2] -= num_pair_2 * 2

if count_mems[2] == 1 and count_mems[1] >= 2:
    count_mems[2] -= 1 
    count_mems[1] -= 2 
    count += 1 
    
elif count_mems[2] == 1 and count_mems[1] == 1:
    count_mems[2] -= 1 
    count_mems[1] -= 1 
    count += 1 

for key in count_mems:
    if key == 1 and count_mems[key] != 0:
        count += int(math.ceil(count_mems[1] / 4))  
    
    if key == 2 and count_mems[key] != 0:
        count += count_mems[key]
    
    if key == 3 and count_mems[key] != 0:
        count += count_mems[key]
    
print(count)
