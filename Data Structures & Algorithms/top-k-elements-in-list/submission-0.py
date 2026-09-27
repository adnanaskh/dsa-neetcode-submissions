class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for v in nums:
            map[v] = map.get(v, 0) +1

        res = heapq.nlargest(k, map, key=map.get)
        return res