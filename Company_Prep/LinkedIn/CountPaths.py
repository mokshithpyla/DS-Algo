# slowww
# def countWays(x, y):
#     if x == m - 1 and y == n - 1:
#         return 1
#     if x > m - 1 or y > n - 1:
#         return 0
#     if y == n - 1:
#         countWays(x + 1, y)
#     if x == m - 1:
#         countWays(x, y + 1)
#     if (x, y) in visited:
#         return visited[(x, y)]
#     else:
#         ways = countWays(x + 1, y) + countWays(x, y + 1)
#         return ways
t = int(input())
for _ in range(t):
    visited = {}
    m, n = map(int, input().split())
    # number_of_ways = countWays(0, 0)
    # print(number_of_ways)
    number_of_paths = [[1]*n]*m
    for i in range(1, m):
        for j in range(1, n):
            number_of_paths[i][j] = number_of_paths[i-1][j] + number_of_paths[i][j-1]
    print((number_of_paths[-1][-1]) % (10**9+7))