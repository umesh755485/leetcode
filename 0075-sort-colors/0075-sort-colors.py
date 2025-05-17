class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        for i in range(n-1):
            for j in range(n-1-i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
       
