# # Recursive: TLE
# import sys
# sys.setrecursionlimit(1500)
# def go(index, taken):
#   if taken == 0:
#     return 0
#   if taken < 0:
#     return float("-inf")
#   if index > n:
#     return 0
#   if (index, taken) in cache:
#     return cache[(index, taken)]
#   s = 0
#   cache[(index, taken)] = 0
#   for i in range(k+1):
#     s += stackOfPlates[index][i]
#     cache[(index, taken)] = max(cache[(index, taken)], s + go(index + 1, taken - i))
#   return cache[(index, taken)]
  
# t = int(input())
# for _ in range(t):
#   [n, k, p] = list(map(int, input().split()))
#   cache = {}
#   stackOfPlates = [[0]*(k+1)]
#   for x in range(n):
#     stack = list(map(int, input().split()))
#     stackOfPlates.append([0]+stack)
#   # transformed = []
#   # for x in range(n+1):
#   #   transformed.append([0]*(k+1))
#   # for i in range(1, n+1):
#   #   for j in range(1, k+1):
#   #     transformed[i][j] = stackOfPlates[i-1][j-1]
  
#   ans = go(1, p)
#   print("Case #{}: {}".format(_+1, ans))

# Iterative: 
def findMaxBeauty(n, k, p):
    beauty = [[0]*(p + 1) for x in range(n+1)]
    for x in range(n):
        beauty[x+1] = beauty[x][:]
        s = 0
        stack = list(map(int, input().split()))
        for y in range(k):
            s += stack[y]
            for z in range(p - y):
                beauty[x + 1][z + y + 1] = max(beauty[x + 1][z + y + 1], s + beauty[x][z])
    return beauty[n][p]
t = int(input())
for _ in range(t):
    n, k, p = map(int, input().split())
    ans = findMaxBeauty(n, k, p)
    print("Case #{}: {}".format(_+1, ans))