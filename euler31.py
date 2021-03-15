# Credits to: https://blog.dreamshire.com/project-euler-31-solution/

coins = [200, 100, 50, 20, 10, 5, 2, 1]
target = 200
ways = [1] + [0]*target

for coin in coins:
  for i in range(coin, target+1):
    ways[i] += ways[i - coin]

 ways[target]
