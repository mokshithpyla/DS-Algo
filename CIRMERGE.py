
t = int(input())
for _ in range(t):
    n = int(input())
    elements = list(map(int, input().split()))
    circle = ModifiableCycle(elements)
    s = 0
    penalty=0
    for i in range(n-1):
        a,b = select_numbers(circle)
        print(a, b)
        penalty += calculate_penalty(a, b)
        circle = erase_numbers(a, b, circle)
        if circle.__sizeof__() == 1:
            break
    print('penalty', penalty)

