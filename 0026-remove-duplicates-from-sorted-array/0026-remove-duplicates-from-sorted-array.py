class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1

        for read in range(1, len(nums)):
            if nums[write - 1] == nums[read]:
                continue
            else:
                nums[read], nums[write] = nums[write], nums[read]

            write += 1

        return write