# array | dynamic-programming
# bloomberg
def uniquePathsWithObstacles( obstacleGrid) -> int:
    if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
        return 0              
    m, n = len(obstacleGrid), len(obstacleGrid[0])        
        
    dp=[[0] *n for i in range(m)]        
    dp[0][0]=1
                        
    for row in range(m):
        for col in range(n):
            if obstacleGrid[row][col]==0:
                dp[row][col] +=  dp[row-1][col] if row-1>=0 else 0
                dp[row][col]+= dp[row][col-1] if col-1>=0 else 0
         
    return dp[-1][-1]
    
    
if __name__ == '__main__':
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    ans = uniquePathsWithObstacles(obstacleGrid)
    print(ans)