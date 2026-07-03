class Solution:
    def whichRow(self, matrix: List[List[int]], target: int):
        m = 0
        while m < len(matrix):
            if matrix[m][-1] < target:
                m += 1
            elif matrix[m][-1] == target:
                return True  # Found the target in last column
            else:
                return matrix[m]  # Found potential row
        return None
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L=self.whichRow(matrix,target)
        if L==True:
            return L
        elif L==None:
            return False
        
        l,r=0,len(L)-1
        while l<=r:
            ty=(l+r)//2
            if L[ty] >target:
                r=ty-1
            elif L[ty]<target:
                l=ty+1
            else:
                return True
        return False



