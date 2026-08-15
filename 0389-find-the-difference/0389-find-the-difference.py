class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            count[ch] = count.get(ch, 0) - 1
            if count[ch] < 0:
                return ch