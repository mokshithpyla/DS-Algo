#
#
# def findMaxes(a, first_max, second_max):
#     for i in range(2,len(a)):
#         if a[i] > first_max:
#             second_max = first_max
#             first_max = a[i]
#         else:
#             if a[i] > second_max:
#                 second_max = a[i]
#     return first_max, second_max
# t = int(input())
# for _ in range(t):
#     n,z = map(int,input().split())
#     a = list(map(int,input().split()))
#     first_max = max(a[0], a[1])
#     second_max = min(a[0], a[1])
#     first_max, second_max = findMaxes(a, first_max, second_max)
#     hits = 0
#     for i in range(z):
#         print(a)
#         if first_max > second_max*2:
#             hits += second_max*2
#             first_max -= second_max
#             print(first_max, second_max)
#             a.remove(second_max)
#         else:
#             hits += first_max
#         first_max, second_max = findMaxes(a, first_max, second_max)
#     print(hits)
t = int(input())
for _ in range(t):
    n,z = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    hits = 0
    for i in range(z):

        if a[0] > a[1]*2:
            hits += a[1]*2
            a[0] -= a[1]
            a.remove(a[1])
        else:
            hits += a[0]
        a.sort(reverse=True)
    print(hits)
