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
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==1:
            return self.exist(matrix[0],target)
        l,r=0,len(matrix)-1
        t=len(matrix[0])
        while l<=r:
            mid=(l+r)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                res= self.exist(matrix[mid],target)
                return res
            elif matrix[mid][-1]<=target:
                l=mid+ 1
            else:
                r=mid-1
        return False
