class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        result = [intervals[0]]
        #no need of checking the first one that why we use indexing
        for start , end in intervals[1:]:
            last = result[-1][1]
            if start <= last:
                result[-1][1] = max(last,end)
            else:
                result.append([start,end])

        return result
