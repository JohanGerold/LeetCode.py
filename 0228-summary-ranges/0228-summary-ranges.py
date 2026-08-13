class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        j = 1
        group = []

        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[j] == nums[j-1] + 1:
                j += 1
            group.append([nums[i], nums[j-1]])
            i = j

        result = []

        for start, end in group:
            if start == end:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(end))
                
        return result