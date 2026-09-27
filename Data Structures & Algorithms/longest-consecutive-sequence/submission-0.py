class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nset = set(nums)
        ln = 0

        for i in nums:
            if (i - 1) not in nset:
                lo = 0
                while (i + lo) in nset:
                    lo+=1
                ln = max(ln, lo)
        return ln

