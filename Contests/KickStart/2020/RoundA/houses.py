t = int(input())
for _ in range(t):
  n, budget = map(int, input().split())
  prices = list(map(int, input().split()))
  prices.sort()
  ans = 0
  for price in prices:
    if price <= budget:
      ans += 1
      budget -= price
  print("Case #{}: {}".format(_+1, ans))