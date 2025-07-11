class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        cnt=0
        for ele in words:
            k=set(ele)
            if ele[::-1] in words and len(k)!=1:
                cnt+=1
        return cnt//2
