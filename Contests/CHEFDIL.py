# cook your dish here
t = int(input())
for _ in range(t):
    S = input()
    xor_sum = 0
    n = len(S)
    for i in range(n):
        xor_sum = xor_sum ^ int(S[i])
    if xor_sum == 1:
        print("WIN")
    else:
        print("LOSE")