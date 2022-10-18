class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M,N=len(matrix), len(matrix[0])
        rstart,rend=0,M-1
        while rstart<rend:
            rmid=(rstart+rend)//2
            if matrix[rmid][-1]==target:
                return True
            elif matrix[rmid][-1]<target:
                rstart=rmid+1
            else:
                rend=rmid
        desired_row=rstart
        cstart,cend=0,N-1
        while cstart<cend:
            cmid=(cstart+cend)//2
            if matrix[desired_row][cmid]==target:
                return True
            elif matrix[desired_row][cmid]<target:
                cstart=cmid+1
            else:
                cend=cmid-1
        desired_col=cstart
        return matrix[desired_row][desired_col]==target
