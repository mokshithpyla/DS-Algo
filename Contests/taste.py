# codechef june cookoff
try:
    t=int(input())
    for _ in range(t):
        n,d=map(int,input().split())
        taste=[0]*d
        for i in range(n):
            d,t=map(int,input().split())
            if taste[d-1]<t:
                taste[d-1]=t
        taste.sort()
        tastiness=taste[-1]+taste[-2]
        print(tastiness)
except Exception:
    print(end='')
# t=int(raw_input())
# for _ in range(t):
#     n,d=map(int,raw_input().split())
#     taste=[0]*d
#     for i in range(n):
#         d,t=map(int,raw_input().split())
#         if taste[d]<t:
#             taste[d]=t
#     taste.sort()
#     tastiness=taste[-1]+taste[-2]
#     print(tastiness)
#     3 7
# 5 12
# 2 5
# 5 10

# 2
# 3 6
# 5 7
# 1 9
# 2 5
# 3 7
# 5 8
# 2 5
# 5 10