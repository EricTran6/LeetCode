class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seenPair = set()
        count = 0
        for num in nums:
            val1, val2 = num + k, num - k
            if val1 in seen:
                if (val1, num) not in seenPair:
                    count += 1
                    seenPair.add((val1, num))
                    seenPair.add((num, val1))
            if val2 in seen:
                if (val2, num) not in seenPair:
                    count += 1
                    seenPair.add((val2, num))
                    seenPair.add((num, val2))
            seen[num] += 1
        return count
