# codeforces - 71A
n = int(input())
for i in range(n):
    word = input()
    if len(word) < 11:
        print(word)
    else:
        print(word[0] + str(len(word)-2) + word[len(word)-1])
