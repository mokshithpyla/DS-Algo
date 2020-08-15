def solution(data, n):
    # Your code here
    countMinionShifts = {}
    for each in data:
        if each not in countMinionShifts:
            countMinionShifts[each] = 1
        else:
            countMinionShifts[each] += 1
    mostWorst = []
    for each in data:
        if countMinionShifts[each] > n:
            mostWorst.append(each)

    data = [x for x in data if x not in mostWorst]

solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)