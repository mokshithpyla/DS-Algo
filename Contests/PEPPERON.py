t = int(input())
for _ in range(t):
    n = int(input())
    pizza = []
    left = 0
    right = 0
    reversals = {}
    for i in range(n):
        pizza.append(list(map(int, input().split())))
        reversals[i] =0
    for i in range(n):
        for j in range(n):
            if pizza[i][j] == 1:
                if pizza[i][n-j] == 0:
                    reversals[i] += 1
                else:
                    reversals[i] -= 1
                if j < n//2:
                    left += 1
                else:
                    right += 1
            else:
                if pizza[i][n-j] == 1:
                    reversals[i] += 1
                else:
                    reversals[i] -= 1
    difference = abs(left - right)



