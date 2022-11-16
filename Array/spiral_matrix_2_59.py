class Solution:
    def generateMatrix(self, n):
        matrix = [[0]*n for i in range(n)]
        left = 0
        right =n
        top = 0
        bottom = n
        num=1
        while left<right and top<bottom:
            # top row 
            for i in range(left, right):
                matrix[top][i]=num
                num+=1
            top+=1
            # right column 
            for i in range(top, bottom):
                matrix[i][right-1]=num
                num+=1
            right-=1
            # bottom row
            for i in range(right-1,left-1,-1):
                matrix[bottom-1][i]=num
                num+=1
            bottom-=1
            #left column
            for i in range(bottom-1, top-1,-1):
                matrix[i][left]=num
                num+=1
            left+=1
        return matrix
if __name__ =="__main__":
    ob=Solution()
    n=3
    ans=ob.generateMatrix(n)
    print(ans)