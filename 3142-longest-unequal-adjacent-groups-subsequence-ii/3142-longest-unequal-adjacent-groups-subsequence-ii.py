from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        
        def hamming_distance(w1, w2):
            return sum(a != b for a, b in zip(w1, w2))
        
        dp = [1] * n 
        prev = [-1] * n 
        
        for i in range(n):
            for j in range(i):
                if (groups[i] != groups[j] and
                    len(words[i]) == len(words[j]) and
                    hamming_distance(words[i], words[j]) == 1):
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
        
        max_len = max(dp)
        idx = dp.index(max_len)
        
        res_indices = []
        while idx != -1:
            res_indices.append(idx)
            idx = prev[idx]
        res_indices.reverse()
        
        return [words[i] for i in res_indices]
