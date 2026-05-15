class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        roat_arr = [0]*n
        for i in range(n):
            roat_arr[(i+k)%n]=nums[i]
        nums[:] = roat_arr[:]
        