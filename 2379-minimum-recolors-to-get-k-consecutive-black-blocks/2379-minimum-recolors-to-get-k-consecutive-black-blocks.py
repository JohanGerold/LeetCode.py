class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        current_whites = 0

        for char in blocks[:k]:
            if char == "W":
                current_whites += 1
            min_whites = current_whites

        for i in range(k, len(blocks)):
            if blocks[i - k] == "W":
                current_whites -= 1
            if blocks[i] == "W":
                current_whites += 1

            min_whites = min(current_whites, min_whites)
    
        return min_whites