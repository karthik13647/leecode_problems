class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        keep=set()
        ele=str(n)
        while ele not in keep:
            keep.add(ele)
            summ=0
            for digit in ele:
                digit=int(digit)
                summ+=digit**2
            if summ==1: return True
            ele=str(summ)
        return False