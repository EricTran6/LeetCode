class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase = ""
        for i in range(len(s)):
            if "A" <= s[i] <= "Z" or "a" <= s[i] <= "z" or "0" <= s[i] <= "9":
                lowercase += s[i]
        lowercase = lowercase.lower()
        print(lowercase)

        l = 0
        r = len(lowercase) - 1
        if len(lowercase) == 1:
            return True
        for i in range(len(lowercase) // 2):
            if lowercase[l] != lowercase[r]:
                return False
            l += 1
            r -= 1
        return True
