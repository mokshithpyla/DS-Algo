t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    S = input()
    L = [0]*q
    R = [0]*q
    characters = set()
    for i in range(q):
        L[i], R[i] = map(int, input().split())
    char_count = [[0] * 26 for i in range(n+1)]
    # char_count[0][abs(ord(S[0])-ord('A'))] = 1
    # characters.add(abs(ord(S[0])-ord('A')))
    for i in range(n):
        for j in range(26):
            char_count[i+1][j] = char_count[i][j]
        char_count[i+1][ord(S[i])-ord('A')] += 1
        characters.add(ord(S[i])-ord('A'))
    print(char_count)
    # print(characters)
    ans = 0
    memo = {}
    for i in range(q):
        frequency = 0
        print(L[i], R[i])
        if (L[i], R[i]) in memo:
            frequency = memo[(L[i], R[i])]
            # print('memoized')
        else:
            for j in characters:
                frequency += (char_count[R[i]][j] - char_count[L[i]-1][j]) & 1
            memo[(L[i], R[i])] = frequency
        print(frequency)
        if frequency <= 1:
            ans += 1
    print("Case #{}: {}".format(_+1, ans))









# 2
# 7 5
# ABAACCA
# 3 6
# 4 4
# 2 5
# 6 7
# 3 7
# 3 5
# XYZ
# 1 3
# 1 3
# 1 3
# 1 3
# 1 3