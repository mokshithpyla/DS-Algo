t = int(input())
for _ in range(t):
    n = int(input())
    x = [0] * n
    y = [0] * n
    points = list(map(int, input().split()))
    k = 0
    for i in range(0, len(points), 2):
        x[k] = points[i]
        y[k] = points[i+1]
        k += 1
    steps = 0
    k = 0
    for i in range(0, len(x)-1):
        steps += max(abs(x[i+1] - x[i]), abs(y[i+1] - y[i]))
    print(steps)
