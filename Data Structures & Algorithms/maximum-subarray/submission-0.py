class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = nums[0]
        for n in nums:
            # 0+2,2+(-3),etc
            cur_sum += n 
            cur_sum = max(cur_sum,n)
            max_sum = max(max_sum, cur_sum)
        return max_sum

        

        