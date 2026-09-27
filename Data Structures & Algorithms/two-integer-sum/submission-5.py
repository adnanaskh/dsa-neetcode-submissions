class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ind = {}

        for i, c in enumerate(nums):
            d = target - c
            if d in ind:
                return [ind[d], i]
            ind[c] = i