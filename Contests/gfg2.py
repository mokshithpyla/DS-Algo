#code
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    max_diff1 = 0
    max_diff2 = 0
    b = [0] * n
    c = [0] * n
    for i in range(n):
        if i%2 == 0:
            b[i] = a[i]
            c[i] = 1
        else:
            c[i] = a[i]
            b[i] = 1
    max_diff = 0
    for i in range(1, n):
        # max_diff1 += abs(b[i] - b[i-1])
        # max_diff2 += abs(c[i] - c[i-1])
    # print(max(max_diff1, max_diff2))

    print(max_diff)