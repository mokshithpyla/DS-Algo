t = int(input())
for _ in range(t):
    S = input()
    original = set()
    for each in S:
        if each not in original:
            original.add(each)
            print(each, end='')
    print()