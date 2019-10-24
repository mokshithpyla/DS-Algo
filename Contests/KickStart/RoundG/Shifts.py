import sys
sys.setrecursionlimit(1500)
def findDifferentPaths(level, ah, bh):
    if level == n:
        if ah >= h and bh >= h:
            return 1
        else:
            return 0
    else:
        ways = findDifferentPaths(level+1, ah + a[level], bh) + findDifferentPaths(level+1, ah, bh + b[level]) + findDifferentPaths(level+1, ah + a[level], bh + b[level])
        return ways
t = int(input())
for _ in range(t):
    n, h = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = findDifferentPaths(0, 0, 0)
    print("Case #{}: {}".format(_+1, ans))