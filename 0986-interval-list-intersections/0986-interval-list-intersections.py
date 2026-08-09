class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        finallist = []

        i = 0
        j = 0

        while i < len(firstList) and j < len(secondList):

            if firstList[i][1] < secondList[j][1]:
                max_num = max(firstList[i][0], secondList[j][0])
                min_num = min(firstList[i][1], secondList[j][1])
                intersection = max_num, min_num
                i += 1
            else:
                max_num = max(firstList[i][0], secondList[j][0])
                min_num = min(firstList[i][1], secondList[j][1])
                intersection = max_num, min_num
                j += 1

            if max_num <= min_num:
                finallist.append([max_num, min_num])
        return finallist