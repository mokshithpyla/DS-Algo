t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    S = list(input())
    letters = set(S)
    subs = []
    for i in range(q):
        subs.append(list(map(int, input().split())))
    counter = {}
    letters = []
    # for each in S:
    #     if each not in S:
    #         letters.append(each)
    # for i in range(len(S)):
    #     if
    for i in range(len(S)):
        if S[i] not in counter:
            counter[S[i]] = [1, i]
        else:
            counter[S[i]][0] += 1
            counter[S[i]][1] = i

    for each in subs:
        start = each[0]-1
        end = each[1]
        length = end - start + 1
        rich_length = length//2


