class Solution:
    def reverseBits(self, n: int) -> int:
        bits = list(bin(n)[2:].zfill(32))

        i = 0 
        j = len(bits)-1
        while i<j:
            temp = bits[i]
            bits[i] = bits[j]
            bits[j] = temp

            i+=1
            j-=1
        
        s = "".join(bits)
        return int(s, 2)

