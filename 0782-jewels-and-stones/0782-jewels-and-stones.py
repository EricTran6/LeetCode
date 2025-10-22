class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        jewels_count = 0

        for s in stones:
            if s in jewels:
                jewels_count += 1
        return jewels_count