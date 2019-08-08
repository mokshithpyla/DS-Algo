def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right)// 2
        left_wala = nums[left]
        right_wala = nums[right]
        if nums[mid] is target:
            print(left, right, left_wala, right_wala, 'here')
            return mid
        if target is left_wala:
            return left
        if target is right_wala:
            return right
        elif right_wala > left_wala:
            if target is nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if target is nums[mid]:
                return mid
            if nums[mid] is target:
                return mid
            if target is left_wala:
                return left

            elif target < right_wala:
                if target < nums[mid] and nums[mid]< right_wala:
                    right = mid - 1
                else:
                    left = mid + 1
            elif target > left_wala:
                if target > nums[mid] and nums[mid] > left_wala:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                return -1

    return -1



print(search([278,280,281,286,287,290,2,3,4,8,9,14,15,16,21,24,25,31,32,34,36,37,42,45,51,52,54,55,60,63,66,68,69,71,76,81,83,84,85,86,87,94,97,99,106,107,110,113,114,115,118,120,121,125,134,136,137,138,142,143,147,150,152,159,160,161,165,166,174,176,178,186,187,189,190,191,195,196,198,204,212,216,217,220,221,222,225,227,229,232,237,239,242,245,251,263,264,274,275,276,277]
,286))