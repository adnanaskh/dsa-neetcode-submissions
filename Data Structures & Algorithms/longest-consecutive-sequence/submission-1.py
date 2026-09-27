class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nset = set(nums)
        n = len(nums)

        res = 0

        for i in nums:
            if i-1 not in nset:
                lo = 0
                while i+lo in nset:
                    lo+=1
                res = max(lo, res)
        return res
