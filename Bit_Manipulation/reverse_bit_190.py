# bit-manipulation
# airbnb | apple
class Solution:
    def reverseBits(self, n: int) -> int:
        output=0
        for i in range(32):
            output<<=1
            if n&1:
                output=output|1
            n>>=1
        return output