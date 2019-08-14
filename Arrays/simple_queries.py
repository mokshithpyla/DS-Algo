import math
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        def number_of_divisors(n):
            cnt = 0
            for i in range(1, (int)(math.sqrt(n)) + 1) :
                if (n % i == 0) :
                    if (n / i == i) :
                        cnt = cnt + 1
                    else:
                        cnt = cnt + 2
            return cnt
        G = []
        for i in range(len(A)):
            for j in range(i,len(A)):
                G.append(A[j])
        print(G)
        for i in range(len(G)):
            G[i] = (int(math.sqrt(pow(G[i], number_of_divisors(G[i]))))) % (pow(10, 9) + 7)
        # print(G)
        G.sort(reverse=True)
        # print(G)
        k = 0
        for each in G:
            print(k, each)
            k+=1
        X = []
        for j in range(len(B)):
            X.append(G[B[j]-1])
        # print(X)
        return X
s = Solution()
print(s.solve([ 39, 99, 70, 24, 49, 13, 86, 43, 88, 74, 45, 92, 72, 71, 90, 32, 19, 76, 84, 46, 63, 15, 87, 1, 39, 58, 17, 65, 99, 43, 83, 29, 64, 67, 100, 14, 17, 100, 81, 26, 45, 40, 95, 94, 86, 2, 89, 57, 52, 91, 45 ]
        , [ 1221, 360, 459, 651, 958, 584, 345, 181, 536, 116, 1310, 403, 669, 1044, 1281, 711, 222, 280, 1255, 257, 811, 409, 698, 74, 838 ]))
