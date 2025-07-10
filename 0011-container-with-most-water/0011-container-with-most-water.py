class Solution:
    def maxArea(self, h: List[int]) -> int:
        l=0
        r=len(h)-1
        water=float("-inf")
        pre_water=0
        b=r
        while(l<r):
            if h[l]<=h[r]:
                pre_water=h[l]*b
                l+=1
            else:
                pre_water=h[r]*b
                r-=1
            b-=1
            water=max(water,pre_water)
        return water
