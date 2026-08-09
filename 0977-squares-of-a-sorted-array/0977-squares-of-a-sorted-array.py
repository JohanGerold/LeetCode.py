class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [abs(num) for num in nums]
        nums = [num**2 for num in nums]
        nums.sort()
        return nums