class Solution(object):
    def firstUniqChar(self, s):
        seen = set()
        repeated = set()

        for char in s:
            if char not in seen:
                seen.add(char)
            else:
                repeated.add(char)

        for j, char2 in enumerate(s):
            if char2 not in repeated:
                return j

        return -1
        