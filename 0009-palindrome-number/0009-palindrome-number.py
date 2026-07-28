class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        store = []
        for i in s:
            store.append(i)
        if store == store[::-1]:
            return True
        else:
            return False