# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
#
# class Solution:
#     # @param intervals, a list of Intervals
#     # @param new_interval, a Interval
#     # @return a list of Interval
#     def insert(self, intervals, new_interval):
#         # new_start = new_interval[0]
#         # new_end = new_interva[1]
#         new_start, new_end = new_interval.start, new_interval.end
#         final_intervals = set()
#         merged = False
#         merge_once = False
#         least = False
#         done = False
#         for i in range(len(intervals)):
#             start, end = intervals[i].start, intervals[i].end
#             if max(start, new_start) > min(end, new_end):
#                 merged_interval = Interval(new_start, new_end)
#                 if merge_once:
#                     final_intervals.add(merged_interval)
#                     merge_once = False
#                 final_intervals.add(intervals[i])
#             else:
#                 new_start = min(start, new_start)
#                 new_end = max(end, new_end)
#                 merged = True
#                 merge_once = True
#         if not merged:
#             final_intervals.add(Interval(new_start, new_end))
#
#         return final_intervals
#
# s = Solution()
# x = (s.insert([Interval(3,6),Interval(8,10)], Interval(1,2)))
# for each in x:
#     print(each.start, each.end)

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import operator
class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, U, new_interval):

        if new_interval.start > new_interval.end :
            new_interval.start, new_interval.end = new_interval.end, new_interval.start

        U.append(new_interval)

        res = []
        U.sort(key = operator.attrgetter('start', 'end'))
        if len(U) <= 1 :
            return U
        length = len(U)

        for i in range(length-1) :
            #Checking if the itervals overlap
            if U[i].end >= U[i+1].start :
                #Checking the max end between two intervals and setting the i+1 interval to that
                if U[i].end > U[i+1].end :
                    U[i+1].start = U[i].start
                    U[i+1].end = U[i].end
                else :
                    U[i+1].start = U[i].start
                    U[i+1].end = U[i+1].end
                #Negating the unwanted intervals
                U[i].start = -U[i].start
                U[i].end = -U[i].end

        #Taking only the positive intervals in the result
        for i in range(length) :
            if U[i].start >=0 :
                x = U[i].start
                y = U[i].end
                res.append(Interval(x,y))

        return res


                