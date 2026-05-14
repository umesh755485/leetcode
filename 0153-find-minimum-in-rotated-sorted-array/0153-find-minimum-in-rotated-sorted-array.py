class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = float('inf')
        for i in range(len(nums)):
            if nums[i]<mini:
                mini = nums[i]
        return mini
    print(findMin)  
        