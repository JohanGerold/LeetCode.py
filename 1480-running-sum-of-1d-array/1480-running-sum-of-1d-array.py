class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        e = []
        s = 0

        for num in nums:
            s += num
            e.append(s)
        return e