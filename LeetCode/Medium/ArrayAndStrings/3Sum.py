class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        triplets = []
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = nums[left] + nums[right] + nums[i]
                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    triplets.append([nums[left], nums[right], nums[i]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return triplets
        