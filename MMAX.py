# cook your dish here

def minDistribute():
    f = k//n
    a = [0]*n
    r = k % n

    if k % n == 0:
        print('0')
        return
    else:
        for i in range(r):
            if r == 0:
                break
            a[i] += 1
            r -= 1
        maxDistribute(a, k % n)
        return


def maxDistribute(a, r):
    b = [0]*n
    # c1 = a.count(a[0])  # 2
    # c2 = a.count(a[n-1])  # 1
    c1 = r
    c2 = n - r
    if c1 < c2:
        less = c1
        less_no = a[0]
        more_no = a[n-1]
    elif c1 > c2:
        less = c2
        less_no = a[n-1]
        more_no = a[0]
    else:
        less_no = more_no = a[0]
        less = c1
    if c1 == c2:
        for i in range(n):
            if i % 2 == 0:
                b[i] = a[0]
            else:
                b[i] = a[n-1]
    else:
        for i in range(n):
            if less > 0:
                if i % 2 == 0:
                    b[i] = more_no
                else:
                    b[i] = less_no
                    less -= 1
            else:
                b[i] = more_no
    s2 = 0
    for i in range(len(b)-1):
        s2 += abs(b[i]-b[i+1])
    print(s2)
    return


t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    minDistribute()
