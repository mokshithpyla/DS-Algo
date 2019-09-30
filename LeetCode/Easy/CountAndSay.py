class Solution:
    def countAndSay(self, n):
        rule = {'1':'11', '2':'12', '3':'13', \
                '11':'21', '22':'22', '33':'23', \
                '111':'31', '222':'32', '333':'33'}
        if n == 1:
            return '1'

        s = '1'
        for _ in range(n - 1):    #iterate n-1 times
            p = 0
            part = []    #split s into parts (eg. 1211 into ['1','2','11'])

            for i in range(len(s)):    #take out consecutive same number
                if s[i] == s[p]:
                    continue
                part.append(s[p: i])
                p = i
            part.append(s[p:])

            s = ''.join([rule[item] for item in part])    #join mapped parts together
        return s      