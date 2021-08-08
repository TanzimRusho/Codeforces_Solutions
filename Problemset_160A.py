n = int(input())

coins = [int(x) for x in input().split()]

coins = sorted(coins, reverse=True)

sum_coins_half = sum(coins) / 2

sum_my_coins = 0

count = 0

for i in range(n):
    sum_my_coins += coins[i]
    count += 1
    if sum_my_coins > sum_coins_half:
        break
    else:
        continue
    
print(count)
