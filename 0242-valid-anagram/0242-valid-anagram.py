class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arrS = {}
        arrT = {}
        for i in range(len(s)):
            arrS[s[i]] = arrS.get(s[i], 0) + 1
            arrT[t[i]] = arrT.get(t[i], 0) + 1
        if arrS != arrT:
            return False
        return True