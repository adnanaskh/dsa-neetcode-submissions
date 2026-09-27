class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n+1):
            b = list(bin(i)[2:])
            c = 0
            for j in b:
                if j == '1':
                    c +=1
            res.append(c)

        return res