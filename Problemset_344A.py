n = int(input())

array = []

magnet = input()

array.append(magnet)

count = 1 

for i in range(1, n):
    magnet = input()
    
    array.append(magnet)

    if array[i] == '10' and array[i-1] == '01':
        count += 1 
        
    elif array[i] == '01' and array[i-1] == '10':
        count += 1 
    
    elif array[i] == '10' and array[i-1] == '10':
        continue
    
    else:
        continue
    
print(count)    
