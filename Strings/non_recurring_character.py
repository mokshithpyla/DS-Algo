t = int(input())
for _ in range(t):
    n = int(input())
    S = list(input())
    flag = False
    originals = {}
    for i in range(n):
        if S[i] not in originals:
            originals[S[i]] = [1, i]
        else:
            originals[S[i]][0] += 1
            originals[S[i]][1] = i
    for i in range(n):
        if originals[S[i]][0] == 1:
            print(S[i])
            flag = True
            break
    if not flag:
        print(-1)
# 3
# 5
# hello
# 12
# zxvczbtxyzvy
# 6
# xxyyzz