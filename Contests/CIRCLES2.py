t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist_between_centres = ((x1-x2)**2 + (y1-y1) ** 2) ** 0.5
    if dist_between_centres+r1 < r2:
        print('NO')
    else:
        print('YES')
        print(x1, y1)