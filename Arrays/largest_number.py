def largestNumber(A):
    max_digit = int(str(A[0])[0])
    largest = [max_digit]
    ans = ''
    for i in range(1, len(A)):
        number = str(A[i])
        if int(number[0]) > int(max_digit):
            largest.append(number)
        elif int(number[0]) == int(max_digit):
            len(number)
            if int(number[-1]) > max_digit:
                largest.append(number)
            else:
                temp = largest.pop(0)
                largest.append(number)
                largest.append(temp)
        else:
            temp = largest.pop(0)
            largest.append(number)
            largest.append(temp)
        max_digit = int(number[0])
    for i in range(len(largest)-1,-1,-1):
        ans += str(largest[i])
    return ans

print(largestNumber([ 9, 99, 999, 9999, 9998 ]))