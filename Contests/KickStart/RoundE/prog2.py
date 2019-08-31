t = int(input())
for _ in range(t):
    d, s = map(int, input().split())
    c = [0] * s
    e = [0] * s
    for i in range(s):
        c[i], e[i] = map(int, input().split())
    a = [0] * d
    b = [0] * d
    for i in range(d):
        a[i], b[i] = map(int, input().split())
    for i in range(d):
        for j in range(s):
            targetc = a[i]
            targete = b[i]

    ans = 0
    print("Case #{}: {}".format(_+1, ans))



