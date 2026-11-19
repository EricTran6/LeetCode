class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        counts = Counter(nums)
        count = 0
        for num in counts:
            count += counts[num] * counts[num + k]
        return count