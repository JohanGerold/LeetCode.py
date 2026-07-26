class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequency = {}
        seen = set()
        store = []
        for num in arr:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        for num in frequency.values():
            seen.add(num)
            store.append(num)

        if len(seen) == len(store):
            return True
        else:
            return False