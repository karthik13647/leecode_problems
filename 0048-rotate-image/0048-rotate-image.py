class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        a=len(matrix[0])
        for i in range(a):
            for j in range(0,i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(a):
            matrix[i].reverse()
