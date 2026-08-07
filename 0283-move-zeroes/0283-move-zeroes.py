class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        result = []
        result_without = []

        for num in nums:
            if num == 0:
                result.append(num)
            else:
                result_without.append(num)

        final = result_without + result
        nums[:] = final
        return nums
        