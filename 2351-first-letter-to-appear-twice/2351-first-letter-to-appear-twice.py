class Solution:
    def repeatedCharacter(self, s: str) -> str:
        w = set()

        for char in s:
            if char in w:
                return char
            else:
                w.add(char) 