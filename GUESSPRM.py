t = int(input())
for _ in range(t):
    x = 3
    while True:
        print('1', x)
        result = int(input())
        if result == 0:
            print('2', x*x)
            verdict = input()
            break
        if result == x*x:
            x += 1
    print(verdict)
    if verdict is 'No':
        break