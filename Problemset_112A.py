text1 = input()
text2 = input()

text1 = text1.lower()
text2 = text2.lower()

equal = True

for i, j in zip(text1, text2):
    if ord(i) == ord(j):
        continue
    
    elif ord(i) > ord(j):
        print(1)
        equal = False
        break
    
    else:
        print(-1)
        equal = False
        break
    
if equal:
    print(0)
