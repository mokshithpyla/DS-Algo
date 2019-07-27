# t = int(input())
# for _ in range(t):
#     S = list(input())
#     t = 0
#     ans = 0
#     for i in range(len(S)):
#         if S[i] == '<':
#             t += 1
#         else:
#             t -= 1
#             if t == 0:
#                 ans = max(ans, i+1)
#             elif t < 0:
#                 break   # string s whole is invalid.
#
#     print(ans)
#
# # 3
# <<>>
# ><
# <>>>


marks = {6.71 :  '1-1',
         7.79  :'1-2',
         7.58  :'2-1',
         6.375 :'2-2',
         6.83 :'3-1',
         7.75 :'3-2',
         }
print(sum(marks)/6)