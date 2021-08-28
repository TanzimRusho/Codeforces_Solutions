n = int(input())

x = []
y = []
z = []

for i in range(n):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    x.append(a)
    y.append(b)
    z.append(c)

if sum(x) == sum(y) == sum(z) == 0:
    print("YES")
else:
    print("NO")
