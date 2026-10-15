class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sort =  sorted(nums,reverse = True)

        return sort[k-1]

        