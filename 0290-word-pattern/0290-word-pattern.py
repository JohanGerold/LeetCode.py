class Solution(object):
    def wordPattern(self, pattern, s):
        frequency = {}
        used = set()
        for char, char2 in zip(pattern, s.split()):
            if len(pattern) != len(s.split()):
                return False
            if char in frequency:
                if frequency[char] != char2:
                    return False
            else:
                if char2 in used:
                    return False
            frequency[char] = char2
            used.add(char2)

        return True
        