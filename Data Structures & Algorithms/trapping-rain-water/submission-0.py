class Solution:
    def trap(self, height: List[int]) -> int:
        prefix=[]
        suffix=[0]*len(height)
        #prefix
        maxi=height[0]
        for i in range(len(height)):
            maxi=max(maxi,height[i])
            prefix.append(maxi)
        #suffix
        maxs=height[len(height)-1]
        for i in range(len(height)-1,-1,-1):
            maxs=max(maxs,height[i])
            suffix[i]=maxs

        water=[0]*len(height)
        for i in range(len(prefix)):
            water[i] = min(prefix[i], suffix[i]) - height[i]
        
        return sum(water)