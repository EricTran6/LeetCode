class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arrS = {}
        arrT = {}
        for ch in range(len(s)):
            arrS[s[ch]] = arrS.get(s[ch], 0) + 1
            arrT[t[ch]] = arrT.get(t[ch], 0) + 1
        if arrS != arrT:
            return False
        return True
            