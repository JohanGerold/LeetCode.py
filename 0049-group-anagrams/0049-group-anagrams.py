class Solution(object):
    def groupAnagrams(self, strs):
        store = {}
        for char in strs:
            keys = "".join(sorted(char))
            if keys in store:
                store[keys] += [char]
            else:
                store[keys] = [char]


        return list(store.values())

        