# cook your dish here
alphabet = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0,
}

n = int(input())
text = input()

for i in range(n):
    if text[i] in ['a', 'A']:
        alphabet['a'] += 1
    elif text[i] in ['b', 'B']:
        alphabet['b'] += 1
    elif text[i] in ['c', 'C']:
        alphabet['c'] += 1
    elif text[i] in ['d', 'D']:
        alphabet['d'] += 1
    elif text[i] in ['e', 'E']:
        alphabet['e'] += 1
    elif text[i] in ['f', 'F']:
        alphabet['f'] += 1
    elif text[i] in ['g', 'G']:
        alphabet['g'] += 1
    elif text[i] in ['h', 'H']:
        alphabet['h'] += 1
    elif text[i] in ['i', 'I']:
        alphabet['i'] += 1
    elif text[i] in ['j', 'J']:
        alphabet['j'] += 1
    elif text[i] in ['k', 'K']:
        alphabet['k'] += 1
    elif text[i] in ['l', 'L']:
        alphabet['l'] += 1
    elif text[i] in ['m', 'M']:
        alphabet['m'] += 1
    elif text[i] in ['n', 'N']:
        alphabet['n'] += 1
    elif text[i] in ['o', 'O']:
        alphabet['o'] += 1
    elif text[i] in ['p', 'P']:
        alphabet['p'] += 1
    elif text[i] in ['q', 'Q']:
        alphabet['q'] += 1
    elif text[i] in ['r', 'R']:
        alphabet['r'] += 1
    elif text[i] in ['s', 'S']:
        alphabet['s'] += 1
    elif text[i] in ['t', 'T']:
        alphabet['t'] += 1
    elif text[i] in ['u', 'U']:
        alphabet['u'] += 1
    elif text[i] in ['v', 'V']:
        alphabet['v'] += 1
    elif text[i] in ['w', 'W']:
        alphabet['w'] += 1
    elif text[i] in ['x', 'X']:
        alphabet['x'] += 1
    elif text[i] in ['y', 'Y']:
        alphabet['y'] += 1
    elif text[i] in ['z', 'Z']:
        alphabet['z'] += 1
    
letter_is_present = True 
    
for key in alphabet:
    if alphabet[key] == 0:
        print("NO")
        letter_is_present = False
        break 

if letter_is_present:
    print("YES")
      
