class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        count = 0
        for num in counts:
            if k == 0:
                if counts[num] > 1:
                    count += 1
            else:
                if num + k in counts:
                    count += 1
        return count