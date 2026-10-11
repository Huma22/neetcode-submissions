class Solution(object):
    def moveZeroes(self, nums):
        temp = []
        zero = []
        for n in nums:
            if n != 0:
                temp.append(n)
                print('temp',temp)
            else:
                zero.append(n)
                print('temp',temp)
        merge_list = temp + zero
        print('check',merge_list)
        nums[:] = merge_list

