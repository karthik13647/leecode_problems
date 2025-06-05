class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return Counter(s)==Counter(t)
        l=[0]*26
        for ele in s:
            l[ord(ele)-97]+=1
        for ele in t:
            l[ord(ele)-97]-=1
        for ele in l:
            if ele!=0:
                return False
        return True