s = input()

count_upper = 0
count_lower = 0

for ch in s:
    if ch.islower():
        count_lower += 1 
    elif ch.isupper():
        count_upper += 1 
        
if count_upper > count_lower:
    print(s.upper())
elif count_lower > count_upper:
    print(s.lower())
else:
    print(s.lower())
