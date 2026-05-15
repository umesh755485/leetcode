from collections import Counter
from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        mx = max(freq.values())
        ans = 0
        for v in freq.values():
            if v == mx:
                ans += v
        return ans

print(Solution().maxFrequencyElements([1, 2, 2, 3, 1, 4]))  # 4