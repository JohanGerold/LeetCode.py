class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        write = 0

        for read in range(0, len(nums)):
            if nums[read] % 2 == 0 or nums[read] == 0:
                nums[read], nums[write] = nums[write], nums[read]
                write += 1
        
        return nums