class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        x = 0

        for i in range(x, n + 1):
            if i not in nums:
                return i