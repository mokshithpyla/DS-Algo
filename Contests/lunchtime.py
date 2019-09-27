t = int(input())
for _ in range(t):
    n, q, k, l, r = map(int, input().split())
    temperature = [0]*n
    price = [0]*n
    for i in range(n):
        temperature[i], price[i] = map(int, input().split())
    temps = temperature[:]
    for m in range(1, q+1):
        cheap_prices = []
        # print('m=',m)
        for i in range(n):
            if temperature[i] > k+1:
                # temperature[i] -= m
                temps[i] = temperature[i]-m
                if temperature[i] < k:
                    # temperature[i] = k
                    temps[i] = k
            elif temperature[i] < k-1:
                # temperature[i] += m
                temps[i] = temperature[i] + m
                if temperature[i] > k:
                    # temperature[i] = k
                    temps[i] = k
            else:
                # temperature[i] = k
                temps[i] = k
            # if temperature[i] >= l and temperature[i] <= r:
            if temps[i] >= l and temps[i] <= r:
                # print(temperature[i], price[i])
                cheap_prices.append(price[i])
        # print(cheap_prices)
        if len(cheap_prices) != 0:
            print(min(cheap_prices), end=' ')
        else:
            print(-1, end=' ')
    print()

# t = int(input())
# for _ in range(t):
#     n, q, k, l, r = map(int, input().split())
#     temperature = [0]*n
#     price = [0]*n
#     for i in range(n):
#         temperature[i], price[i] = map(int, input().split())
#     cheap_prices = []
#     for i in range(n):
#         for m in range(1, q+1):
#             if temperature[i] > k+1:
#                 temperature[i] -= m
#                 if temperature[i] < k:
#                     temperature[i] = k
#             elif temperature[i] < k-1:
#                 temperature[i] += m
#                 if temperature[i] > k:
#                     temperature[i] = k
#             else:
#                 temperature[i] = k
#             if temperature[i] >= l and temperature[i] <= r:
#                 cheap_prices.append(price[i])
#     if cheap_prices:
#         print(min(cheap_prices))
#     else:
#         print(-1)