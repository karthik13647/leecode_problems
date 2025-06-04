class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        k=s[::-1]
        return ' '.join(k)