class Solution:
    def isValid(self, word: str) -> bool:
        vow="aeiou"
        con="bcdfghjklmnpqrstvwxyz"
        digit_cnt=0
        vow_cnt=0
        con_cnt=0
        other_cnt=0
        if len(word)<3:
            return False
        else:
            for ele in word:
                ele=ele.lower()
                if ele in vow:
                    vow_cnt+=1
                elif ele in con:
                    con_cnt+=1
                elif ele.isdigit():
                    continue
                else:
                    return False
        return vow_cnt >= 1 and con_cnt >= 1

