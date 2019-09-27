t = int(input())
for _ in range(t):
    a1, a2, a3, c1, c2, c3 = map(int, input().split())
    ages = [a1, a2, a3]
    gifts = [c1, c2, c3]
    flag = True
    for i in range(0, 2):
        for j in range(i+1, 3):
            if ages[i] > ages[j]:
                if gifts[i] <= gifts[j]:
                    flag = False
                    break
            elif ages[i] < ages[j]:
                if gifts[i] >= gifts[j]:
                    flag = False
                    break
            else:
                if gifts[j] != gifts[i]:
                    flag = False
                    break
        if not flag:
            break
    if flag:
        print('FAIR')
    else:
        print('NOT FAIR')
    # for i in range(3):
    #     if ages[i] not in memo:
    #         memo[ages[i]] = gifts[i]
    #     else:
    #         if memo[ages[i]] != gifts[i]:
    #             flag = False
    # # print(memo)
    # if not flag:
    #     print('NOT FAIR')
    # else:
    #     ages.sort(reverse=True)
    #     for i in range(len(ages)-1):
    #         if memo[ages[i]] < memo[ages[i+1]]:
    #             flag = False
    #             break
    #     if flag:
    #         print('FAIR')
    #     else:
    #         print('NOT FAIR')



# 5
# 5 7 10 10 20 50
# 5 5 5 20 10 20
# 10 1 17 5 10 15
# 3 6 3 8 10 9
# 8 5 5 50 10 10