class Solution:
    # Traverse the list of numbers for a k > i > j
    # Look for i: the first minimum, and j: the second minimum 
    # if there is a k > i > j (else part) return True!
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = j = float('inf')
        for k in nums:
            if k <= i:
                i = k
            elif k <= j:
                j = k
            else:
                return True
        return False