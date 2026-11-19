class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        seen = defaultdict(int)
        count = 0
        for num in nums:
            val1, val2 = num + k, num - k
            if val1 in seen:
                count += seen[val1]
            if val2 in seen:
                count += seen[val2]
            seen[num] += 1
        return count