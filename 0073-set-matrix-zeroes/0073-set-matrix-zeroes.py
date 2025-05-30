class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=[0]*len(matrix)
        col=[0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    rows[i]=1
                    col[j]=1
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if rows[i]==1 or col[j]==1:
                    matrix[i][j]=0
                        