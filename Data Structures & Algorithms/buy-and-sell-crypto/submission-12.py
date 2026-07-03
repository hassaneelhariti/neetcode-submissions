class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=1
        maxi=0
        while i<len(prices):
            if j==len(prices):
                break
            elif prices[j]-prices[i] <0:
                i=j
            elif prices[j]-prices[i] >maxi:
                maxi=prices[j]-prices[i]
            j=j+1
        return maxi