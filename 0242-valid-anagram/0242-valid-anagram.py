class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrS = {}
        arrT = {}
        for ch in s:
            arrS[ch] = arrS.get(ch, 0) + 1
        for ch in t:
            arrT[ch] = arrT.get(ch, 0) + 1
        if arrS != arrT:
            return False
        return True
            