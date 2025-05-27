class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return Counter(s)==Counter(t)
        a=[0 for i in range(26)]
        for ele in s:
            a[ord(ele)-97]+=1
        for ele in t:
            a[ord(ele)-97]-=1
        for el in a:
            if el:
                return False
        return True