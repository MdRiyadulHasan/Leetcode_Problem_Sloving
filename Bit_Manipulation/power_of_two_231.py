# math | bit-manipulation
# google
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n!=0 and n&(n-1)==0:
            return True
        else:
            return False
if __name__ == '__main__':
    n=int(input())
    s=Solution()
    result = s.isPowerOfTwo(n)
    print(result)