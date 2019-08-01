# July Challenge
# https://www.codechef.com/JULY19B/problems/CHFM

def findCoin(numbers, mean):
    if mean in numbers:
        return numbers.index(mean)+1
    else:
        return 'Impossible'


t = int(input())
for _ in range(t):
    n = int(input())
    numbers = list(map(int,input().split()))
    mean = sum(numbers)/n
    ans = findCoin(numbers, mean)
    print(ans)

