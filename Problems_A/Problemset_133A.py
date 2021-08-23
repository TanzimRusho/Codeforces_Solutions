instructions = ['H', "Q", '9']

text = input()

flag = True

for i in text:
    if i in instructions:
        print("YES")
        flag = False
        break
    else:
        continue
        
if flag:
    print("NO")
