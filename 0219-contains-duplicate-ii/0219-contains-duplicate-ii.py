class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}

        for i, num in enumerate(nums):
            if num in seen:
                if abs(i - seen[num]) <= k:
                    return True
                    break
                seen[num] = i
            else:
                seen[num] = i

        return False
        