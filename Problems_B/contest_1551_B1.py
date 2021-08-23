t = int(input())

for i in range(t):
    text = input()
    
    dict_ = {} 
    color = 0
    
    for ch in text:
        if ch not in dict_:
            dict_[ch] = 1
            #color += 0.5
        else:
            dict_[ch] += 1
    
    for ch in dict_:        
        if dict_[ch] == 1:
            color += 0.5
        elif dict_[ch] == 2:
            color += 1
        else:
            color += 1
        
    print(int(color))
