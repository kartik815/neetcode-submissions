class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        m = len(s)
        if m==0:
            return True
        i, j = 0, 0
        flag = False
        while i < m:
            while j < n:
                if s[i] == t[j]:
                    if(i == (m-1)):
                        return True
                    i+=1
                    j+=1
                    if j == n:
                        return False
                    flag = True

                else:
                    j+=1
                    flag=False

            if not flag:
                return False
        return flag




        