t = int(input())
for _ in range(t):
    nl, L = map(int, input().split())
    nr, R = map(int, input().split())
    fx = 0
    for x in range(L, R+1):
        number_in_place = list(map(int, str(x)))
        prev_num = next_num = 0
        n = len(number_in_place)
        for i in range(n):
            if i is 0:
                prev_num = -1
            else:
                prev_num = number_in_place[i-1]
            if i is n-1:
                next_num = -1
            else:
                next_num = number_in_place[i+1]
            if number_in_place[i] is not prev_num and number_in_place[i] is next_num:
                fx += number_in_place[i] * pow(10, n-i-1)
                continue
            if number_in_place[i] is prev_num and number_in_place[i] is not next_num:
                continue
            if number_in_place[i] is prev_num and number_in_place[i] is next_num:
                continue
            fx += number_in_place[i] * pow(10, n-i-1)
    print(fx)

