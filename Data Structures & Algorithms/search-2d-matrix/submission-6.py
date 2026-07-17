class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        for i in range(len(matrix)):
            l,r=0,len(matrix[0])-1    
            while l<=r:
                midj=(l+r)//2
                if matrix[i][midj]==target:
                    return True
                elif matrix[i][midj]<target:
                    l=midj+1
                else:
                    r=midj-1
                    
        return False       
            

