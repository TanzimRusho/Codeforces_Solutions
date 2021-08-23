n = int(input())

start = "I hate"
end = " it"
string = ""

for i in range(2, n+1):
    if i%2 == 0:
        string += " that I love"
    else:
        string += " that I hate"
        
if n == 1:
    print(start+end)
else:
    print(start+string+end)
