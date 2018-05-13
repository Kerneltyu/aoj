n = int(input())
data = list(map(int, [input() for i in range(n)]))
inf = -float("inf")
dp = [inf for i in range(n)]
tsum = 0
for i in range(1, n):
    t = data[i]-data[i-1]
    tsum += t
    if(dp[i] < tsum):
        dp[i] = tsum
    else:
        dp[i] = dp[i-1]
    if tsum < 0:
        tsum = 0
print(max(dp))
