class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        print('seen',seen)
        longest = 0

        for n in nums:
            # we have to check for start of the seq 
            if (n-1) not in seen:
                length = 0
                while(n+length) in seen:
                    length +=1
                longest = max(length,longest)
                print('check', longest)
        return longest

        


 

        