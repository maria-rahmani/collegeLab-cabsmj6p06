import sys

def matrix_chain_multiplication(dims):
    n = len(dims)
    # dp[i][j] stores minimum multiplications for matrices i to j
    dp = [[0] * n for _ in range(n)]
    
    for length in range(2, n):  # Chain length
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    return dp[1][n - 1]

# Example usage
dims = [10, 30, 5, 60]  # Matrix dimensions
print("Minimum cost:", matrix_chain_multiplication(dims))   
