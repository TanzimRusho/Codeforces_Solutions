n = int(input())

array = [int(x) for x in input().split()]

hard = False

for i in range(n):
    if array[i] == 1:
        print("HARD")
        hard = True
        break
    
if hard == False:
    print("EASY")
