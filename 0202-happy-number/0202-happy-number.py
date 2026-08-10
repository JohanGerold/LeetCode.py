class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n = n // 10

            return total

        slow = n
        fast = n
        while True:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

            if fast == 1:
                return True
            if slow == fast:
                return False
        