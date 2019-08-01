#
# def countOnes(Q, i, ones):
#
#     Q, Q1 = logical_xor(Q, i)
#     i[0] += 1
#     E = ones[0]
#     O = ones[1]
#     # print(Q)
#     # print(Q1)
#     for each in Q1:
#         if bin(each).count('1') % 2 == 0:
#             E += 1
#         else:
#             O += 1
#     ones = [E, O]
#     if i[0] == n:
#         print(ones[0], ones[1])
#         return
#     if i[0] == 0:
#         print(ones[0], ones[1])
#         countOnes(Q, i, ones)
#     else:
#         print(ones[0], ones[1])
#         countOnes(Q, i, ones)
#
#
# def logical_xor(Q, i):
#
#     x = int(input())
#     # new = set()
#     # new.add(x)
#     new = set()
#     new.add(x)
#     if x not in Q:
#         Q.add(x)
#     else:
#         return Q, set()
#     if i[0] == 0:
#         return Q, [x]
#     for y in Q:
#         if y != x:
#             new.add(x ^ y)
#     Q.update(new)
#     # new.add(x)
#     return Q, new
#
#
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     Q = set()
#     i = [0]
#     countOnes(Q, i, [0, 0])
#     print('hey')

    # print(counting[0], counting[1])
    # print(calc)

# 1
# 3
# 4
# 2
# 7




t = int(input())
for _ in range(t):
    n = int(input())
    Q = set()
    e = 0
    o = 0
    for i in range(n):
        x = int(input())
        if x not in Q:
            Q.add(x)
        else:
            print(e, o)
            continue
        new = set()
        new.add(x)
        for y in Q:
            if y != x:
                new.add(y ^ x)
        # print(Q)
        # print(new)
        for each in new:
            if bin(each).count('1') % 2 == 0:
                e += 1
            else:
                o += 1
        print(e, o)
        Q.update(new)


