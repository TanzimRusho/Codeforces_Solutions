n, t = input().split()
n, t = int(n), int(t)

Q = input()
length = len(Q)
Q = list(Q)

for j in range(t):
    flag = False
    for i in range(length-1):
        if flag:
            flag = False
            continue
        if Q[i] == "B" and Q[i+1] == "G":
            Q[i], Q[i+1] = Q[i+1], Q[i]
            flag = True
        else:
            flag = False
            
print("".join(Q))
