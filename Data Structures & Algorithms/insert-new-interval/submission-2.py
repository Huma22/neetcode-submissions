
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for interval in intervals:

            # Old interval comes before new interval
            if interval[1] < newInterval[0]:
                result.append(interval)

            # Old interval comes after new interval
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval

            # Intervals overlap
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

        result.append(newInterval)

        return result
