class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=list(zip(*strs))
        s=""
        for ele in l:
            if len(set(ele))==1:
                s+=ele[0]
            else:
                break
        return s
