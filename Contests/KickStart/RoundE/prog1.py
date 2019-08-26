def find(x):
    if f[x] == x:
        return x
    else:
        f[x] = find(f[x])
        return f[x]


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ans = (n-1) << 1
    f = []
    for i in range(0, n+1):
        f.append(i)
    c = [0]*m
    d = [0]*m
    for i in range(m):
        c[i], d[i] = map(int, input().split())
    for i in range(m):
        u = find(c[i])
        v = find(d[i])
        print(u, v)
        print(f)
        if u == v:
            continue
        f[u] = v
        ans -= 1
    print("Case #{}: {}".format(_+1, ans))

