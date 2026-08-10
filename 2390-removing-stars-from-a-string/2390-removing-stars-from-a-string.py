class Solution:
    def removeStars(self, s: str) -> str:
        k = len(s) - 1
        skip = 0
        s_new = ""

        for read in range(k, -1, -1):
            if s[read] == "*":
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                s_new += s[read]
        s_reverse = s_new[::-1]
        return s_reverse