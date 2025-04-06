
def climbStairs( n):
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[1] = 1  # 1 way to reach step 1 (1 step)
    dp[2] = 2  # 2 ways to reach step 2 (1+1 or 2)
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
    
x = 7
print(climbStairs(x))
