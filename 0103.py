#0103
# https://www.acmicpc.net/problem/9251
# DP, LCS problem


def LCS(a: str, b:str):
    dp = []
    w = len(a) + 1
    h = len(b) + 1
    # initialize 2d dp with 0.
    # cols(width) are a, rows(height) are b.
    dp = [[0] * w for _ in range(h)]
    
    # find LCS
    for i in range(1,h):
        for j in range(1,w):
            if a[j-1] == b[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
    
    return dp[h-1][w-1]

a= input()
b = input()
print(LCS(a,b))




