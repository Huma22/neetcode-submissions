
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sort = sorted(intervals)
        res = []

        for interval in sort:
            if len(res) == 0:
                res.append(interval)

            else:
                last = res[-1]

                if interval[0] <= last[1]:
                    last[1] = max(last[1], interval[1])

                else:
                    res.append(interval)

        return res
