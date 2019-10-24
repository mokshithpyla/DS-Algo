t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    integers = list(map(int, input().split()))

    ans = -1
    limit = sum(integers)
    if m == 0:
        xor_sum = 0
        for each in integers:
            xor_sum += each ^ k
        if xor_sum <= m:
            ans = max(ans, k)
    else:
        for k in range(1, m+1):
            xor_sum = 0
            for each in integers:
                xor_sum += each ^ k
            if xor_sum <= m:
                ans = max(ans, k)
    print("Case #{}: {}".format(_+1, ans))

# 4
# 3 27
# 8 2 4
# 4 45
# 30 0 4 11
# 1 0
# 100
# 6 2
# 5 5 1 5 1 0

