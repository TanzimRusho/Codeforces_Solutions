num = input()

count = 0

for digit in num:
    if digit in ["4", "7"]:
        count += 1

if count == 4 or count == 7:
    print("YES")
else:
    print("NO")