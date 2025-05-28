class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=float('-inf')
        mini=float('inf')
        for i in range(len(prices)):
            mini=min(prices[i],mini)
            maxi=max(maxi,prices[i]-mini)
        return maxi