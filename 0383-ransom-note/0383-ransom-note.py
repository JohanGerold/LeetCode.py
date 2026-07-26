class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        frequency = {}
        check = ""

        for char in magazine:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

        for char in ransomNote:
            if char in frequency and frequency[char] > 0:
                check += char
                frequency[char] -= 1
            else:
                break

        if check == ransomNote:
            return True
        else:
            return False
        