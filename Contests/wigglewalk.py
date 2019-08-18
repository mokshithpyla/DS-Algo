t = int(input())
k = 0
for _ in range(t):
    n, r, c, sr, sc = map(int, input().split())
    directions = list(input())
    visited = []
    rows = {}
    columns = {}
    sr -= 1
    sc -= 1
    for i in range(r):
        rows[i] = set()
    for j in range(c):
        columns[j] = set()
    for i in range(n):
        rows[sr].add(sc)
        columns[sc].add(sr)
        dir = directions[i]
        if dir == 'N':
            sr -= 1
            while sr in columns[sc]:
                sr -= 1
        elif dir == 'S':
            sr += 1
            while sr in columns[sc]:
                sr += 1
        elif dir == 'E':
            sc += 1
            while sc in rows[sr]:
                sc += 1
        else:
            sc -= 1
            while sc in rows[sr]:
                sc -= 1
    k += 1
    print('Case #', k, ':', sep='', end='')
    print('', sr+1, sc+1)
# 3
# 5 3 6 2 3
# EEWNS
# 4 3 3 1 1
# SESE
# 11 5 8 3 4
# NEESSWWNESE