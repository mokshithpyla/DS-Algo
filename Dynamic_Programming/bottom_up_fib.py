
# CS Dojo
# def fib(n):
#     if n==1 or n==2:
#         return 1
#     bottom_up=[None]*(n+1)
#     bottom_up[1]=1
#     bottom_up[2]=2
#     for i in range(3,n+1):
#         bottom_up[i]=bottom_up[i-1]+bottom_up[i-2]
#     return bottom_up[n]
#
# n=int(input('Enter value of n:'))
# print(n,'th fibonacci term is: ',fib(n),sep='')

# MIT Open Courseware
fib = {}
f = 0
n = int(input("Enter the value of n: "))
for i in range(1, n+1):
    if i <= 2:
        f = 1
    else:
        f = fib[i-1] + fib[i-2] # Constructing the subproblems from the beginning
    fib[i] = f
    print(f)
# print(fib[n])
