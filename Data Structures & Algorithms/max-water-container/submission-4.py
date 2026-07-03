class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j=0,len(heights)-1
        maxim=[]


        while i<j :
            maxim.append((j - i) * min(heights[i],heights[j]))
            if heights[i]>heights[j]:
                
                j-=1
            elif heights[i]<=heights[j] :
                i+=1

        return max(maxim)