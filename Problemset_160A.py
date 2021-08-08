n = int(input())

coins = [int(x) for x in input().split()]

coins = sorted(coins)

sum_me = 0

sum_coins = sum(coins) / 2

length = len(coins)

count = 0

for i in range(length):
    sum_me += coins[i]
    count += 1
    if sum_me <= sum_coins:
        continue
    else:
        break
            
print(count)
