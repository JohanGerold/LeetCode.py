class Solution(object):
    def majorityElement(self, nums):
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        for count in frequency:
            if frequency[count] > len(nums)/2:
                return count
        return False
        