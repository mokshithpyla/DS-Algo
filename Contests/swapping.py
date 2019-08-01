# cook your dish here
def S(list_of_numbers):
    s = 0
    for j in range(len(list_of_numbers)):
        s += list_of_numbers[j]*(j+1)
    return s

def swap(nums, i):
    temp = nums[i]
    nums[i] = nums[i+1]
    nums[i+1] = temp
    swap_sum = nums[i]*i + nums[i+1]*(i+1)
    return swap_sum
    # return nums

t = int(input())
for _ in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    max_sum = S(numbers)
    memo = 0
    for i in range(n-2):
        option1 = numbers[:]
        option2 = numbers[:]
        initial = swap(option1, i)
        final = swap(option2, i+1)
        if initial < final:
            max_sum = max(max_sum, S(option2))
            print('2', option1, option2)
        else:
            max_sum = max(max_sum, S(option1))
            print('1', option1, option2)
    print(max_sum)