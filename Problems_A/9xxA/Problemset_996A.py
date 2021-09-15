n = int(input())

divisors = [100, 20, 10, 5, 1]

count = 0 

for divisor in divisors:
    while n // divisor != 0: 
        #print("divisor: {}".format(divisor))
        note_count = n // divisor
        #print("note count: {}".format(note_count))
        n %= divisor
        #print("n: {}".format(n))
        count += note_count
        #print("count: {}".format(count))
        #print()
        
print(count)
