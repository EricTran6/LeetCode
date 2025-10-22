class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return answer
            answer += strs[0][i]
        return answer
