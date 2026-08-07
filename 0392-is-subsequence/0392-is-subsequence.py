class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        ls = []
        result = list(s)

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                ls.append(t[j])
                i += 1
            j += 1

        if ls == result:
            return True
        else:
            return False