
def countOnes(Q, i, ones):

    Q, Q1 = logical_xor(Q, i)
    E = ones[0]
    O = ones[1]
    print(Q)
    print(Q1)
    for each in Q1:
        # if each not in calc:
        # calc[each] = bin(each).count('1')
        if bin(each).count('1') % 2 == 0:
            E += 1
        else:
            O += 1
        # else:
        #     if calc[each] % 2 == 0:
        #         E += 1
        #     else:
        #         O += 1
    ones = [E, O]
    if i == n-1:
        print(ones[0], ones[1])
        return
    if i == 0:
        print(ones[0], ones[1])
        return countOnes(Q, i+1, ones)
    print(ones[0], ones[1])
    return countOnes(Q, i+1, ones)


def logical_xor(Q, i):

    x = int(input())
    # new = set()
    # new.add(x)
    new  = []
    new.append(x)
    if x not in Q:
        Q.add(x)
    else:
        return Q, set()
    if i == 0:
        return Q, [x]
    for y in Q:
        if y != x:
            new.append(x ^ y)
    # Q.update(new)
    # new.add(x)
    return Q, new


t = int(input())
for _ in range(t):
    n = int(input())
    Q = set()
    i = 0
    countOnes(Q, i, [0, 0])
    # print(counting[0], counting[1])
    # print(calc)

