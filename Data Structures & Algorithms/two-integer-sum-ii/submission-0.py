class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if target == total:
                return[left+1,right+1]
                print('check the return',[left,right])
            elif total < target:
                left += 1
            else:
                right -= 1

        