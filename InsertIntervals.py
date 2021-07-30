class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []

        for i in range(len(intervals)):
            interval = intervals[i]

            #if our new interval falls before all other intervals, we are ready return
            if newInterval[1] < interval[0]:
                output.append(newInterval)
                return output + intervals[i:]

            #if our interval does not quite fall before all intervals, but stil does not overlap
            if newInterval[0] > interval[1]:
                output.append(interval)
            else:
                newInterval = [min(newInterval[0],interval[0]),max(newInterval[1],interval[1])]

        output.append(newInterval)

        return output