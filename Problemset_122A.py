input_num = int(input())

lucky_numbers = []

for num in range(1, 1001):
    flag = True
    num = str(num)
    
    for ch in num:
        if ch in ["4", "7"]:
            continue
        else:
            flag = False
            
    if flag:
        lucky_numbers.append(int(num))
    
    
new_flag = True        
        
for num in lucky_numbers:
    if input_num % num == 0:
        print("YES")
        new_flag = False
        break
    
if new_flag:    
    print("NO")
