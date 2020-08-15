def solution(total_lambs):
    totals = [generous(total_lambs), stingy(total_lambs)]
    difference = max(totals) - min(totals)
    return difference

def generous(total_lambs):
    num = 1
    while True:
        total = 2**(num) - 1
        if total <= total_lambs:
            num += 1
        else:
            num -= 1
            break
    return num

def stingy(total_lambs):
    num = 1
    while True:
        total = (fibonacci(num + 2) - 1)
        if total <= total_lambs:
            num += 1
        else:
            num -= 1
            break
    return num

def fibonacci(num):
    a, b = 1, 1

    for _ in range(1, num):
        a, b = b, a + b

    return a

