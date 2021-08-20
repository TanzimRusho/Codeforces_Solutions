k,l,m,n,d = input(),input(),input(),input(),input() 
k,l,m,n,d = int(k),int(l),int(m),int(n),int(d)

count = 0

for i in range(1, d+1):
    if (i%k == 0) or (i%l == 0) or (i%m == 0) or (i%n == 0): 
        count += 1 
        
print(count)