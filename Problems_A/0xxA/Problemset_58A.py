s = input()
new_str = ""
hello = "hello"
length = len(hello)

for j in range(length):
    if hello[j] in s:
        i = s.index(hello[j])
        s = s[i+1:]
        new_str += hello[j]

if new_str == "hello":
    print("YES")
else:
    print("NO")
