class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7

        def is_valid(col):
            for i in range(1, m):
                if col[i] == col[i-1]:
                    return False
            return True

        from itertools import product

        colors = [0, 1, 2]
        valid_cols = []
        for col in product(colors, repeat=m):
            if is_valid(col):
                valid_cols.append(col)

        compat = {}
        for c1 in valid_cols:
            compat[c1] = []
            for c2 in valid_cols:
                if all(x != y for x, y in zip(c1, c2)):
                    compat[c1].append(c2)

       
        dp = {col: 1 for col in valid_cols}
        for _ in range(n-1):
            new_dp = {col: 0 for col in valid_cols}
            for col in valid_cols:
                for prev in compat[col]:
                    new_dp[col] = (new_dp[col] + dp[prev]) % MOD
            dp = new_dp

        return sum(dp.values()) % MOD
