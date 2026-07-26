class Solution(object):
    def intersection(self, nums1, nums2):
        a = set()
        b = set()
        for num in nums1:
            a.add(num)
        for num in nums2:
            b.add(num)

        result = a.intersection(b)
        return list(result)
        