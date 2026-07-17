class Solution:
    def exist(self,submatrix,target):
        l,r=0,len(submatrix)-1    
        while l<=r:
            midj=(l+r)//2
            if submatrix[midj]==target:
                return True
            elif submatrix[midj]<target:
                l=midj+1
            else:
                r=midj-1
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        for i in range(len(matrix)):
            res= self.exist(matrix[i],target)
            if res : return res
        return False       
