class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for n in s:
            if (n - 1) not in s:
                curr = 1
                while n + 1 in s:
                    curr += 1
                    n += 1
                longest = max(curr,longest)
        return longest
