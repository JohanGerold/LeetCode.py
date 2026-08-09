class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))

        for word in dictionary:
            i = 0
            j = 0

            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1

                if j == len(word):
                    return word
        return ""