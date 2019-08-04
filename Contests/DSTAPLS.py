t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k == 1:
        print('NO')
        continue
    # candidate 1:
    apples_per_box = n//k
    # candidate 2:
    if apples_per_box % k == 0:
        print('NO')
    else:
        print('YES')

# 3
# 5 1
# 4 2
# 10 10