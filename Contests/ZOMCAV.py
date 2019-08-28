t = int(input())
for _ in range(t):
    n = int(input())
    C = list(map(int, input().split()))
    H = list(map(int, input().split()))
    total_zeroes = 0
    for i in range(n):
        left_zeroes = 0
        right_zeroes = 0
        if C[i] <= i:
            left_zeroes = i - C[i]
        if C[i] <= n - i - 1:
            right_zeroes = (n - i - 1) - C[i]
        total_zeroes += left_zeroes + right_zeroes
    max_sum = n*n
    c1 = max_sum - total_zeroes
    c2 = sum(H)
    if c1 == c2:
        print('YES')
    else:
        print('NO')
