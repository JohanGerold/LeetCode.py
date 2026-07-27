class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        current_avg = sum(arr[:k])
        max_avg = current_avg

        if current_avg/k >= threshold:
            count += 1

        for i in range(k, len(arr)):
            current_avg = current_avg + arr[i] - arr[i-k]
            max_avg = current_avg/k
            if max_avg >= threshold:
                count += 1

        return count