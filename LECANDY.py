# https://www.codechef.com/problems/LECANDY

t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))

    for each in a:
        c -= each
    if c < 0:
        print('No')
    else:
        print('Yes')

# Inputs:
# 2
# 2 3
# 1 1
# 3 7
# 4 2 2