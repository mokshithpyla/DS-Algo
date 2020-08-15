class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Approach 1:
        # anaGroups = {}
        # for each in strs:
        #     sortedStr = tuple(sorted(each))
        #     if sortedStr in anaGroups:
        #         anaGroups[sortedStr].append(each)
        #     else:
        #         anaGroups[sortedStr] = [each]
        # return anaGroups.values()
        
        # Approach 2:
        charCounts = {}
        for each in strs:
            charCount = [0]*26
            for char in each:
                charCount[ord(char)-ord('a')] += 1
            charCount = tuple(charCount)
            if charCount in charCounts:
                charCounts[charCount].append(each)
            else:
                charCounts[charCount] = [each]
        return charCounts.values()