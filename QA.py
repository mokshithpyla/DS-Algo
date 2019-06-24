
t=int(input())
for _ in range(t):
    n=int(input())
    correct_answers=list(input())
    my_answers=list(input())
    score=0
    for i in range(n):
        if i==n-1:
            if my_answers[i]==correct_answers[i]:
                score+=1
            else:
                break
        elif my_answers[i]==correct_answers[i]:
            score+=1
        elif my_answers[i]!='N' and my_answers[i]!=correct_answers[i]:
            my_answers[i+1]='N'
    print(score)

# 3
# 6
# ABCDAB
# ABCDAB
# 8
# DDCABCCA
# DNCBBBBA
# 3
# CDD
# NDC