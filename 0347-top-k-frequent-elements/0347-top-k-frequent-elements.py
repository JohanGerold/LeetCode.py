class Solution(object):
    def topKFrequent(self, nums, k):
        frequency = {}
        answer = []

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        while k > 0:

            largest_num = 0
            largest_count = 0

            for num, count in frequency.items():
                if count > largest_count:
                    largest_count = count
                    largest_num = num
            answer.append(largest_num)
            frequency.pop(largest_num)

            k -= 1
        return answer
        