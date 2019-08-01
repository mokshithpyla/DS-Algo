# https://www.codechef.com/submit/RAINBOWA

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    mid = len(arr) // 2
    values=[1,2,3,4,5,6,7]
    if len(arr) % 2 == 0:
        a = arr[:mid]
        b = arr[mid:]
    else:
        a = arr[:mid]
        b = arr[mid + 1:]
    # print(b)
    b=b[::-1]
    # print(a)
    # print(b)
    flag=0
    for each in arr:
        if each not in values:
            flag=1
            break
    for each in values:
        if each not in arr:
            flag=1
            break
    if a == b and flag==0:
        print('yes')
    else:
        print('no')

# 3
# 19
# 1 2 3 4 4 5 6 6 6 7 6 6 6 5 4 4 3 2 1
# 14
# 1 2 3 4 5 6 7 6 5 4 3 2 1 1
# 13
# 1 2 3 4 5 6 8 6 5 4 3 2 1