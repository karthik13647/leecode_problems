class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # n=len(goal)
        # val=-1
        # if len(s)!=len(goal):
        #     return False
        # for i in range(len(goal)):
        #     if goal[i]==s[0]:
        #         val=i
        # if val==-1:
        #     return False
        
        # for i in range(len(s)):
        #     if s[i]!=goal[(val+i)%n]:
        #         return False
        # return True

        if len(s)!=len(goal):
            return False
        return goal in s+s