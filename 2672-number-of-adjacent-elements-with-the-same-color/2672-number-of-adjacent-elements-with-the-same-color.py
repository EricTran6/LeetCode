class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        nums = [0] * n
        count = 0
        result = []
        for idx, color in queries:
            prev = nums[idx - 1] if idx > 0 else 0
            nex = nums[idx + 1] if idx < n - 1 else 0
            if nums[idx] != 0 and nums[idx] == prev:
                count -= 1
            if nums[idx] != 0 and nums[idx] == nex:
                count -= 1
            nums[idx] = color
            if nums[idx] != 0 and nums[idx] == prev:
                count += 1
            if nums[idx] != 0 and nums[idx] == nex:
                count += 1
            result.append(count)
        return result



        