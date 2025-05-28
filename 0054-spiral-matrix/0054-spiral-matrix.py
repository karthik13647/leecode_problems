class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n= len(matrix),len(matrix[0])
        i,j=0,0
        top,left,down,right=1,2,3,4
        a=[]
        top_wall=0
        left_wall=n
        down_wall=m
        right_wall=-1
        direction=top
        while(len(a)!=m*n):
            if direction==top:
                while j<left_wall:
                    a.append(matrix[i][j])
                    j+=1
                i,j=i+1,j-1
                left_wall-=1
                direction=left
            elif direction==left:
                while i<down_wall:
                    a.append(matrix[i][j])
                    i+=1
                i,j=i-1,j-1
                down_wall-=1
                direction=down
            elif direction==down:
                while j>right_wall:
                    a.append(matrix[i][j])
                    j-=1
                i,j=i-1,j+1
                right_wall+=1
                direction=right
            else:
                while i>top_wall:
                    a.append(matrix[i][j])
                    i-=1
                i,j=i+1,j+1
                top_wall+=1
                direction=top
        return a
                
            
