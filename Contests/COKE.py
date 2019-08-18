t = int(input())
for _ in range(t):
    n, m, k, l, r = map(int, input().split())
    temperature = [0]*n
    price = [0]*n
    for i in range(n):
        temperature[i], price[i] = map(int, input().split())
    cheap_prices = []
    for i in range(n):
        if temperature[i] > k+1:
            temperature[i] -= m
            if temperature[i] < k:
                temperature[i] = k
        elif temperature[i] < k-1:
            temperature[i] += m
            if temperature[i] > k:
                temperature[i] = k
        else:
            temperature[i] = k
        if temperature[i] >= l and temperature[i] <= r:
            cheap_prices.append(price[i])
    if cheap_prices:
        print(min(cheap_prices))
    else:
        print(-1)

