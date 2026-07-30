class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        w_size = 2*k + 1
        mid = w_size//2

        w = sum(nums[:w_size])
        w_avg = w//w_size
        w_avg2 = w

        result = [-1] * len(nums)
        if len(nums) < w_size:
            return result
        else:
            result[mid] = w_avg
        
        for i in range(w_size, len(nums)):
            w = w + nums[i] - nums[i-w_size]
            w_avg2 = w//w_size
            mid += 1
            result[mid] = w_avg2
        return result