vowels = ["a", "e", "i", "o", "u", "y"]

text = input()
text = text.lower()

for letter in text:
    if letter in vowels:
        text = text.replace(letter, "")

new_string = ""        
for i in range(len(text)):
    new_string += "." + text[i]


print(new_string)
