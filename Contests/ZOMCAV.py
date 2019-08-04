# t = int(input())
# for _ in range(t):
#     n = int(input())
#     C = list(map(int, input().split()))
#     H = list(map(int, input().split()))
#     # radiation_levels = [0] * n
#     memo = []
#     for i in range(n):
#         underflow = overflow = 0
#         ones = 2 * C[i] + 1
#         left_zeroes = 0
#         right_zeroes = 0
#         if C[i] > i:
#             underflow = C[i] - i
#         else:
#             left_zeroes = i - C[i]
#         if C[i] > n - i - 1:
#             overflow = C[i] - (n - i - 1)
#         else:
#             right_zeroes = (n - i - 1) - C[i]
#         ones = ones - (underflow + overflow)
#         # temp = [0] * left_zeroes + [1] * ones + [0] * right_zeroes
#         temp = [left_zeroes, ones, right_zeroes]
#         memo.append(temp)
#         # for j in range(n):
#         #     radiation_levels[j] += temp[j]
#     x = [0] * n
#     for each in memo:
#         temp = [0] * each[0] + [1] * each[1] + [0] * each[2]
#
#     radiation_levels = [sum(i) for i in zip(*memo)]
#     # print(radiation_levels)
#     radiation_levels.sort()
#     H.sort()
#     if H == radiation_levels:
#         print('YES')
#     else:
#         print('NO')

# 2
# 5
# 1 2 3 4 5
# 1 2 3 4 5
# 5
# 5 4 3 2 1
# 1 2 3 4 5
from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    C = list(map(int, input().split()))
    H = list(map(int, input().split()))
    # radiation_levels = [0] * n
    memo = []
    radiation_power = defaultdict
    for i in range(n):
        underflow = overflow = 0
        ones = 2 * C[i] + 1
        left_zeroes = 0
        right_zeroes = 0
        if C[i] > i:
            underflow = C[i] - i
        else:
            left_zeroes = i - C[i]
        if C[i] > n - i - 1:
            overflow = C[i] - (n - i - 1)
        else:
            right_zeroes = (n - i - 1) - C[i]
        ones = ones - (underflow + overflow)
        radiation_power[i] += 1
        # for j in range(n):
        #     radiation_levels[j] += temp[j]
    x = [0] * n
    for each in memo:
        temp = [0] * each[0] + [1] * each[1] + [0] * each[2]

    radiation_levels = [sum(i) for i in zip(*memo)]
    # print(radiation_levels)
    radiation_levels.sort()
    H.sort()
    if H == radiation_levels:
        print('YES')
    else:
        print('NO')