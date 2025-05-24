class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        m=float('-inf')
        for ele in nums:
            if ele==1:
                cnt+=1
            else:
                cnt=0
            if m<cnt:
                m=cnt
            # m=max(cnt,m)
        return m