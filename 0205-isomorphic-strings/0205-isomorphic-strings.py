class Solution(object):
    def isIsomorphic(self, s, t):
        mapping = {}
        used = set()

        for char, char2 in zip(s, t):

            if char in mapping:
                if mapping[char] != char2:
                    return False
                    break

            else:
                if char2 in used:
                    return False
                    break

                mapping[char] = char2
                used.add(char2)

        return True
        