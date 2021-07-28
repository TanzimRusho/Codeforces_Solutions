n = int(input())

text = input()

count = 0

for i in range(1, len(text)):
    if text[i] == text[i-1]:
        count += 1
    
print(count)
