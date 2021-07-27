text = input()

nums = []

for ch in text:
    if ch.isdigit() == True:
        nums.append(ch)
        
nums = sorted(nums)
string = ""

length = len(nums)

for i in range(length):
    if i == length-1:
        string += nums[i]
        break
    string += nums[i] + "+"
    
print(string)
