class Solution(object):
    def isAnagram(self, s, t):
        frequency = {}
        frequency2 = {}
        for char in s:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

        for char in t:
            if char in frequency2:
                frequency2[char] += 1
            else:
                frequency2[char] = 1

        if frequency == frequency2:
            return True
        else:
            return False 
        