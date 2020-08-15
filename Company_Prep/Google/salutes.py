def solution(s):
# Your code here
    cross = 0
    salute = 0
    for i in range(len(s)):
        if s[i] is '<':
            cross += 1
    for x in range(len(s)):
        if s[x] is '>':
            salute += cross
        elif s[x] is '<':
            cross -= 1
    salutes = salute * 2
    return salutes

