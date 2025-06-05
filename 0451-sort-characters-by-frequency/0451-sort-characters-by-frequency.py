class Solution:
    def frequencySort(self, s: str) -> str:
        counter=Counter(s)
        a=[]
        for key,freq in  sorted(counter.items(),key=lambda x:-x[1]):
        # for key,freq in counter.most_common():
            a+=[key]*freq
        return ''.join(a)