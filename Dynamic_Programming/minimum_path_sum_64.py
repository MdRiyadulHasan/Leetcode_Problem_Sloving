# array | dynamic-programming 
def minPathSum( grid) -> int:
    m,n = len(grid),len(grid[0])
    res=[[float('inf')]*(n+1) for i in range(m+1)]
    res[m][n-1]=0
    for r in range(m-1,-1,-1):
        for c in range(n-1,-1,-1):
            res[r][c]=grid[r][c]+min(res[r+1][c],res[r][c+1])
    return res[0][0]
if __name__ == '__main__':
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    ans=minPathSum(grid)
    print(ans)

