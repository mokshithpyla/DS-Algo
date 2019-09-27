# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
#
# Example:

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans =[]
        for each in range(1, n+1):
            if each % 3 ==0 and each % 5 == 0:
                ans.append('FizzBuzz')
                continue
            if each % 3 == 0:
                ans.append('Fizz')
            elif each % 5 == 0:
                ans.append('Buzz')
            else:
                ans.append(str(each))
        return ans