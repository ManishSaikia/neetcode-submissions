class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS=len(matrix),len(matrix[0])
        left,right=0,ROWS*COLS-1
        while left<=right:
            mid=(right-left)+left//2
            rows,cols=mid//COLS,mid%COLS
            if matrix[rows][cols]<target:
                left=mid+1
            elif matrix[rows][cols]>target:
                right=mid-1
            else:
                return True
        return False
            