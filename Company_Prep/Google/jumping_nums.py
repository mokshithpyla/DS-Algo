from collections import deque
def bfs(x, num):
    q = deque()
    q.appendleft(num)
    while len(q) != 0:
        num = q.popleft()
        if num <= x:
            ans.append(num)
            ld = num % 10
            if ld == 0:
                q.appendleft(num*10 + ld + 1)
            elif ld == 9:
                q.appendleft(num*10 + ld - 1)
            else:
                q.appendleft(num*10 + ld - 1)
                q.appendleft(num*10 + ld + 1)


t = int(input())
for _ in range(t):
    x = int(input())
    print('0', end=' ')
    ans = []
    for i in range(1, 10):
        bfs(x, i)
    ans.sort()
    for each in ans:
        print(each, end=' ')