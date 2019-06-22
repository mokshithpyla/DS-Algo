# https://www.codechef.com/problems/CNOTE
t = int(input())
for _ in range(t):
    x, y, k, n = map(int, input().split())
    p = []
    c = []
    for i in range(n):
        pici = list(map(int, input().split()))
        p.append(pici[0])
        c.append(pici[1])
    pages_left = x - y
    for i in range(n):
        if k >= c[i] and pages_left <= p[i]:
            pages_left -= p[i]
            break

    if pages_left <= 0:
        print('LuckyChef')
    else:
        print('UnluckyChef')

# Inputs:
# 3
# 3 1 2 2
# 3 4
# 2 2
# 3 1 2 2
# 2 3
# 2 3
# 3 1 2 2
# 1 1
# 1 2