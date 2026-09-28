class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        freqs1 = [0] * 26
        for c in s1:
            freqs1[ord(c) - ord('a')] += 1

        cur_freqs = [0] * 26
        l = 0
        for r in range(len(s2)):
            cur_freqs[ord(s2[r]) - ord('a')] += 1
            if cur_freqs == freqs1:
                return True
            while r - l + 1 >= len(s1):
                cur_freqs[ord(s2[l]) - ord('a')] -= 1
                l += 1

        return False