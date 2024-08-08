class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = []
        dp.append(0)
        dp.append(1)
        dp.append(1)
        if n < 3:
            return dp[n]
        index = 2
        while index != n:
            total = dp[index-2] + dp[index-1] + dp[index]
            dp.append(total)
            index += 1
        return dp[n]

