t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    modifications = []
    for i in range(q):
        x, y = map(int, input().split())
        modifications.append([x, y])
    print('Case #', _+1, ':', sep='', end='')
    # initial_xor = xor_sum
    prev_xor = 0
    xor_sum = 0
    for i in range(q):
        largest_sub_interval = n
        first = 0
        last = n-1
        if i is 0:
            a[modifications[i][0]] = modifications[i][1]
            for k in range(n):
                xor_sum = xor_sum ^ a[k]
            prev_xor = xor_sum
        else:
            xor_sum = prev_xor ^ a[modifications[i][0]] ^ modifications[i][1]
            prev_xor = xor_sum
        while first <= last:
            if bin(xor_sum).count('1') % 2 is 0:
                break
            if first == last:
                prev_xor = prev_xor ^ a[first]
                xor_sum = prev_xor
                first += 1
                largest_sub_interval = n - first
            else:
                largest_sub_interval -= 1
                xor_sum = xor_sum ^ a[last]
                last -= 1
        if largest_sub_interval >= 2:
            print('', largest_sub_interval, end='')
        else:
            largest_sub_interval = 0
            print('', largest_sub_interval, end='')
    print()

